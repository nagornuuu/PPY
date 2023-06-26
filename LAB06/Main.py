import MyLinkedList
import Student

my_list = MyLinkedList.MyLinkedList()
# Dodawanie elementów do listy
my_list.append(3)
my_list.append(1)
my_list.append(4)
my_list.append(1)

# Wyświetlanie listy
print("Lista po dodaniu elementow:")
print(my_list)

# Usuwanie elementów z listy
my_list.delete(1)

# Wyświetlanie listy po usunięciu elementów
print("Lista po usunieciu elementow:")
print(my_list)

# Pobieranie elementow z listy
print("Element o wartosci 3:")
print(my_list.get(3))

# Dodawanie kolejnych elementow do listy w sposob posortowany
my_list.append(2)
my_list.append(5)
my_list.append(0, func=lambda x, y: x > y)

# Wyswietlanie listy po dodaniu kolejnych elementow
print("Lista po dodaniu kolejnych elementów:")
print(my_list)





