import ssl
import sqlite3
import pandas as pd
from sklearn import preprocessing
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import cross_val_score, LeaveOneOut
from sklearn.svm import SVC

class Wine:
    def __init__(self, variables, target):
        self.target = target
        self.variables = variables

    def __repr__(self):
        return f"Wine(variables = {self.variables}, target = {self.target})"

    def get(self):
      return self.target

ssl._create_default_https_context = ssl._create_unverified_context

#Wczytaj dane z adresu podanego w pliku tekstowym: pliktextowy.txt
# do ramki danych.
#Użyj reszty wierszy jako nagłówków ramki danych.
#Uwaga! Zobacz która zmienna jest zmienną objaśnianą, będzie to potrzebne do dalszych zadań.


url = "https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data"
headers = ["TypeOf", "Alcohol", "Malic_acid", "Ash",
           "Alcalinity_of_ash", "Magnesium", "Total_phenols",
           "Flavanoids", "Nonflavanoid_phenols", "Proanthocyanins",
           "Color_intensity", "Hue", "OD280_OD315_of_diluted_wines", "Proline"]

df = pd.read_csv(url, names = headers) # tutaj podmień df. Ma zawierać wczytane dane.


#Zadanie1 przypisz nazwy kolumn z df w jednej linii:   (2pkt)
wynik1 = df.columns.tolist()
print(wynik1)


#Zadanie 2: Wypisz liczbę wierszy oraz kolumn ramki danych w jednej linii.  (2pkt)
wynik2 = f"Liczba wierszy: {df.shape[0]}, Liczba kolumn: {df.shape[1]}"
print(wynik2)


#Zadanie Utwórz klasę Wine na podstawie wczytanego zbioru:
#wszystkie zmienne objaśniające powinny być w liscie.
#Zmienna objaśniana jako odrębne pole.
# metoda __init__ powinna posiadać 2 parametry:
#listę (zmienne objaśniające) oraz liczbę(zmienna objaśniana).
#nazwy mogą być dowolne.


# Klasa powinna umożliwiać stworzenie nowego obiektu na podstawie
# już istniejącego obiektu jak w pdf z lekcji lab6.
# podpowiedź: metoda magiczna __repr__
#Nie pisz metody __str__.


#Zadanie 3 Utwórz przykładowy obiekt:   (3pkt)
wynik3 = Wine([1, 2, 3], 4) #do podmiany. Pamiętaj - ilość elementów, jak w zbiorze danych.
#Uwaga! Pamiętaj, która zmienna jest zmienną objaśnianą
print(wynik3)


#Zadanie 4.                             (3pkt)
#Zapisz wszystkie dane z ramki danych do listy obiektów typu Wine.
#Nie podmieniaj listy, dodawaj elementy.
#Uwaga! zobacz w jakiej kolejności podawane są zmienne objaśniane i objąśniająca.
# Podpowiedź zobacz w pliktextowy.txt
wineList = []
for index, row in df.iterrows():
    list = row[1:].tolist()
    var = row[0]
    wine = Wine(list, var)
    wineList.append(wine)

wynik4 = len(wineList)
print(wynik4)


#Zadanie5 - Weź ostatni element z listy i na podstawie         (3pkt)
#wyniku funkcji repr utwórz nowy obiekt - eval(repr(obiekt))
#do wyniku przypisz zmienną objaśnianą z tego obiektu:
wynik5 = eval(repr(wineList[-1])).target
print(wynik5)


#Zadanie 6:                                                          (3pkt)
#Zapisz ramkę danych  do bazy SQLite nazwa bazy(dopisz swoje imię i nazwisko):
# wines_imie_nazwisko, nazwa tabeli: wines.
#Następnie wczytaj dane z tabeli wybierając z bazy danych tylko wiersze z typem wina nr 3
# i zapisz je do nowego data frame:
wynik6 = "W następnej linijce podmień na nowy  data frame z winami tylko klasy trzeciej:"

connection = sqlite3.connect('wines_Andrii_Nahornyi.db')
df.to_sql('wines', connection, if_exists = 'replace', index = False)
query = "SELECT * FROM wines WHERE TypeOf = 3"
wynik6 = pd.read_sql_query(query, connection)

connection.close()

print(wynik6.shape)


#Zadanie 7                                                          (1pkt)
#Utwórz model regresji Logistycznej z domyślnymi ustawieniami:

model = LogisticRegression()

wynik7 = model.__class__.__name__
print(wynik7)

# Zadanie 8:                                                        (3pkt)
#Dokonaj podziału ramki danych na dane objaśniające i  do klasyfikacji.
#Znormalizuj dane objaśniające za pomocą:
#preprocessing.normalize(X)
# Wytenuj model na wszystkich danych bez podziału na zbiór treningowy i testowy.
# Wykonaj sprawdzian krzyżowy, używając LeaveOneOut() zamiast KFold (Parametr cv)
#  Podaj średnią dokładność (accuracy)

X = df.iloc[:, 1:]
y = df.iloc[:, 0]
X_normalized = preprocessing.normalize(X)
model = LogisticRegression()
model.fit(X_normalized, y)

scores = cross_val_score(model, X_normalized, y, cv = LeaveOneOut(), scoring = "accuracy")
wynik8 = scores.mean()
print(wynik8)