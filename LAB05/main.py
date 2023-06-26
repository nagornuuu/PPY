import smtplib
from email.mime.text import MIMEText

#
# users = {}
# print(users)
#
# users = {"lukasz": "email@gmail.com",
#         "joe": "joe@gmail.com",
#         "test": "test@gmail.com",
#         "admin": "admin@gmail.com"}
# print(users)
#
# user1 = {"name": "lukasz", "email": "email@gmail.com"}
# user2 = {"name": "joe", "email": "joe@gmail.com"}
# user3 = {"name":  "test", "email":"test@gmail.com"}
# user4 = {"name": "admin", "email": "admin@gmail.com"}
# print(user1)
#
# print(user1.get("name"))
# print(users.get("lukasz"))
# print(users.get("alice", "Invalid username"))
#
# print(users["alice"])
# users["alice"] = "alice@gmail.com"
# print(users["alice"])
#
# deleting user
# if "alice" in users:
#    del users["alice"]
# print(users)
#
# users["alice"] = "alice@gmail.com"
# if "alice" in users:
#    print(users.pop("alice"))
# wypisywanie key - username
# for e in users:
#    print(e)
#
# wypisywanie key - username
# for e in users.keys():
#    print(e)
#
# wypisywanie key and value - username and emails
# for key, value in users.items():
#    print("key is " + key + " values is " + value)
#
# wypisywanie value - emails
# for value in users.values():
#    print(value)
#
# sortowanie wartosci
# sorted_dict = {}
# for key in sorted(users.keys()):
#    sorted_dict[key] = value
#
# sortowanie wartosci w inne strone
# sorted_dict = {}
# for key in sorted(users.keys(), reverse = True):
#    value = users[key]
#    sorted_dict[key] = value
# print(sorted_dict)
#
# users = {
#    "lukasz": 100,
#    "joe": 90,
#    "test": 60,
#    "admin": 75
# }
# print(users.items())
#
# def get_value(item):
#    return item[1]
#
# sorted_values = sorted(users.items(), key = get_value)
# print(sorted_values)
# sorted_values = dict(sorted_values)
# print(sorted_values)
#
# dict_list = []
# dict_list.append(user1)
# dict_list.append(user2)
# dict_list.append(user3)
# dict_list.append(user4)
# print(dict_list)
#
# wypisuje liczbe users
# print(len(users))
#
# dodawanie hasla
# for i in range(0, len(dict_list)):
#     if "password" not in dict_list[i]:
#         dict_list[i]["password"] = "haslo"
# print(dict_list)
#
# zmiena hasla
# for i in range(0, len(dict_list)):
#     if "password" not in dict_list[i]:
#         dict_list[i]["password"] = "zmieniam"
# print(dict_list)
#
# dodawanie listy
# for i in range(0, len(dict_list)):
#    dict_list[i]["adresy"] = ["koszykowa 86",
#                              "akademicka 9"]
# print(dict_list)
#
# dodawanie listy
# for i in range(0, len(dict_list)):
#    dict_list[i]["adresy"] = {"adres 1": "koszykowa 86",
#                              "adres 2": "akademicka 9"}
# print(dict_list)
#
# czytanie z pliku i wypisywanie
# filepath = "students0.txt"
# with open(filepath) as file_object:
#    for line in file_object:
#        print(line.rstrip())
#
# tworzenia pliku i zapisywanie danych do pliku:
# students = ["jan", "alicja"]
# filepath = "students01.txt"
# with open(filepath, "w") as file_object:
#    for e in students:
#        line = f"hello {e} \n"
#        file_object.write(line)
#
# def send_email(subject, body, sender, recipients, password):
#    msg = MINEText(body)
#    msg['Subject'] = subject
#    msg['From'] = sender
#    msg['To'] = ', '.join(recipients)
#    smtp_server = smtplib.SMTP_SSl('smtp.gmail.com', 465)
#    smtp_server.login(sender, password)
#    smtp_server.sendmail(sender, recipients, msg.as_string())
#    smtp_server.quit()


def save_to_file(students):
    with open('students.txt', 'w') as f:
        for email, student in students.items():
            f.write(
                f"{email}, {student['name']}, {student['surname']}, {student['points']}, {student['grade']}, {student['status']}\n")


def load_from_file():
    try:
        with open('students.txt', 'r') as f:
            students = {}
            for line in f:
                email, name, surname, points, grade, status = line.strip().split(',')
                students[email] = {'name': name, 'surname': surname, 'points': int(points), 'grade': grade,
                                   'status': status}
    except FileNotFoundError:
        students = {}
    return students


def add_student(students, email, name, surname, points):
    if email in students:
        print("Student o podanym adresie email juz istnieje")
    else:
        students[email] = {'name': name, 'surname': surname, 'points': points, 'grade': '', 'status': ''}
        save_to_file(students)
        print(f"Student {name} {surname} zostal dodany do bazy danych.")


def remove_student(students, email):
    if email in students:
        del students[email]
        save_to_file(students)
        print(f"Student o adresie email {email} zostal usuniety z bazy danych.")
    else:
        print("Nie znaleziono studenta o podanym adresie email.")


def grade_students(students):
    for email, student in students.items():
        if student['grade'] == '' and student['status'] != 'GRADED' and student['status'] != 'MAILED':
            points = student['points']
            if 51 <= points <= 60:
                grade = 3
            elif 61 <= points <= 70:
                grade = 3.5
            elif 71 <= points <= 80:
                grade = 4
            elif 81 <= points <= 90:
                grade = 4.5
            elif 91 <= points <= 100:
                grade = 5
            else:
                grade = 2
            student['grade'] = grade
            student['status'] = 'GRADED'
            save_to_file(students)
            print(f"Student {student['name']} {student['surname']} otrzymał ocenę {grade}.")


def send_email(students):
    for email, student in students.items():
        if student['status'] == 'GRADED' and student['status'] != 'MAILED':
            grade = student['grade']
            name = student['name']
            surname = student['surname']
            body = f"Ocena: {grade} dla {name} {surname}"
            msg = MIMEText(body)
            msg['Subject'] = "Wystawianie ocen"
            msg['From'] = "sender"
            msg['To'] = ', '.join([student['email']])
            smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            mail = 's24918@pjwstk.edu.pl'
            smtp_server.login(mail, 'vyftdjpumglskylb')
            smtp_server.sendmail(mail, [student['email']], msg.as_string())
            smtp_server.quit()
            student['status'] = 'MAILED'


def print_students(students):
    for email, student in students.items():
        print(students[email])


students = load_from_file()
while True:
    print("Wybierz jedną z opcji:")
    print("1. Wypisz studentow")
    print("2. Dodaj studenta")
    print("3. Usuń studenta")
    print("4. Wystaw oceny")
    print("5. Wyślij maile")
    print("6. Wyjście")

    choice = input("Wybierz opcję: ")

    if choice == "1":
        print_students(students)
    elif choice == "2":
        email = input("Podaj adres email: ")
        name = input("Podaj imię: ")
        surname = input("Podaj nazwisko: ")
        points = int(input("Podaj liczbę uzyskanych punktów z przedmiotu Podstawy Programowania Python: "))
        add_student(students, email, name, surname, points)
    elif choice == "3":
        email = input("podaj adres email studenta ktorego chcesz usunac: ")
        remove_student(students, email)
    elif choice == "4":
        grade_students(students)
    elif choice == "5":
        send_email(students)
    elif choice == "6":
        exit(0)
    else:
        print("Niepoprawna opcja. Wybierz 1-5")
