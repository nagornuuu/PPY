import math

#Przyklad 1
#def my_fucntion():
#    print("Hello world")
#my_fucntion()

#przyklad 2
#def my_fucntion_with_parameter(name):
#    print(f"hello {name}")
#my_fucntion_with_parameter("Lukasz")

#pryzklad 3
#def my_function_with_parameters(name,surname):
#    print(f"Hello {name} {surname}")
#my_function_with_parameters("Lukasz", "Kwasniewicz")
#my_function_with_parameters("kwasniewicz", "Lukasz")
#my_function_with_parameters(surname = "Kwasniewicz", name = "Lukasz")

#pryzklad 4
#def my_function_default(surname, name = "Alice"):
#    print(f"hello {name} {surname}")
#my_function_default(surname = "Kwasniewicz", name = "Bob")

#pryzklad 5
#def my_function_default(surname, name, middle = ''):
#    person_data = name
#    if middle:
#        person_data += " " + middle
#    person_data += " " + surname
#    print(f"hello {person_data}")
#my_function_default(surname = "Doe", name = "Alice", middle = "Joe")

#pryzklad 6
#def my_function_default2(surname, name, middle = ''):
#    person_data = name
#    if middle:
#        person_data += " " + middle
#    person_data += " " + surname
#    return person_data
#person_info = my_function_default2(surname = "Doe", name = "Alice", middle = "Joe")
#print("hello " + person_info)

#pryzklad 7
#names = ["Alice", "Bob"]
#print(names)
#def hello_list(names):
#    for i in range(0, len(names)):
#        names[i] = "hello " + names[i]
#hello_list(names)
#print(names)

#pryzklad 8
#def hello_multiply(*people, lang):
#    greet = ""
#    if lang == "PL":
#        greet = "Witaj"
#    elif lang == "FR":
#        greet = "Bonjour"
#    for p in people:
#        print(f"{greet} {p}")
#hello_multiply("PL", "Alice", "Bob", "Lukasz", lang = "PL")

#zad 1
def zad1(floor_length, floor_width, panel_length, panel_width, number_of_panels_in_package):
    p_floor = floor_length * floor_width
    p_place = p_floor * 1.1
    p_panel = panel_width * panel_length
    number_of_panel = math.ceil(p_place / p_panel)
    number_of_package = math.ceil(number_of_panel / number_of_panels_in_package)
    return number_of_package
print("Potrzeba : " + str(zad1(4, 4, 0.20, 1, 10)))

#zad 2
def zad2(*numbers):
    for i in numbers:
        if i < 2:
            print(f"{i} is not prime")
        else:
            for n in range(2, i):
                if (i % n) == 0:
                    print(f"{i} is not prime")
                    break
            else:
                print(f"{i} is prime number")
zad2(0, 1, 2, 3, 4, 5)

#zad 3
def zad3(message, key, alphabet=''):
    message = message.lower()
    if not alphabet:
        alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i','j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    result = ""
    for char in data:
        if char in alphabet:
            index = alphabet.index(char)
            new_position = (index + key) % len(alphabet)
            result += alphabet[new_position]
        else:
            result += char
    return result

data = "The Project Gutenberg eBook of Alice’s Adventures in Wonderland, by Lewis Carroll"
enc = zad3(data, 5)
print(enc)

enc = zad3(data, 3, ["a", "B"])
print(enc)
