import sqlite3
import tkinter as tk
from tkinter import ttk
import mysql.connector

root = tk.Tk()
root.title("Book Store")
root.iconbitmap("./bookshelf.ico")


#Pobranie danych z tabeli
def fetch_data():

    connection = mysql.connector.connect(
        host = "db4free.net",
        user = "s24918",
        password = "",
        database = "s24918database"
    )

    cursor = connection.cursor()
    cursor.execute("SELECT * FROM books")
    result = cursor.fetchall()
    cursor.close()                                  # Zamknięcie kursora
    connection.close()                                # Zamknięcie połączenia
    return result


def load_data():

    data = fetch_data()

    # Usunięcie poprzednich danych
    treeview.delete(*treeview.get_children())

    # Dodanie nowych danych
    for row in data:
        treeview.insert("", "end", values = (row[0], row[1], row[2], row[3], row[4]))


def open_new_book_window():

    window = tk.Toplevel(root)
    window.title("Dodaj nową książkę")

    title_label = ttk.Label(window, text = "Tytuł:")
    title_label.pack()
    title_entry = ttk.Entry(window)
    title_entry.pack()

    author_label = ttk.Label(window, text = "Autor:")
    author_label.pack()
    author_entry = ttk.Entry(window)
    author_entry.pack()

    price_label = ttk.Label(window, text = "Cena:")
    price_label.pack()
    price_entry = ttk.Entry(window)
    price_entry.pack()

    category_label = ttk.Label(window, text = "Kategoria:")
    category_label.pack()
    category_entry = ttk.Entry(window)
    category_entry.pack()

    def add_new():
        title = title_entry.get()
        author = author_entry.get()
        price = price_entry.get()
        category = category_entry.get()

        connection = mysql.connector.connect(
            host = "db4free.net",
            user = "s24918",
            password = "",
            database = "s24918database"
        )

        cursor = connection.cursor()
        sql = "INSERT INTO books (title, author, price, category) VALUES (%s, %s, %s, %s)"

        params = (title, author, price, category)
        cursor.execute(sql, params)
        connection.commit()      # Zapisanie zmian w bazie
        cursor.close()           # Zamknięcie kursora
        connection.close()       # Zamknięcie połączenia

        load_data()

        # Zamknięcie okna po zapisaniu zmian
        window.destroy()


    add_button = ttk.Button(window, text = "Dodaj", command = add_new)
    add_button.pack()


def open_details_window(event):

    # Pobranie zaznaczonego elementu
    selected = treeview.focus()

    if selected:

        # Pobranie danych z zaznaczonego elementu
        item_data = treeview.item(selected)
        item_values = item_data["values"]

        # Tworzenie nowego okna
        window = tk.Toplevel(root)
        window.title("Szczegóły")

        # Tworzenie i wyświetlanie widgetów opartych na danych z zaznaczonego elementu
        id_label = ttk.Label(window, text = "ID:")
        id_label.pack()
        id_entry = ttk.Entry(window)
        id_entry.insert(0, item_values[0])
        id_entry.config(state = "disabled")     #Uniemożliwienie zmiany id
        id_entry.pack()

        title_label = ttk.Label(window, text = "Tytuł:")
        title_label.pack()
        title_entry = ttk.Entry(window)
        title_entry.insert(0, item_values[1])
        title_entry.pack()

        author_label = ttk.Label(window, text = "Autor:")
        author_label.pack()
        author_entry = ttk.Entry(window)
        author_entry.insert(0, item_values[2])
        author_entry.pack()

        price_label = ttk.Label(window, text = "Cena:")
        price_label.pack()
        price_entry = ttk.Entry(window)
        price_entry.insert(0, item_values[3])
        price_entry.pack()

        category_label = ttk.Label(window, text = "Kategoria:")
        category_label.pack()
        category_entry = ttk.Entry(window)
        category_entry.insert(0, item_values[4])
        category_entry.pack()

        def update():
            title = title_entry.get()
            author = author_entry.get()
            price = price_entry.get()
            category = category_entry.get()
            id = id_entry.get()

            connection = mysql.connector.connect(
                host = "db4free.net",
                user = "s24918",
                password = "",
                database = "s24918database"
            )

            cursor = connection.cursor()
            sql = "UPDATE books SET title=%s, author=%s, price=%s, category=%s WHERE id=%s"
            params = (title, author, price, category, id)
            cursor.execute(sql, params)
            connection.commit()
            cursor.close()
            connection.close()
            load_data()
            window.destroy()

        update = ttk.Button(window, text = "Aktualizuj", command = update)
        update.pack()

        def delete():
            connection = mysql.connector.connect(
                host="db4free.net",
                user="s24918",
                password="",
                database="s24918database")

            cursor = connection.cursor()
            params = (id_entry.get(),)
            sql = "DELETE FROM books WHERE id=%s"
            cursor.execute(sql,params)

            connection.commit()
            cursor.close()
            connection.close()

            load_data()
            window.destroy()


        update = ttk.Button(window, text = "Usun", command = delete)
        update.pack()


add_new_book_button = tk.Button(root, text = "Dodaj nową książkę", command = open_new_book_window)

# Utworzenie widżetu Treeview
treeview = ttk.Treeview(root)
treeview["columns"] = ("id", "title", "author", "price", "category")
treeview.column("#0", width = 0)
treeview.heading("id", text = "ID")
treeview.heading("title", text = "Tytuł")
treeview.heading("author", text = "Autor")
treeview.heading("price", text = "Cena")
treeview.heading("category", text = "Kategoria")
treeview.bind("<Double-1>",open_details_window)


# Wyświetlenie widżetu Treeview
treeview.pack()

add_new_book_button.pack(side = "left")

#Wywołanie funkcji wczytującej dane
load_data()
root.mainloop()


def add_book(title, author, price, category):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Books (title, author, price, category) VALUES = (?, ?, ?, ?)",
    (title, author, price, category))

    conn.commit()
    conn.close()


def create_book(title, author, price, category):
    try:
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Books (title, author, price, category)"
                       " VALUES (?, ?, ?, ?)",
                        (title, author, price, category))
        conn.commit()
    except sqlite3.Error as e:
        print(f"Error: {e}")
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()


if __name__ == "__main__":
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS Books (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            title TEXT,
                            author TEXT,
                            price REAL,
                            category TEXT
                    )''')
    conn.commit()
    conn.close()
   # create_book("s24918database.db","Book 1", "Author 1", 9.99, "Fiction")