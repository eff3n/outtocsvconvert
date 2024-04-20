# Instrukcja uruchomienia skryptu w środowisku wirtualnym

## Wymagane zależności
- Python 3.7 lub nowszy
- numpy
- pandas

Zainstalować je można za pomocą:

```
pip install numpy pandas
```

## Instalacja zależności
1. Utwórz środowisko wirtualne: `python3 -m venv venv`
2. Aktywuj środowisko wirtualne:
   - Na Windows: `venv\Scripts\activate`
   - Na Unix lub MacOS: `source venv/bin/activate`
3. Zainstaluj wymagane zależności: `pip install numpy pandas`

## Uruchomienie skryptu
Po zainstalowaniu zależności, utwórz katalog input_files w tym samym katalgu co skrypt i wrzuć do niego pliki z rozszerzeniem .out. Następnie możesz uruchomić skrypt za pomocą polecenia: `python converter.py`

## Deaktywacja środowiska wirtualnego
Po zakończeniu pracy, możesz deaktywować środowisko wirtualne za pomocą polecenia: `deactivate`
