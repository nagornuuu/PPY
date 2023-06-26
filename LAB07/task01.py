import sqlite3
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Book Store")
root.iconbitmap("./bookshelf.ico")


#Pobranie danych z tabeli
def fetch_data():
    connection = sqlite3.connect('database.db')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Student")
    result = cursor.fetchall()
    cursor.close()  # Zamknięcie kursora
    cursor.close()  # Zamknięcie połączenia
    return result


treeview = ttk.Treeview(root)
treeview["columns"] = ("id", "mail", "imie", "nazwisko",
                       "project", "lista1", "lista2", "lista3",
                       "hw1", "hw2", "hw3", "hw4", "hw5", "hw6", "hw7", "hw8", "hw9", "hw10",
                       "grade", "status")
treeview.column("#0", width = 0)
treeview.column('id', width = 50)
treeview.column('mail', width = 200)
treeview.column('imie', width = 100)
treeview.column('nazwisko', width = 100)
treeview.column('project', width = 100)
treeview.column('lista1', width = 100)
treeview.column('lista2', width = 100)
treeview.column('lista3', width = 100)
treeview.column('hw1', width = 50)
treeview.column('hw2', width = 50)
treeview.column('hw3', width = 50)
treeview.column('hw4', width = 50)
treeview.column('hw5', width = 50)
treeview.column('hw6', width = 50)
treeview.column('hw7', width = 50)
treeview.column('hw8', width = 50)
treeview.column('hw9', width = 50)
treeview.column('hw10', width = 70)
treeview.column('grade', width = 150)
treeview.column('status', width = 100)

treeview.heading("id", text = "ID")
treeview.heading("mail", text = "Mail")
treeview.heading("imie", text = "Imie")
treeview.heading("nazwisko", text = "Nazwisko")
treeview.heading("project", text = "Projekt")
treeview.heading("lista1", text = "Lista 1")
treeview.heading("lista2", text = "Lista 2")
treeview.heading("lista3", text = "Lista 3")
treeview.heading("hw1", text = "Zad 1")
treeview.heading("hw2", text = "Zad 2")
treeview.heading("hw3", text = "Zad 3")
treeview.heading("hw4", text = "Zad 4")
treeview.heading("hw5", text = "Zad 5")
treeview.heading("hw6", text = "Zad 6")
treeview.heading("hw7", text = "Zad 7")
treeview.heading("hw8", text = "Zad 8")
treeview.heading("hw9", text = "Zad 9")
treeview.heading("hw10", text = "Zad 10")
treeview.heading("grade", text = "Ocena końcowa")
treeview.heading("status", text = "Status")

def load_data():
    data = fetch_data()
    treeview.delete(*treeview.get_children())
    for row in data:
        treeview.insert("", "end", values = (row[0], row[1], row[2], row[3], row[4], row[5], row[6],
                                            row[7], row[8], row[9], row[10], row[11], row[12], row[13],
                                            row[14], row[15], row[16], row[17], row[18], row[19]))

def open_details_window(event):
    selected_item = treeview.focus()
    if selected_item:
        item_data = treeview.item(selected_item)
        values = item_data['values']
        print(values)


