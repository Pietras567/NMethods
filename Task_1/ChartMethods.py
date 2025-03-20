import numpy as np
from matplotlib import pyplot as plt
from CalcMethods import *

def rysujwykres(x_min, x_max, xzero, type, wzor, metoda):
    # Lista wartości x
    x = np.arange(x_min, x_max, 0.001)


    # Lista wartości y
    y = [funkcja(wzor, punkt) for punkt in x]

    # Rysowanie wykresu
    plt.plot(x, y)

    # Zaznaczenie miejsca zerowego
    plt.axvline(xzero, color='red', linestyle='dashed')

    # Zaznaczenie osi x dla y=0
    plt.axhline(0, color='black')

    # Etykiety osi
    plt.xlabel("x")
    plt.ylabel("f(x)")

    # Tytuł wykresu
    plt.title(metoda + '; ' + type)
    plt.legend(['f(x) = ' + str(wzor)] + ['x0 = ' + str(xzero)])


    # Wyświetlenie wykresu
    plt.show()