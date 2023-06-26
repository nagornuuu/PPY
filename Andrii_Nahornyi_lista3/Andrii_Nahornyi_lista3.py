# Zadanie 1 (4pkt):
# Utwórz klasę iteratora dla listy. Użyj go do wstawienia elementów listy lista1 do strina.
# elementy mają znajdować się w stringu jednym wierszu niczym nierozdzielone:
lista1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]


class ListIterator:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        item = self.data[self.index]
        self.index += 1
        return item


iterator = ListIterator(lista1)
wynik1 = "".join(str(item) for item in iterator)

print(wynik1)


# Zadanie2: (4pkt)
# Napisz funkcję fizzbuzz(n), która używając listy składanej zwróci
# listę od 1 do n włącznie liczb lub wyrazów Fizz, Buzz, FizzBuzz, zgodnie ze standradową
# reguła gry w FizzBuzz:
# Jeśli liczba jest podzielna przez 3 i niepodzielna przez 5, zamiast liczby mamy "Fizz".
# Jeśli liczba jest podzielna przez 5 i niepodzielna przez 3, zamiast liczby mamy "Buzz".
# Jeśli liczba jest zarówno podzielna przez 3, jak i przez 5, zamiast liczby mamy "FizzBuzz".


def fizbuzz(n):
    return ['Fizz' if i % 3 == 0 and i % 5 != 0 else
            'Buzz' if i % 5 == 0 and i % 3 != 0 else
            'FizzBuzz' if i % 3 == 0 and i % 5 == 0 else
            i for i in range(1, n + 1)]


wynik2 = fizbuzz(16)
print(wynik2)


# Zadanie 3 (4pkt):
# Napisz generator zwracający n wyrazów ciągu Lucasa
# do wyniku zapisz 6 element tego ciągu.

def lucas(n=6):
    a, b = 2, 1
    for i in range(n):
        yield a
        a, b = b, a + b


lucastab = []

for number in lucas(6):
    lucastab.append(number)

wynik3 = lucastab[5]
print(wynik3)


# Zadanie4 (4pkt):
# Uzyj klasy napisanej na ostatnich zajęciach - wersji z iteratorem (wklej tutaj klasę)
# Do przechowywania znaków kodu javy z pliku Main.java.

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Stack is empty")

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def __iter__(self):
        return self

    def __next__(self):
        if not self.is_empty():
            return self.pop()
        else:
            raise StopIteration


def read_lines(filename):
    with open(filename, 'r') as file:
        for line in file:
            yield line


linereader = read_lines('Main.java')
obiekt = Stack()

for line in linereader:
    for char in line:
        obiekt.push(char)

wynik4 = "wstaw w wynik4"
# następnie wstaw do niej znaki z kodu javy, które wczytasz z pliku Main.java
# ODKOMENTUJ poniższą linijkę, gdy utworzysz obiekt i dodasz do niego znaki:
'''
!odkomentuj wynik4!:
'''
wynik4 = obiekt.size()
print(wynik4)


# Zadanie 5 (4pkt):
# Napisz funkcję, która sprawdzi poprawność kodu javy, używając obiektu z poprzedniego zadania
# i uwzględniając tylko nawiasy w kodzie.
# funkcja ma zwrocic True albo False w zależności czy kod jest poprawny czy nie.

def validation(kod_o):
    s = Stack()
    opens = ['(', '{', '[', '<']
    closes = [')', '}', ']', '>']

    for i in kod_o:
        if i in opens:
            s.push(i)
        elif i in closes:
            if s.is_empty():
                return False
            top = s.pop()
            if opens.index(top) != closes.index(i):
                return False

    if s.is_empty():
        return True
    else:
        return False


wynik5 = validation(kod_o = obiekt)
print(wynik5)
