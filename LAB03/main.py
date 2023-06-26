import random
import getpass

# print(random.randint(0,10))
# import getpass
# choice = getpass.getpass('wybor: ')
# print(choice)
## komentarze
## nie ma
## wielu
## wierzy
#
# '''
#    tekst
#    tekst2
# '''
#
# temperature = float(input("pomiar temperatury: "))

# if temperature < 28 or temperature > 41:
#    print("uwaga zagrozenie zycia!")
# else:
#    print("temp: " + str(temperature))

# my_pressure = input("pomiar temperatury: ")
# my_symptom = input("objawy: ")

# pressure = "180/110"
# symptom = "bol w klatce piersiowej"

# if my_pressure == pressure and my_symptom == symptom:
#    print("wezwac pogotowie!")
# else:
#    ("...nadcisinienie")

# while True:
#    dane = input("podaj liczbe /(end konczy)")
#    if dane == "end":
#        print("koniec!")
#        break
#    print(dane)

# i = 0
# while i < 10:
#    print(i)
#    i += 1

# i = 0
# while i < 10:
#    if i == 5:
#        break
#    print(i)
#    i += 1
#
# i = 0
# while i < 10:
#    i += 1
#    if i == 5:
#        continue
#    print(i - 1)
#
# for i in range(0, 10):
#    if i == 5:
#        continue
#    print("for loop : " + str(i))
#
# for i in range(0, 10, 2):
#    if i == 5:
#        continue
#    print("for loop 2: " + str(i))
#
# moja_lista = ["Warszawa","Krakow","Wroclaw","Lodz","Poznan","Gdansk","Szczecin","Bydgosz","Lublin", "Bialystok"]
#
# index = 0
# moja_lista[index] = "Warszawa2"
# print(moja_lista[index])
#
# moja_lista.append("Plock")
# print(moja_lista)
#
# moja_lista.insert(0, "Warszawa")
# print(moja_lista)
#
# del moja_lista[len(moja_lista) - 1]
# print(moja_lista)
#
# print(moja_lista.pop())
# print(moja_lista)
# print(moja_lista.pop(1))
# print(moja_lista)
# moja_lista[-1] = 'Bialystok'
# print(moja_lista)
# to_insert = moja_lista.index('Bialystok')
# moja_lista.insert(to_insert, "Lublin")
# print(moja_lista)
#
# print(moja_lista.remove("Lodz"))
#
# moja_lista.extend( ["Lodz", "nowa", "nowa"])
# print(moja_lista)
#
# miasto = "Lodzzzz"
# if miasto in moja_lista:
#    moja_lista.remove(miasto)
# else:
#    print("brak")
#
# miasto = "nowaa"
# while miasto in moja_lista:
#    moja_lista.remove(miasto)
# print(moja_lista)
#
# moja_lista[len(moja_lista) - 1]
#
# for element in moja_lista:
#    print(element)
#
##len, min, max, sum
# print(max(moja_lista))
#
# cities = "Warszawa, Krakow, Wroclaw, lodz, poznan, gdansk, szczecin, bydgoszcz, lublin, bialystok"
# moja_lista = cities.split(",")

# zad 1
liczby = input("Podaj liczbe rozdielone przecinkiem: ")
liczby_list = liczby.split(",")

num_list = []
for liczby in liczby_list:
    num_list.append(int(liczby))

max_num = num_list[0]
min_num = num_list[0]
for num in num_list:
    if num > max_num:
        max_num = num
    if num < min_num:
        min_num = num

print("Najwieksza liczba: ", max_num)
print("Najmniejsza liczba: ", min_num)

# zad 2
# Napisz program, który wyświetli plan wycieczki – wybierając losowo z listy 10 największych miast w Polsce miasta do odwiedzenia.
# Miast ma być 10, nie mogą się powtarzać. (20%)

cities = ["Warszawa", "Krakow", "Wroclaw", "Lodz", "Poznan", "Gdansk", "Szczecin", "Bydgosz", "Lublin", "Bialystok"]
cityToVisit = []

while len(cityToVisit) < 10:
    city = random.choice(cities)
    if city not in cityToVisit:
        cityToVisit.append(city)

print("plan wycieczki: ")
for i, city in enumerate(cityToVisit):
    print(i + 1, city)

# zad 3
# Napisz grę – papier nożyce kamień. (60%) Gra pozwoli wybrać ilość rund. Pozwoli wybrać tryb gry – komputer / 2 graczy (hot seats)
# Pozwoli nazwać graczy. Zapamięta wynik z każdej rundy. Na koniec wyświetli listę wyników oraz ostateczny wynik z informacją,
# który gracz wygrał. W opcji hot seats należy użyć getpass


print("Witaj w grze Papier, Nozyce, Kamien!")

while True:
    num_rounds = int(input("Ile rund chcesz zagrac? (1-5): "))
    if num_rounds not in [1, 2, 3, 4, 5]:
        print("niepoprawna wartosc, wpisz ponowie: ")
    else:
        break

while True:
    tryb = int(input("Wybierz tryb gry -  komputer (1) / 2 graczy (2) "))
    if tryb == 1 or tryb == 2:
        break
    else:
        print("niepoprawna wartosc, wpisz ponowie: ")

if tryb == 1:
    player1 = input("Player 1, wpisz swoje imie: ")
    player2 = "Komputer"
else:
    player1 = input("Player 1, wpisz swoje imie: ")
    player2 = input("Player 2, wpisz swoje imie: ")

results = {player1: 0, player2: 0}

for i in range(num_rounds):
    print("Runda " + str(i + 1) + ":")

    if tryb == 2:
        while True:
            choice1 = getpass.getpass(player1 + ", podaj swoj wybor(1 - papier, 2 - nozyce, 3 - kamien): ")
            print(player1 + " wybrał " + choice1)
            if choice1 == '1' or choice1 == '2' or choice1 == '3':
                break
            else:
                print("Niepoprawny wybor, wpisz ponownie")
        while True:
            choice2 = getpass.getpass(player2 + ", podaj swoj wybor(1 - papier, 2 - nozyce, 3 - kamien): ")
            print(player2 + " wybieral " + choice2)
            if choice2 == '1' or choice2 == '2' or choice2 == '3':
                break
            else:
                print("Niepoprawny wybor, wpisz ponownie")
    else:
        choice1 = getpass.getpass(player1 + ", podaj swoj wybor(1 - papier, 2 - nozyce, 3 - kamien): ")
        print(player1 + " wybrał " + choice1)
        choice2 = random.choice(['1', '2', '3'])
        print(player2 + " wybieral " + choice2)

    if choice1 == choice2:
        print("Remis")
    elif (choice1 == '1' and choice2 == '2') or \
            (choice1 == '2' and choice2 == '3') or \
            (choice1 == '3' and choice2 == '1') or \
            (choice2 == '1' and choice1 == '3') or \
            (choice2 == '3' and choice1 == '2') or \
            (choice2 == '2' and choice1 == '1'):
        winner = player2
    else:
        winner = player1

        results[winner] += 1
        print("Wygrywa: ", winner)

        print("Wyniki: ")
        for player, score in results.items():
            print(player + ": " + str(score))

        if results[player1] > results[player2]:
            print(player1 + " wygrał grę!")
        elif results[player1] < results[player2]:
            print(player2 + " wygrał grę!")
        else:
            print("Remis!")
