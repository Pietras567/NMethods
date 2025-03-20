from CalcMethods import *

def BisectionMethodEpsilon(punktA, punktB, epsilon, wzor):
    wartoscA = funkcja(wzor, punktA)
    wartoscB = funkcja(wzor, punktB)
    punktX0 = None
    iterations = 1
    if (wartoscA*wartoscB>0):
        print("Podane punkty nie spełniają założeń")
        return
    while (True):
        punktX0 = (punktA + punktB) / 2
        wartoscX0 = funkcja(wzor, punktX0)
        if(abs(wartoscX0)<epsilon):
            print("Liczba iteracji: " + str(iterations - 1))
            return punktX0
        if(wartoscA*wartoscX0<0):
            punktB = punktX0
        else:
            punktA = punktX0
            wartoscA = wartoscX0
        iterations = iterations + 1


def BisectionMethodIter(punktA, punktB, iter, wzor):
    myIter = 1
    wartoscA = funkcja(wzor, punktA)
    wartoscB = funkcja(wzor, punktB)
    punktX0 = None
    if (wartoscA*wartoscB>0):
        print("Podane punkty nie spełniają założeń")
        return
    while (True):
        if (myIter > iter):
            print("przekroczono liczbe iteracji")
            return punktX0
        punktX0 = (punktA + punktB) / 2
        wartoscX0 = funkcja(wzor, punktX0)
        if (wartoscA*wartoscX0 < 0):
            punktB = punktX0
        else:
            punktA = punktX0
            wartoscA = wartoscX0
        myIter = myIter + 1

