import math
import numpy as np
import matplotlib.pyplot as plt

def wybierz_funkcje():
    """
    Funkcja umożliwiająca użytkownikowi wybór funkcji matematycznej.
    """
    nazwy_funkcji = ["x+11", "|x|", "3x^4-4x^3+2x^2-3x+4", "sin(x)", "(-x+4)*cos(x)", "6|x|*cos(x)", "|3sin(6x)+4|", "|4xlog(|x|, 7)|"]
    print("Wybierz funkcję:")
    for i, nazwa in enumerate(nazwy_funkcji, start=1):
        print(f"[{i}] {nazwa}")
    while True:
        try:
            wybor = int(input("\nWybieram: "))
            if wybor not in range(1, len(nazwy_funkcji) + 1):
                raise ValueError
            return wybor
        except ValueError:
            print("Błędny wybór! Wprowadź liczbę odpowiadającą funkcji.")

def wczytaj_zakres():
    """
    Funkcja wczytująca zakres dla interpolacji.
    """
    while True:
        try:
            poczatek, koniec = map(float, input("\nWprowadz zakres (oddzielając wartości spacją): ").split())
            if poczatek >= koniec:
                raise ValueError
            return poczatek, koniec
        except ValueError:
            print("Błędny zakres! Upewnij się, że wartość początkowa jest mniejsza niż wartość końcowa.")

def wczytaj_krok_interpolacji():
    """
    Funkcja wczytująca krok interpolacji.
    """
    while True:
        try:
            krok = float(input("\nWprowadz krok interpolacji: "))
            if krok <= 0:
                raise ValueError
            return krok
        except ValueError:
            print("Błędny krok interpolacji! Krok musi być liczbą dodatnią.")

def wczytaj_liczbe_wezlow():
    """
    Funkcja wczytująca liczbę węzłów dla interpolacji.
    """
    while True:
        try:
            liczba_wezlow = int(input("\nWprowadz ilosc wezlow: "))
            if liczba_wezlow <= 0:
                raise ValueError
            return liczba_wezlow
        except ValueError:
            print("Błędna liczba wezłów! Podaj liczbę całkowitą większą od zera.")

def oblicz_wartosci_funkcji(poczatek, koniec, wybor, krok):
    """
    Funkcja obliczająca wartości funkcji w zadanym zakresie.
    """
    x_wartosci = np.arange(poczatek, koniec, krok)
    y_wartosci = [funkcje_matematyczne[wybor - 1](x) for x in x_wartosci]
    return x_wartosci, y_wartosci

def oblicz_wspolrzedne_wezlow(liczba_wezlow, poczatek, koniec):
    """
    Funkcja obliczająca współrzędne węzłów Czebyszewa.
    """
    wezly = []
    for i in range(liczba_wezlow):
        x = math.cos(math.pi * (2 * i + 1) / (2 * liczba_wezlow + 1))
        x = (((koniec - poczatek) * x) + (poczatek + koniec)) * 0.5
        wezly.append(x)
    return wezly

def oblicz_wartosci_wezlow(wezly, wybor):
    """
    Funkcja obliczająca wartości funkcji w węzłach interpolacji.
    """
    wartosci_wezlow = [funkcje_matematyczne[wybor - 1](x) for x in wezly]
    return wartosci_wezlow

def interpolacja_lagrangea(wezly, wartosci_wezlow, poczatek, koniec, krok):
    """
    Funkcja wykonująca interpolację Lagrange'a.
    """
    x_interpolacji = np.arange(poczatek, koniec, krok)
    y_interpolacji = []
    for i in x_interpolacji:
        y = 0
        for j, wezel_j in enumerate(wezly):
            iloczyn = wartosci_wezlow[j]
            for k, wezel_k in enumerate(wezly):
                if j != k:
                    iloczyn *= ((i - wezel_k) / (wezel_j - wezel_k))
            y += iloczyn
        y_interpolacji.append(y)
    return x_interpolacji, y_interpolacji

def oblicz_interpolacje_dla_x(wezly, wartosci_wezlow, x):
    """
    Funkcja obliczająca wartość interpolacji dla określonej wartości x.
    """
    y_interpolacji = 0
    for j, wezel_j in enumerate(wezly):
        iloczyn = wartosci_wezlow[j]
        for k, wezel_k in enumerate(wezly):
            if j != k:
                iloczyn *= ((x - wezel_k) / (wezel_j - wezel_k))
        y_interpolacji += iloczyn
    return y_interpolacji