def AddStudent():
    window = tk.Toplevel(root)
    window.title("Dodaj nowego studenta")

    idLabel = ttk.Label(window, text = "id: ")
    idLabel.grid(row = 0, column = 0)
    idEntry = ttk.Entry(window)
    idEntry.grid(row = 0,column = 1)

    mail_label = ttk.Label(window, text = "Mail:")
    mail_label.grid(row = 1, column = 0)
    mail_entry = ttk.Entry(window)
    mail_entry.grid(row = 1, column = 1)

    name_label = ttk.Label(window, text = "Imie:")
    name_label.grid(row = 2, column = 0)
    name_entry = ttk.Entry(window)
    name_entry.grid(row = 2, column = 1)

    surname_label = ttk.Label(window, text = "Nazwisko:")
    surname_label.grid(row = 3, column = 0)
    surname_entry = ttk.Entry(window)
    surname_entry.grid(row = 3, column = 1)

    project_label = ttk.Label(window, text = "Ocena projektu:")
    project_label.grid(row = 4, column = 0)
    project_entry = ttk.Entry(window)
    project_entry.grid(row = 4, column = 1)

    list1_label = ttk.Label(window, text = "Ocena listy 1:")
    list1_label.grid(row = 5, column = 0)
    list1_entry = ttk.Entry(window)
    list1_entry.grid(row = 5, column = 1)

    list2_label = ttk.Label(window, text = "Ocena listy 2:")
    list2_label.grid(row = 6, column = 0)
    list2_entry = ttk.Entry(window)
    list2_entry.grid(row = 6, column = 1)

    list3_label = ttk.Label(window, text="Ocena listy 3:")
    list3_label.grid(row = 7, column = 0)
    list3_entry = ttk.Entry(window)
    list3_entry.grid(row = 7, column = 1)

    hw1_label = ttk.Label(window, text="hw1:")
    hw1_label.grid(row = 8, column = 0)
    hw1_entry = ttk.Entry(window)
    hw1_entry.grid(row = 8, column = 1)

    hw2_label = ttk.Label(window, text =" hw2:")
    hw2_label.grid(row = 9, column = 0)
    hw2_entry = ttk.Entry(window)
    hw2_entry.grid(row = 9, column = 1)

    hw3_label = ttk.Label(window, text = "hw3:")
    hw3_label.grid(row = 10, column = 0)
    hw3_entry = ttk.Entry(window)
    hw3_entry.grid(row = 10, column = 1)

    hw4_label = ttk.Label(window, text="hw4:")
    hw4_label.grid(row = 11, column = 0)
    hw4_entry = ttk.Entry(window)
    hw4_entry.grid(row = 11, column = 1)

    hw5_label = ttk.Label(window, text="hw5:")
    hw5_label.grid(row = 12, column = 0)
    hw5_entry = ttk.Entry(window)
    hw5_entry.grid(row = 12, column = 1)

    hw6_label = ttk.Label(window, text = "hw6:")
    hw6_label.grid(row = 13, column = 0)
    hw6_entry = ttk.Entry(window)
    hw6_entry.grid(row = 13, column = 1)

    hw7_label = ttk.Label(window, text = "hw7:")
    hw7_label.grid(row = 14, column = 0)
    hw7_entry = ttk.Entry(window)
    hw7_entry.grid(row = 14, column = 1)

    hw8_label = ttk.Label(window, text = "hw8:")
    hw8_label.grid(row = 15, column = 0)
    hw8_entry = ttk.Entry(window)
    hw8_entry.grid(row = 15, column = 1)

    hw9_label = ttk.Label(window, text="hw9:")
    hw9_label.grid(row = 16, column = 0)
    hw9_entry = ttk.Entry(window)
    hw9_entry.grid(row = 16, column = 1)

    hw10_label = ttk.Label(window, text = "hw10:")
    hw10_label.grid(row = 17, column = 0)
    hw10_entry = ttk.Entry(window)
    hw10_entry.grid(row = 17, column = 1)

    final_grade_label = ttk.Label(window, text = "Ocena końcowa:")
    final_grade_label.grid(row = 18, column = 0)
    final_grade_entry = ttk.Entry(window)
    final_grade_entry.grid(row = 18, column = 1)

    status_label = ttk.Label(window, text="Status:")
    status_label.grid(row = 19, column = 0)
    status_entry = ttk.Entry(window)
    status_entry.grid(row = 19, column = 1)

    def add_new():
        global cursor, conenction
        newId = idEntry.get()
        new_mail = mail_entry.get()
        new_name = name_entry.get()
        new_surname = surname_entry.get()
        new_project = project_entry.get()
        new_list1 = list1_entry.get()
        new_list2 = list2_entry.get()
        new_list3 = list3_entry.get()
        new_hw1 = hw1_entry.get()
        new_hw2 = hw2_entry.get()
        new_hw3 = hw3_entry.get()
        new_hw4 = hw4_entry.get()
        new_hw5 = hw5_entry.get()
        new_hw6 = hw6_entry.get()
        new_hw7 = hw7_entry.get()
        new_hw8 = hw8_entry.get()
        new_hw9 = hw9_entry.get()
        new_hw10 = hw10_entry.get()
        new_final_grade = final_grade_entry.get()
        new_status = status_entry.get()

        try:
            conenction = sqlite3.connect('database.db')
            cursor = conenction.cursor()
            sql = "INSERT INTO Students (id, mail, imie, nazwisko, project, lista1, lista2, lista3," \
                  " hw1, hw2, hw3, hw4, hw5, hw6, hw7, hw8, hw9, hw10, grade, status)" \
                  " VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

            params = (newId, new_mail, new_name, new_surname, new_project, new_list1, new_list2, new_list3,
                      new_hw1, new_hw2, new_hw3, new_hw4, new_hw5, new_hw6, new_hw7, new_hw8, new_hw9, new_hw10, new_final_grade, new_status)
            cursor.execute(sql, params)
            conenction.commit()
        except sqlite3.Error as e:
            print(e)
        finally:
            if cursor:
                cursor.close()
            if conenction:
                conenction.close()

        load_data()
        window.destroy()

    addButton = ttk.Button(window, text = "Dodaj", command = add_new)
    addButton.grid()


