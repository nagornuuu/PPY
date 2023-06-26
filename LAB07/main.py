import tkinter as tk
from tkinter import ttk
import mysql
from mysql import connector

root = tk.Tk()
treeview = ttk.Treeview(root)
treeview["columns"] = ("id", "title", "author", "price", "category")
treeview.column("#0", width=0)
treeview.heading("id", text="ID")
treeview.heading("title", text="Tytuł")
treeview.heading("author", text="Autor")
treeview.heading("price", text="Cena")
treeview.heading("category", text="Kategoria")


def open_details_window(event):  # Pobranie zaznaczonego elementu
    selected_item = treeview.focus()
    if selected_item:
        item_data = treeview.item(selected_item)
        values = item_data['values']
        print(values)


def connect():
    return mysql.connector.connect(
        host="db4free.net",
        user="",
        password="",
        database="")


def fetch_data() -> list[tuple]:
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("select * from books;")
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result


def load_data():
    data = fetch_data()

    treeview.delete(*treeview.get_children())
    for row in data:
        treeview.insert("", "end", values=(row[0], row[1], row[2], row[3], row[4]))


def open_add_new_book_window():
    pass


def open_new_book_window():
    new_window = tk.Toplevel(root)
    new_window.title("Dodaj nową książkę")

    title_label = ttk.Label(new_window, text="Tytuł:")
    title_label.pack()
    title_entry = ttk.Entry(new_window)
    title_entry.pack()

    author_label = ttk.Label(new_window, text="Autor:")
    author_label.pack()
    author_entry = ttk.Entry(new_window)
    author_entry.pack()

    price_label = ttk.Label(new_window, text="Cena:")
    price_label.pack()
    price_entry = ttk.Entry(new_window)
    price_entry.pack()

    category_label = ttk.Label(new_window, text="Kategoria:")
    category_label.pack()
    category_entry = ttk.Entry(new_window)
    category_entry.pack()

    def add_new():
        title = title_entry.get()
        author = author_entry.get()
        price = price_entry.get()
        category = category_entry.get()
        try:
            conn = connect()

            cursor = conn.cursor()
            sql = "INSERT INTO books (title, author, price, category) VALUES (%s,%s,%s,%s);"

            params = (title, author, price, category)
            cursor.execute(sql, params)
            conn.commit()
        except Exception as e:
            print(e)
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

        load_data()

        new_window.destroy()

    add_button = ttk.Button(new_window, text="Dodaj", command=add_new)
    add_button.pack()


def open_delete_book_window():
    new_window = tk.Toplevel(root)
    new_window.title("Usuń książkę")

    id_label = ttk.Label(new_window, text="ID:")
    id_label.pack()
    id_entry = ttk.Entry(new_window)
    id_entry.pack()

    def delete():
        _id = id_entry.get()

        conn = connect()

        cursor = conn.cursor()
        sql = "delete from books where id = %s;"

        cursor.execute(sql, tuple(_id))
        conn.commit()
        cursor.close()
        conn.close()

        load_data()

        new_window.destroy()

    add_button = ttk.Button(new_window, text="Usuń", command=delete)
    add_button.pack()


def open_update_book_window():
    new_window = tk.Toplevel(root)
    new_window.title("Usuń książkę")

    id_label = ttk.Label(new_window, text="ID:")
    id_label.pack()
    id_entry = ttk.Entry(new_window)
    id_entry.pack()

    title_label = ttk.Label(new_window, text="Tytuł:")
    title_label.pack()
    title_entry = ttk.Entry(new_window)
    title_entry.pack()

    author_label = ttk.Label(new_window, text="Autor:")
    author_label.pack()
    author_entry = ttk.Entry(new_window)
    author_entry.pack()

    price_label = ttk.Label(new_window, text="Cena:")
    price_label.pack()
    price_entry = ttk.Entry(new_window)
    price_entry.pack()

    category_label = ttk.Label(new_window, text="Kategoria:")
    category_label.pack()
    category_entry = ttk.Entry(new_window)
    category_entry.pack()

    def update():
        _id = id_entry.get()
        title = title_entry.get()
        author = author_entry.get()
        price = price_entry.get()
        category = category_entry.get()

        conn = connect()

        cursor = conn.cursor()
        sql = "update books set title = %s, author = %s, price = %s, category = %s where id = %s;"

        cursor.execute(sql, (title, author, price, category, _id))
        conn.commit()
        cursor.close()
        conn.close()

        load_data()

        new_window.destroy()

    add_button = ttk.Button(new_window, text="Zmień", command=update)
    add_button.pack()


add_new_book = tk.Button(root, text="Dodaj książkę", command=open_new_book_window)
delete_button = tk.Button(root, text="Usuń książkę", command=open_delete_book_window)
delete_button.config(background='red', font=("Helvetica", 9, 'bold'))
update_button = tk.Button(root, text="Zmień książkę", command=open_update_book_window)

treeview.pack(side='top')
add_new_book.pack(side='left', padx=5, pady=5)
delete_button.pack(side='left', padx=5, pady=5)
update_button.pack(side='left', padx=5, pady=5)

treeview.bind("<Double-1>", open_details_window)

load_data()

root.mainloop()