def zapisz_do_pliku(nazwa_funkcji, poczatek, koniec, wezly, wartosci_wezlow):
    """
    Funkcja zapisująca wyniki interpolacji do pliku.
    """
    with open("wyniki.txt", "w") as plik:
        plik.write(f"Funkcja: {nazwa_funkcji}\n")
        plik.write(f"Zakres: {poczatek}  {koniec}\n\n")
        for wezel, wartosc in zip(wezly, wartosci_wezlow):
            plik.write(f"{wezel}  {wartosc}\n")

def main():
    t = 'n'
    while t == 'n':
        wybor = wybierz_funkcje()
        poczatek, koniec = wczytaj_zakres()

        krok = wczytaj_krok_interpolacji()

        x_funkcji, y_funkcji = oblicz_wartosci_funkcji(poczatek, koniec, wybor, krok)

        liczba_wezlow = wczytaj_liczbe_wezlow()
        wezly = oblicz_wspolrzedne_wezlow(liczba_wezlow, poczatek, koniec)
        wartosci_wezlow = oblicz_wartosci_wezlow(wezly, wybor)

        x_interpolacji, y_interpolacji = interpolacja_lagrangea(wezly, wartosci_wezlow, poczatek, koniec, krok)

        plt.figure()
        plt.title("Interpolacja Lagrange'a dla wezlow Czebyszewa")
        plt.xlabel("os X")
        plt.ylabel("os Y")
        plt.grid(True)

        plt.plot(x_funkcji, y_funkcji, label="Funkcja")
        plt.scatter(wezly, wartosci_wezlow, label="Wezly", s=30, color='#88c999', marker='x')
        plt.plot(x_interpolacji, y_interpolacji, label="Interpolacja")

        plt.legend()
        plt.show()

        # Wizualizacja błędu interpolacji
        blad_interpolacji = [funkcje_matematyczne[wybor - 1](x) - oblicz_interpolacje_dla_x(wezly, wartosci_wezlow, x)
                             for x in x_interpolacji]

        plt.figure()
        plt.plot(x_interpolacji, blad_interpolacji, label="Błąd interpolacji")
        plt.title("Błąd interpolacji")
        plt.xlabel("os X")
        plt.ylabel("Błąd")
        plt.grid(True)
        plt.legend()
        plt.show()

        while True:
            try:
                x = float(input("Podaj x: "))
                if poczatek <= x <= koniec:
                    break
                else:
                    raise ValueError
            except ValueError:
                print(f"Wprowadzona wartość musi być liczbą z zakresu [{poczatek}, {koniec}]")

        y_interpolacji = oblicz_interpolacje_dla_x(wezly, wartosci_wezlow, x)
        y_funkcji = funkcje_matematyczne[wybor - 1](x)
        print("Ze wzoru:", y_funkcji)
        print("Z interpolacji:", y_interpolacji)
        print("Blad:", y_funkcji - y_interpolacji)

        nazwa_funkcji = ["x+11", "|x|", "3x^4-4x^3+2x^2-3x+4", "sin(x)", "(-x+4)*cos(x)", "6|x|*cos(x)", "|3sin(6x)+4|", "|4xlog(|x|, 7)|"][wybor - 1]
        zapisz_do_pliku(nazwa_funkcji, poczatek, koniec, wezly, wartosci_wezlow)

        t = input("\nKonczymy dzialanie programu?\n[t] - zakoncz program\n[n] - rozpocznij program od nowa\n\nWybieram: ")

if __name__ == "__main__":
    funkcje_matematyczne = [
        lambda x: x + 11,
        lambda x: abs(x),
        lambda x: (3 * x ** 4) - (4 * x ** 3) + (2 * x ** 2) - (3 * x) + 4,
        lambda x: math.sin(x),
        lambda x: (-x + 4) * math.cos(x),
        lambda x: 6 * abs(x) * math.cos(x),
        lambda x: abs(3 * math.sin(6 * x) + 4),
        lambda x: abs(4*x+math.log(abs(x), 7))
    ]
    main()
