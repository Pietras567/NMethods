from CalcMethods import *

def NewtonMethodEpsilon(punkt, epsilon, wzor, wzorPochodna):
    iterations = 1
    wartosc = funkcja(wzor, punkt)
    while True:
        print(str(punkt) + "    " +str(wartosc) + " Liczba iteracji: " + str(iterations))
        if abs(wartosc) < epsilon:
            print("Liczba iteracji: " + str(iterations - 1))
            return punkt
        wartoscp = funkcja(wzorPochodna, punkt)
        if abs(wartoscp) < epsilon:
            print("Zły punkt startowy")
            break
        punkt = punkt - wartosc/wartoscp
        wartosc = funkcja(wzor, punkt)
        iterations = iterations + 1


def NewtonMethodIter(punkt, iteration, wzor, wzorPochodna):
    myIter = 1
    wartosc = funkcja(wzor, punkt)
    while True:
        print(myIter)
        print(punkt)
        if (myIter > iteration):
            print("przekroczono liczbe iteracji")
            return punkt
        wartoscp = funkcja(wzorPochodna, punkt)
        punkt = punkt - wartosc/wartoscp
        wartosc = funkcja(wzor, punkt)
        myIter = myIter + 1
