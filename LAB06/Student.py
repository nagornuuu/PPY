from typing import List
from enum import Enum
import smtplib
from email.mime.text import MIMEText


class Status(Enum):
    NO_STATUS = 'NO_STATUS'
    GRADED = 'GRADED'
    MAILED = 'MAILED'
    GRADED_AND_MAILED = 'GRADED_AND_MAILED'


class Student:
    def __init__(self, email: str, name: str, surname: str, points: List[int], grade: float):
        self.email = email
        self.name = name
        self.surname = surname
        self.points = points
        self.grade = grade
        self.statusEnum = Status.NO_STATUS

    def __repr__(self):
        return f'Student(email={self.email}, name={self.name} {self.surname}, points={self.points}, grade={self.grade}, status={self.statusEnum.value})'


class MySortedList:
    def __init__(self, max_size):
        self.max_size = max_size
        self.data = []

    def insert(self, value):
        self.data.append(value)
        self.data.sort(reverse = True, key = lambda x: x.grade)
        self.data = self.data[:self.max_size]

    def __len__(self):
        return len(self.data)

    def __iter__(self):
        return iter(self.data)


def read_file(filename: str) -> List[Student]:
    students = []
    with open(filename, 'r') as file:
        for line in file:
            fields = line.strip().split(',')
            if len(fields) != 19:
                continue
            student = Student(fields[0], fields[1], fields[2], [int(x) for x in fields[3:16]], float(fields[17]))
            set_status(fields[18], student)
            students.append(student)
    return students


def grade_students(students: List[Student]):
    for student in students:
        if student.statusEnum in [Status.GRADED, Status.MAILED, Status.GRADED_AND_MAILED] or -1 in student.points:
            continue

        points = student.points
        projectGrade = points[0]
        listsGrades = points[1:4]
        hwGrade = sum(points[4:14])/10
        listGrade = sum(listsGrades)

        if hwGrade > 80:
            listGrade = 60
        elif hwGrade > 70:
            listsGrades.sort()
            listsGrades[0:2] = [20, 20]
            listGrade = sum(listsGrades)
        elif hwGrade > 60:
            listsGrades.sort()
            listsGrades[0] = 20
            listGrade = sum(listsGrades)

        student.grade = (projectGrade + listGrade) * 0.05

        student.status = Status.GRADED
        log_message(f"Graded student {student.email} with grade {student.grade}")


def delete_student(students: List[Student]):
    email = input("Podaj adres email studenta, ktorego chcesz usunac: ")
    for i, student in enumerate(students):
        if email == student.email:
            students.pop(i)
            print(f"Usunieto studenta o adresie email {email}")
            log_message(f"Usunieto studenta o adresie email {email}")
            return

    print(f"Nie znaleziono studenta o adresie email {email}")
    log_message(f"Nie znaleziono studenta o adresie email{email}")


def add_student(students: List[Student]):
    email = input("Podaj adres email studenta: ")
    emails = [student.email for student in students]
    if email in emails:
        print(f"Student o adresie email {email} juz istnieje")
        log_message(f"Student o adresie email {email} juz istnieje")
        return
    name, surname, points, status = \
            input("Podaj imie studenta: "), \
            input("Podaj nazwisko studenta: "),\
            input("Podaj liczbe punktow: "),\
            input("Podaj status: ").upper()

    s1 = Student(email = email, name = name, surname = surname, points = [int(p) for p in points.split(",")], grade = -1)
    set_status(status, s1)
    students.append(s1)
    print(f"Dodano studenta {name} {surname} z adresem email {email}")
    log_message(f"Dodano studenta z adresem email {email}, imie {name}, nazwisko {surname}, punkty {points}")


def set_status(status_str, student):
    if Status.GRADED.value in status_str and Status.MAILED.value in status_str:
        student.statusEnum = Status.GRADED_AND_MAILED
    elif Status.GRADED.value in status_str:
        student.statusEnum = Status.GRADED
    elif Status.MAILED.value in status_str:
        student.statusEnum = Status.MAILED


def print_students(students: List[Student]):
    for s in students:
        print(s)
    log_message(f"Wydrukowano wszystkie dane studentow")


def send_email(students: List[Student]):
    for student in students:
        if 'GRADED' in student.statusEnum.value and 'MAILED' not in student.statusEnum.value:
            body = f"Ocena: {student.grade} dla {student.name} {student.surname}"
            msg = MIMEText(body)
            msg['Subject'] = "Wystawianie ocen"
            msg['From'] = "sender"
            msg['To'] = ', '.join(student.email)
            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
                smtp_server.login('s24918@pjwstk.edu.pl', 'cybsmlcgizbgqrji')
                smtp_server.sendmail('s24918@pjwstk.edu.pl', student.email, msg.as_string())
            student.status = f"MAILED_{input('Provide custom status: ')}"
            log_message(f"Mail was sent to {student.email}.")


def main():
    data = read_file('ocenystudenci')
    while True:
        print("\n--- Menu ---")
        print("1. Wypisz studentow")
        print("2. Wystaw oceny")
        print("3. Usun studenta")
        print("4. Dodaj studenta")
        print("5. Send mail")
        print("0. Wyjdz")

        choice = input("\nWybierz opcje: ")
        if choice == "1":
            print_students(data)
        elif choice == "2":
            grade_students(data)
        elif choice == "3":
            delete_student(data)
        elif choice == "4":
            add_student(data)
        elif choice == "5":
            send_email(data)
        elif choice == "0":
            break
        else:
            print("Nieprawidlowa opcja")


def log_message(message):
    with open('logs.txt', 'a') as log_file:
        log_file.write(f'{message}\n')

if __name__ == '__main__':
    main()
