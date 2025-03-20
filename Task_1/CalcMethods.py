import sympy as sp
from math import *

def funkcja(wzor, x):
    try:
        wartosc = eval(wzor)
        return wartosc
    except Exception as e:
        print(str(e))
        return str(e)
