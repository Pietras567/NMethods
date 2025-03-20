from math import cos, pi
import matplotlib.pyplot as plt
import numpy as np

nazwy_funkcji = ["2x+7", "|x|+2", "3x^4-4x^3+2x^2-3x+4", "sin(x)", "(-x+4)*cos(x)", "6|x|*cos(x)", "|3sin(6x)+4|", "|4xln(|x-0.5|)|"]

funkcje_matematyczne = [
    lambda x: 2*x + 7,
    lambda x: abs(x)+2,
    lambda x: (3 * x ** 4) - (4 * x ** 3) + (2 * x ** 2) - (3 * x) + 4,
    lambda x: np.sin(x),
    lambda x: (-x + 4) * np.cos(x),
    lambda x: 6 * abs(x) * np.cos(x),
    lambda x: abs(3 * np.sin(6 * x) + 4),
    lambda x: np.abs(4 * x + np.log(np.abs(x-0.5)))
]

def chebyshev_gauss(f, k, stopien, a, b):
    """
    Oblicza przybliżoną wartość całki funkcji 'f' przy użyciu metody Gaussa-Czebyszewa.

    Parameters:
        f (function): Funkcja, której całkę chcemy obliczyć.
        k (int): Liczba węzłów całkowania.
        stopien (int): Stopień wielomianu Czebyszewa.
        a (int): Początek przedziału
        b (int): Koniec przedziału

    Returns:
        float: Przybliżona wartość całki funkcji 'f'.
    """
    weight = pi/k
    wezly = []
    for i in range(1, k+1):
        wezly.append(cos(((2*i-1)/(2*k))*pi))

    integral = 0
    for i in range(0, k):
        # Przeskalowanie wezłów do przedziału [a, b]
        x = (a + b) / 2 + (b - a) / 2 * wezly[i]
        integral += weight * f(x) * wielomian_czebyszewa(stopien, wezly[i])

    return integral

memo = {}
def wielomian_czebyszewa(k, x): #k to stopien wielomianu, x to argument
    """
    Oblicza wartość wielomianu Czebyszewa stopnia 'k' w punkcie 'x'.

    Parameters:
        k (int): Stopień wielomianu.
        x (float): Argument wielomianu.

    Returns:
        float: Wartość wielomianu Czebyszewa stopnia 'k' w punkcie 'x'.
    """
    if (k, x) in memo:
        return memo[(k, x)]
    if k == 0:
        return 1
    elif k == 1:
        return x
    else:
        val = 2 * x * wielomian_czebyszewa(k-1, x) - wielomian_czebyszewa(k-2, x)
    memo[(k, x)] = val
    return val

def oblicz_wspolczynniki(k, funkcja, a, b, wezly):
    """
    Oblicza współczynniki wielomianu aproksymującego.

    Parameters:
        k (int): Stopień wielomianu.
        funkcja (function): Funkcja do aproksymacji.
        a (int): Początek przedziału.
        b (int): Koniec przedziału.
        wezly (int): Ilość węzłów przy całkowaniu.

    Returns:
        list: Lista współczynników wielomianu aproksymującego.
    """
    wspolczynniki = []
    for i in range(0, k+1):
        wspolczynniki.append((2/pi)*chebyshev_gauss(funkcja, wezly, i, a, b))

    return wspolczynniki

def przybliz_funkcje(k, x, wspolczynniki, a, b):
    """
    Przybliża wartość funkcji 'funkcja' w punkcie 'x' za pomocą wielomianu aproksymującego.

    Parameters:
        k (int): Stopień wielomianu.
        x (float): Argument funkcji.
        wspolczynniki (list): Współczynniki wielomianu aproksymującego.
        a (int): Początek przedziału.
        b (int): Koniec przedziału.

    Returns:
        float: Przybliżona wartość funkcji 'funkcja' w punkcie 'x'.
    """
    wielomiany = []
    suma = 0
    x_scaled = (2 * x - (a + b)) / (b - a)

    for i in range(1, k+1):
        wielomiany.append(wielomian_czebyszewa(i, x_scaled))
        suma = suma + wspolczynniki[i] * wielomiany[i-1]

    aproksymacja = (wspolczynniki[0]/2)*wielomian_czebyszewa(0, x_scaled) + suma
    return aproksymacja


def main():
    # Użytkownik wybiera numer funkcji
    for i in range(0, len(nazwy_funkcji)):
        print(str(i) + ". " + nazwy_funkcji[i])

    numer_funkcji = int(input("Podaj numer funkcji (0-7): "))
    funkcja = funkcje_matematyczne[numer_funkcji]

    # Użytkownik podaje stopień wielomianu aproksymującego
    stopien = int(input("Podaj stopień wielomianu aproksymującego: "))

    # Użytkownik podaje liczbę węzłów całkowania
    liczba_wezlow = int(input("Podaj liczbę węzłów całkowania: "))

    # Użytkownik podaje przedział aproksymacji
    przedzial = input("Podaj przedział aproksymacji (format: a,b): ").split(',')
    a, b = float(przedzial[0]), float(przedzial[1])

    # Użytkownik podaje krok dla aproksymacji punktów na wykresie
    krok = float(input("Podaj krok dla aproksymacji i punktów na wykresie: "))

    # Obliczanie współczynników
    wspolczynniki = oblicz_wspolczynniki(stopien, funkcja, a, b, liczba_wezlow)

    # Tworzenie wykresu
    x = np.arange(a, b, krok)
    y_aproksymacja = [przybliz_funkcje(stopien, xi, wspolczynniki, a, b) for xi in x]
    y_funkcja = [funkcja(xi) for xi in x]
    y_roznica = [abs(y_funkcja[i] - y_aproksymacja[i]) for i in range(len(y_funkcja))]

    for i in range(0, 1000):
        print("A: " + str(y_aproksymacja[i]) + " F: " + str(y_funkcja[i]) + " R: " + str(y_roznica[i]))

    # Wykres funkcji
    plt.figure(figsize=(12, 6))
    plt.subplot(1, 2, 1)
    plt.title(f'Funkcja: {nazwy_funkcji[numer_funkcji]}')
    plt.plot(x, y_funkcja, label='Funkcja aproksymowana')
    plt.plot(x, y_aproksymacja, label='Funkcja aproksymująca', linestyle='--')
    plt.legend(title=f'Krok aproksymacji: {krok}\n'
                     f'Stopień wielomianu: {stopien}\n'
                     f'Liczba węzłów przy całkowaniu: {liczba_wezlow}')


    # Wykres różnicy
    plt.subplot(1, 2, 2)
    plt.title('Różnica')
    plt.plot(x, y_roznica, label='Różnica', linestyle=':')
    plt.legend()

    plt.show()


if __name__ == "__main__":
    main()
