import pandas as pd
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split, KFold, cross_val_score, GridSearchCV
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from matplotlib import pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import numpy as np
import ssl

# Wyłączenie weryfikacji certyfikatu SSL -problem z ssl
ssl._create_default_https_context = ssl._create_unverified_context
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
# Nagłówki kolumn:
headers = ["sepal_length", "sepal_width", "petal_length", "petal_width",
           "class"]
# Pobieraniei przypisanie nagłówków:
df = pd.read_csv(url, names = headers)

# Rozdzielenie zmiennych na dane testowe i treningowe
X = df.iloc[:, :-1].values
y = df.iloc[:, -1].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 2023)

# X to lista statystyk liści, Y to lista nazw
## wywołanie nowego modelu
#knn = KNeighborsClassifier(n_neighbors = 5)
## trenowanie modelu - wrzucamy nowe dane
#knn.fit(X_train, y_train)
## walidacja krzyżowa
#kfold = KFold(n_splits = 5, random_state = 2023, shuffle = True)
#scores = cross_val_score(knn, X_train, y_train, cv = kfold, scoring = "accuracy")
#print("Wyniki sprawdzianu krzyżowego:")
#print(scores)
#print(f"Średnia dokładność: {scores.mean()}")
#param_grid = {
#    'n_neighbors': list(range(1, 21)),  # liczba sąsiadów od 1 do 20
#    'metric': ['euclidean', 'manhattan']
#}
#grid_search = GridSearchCV(knn, param_grid, cv = KFold(n_splits = 5,random_state = 2023, shuffle = True))
#grid_search.fit(X_train, y_train)
#results = pd.DataFrame(grid_search.cv_results_)
#print(results)
#print("Najlepsze parametry: ", grid_search.best_params_)
#print("Najlepszy wynik: ", grid_search.best_score_)
#best_model = grid_search.best_estimator_
#best_model = grid_search.best_estimator_
#print(best_model)
#best_predict = best_model.predict(X_test)
#print("Dokładność modelu na zbiorze testowym: ", accuracy_score(y_test, best_predict))
#best_predict_train = best_model.predict(X_train)
#print("Dokładność na zbiorze treningowym: ", accuracy_score(y_train,best_predict_train))
#best_predict = best_model.predict(X_test)
#print("Dokładność na zbiorze testowym: ", accuracy_score(y_test, best_predict))
#cm_train = confusion_matrix(y_train, best_predict_train)
#print("Macierz pomyłek dla zbioru treningowego:")
#print(cm_train)
#report = classification_report(y_train, best_predict_train)
#print(report)

# Inicjalizacja modelu SVM
svm = SVC()

# Trenowanie modelu
svm.fit(X_train, y_train)

# Walidacja krzyżowa
kfold = KFold(n_splits = 5, random_state = 2023, shuffle = True)
scores = cross_val_score(svm, X_train, y_train, cv = kfold, scoring = "accuracy")

print("Wyniki sprawdzianu krzyżowego:")
print(scores)
print(f"Średnia dokładność: {scores.mean()}")

# Strojenie modelu za pomocą GridSearchCV
param_grid = {
    'C': [0.1, 1, 10],
    'kernel': ['linear', 'rbf', 'sigmoid'],
    'gamma': [0.1, 1, 10]
}

grid_search = GridSearchCV(svm, param_grid, cv = KFold(n_splits = 5, random_state = 2023, shuffle = True))
grid_search.fit(X_train, y_train)

# Wyświetlanie wyników strojenia
results = pd.DataFrame(grid_search.cv_results_)
print(results)
results.to_csv("results.csv")
print(results["mean_test_score"])

print("Najlepsze parametry: ", grid_search.best_params_)
print("Najlepszy wynik: ", grid_search.best_score_)
best_model = grid_search.best_estimator_

# Testowanie modelu na zbiorze testowym
best_predict = best_model.predict(X_test)
print("Dokładność modelu na zbiorze testowym: ", accuracy_score(y_test, best_predict))

# Testowanie modelu na zbiorze treningowym
best_predict_train = best_model.predict(X_train)
print("Dokładność modelu na zbiorze treningowym: ", accuracy_score(y_train, best_predict_train))

# Macierz pomyłek dla zbioru treningowego
cm_train = confusion_matrix(y_train, best_predict_train)
print("Macierz pomyłek dla zbioru treningowego:")
print(cm_train)

# Raport klasyfikacji dla zbioru treningowego
report = classification_report(y_train, best_predict_train)
print(report)

# Generowanie raportu w formacie PDF
with PdfPages('raport.pdf') as pdf:
    # Wykres dokładności modelu na zbiorze treningowym i testowym
    plt.figure()
    plt.plot(range(1, 6), scores, marker = 'o')
    plt.xlabel('Fold')
    plt.ylabel('Accuracy')
    plt.title('Cross-Validation Accuracy')
    plt.grid(True)
    pdf.savefig()
    plt.close()

    # Macierz pomyłek dla zbioru treningowego
    plt.figure()
    cm = confusion_matrix(y_train, best_predict_train)
    classes = np.unique(y_train)
    plt.imshow(cm, interpolation = 'nearest', cmap = plt.cm.Blues)
    plt.title('Confusion Matrix - Training Set')
    plt.colorbar()
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation=45)
    plt.yticks(tick_marks, classes)
    plt.xlabel('Predicted Label')
    plt.ylabel('True Label')
    plt.tight_layout()
    for i in range(cm.shape[0]):
        for j in range(cm.shape[1]):
            plt.text(j, i, cm[i, j],
                     horizontalalignment = "center",
                     color = "white" if cm[i, j] > cm.max() / 2. else "black")
    pdf.savefig()
    plt.close()

    # Macierz pomyłek dla zbioru testowego
    plt.figure()
    cm = confusion_matrix(y_test, best_predict)
    classes = np.unique(y_train)
    plt.imshow(cm, interpolation = 'nearest', cmap = plt.cm.Blues)
    plt.title('Confusion Matrix - Test Set')
    plt.colorbar()
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation = 45)
    plt.yticks(tick_marks, classes)
    plt.xlabel('Predicted Label')
    plt.ylabel('True Label')
    plt.tight_layout()
    for i in range(cm.shape[0]):
        for j in range(cm.shape[1]):
            plt.text(j, i, cm[i, j],
                     horizontalalignment = "center",
                     color = "white" if cm[i, j] > cm.max() / 2. else "black")
    pdf.savefig()
    plt.close()

    # Raport klasyfikacji dla zbioru treningowego
    plt.figure()
    plt.text(0.1, 0.5, report, fontsize = 12, verticalalignment = 'center')
    plt.axis('off')
    plt.title('Classification Report - Training Set')
    pdf.savefig()
    plt.close()