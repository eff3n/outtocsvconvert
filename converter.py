import os
import numpy as np
from datetime import datetime
import pandas as pd

# Określ katalog, w którym znajdują się pliki .out
input_dir = r"input_files"

# Pobierz listę wszystkich plików .out w katalogu
file_list = [f for f in os.listdir(input_dir) if f.endswith('.out')]

# Poproś użytkownika o podanie liczby iteracji do wyboru
iterations = input("Wpisz liczbę badanych iteracji (ENTER dla wartości domyślnej - 50): ")
iterations = int(iterations) if iterations else 50

# Zainicjuj listę do przechowywania danych wyjściowych
output_data = []

# Przeiteruj przez każdy plik
for file_name in file_list:
    # Otwórz plik wejściowy
    with open(os.path.join(input_dir, file_name), 'r') as input_file:
        # Przeczytaj wszystkie linie z pliku
        lines = input_file.readlines()
        
        # Znajdź wiersz, który zawiera nazwy zmiennych
        for i, line in enumerate(lines):
            if line.strip().split()[0] == '1':
                variable_names = lines[i-1].strip().split()[1:]
                break
        
        variable_names = [var.strip('\"') if var != variable_names[-1] else var[:-3].strip('\"') for var in variable_names]

        
        # Pobierz dane z ostatnich 'iterations' wierszy
        data = []
        for line in lines[-iterations:]:
            try:
                row = list(map(float, line.strip().split()[1:]))
                data.append(row)
            except ValueError as e:
                print(f"Pomijam linię z powodu błędu: {e}")
        
        # Oblicz średnią z wybranych wierszy
        means = np.mean(data, axis=0)
        
        # Pobierz aktualną datę i czas
        now = datetime.now()
        date_time = now.strftime("%m/%d/%Y, %H:%M:%S")

        # Utwórz DataFrame z nazwami zmiennych i średnią
        df = pd.DataFrame([list(means)], columns=variable_names)
        df.insert(0, 'Nazwa pliku', file_name)
        df.insert(1, 'Badane iteracje', iterations)
        df.insert(2, 'Data wykonania', date_time)

        # Dodaj DataFrame do danych wyjściowych
        output_data.append(df)

# Otwórz plik wyjściowy
with open('wynik.csv', 'w') as f:
    # Zapisz każdy DataFrame do pliku
    for df in output_data:
        df.to_csv(f, index=False)

# Wydrukuj komunikat o powodzeniu
print("Plik z wynikiem utworzony.")
