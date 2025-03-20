import matplotlib.pyplot as plt
from BisectionMethods import *
from NewtonMethods import *
from CalcMethods import *
from ChartMethods import *
from math import *
fun1 = "x**3 + 3*x**2 + x + 7"
fun1P = "3*x**2 + 6*x + 1"
fun2 = "sin(x)+tan(x)"
fun2P = "cos(x)+(1/((cos(x))**2))"
fun3 = "5*(e**(-2*x))-2"
fun3P = "-10*(e**(-2*x))"
fun4 = "2*x**4-3*x**3-4*x**2+x-2**x"
fun4P = "8*x**3-9*x**2-8*x+1-log(2, e)*2**x"
#print(funkcja(fun1, 7))

valueOfAlg = 212222

while (valueOfAlg > 4) | (valueOfAlg < 1):
    print("MENU")
    print("1. Algorytm Newtona do wyznaczania miejsc zerowych - wersja z |f(xi)|<ε dla warunku stopu")
    print("2. Algorytm Newtona do wyznaczania miejsc zerowych - wersja z limitem iteracji dla warunku stopu")
    print("3. Algorytm Bisekcji do wyznaczania miejsc zerowych - wersja z |f(xi)|<ε dla warunku stopu")
    print("4. Algorytm Newtona do wyznaczania miejsc zerowych - wersja z limitem iteracji dla warunku stopu")
    valueOfAlg = int(input("Podaj wartość odpowiednią dla danego algorytmu i warunku stopu: "))

if valueOfAlg == 1:
    valueOfAlg = 212222

    while (valueOfAlg > 5) | (valueOfAlg < 1):
        print("MENU")
        print("1. Przykładowa Funkcja wielomianowa")
        print("2. Przykładowa Funkcja trygonometryczna")
        print("3. Przykładowa Funkcja wykładnicza")
        print("4. Przykładowa złożenie funkcji")
        print("5. Własna funkcja")
        valueOfAlg = int(input("Podaj wartość odpowiednią dla danej funkcji: "))


    minX = float(input("Podaj minimalną włączna wartość dla przedziału, w którym poszukawana będzie dane miejsce zerowe: "))
    maxX = float(input("Podaj maksymalną włączna wartość dla przedziału, w którym poszukawana będzie dane miejsce zerowe: "))
    startX = float(input("Wprowadź początkową wartość dla punktu, od którego rozpoczniemy poszukiwania: "))
    epsilon = float(input("Wprowadź wartość dla warunku stopu: "))
    if valueOfAlg == 1:
        rysujwykres(minX, maxX, NewtonMethodEpsilon(startX, epsilon, fun1, fun1P), ("Epsilon " + str(epsilon)), fun1, "Metoda Newtona")
    elif valueOfAlg == 2:
        rysujwykres(minX, maxX, NewtonMethodEpsilon(startX, epsilon, fun2, fun2P), ("Epsilon " + str(epsilon)), fun2, "Metoda Newtona")
    elif valueOfAlg == 3:
        rysujwykres(minX, maxX, NewtonMethodEpsilon(startX, epsilon, fun3, fun3P), ("Epsilon " + str(epsilon)), fun3, "Metoda Newtona")
    elif valueOfAlg == 4:
        rysujwykres(minX, maxX, NewtonMethodEpsilon(startX, epsilon, fun4, fun4P), ("Epsilon " + str(epsilon)), fun4, "Metoda Newtona")
    else:
        fun = str(input("Wprowadź wzór: "))
        funP = str(input("Wprowadź wzór pochodnej: "))
        rysujwykres(minX, maxX, NewtonMethodEpsilon(startX, epsilon, fun, funP), ("Epsilon " + str(epsilon)), fun, "Metoda Newtona")

elif valueOfAlg == 2:
    valueOfAlg = 212222

    while (valueOfAlg > 5) | (valueOfAlg < 1):
        print("MENU")
        print("1. Przykładowa Funkcja wielomianowa")
        print("2. Przykładowa Funkcja trygonometryczna")
        print("3. Przykładowa Funkcja wykładnicza")
        print("4. Przykładowa złożenie funkcji")
        print("5. Własna funkcja")
        valueOfAlg = int(input("Podaj wartość odpowiednią dla danej funkcji: "))

    minX = float(
        input("Podaj minimalną włączna wartość dla przedziału, w którym poszukawana będzie dane miejsce zerowe: "))
    maxX = float(
        input("Podaj maksymalną włączna wartość dla przedziału, w którym poszukawana będzie dane miejsce zerowe: "))
    startX = float(input("Wprowadź początkową wartość dla punktu, od którego rozpoczniemy poszukiwania: "))
    iter = int(input("Wprowadź wartość dla warunku stopu: "))
    if valueOfAlg == 1:
        rysujwykres(minX, maxX, NewtonMethodIter(startX, iter, fun1, fun1P), ("Liczba iteracji " + str(iter)),
                        fun1, "Metoda Newtona")
    elif valueOfAlg == 2:
        rysujwykres(minX, maxX, NewtonMethodIter(startX, iter, fun2, fun2P), ("Liczba iteracji " + str(iter)),
                        fun2, "Metoda Newtona")
    elif valueOfAlg == 3:
        rysujwykres(minX, maxX, NewtonMethodIter(startX, iter, fun3, fun3P), ("Liczba iteracji " + str(iter)),
                        fun3, "Metoda Newtona")
    elif valueOfAlg == 4:
        rysujwykres(minX, maxX, NewtonMethodIter(startX, iter, fun4, fun4P), ("Liczba iteracji " + str(iter)),
                        fun4, "Metoda Newtona")
    else:
        fun = str(input("Wprowadź wzór: "))
        funP = str(input("Wprowadź wzór pochodnej: "))
        rysujwykres(minX, maxX, NewtonMethodIter(startX, iter, fun, funP), ("Liczba iteracji  " + str(iter)), fun,
                        "Metoda Newtona")
