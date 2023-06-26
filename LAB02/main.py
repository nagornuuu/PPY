#zad 1 a)
string1 = "Python 2023"
string2 = "Python 2023"
string3 = string1
print(string1 == string2)  #true
print(string2 == string3)  #true
#b)
print(type(string1), hex(id(string1))) #<class 'str'> 0x14de271ea30
print(type(string2), hex(id(string2))) #<class 'str'> 0x14de271ea30
print(type(string3), hex(id(string3))) #<class 'str'> 0x14de271ea30
string3 = "Java 11"
print(string1 == string2) #true
print(string2 == string3) #false
print(type(string1), hex(id(string1))) #<class 'str'> 0x1c0cdf4ea30
print(type(string2), hex(id(string2))) #<class 'str'> 0x1c0cdf4ea30
print(type(string3), hex(id(string3))) #<class 'str'> 0x1c0cdf56430

#zad 2
print("KALKULATORZ")
num1 = float(input("podaj pierwsza liczbe: "))
num2 = float(input("podaj druga liczbe: "))

print("wybiersz opcje: ")
print("1) Dodawanie")
print("2) Odejmowanie")
print("3) Mnozenie")
print("4) Dzielenie")

choice = input("Wybiersz (1, 2, 3, 4): ")

if choice == '1':
    result = num1 + num2
    print(num1, "+", num2, "=", result)
elif choice == '2':
    result = num1 - num2
    print(num1, "-", num2, "=", result)
elif choice == '3':
    result = num1 * num2
    print(num1, "*", num2, "=", result)
elif choice == '4':
    if num2 == 0:
        print("Nie mozna dzielic przec zero")
    else:
        result = num1 / num2
        print(num1, "/", num2, "=", result)
else:
    print("Nieprawidlowa opcja")


#zad 3
print("Witam w ankiecie!")

name = input("Podaj swoje imie i nazwisko: ")
age = input("Ile masz lat?")
gender = input("Jakiej jestes plci?")
hobby = input("Jakie jest twoje hobby?")
city = input("W jakim miastie mieszkasz?")
job = input("Czy pracujesz?")
music = input("Jakiego gatunku muzyki sluchasz?")

print("\nOdpowiedzi: ")
print("Imie i nazwisko: ", name)
print("Wiek: ", age)
print("Plec: ", gender)
print("Hobby: ", hobby)
print("Miasto: ", city)
print("Praca: ", job)
print("Gatunek muzyki: ", music)