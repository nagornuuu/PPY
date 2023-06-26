import sys
import wikipediaapi

string = "Ala ma kota"

chars = []
for c in string:
    chars.append(c)

#krotsza wersja
#chars = [ c for c in string]

words = string.split()
word_counts = []
for w in words:
    word_counts.append( len(w))

#krotsza wersja
#word_counts = [ len(w) for w in words]

string = "Ala ma kota"
chars = [ c for c in string if c.isalpha()]

liczby = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
parzyste = [x for x in liczby if x % 2 == 0]
print(parzyste)

print()

list1 = [1, 2, 3, 4, 5]
list2 = [10, 20, 30, 40, 50]
result = [ e1 * e2 for e1 in list1 for e2 in list2 ]
print(result)

print()

result2 = [list1[i] * list2[i] for i in range(len(list1))]
print(result2)

print()

keys = ['student1', 'student2', 'student3']
values = [5, 5, 4]
dictionary = {keys[i]: values[i] for i in range(len(keys))}
print(dictionary)

lista = ["a", "b", "c"]
for e in lista:
    print(e)

print()

iterator = iter(lista)
while True:
    try:
        e = next(iterator)
        print(e)
    except StopIteration:
        print("StopIteration")
        break


class ListIterator:
    def __init__(self, lista):
        self.lista = lista
        self.index = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.index >= len(self.lista):
            raise StopIteration
        else:
            e = self.lista[self.index]
            self.index += 1
            return e

class Stack:

    def __init__(self, max_size=5):
        self.items = []
        self.max_size = max_size

    def push(self, item):
        if len(self.items) < self.max_size:
            self.items.append(item)
        else:
            raise IndexError("Stack overflow")

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

print()

s = Stack()
s.push(1)
s.push(2)
s.push(3)
print(s.pop())              #3
print()

for e in s:
  print(e)

print()

generator = (x for x in range(10000))
size_generator = sys.getsizeof(generator)

list_comp = [x for x in range(10000)]
size_list_comp = sys.getsizeof(list_comp)
print("generator:", size_generator, "bajtow")
print("list comprehension:", size_list_comp, "bajtow")

print()

s.push(1)
s.push(2)
s.push(3)

stack_iter = iter(s)

print(next(stack_iter))
print(next(stack_iter))
print(next(stack_iter))

print()

def even_numbers(max=6):
    number = 0
    while number <= 6:
        yield number
        number += 2

gen = even_numbers()
print(type(gen))
print()
print(next(gen))
print()
print("___________")
gen = even_numbers()
for e in gen:
    print(e)

print()

def read_wiki_titles(filename):
    with open(filename, 'r') as file:
        for line in file:
            yield line.string()


def read_titles(filename):
    with open(filename, 'r') as file:
        for line in file:
            yield line.strip()


title_generator = read_titles("small.txt")
for t in title_generator:
    print(t)

print()

def get_article(title):
    w_api = wikipediaapi.Wikipedia('en')
    page = w_api.page(title)
    if page.exists():
        return page.text
    else:
        return ""

title_generator = read_titles("small.txt")
title = next(title_generator)
art = get_article(title)
print(art)