elif valueOfAlg == 3:
    valueOfAlg = 212222

    while (valueOfAlg > 5) | (valueOfAlg < 1):
        print("MENU")
        print("1. Przykładowa Funkcja wielomianowa")
        print("2. Przykładowa Funkcja trygonometryczna")
        print("3. Przykładowa Funkcja wykładnicza")
        print("4. Przykładowa złożenie funkcji")
        print("5. Własna funkcja")
        valueOfAlg = int(input("Podaj wartość odpowiednią dla danej funkcji"))

    minX = float(
            input("Podaj minimalną włączna wartość dla przedziału, w którym poszukawana będzie dane miejsce zerowe"))
    maxX = float(
            input("Podaj maksymalną włączna wartość dla przedziału, w którym poszukawana będzie dane miejsce zerowe"))
    startA = float(input("Wprowadź początkową wartość dla punktu A, od którego rozpoczniemy poszukiwania"))
    startB = float(input("Wprowadź początkową wartość dla punktu B, od którego rozpoczniemy poszukiwania"))
    epsilon = float(input("Wprowadź wartość dla warunku stopu"))
    if valueOfAlg == 1:
            rysujwykres(minX, maxX, BisectionMethodEpsilon(startA, startB, epsilon, fun1), ("Epsilon " + str(epsilon)), fun1,
                        "Metoda Bisekcji")
    elif valueOfAlg == 2:
            rysujwykres(minX, maxX, BisectionMethodEpsilon(startA, startB, epsilon, fun2), ("Epsilon " + str(epsilon)), fun2,
                        "Metoda Bisekcji")
    elif valueOfAlg == 3:
            rysujwykres(minX, maxX, BisectionMethodEpsilon(startA, startB, epsilon, fun3), ("Epsilon " + str(epsilon)), fun3,
                        "Metoda Bisekcji")
    elif valueOfAlg == 4:
            rysujwykres(minX, maxX, BisectionMethodEpsilon(startA, startB, epsilon, fun4), ("Epsilon " + str(epsilon)), fun4,
                        "Metoda Bisekcji")
    else:
            fun = str(input("Wprowadź wzór: "))
            rysujwykres(minX, maxX, BisectionMethodEpsilon(startA, startB, epsilon, fun), ("Epsilon " + str(epsilon)), fun,
                        "Metoda Bisekcji")
elif valueOfAlg == 4:
    valueOfAlg = 212222

    while (valueOfAlg > 5) | (valueOfAlg < 1):
        print("MENU")
        print("1. Przykładowa Funkcja wielomianowa")
        print("2. Przykładowa Funkcja trygonometryczna")
        print("3. Przykładowa Funkcja wykładnicza")
        print("4. Przykładowa złożenie funkcji")
        print("5. Własna funkcja")
        valueOfAlg = int(input("Podaj wartość odpowiednią dla danej funkcji"))

    minX = float(
            input("Podaj minimalną włączna wartość dla przedziału, w którym poszukawana będzie dane miejsce zerowe"))
    maxX = float(
            input("Podaj maksymalną włączna wartość dla przedziału, w którym poszukawana będzie dane miejsce zerowe"))
    startA = float(input("Wprowadź początkową wartość dla punktu A, od którego rozpoczniemy poszukiwania"))
    startB = float(input("Wprowadź początkową wartość dla punktu B, od którego rozpoczniemy poszukiwania"))
    iter = int(input("Wprowadź wartość dla warunku stopu"))
    if valueOfAlg == 1:
        rysujwykres(minX, maxX, BisectionMethodIter(startA, startB, iter, fun1), ("Liczba iteracji  " + str(iter)),
                        fun1,
                        "Metoda Bisekcji")
    elif valueOfAlg == 2:
        rysujwykres(minX, maxX, BisectionMethodIter(startA, startB, iter, fun2), ("Liczba iteracji  " + str(iter)),
                        fun2,
                        "Metoda Bisekcji")
    elif valueOfAlg == 3:
        rysujwykres(minX, maxX, BisectionMethodIter(startA, startB, iter, fun3), ("Liczba iteracji  " + str(iter)),
                        fun3,
                        "Metoda Bisekcji")
    elif valueOfAlg == 4:
        rysujwykres(minX, maxX, BisectionMethodIter(startA, startB, iter, fun4), ("Liczba iteracji  " + str(iter)),
                        fun4,
                        "Metoda Bisekcji")
    else:
        fun = str(input("Wprowadź wzór: "))
        rysujwykres(minX, maxX, BisectionMethodIter(startA, startB, iter, fun), ("Liczba iteracji  " + str(iter)), fun,
                        "Metoda Bisekcji")