def deleteStudent():
    window = tk.Toplevel(root)
    window.title("Usuń studenta")

    id_label = ttk.Label(window, text = "id:")
    id_label.pack()
    id_entry = ttk.Entry(window)
    id_entry.pack()

    def delete():
        global cursor, connection
        _id = id_entry.get()
        try:
            connection = sqlite3.connect('database.db')
            cursor = connection.cursor()
            sql = "DELETE FROM Students where id = %s;"
            cursor.execute(sql, tuple(_id))
            connection.commit()
        except sqlite3.Error as e:
            print(e)
        finally:
            if cursor:
                cursor.close()
            if connection:
                connection.close()

            load_data()
            window.destroy()

    add_button = ttk.Button(window, text = "Usuń", command = delete)
    add_button.pack()


def updateStudent():
    window = tk.Toplevel(root)
    window.title("Zmien studenta")

    idLabel = ttk.Label(window, text = "id: ")
    idLabel.grid(row = 0, column = 0)
    idEntry = ttk.Entry(window)
    idEntry.grid(row = 0, column = 1)

    mail_label = ttk.Label(window, text = "Mail:")
    mail_label.grid(row = 1, column = 0)
    mail_entry = ttk.Entry(window)
    mail_entry.grid(row = 1, column = 1)

    name_label = ttk.Label(window, text = "Imie:")
    name_label.grid(row = 2, column = 0)
    name_entry = ttk.Entry(window)
    name_entry.grid(row = 2, column = 1)

    surname_label = ttk.Label(window, text = "Nazwisko:")
    surname_label.grid(row = 3, column = 0)
    surname_entry = ttk.Entry(window)
    surname_entry.grid(row = 3, column = 1)

    project_label = ttk.Label(window, text = "Ocena projektu:")
    project_label.grid(row = 4, column = 0)
    project_entry = ttk.Entry(window)
    project_entry.grid(row = 4, column = 1)

    list1_label = ttk.Label(window, text = "Ocena listy 1:")
    list1_label.grid(row = 5, column = 0)
    list1_entry = ttk.Entry(window)
    list1_entry.grid(row = 5, column = 1)

    list2_label = ttk.Label(window, text = "Ocena listy 2:")
    list2_label.grid(row = 6, column = 0)
    list2_entry = ttk.Entry(window)
    list2_entry.grid(row = 6, column = 1)

    list3_label = ttk.Label(window, text = "Ocena listy 3:")
    list3_label.grid(row = 7, column = 0)
    list3_entry = ttk.Entry(window)
    list3_entry.grid(row = 7, column = 1)

    hw1_label = ttk.Label(window, text = "hw1:")
    hw1_label.grid(row = 8, column = 0)
    hw1_entry = ttk.Entry(window)
    hw1_entry.grid(row = 8, column = 1)

    hw2_label = ttk.Label(window, text = "hw2:")
    hw2_label.grid(row = 9, column = 0)
    hw2_entry = ttk.Entry(window)
    hw2_entry.grid(row = 9, column = 1)

    hw3_label = ttk.Label(window, text = "hw3:")
    hw3_label.grid(row = 10, column = 0)
    hw3_entry = ttk.Entry(window)
    hw3_entry.grid(row = 10, column = 1)

    hw4_label = ttk.Label(window, text = "hw4:")
    hw4_label.grid(row = 11, column = 0)
    hw4_entry = ttk.Entry(window)
    hw4_entry.grid(row = 11, column = 1)

    hw5_label = ttk.Label(window, text = "hw5:")
    hw5_label.grid(row = 12, column = 0)
    hw5_entry = ttk.Entry(window)
    hw5_entry.grid(row = 12, column = 1)

    hw6_label = ttk.Label(window, text = "hw6:")
    hw6_label.grid(row = 13, column = 0)
    hw6_entry = ttk.Entry(window)
    hw6_entry.grid(row = 13, column = 1)

    hw7_label = ttk.Label(window, text = "hw7:")
    hw7_label.grid(row = 14, column = 0)
    hw7_entry = ttk.Entry(window)
    hw7_entry.grid(row = 14, column = 1)

    hw8_label = ttk.Label(window, text = "hw8:")
    hw8_label.grid(row = 15, column = 0)
    hw8_entry = ttk.Entry(window)
    hw8_entry.grid(row = 15, column = 1)

    hw9_label = ttk.Label(window, text = "hw9:")
    hw9_label.grid(row = 16, column = 0)
    hw9_entry = ttk.Entry(window)
    hw9_entry.grid(row = 16, column = 1)

    hw10_label = ttk.Label(window, text = "hw10:")
    hw10_label.grid(row = 17, column = 0)
    hw10_entry = ttk.Entry(window)
    hw10_entry.grid(row = 17, column = 1)

    final_grade_label = ttk.Label(window, text = "Ocena końcowa:")
    final_grade_label.grid(row = 18, column = 0)
    final_grade_entry = ttk.Entry(window)
    final_grade_entry.grid(row = 18, column = 1)

    status_label = ttk.Label(window, text = "Status:")
    status_label.grid(row = 19, column = 0)
    status_entry = ttk.Entry(window)
    status_entry.grid(row = 19, column = 1)

    def update():
        global cursor, connection
        newId = idEntry.get()
        new_mail = mail_entry.get()
        new_name = name_entry.get()
        new_surname = surname_entry.get()
        new_project = project_entry.get()
        new_list1 = list1_entry.get()
        new_list2 = list2_entry.get()
        new_list3 = list3_entry.get()
        new_hw1 = hw1_entry.get()
        new_hw2 = hw2_entry.get()
        new_hw3 = hw3_entry.get()
        new_hw4 = hw4_entry.get()
        new_hw5 = hw5_entry.get()
        new_hw6 = hw6_entry.get()
        new_hw7 = hw7_entry.get()
        new_hw8 = hw8_entry.get()
        new_hw9 = hw9_entry.get()
        new_hw10 = hw10_entry.get()
        new_final_grade = final_grade_entry.get()
        new_status = status_entry.get()

        try:
            connection = sqlite3.connect('database.db')

            cursor = connection.cursor()
            sql = "UPDATE Students SET mail = %s, imie = %s, nazwisko = %s, project = %s, lista1 = %s, lista2 = %s, lista3 = %s," \
                  " hw1 = %s, hw2 = %s, hw3 = %s, hw4 = %s, hw5 = %s, hw6 = %s, hw7 = %s, hw8 = %s, hw9 = %s, hw10 = %s," \
                  " grade = %s, status = %s  WHERE id = %s;"

            params = (new_mail, new_name, new_surname, new_project, new_list1, new_list2, new_list3,
                      new_hw1, new_hw2, new_hw3, new_hw4, new_hw5, new_hw6, new_hw7, new_hw8, new_hw9, new_hw10,
                      new_final_grade, new_status, newId)
            cursor.execute(sql, params)
        except sqlite3.Error as e:
            print(e)
        finally:
            if cursor:
                cursor.close()
            if connection:
                connection.close()

        load_data()

        window.destroy()

    add_button = ttk.Button(window, text = "Zmień", command = update)
    add_button.grid()


addNewStudentButton = tk.Button(root, text = "Dodaj nowoge studenta", command = AddStudent)
addNewStudentButton.config(background = 'green', font = ("Helvetica", 9, 'bold'))

deleteButton = tk.Button(root, text = "Usuń studenta", command = deleteStudent)
deleteButton.config(background = 'red', font = ("Helvetica", 9, 'bold'))

updateButton = tk.Button(root, text = "Zmień dane o studencie", command = updateStudent)
updateButton.config(background = 'yellow', font = ("Helvetica", 9, 'bold'))

treeview.pack()
addNewStudentButton.pack(side = "left", padx = 5, pady = 5)
deleteButton.pack(side = "left", padx = 5, pady = 5)
updateButton.pack(side = "left", padx = 5, pady = 5)

treeview.bind("<Double-1>", open_details_window)
load_data()
root.mainloop()

if __name__ == "__main__":
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''
                CREATE TABLE IF NOT EXISTS Student 
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                mail TEXT,
                imie TEXT,
                nazwisko TEXT,
                project REAL,
                lista1 REAL,
                lista2 REAL,
                lista3 REAL,
                hw1 REAL,
                hw2 REAL,
                hw3 REAL,
                hw4 REAL,
                hw5 REAL,
                hw6 REAL,
                hw7 REAL,
                hw8 REAL,
                hw9 REAL,
                hw10 REAL,
                grade REAL,
                status TEXT)''')
    conn.commit()
    conn.close()