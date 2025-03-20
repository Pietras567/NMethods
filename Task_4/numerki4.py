from math import *
from scipy.special import roots_laguerre
import matplotlib.pyplot as plt
import numpy as np
import time


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
def gauss_laguerre_integration(f, n):
    """
    Oblicza przybliżoną wartość całki funkcji 'f' przy użyciu kwadratury Gaussa-Laguerre'a.

    Parameters:
        f (function): Funkcja, której całkę chcemy obliczyć.
        n (int): Liczba węzłów kwadratury Gaussa-Laguerre'a.

    Returns:
        float: Przybliżona wartość całki funkcji 'f'.
    """
    # Obliczanie węzłów i wag dla kwadratury Gaussa-Laguerre'a
    nodes, weights = roots_laguerre(n)
    print("Wezly: " + str(nodes))
    print("Wagi: " + str(weights))

    # Obliczanie wartości całki
    integral = sum(weights[i] * f(nodes[i]) for i in range(n))

    return integral


def newton_cotes(a, b, f, start_no, acc):
    """
    Oblicza przybliżoną wartość całki funkcji 'f' przy użyciu metody Newtona-Cotesa.

    Parameters:
        a (float): Początek przedziału całkowania.
        b (float): Początek przedziału całkowania.
        f (function): Funkcja, której całkę chcemy obliczyć.
        start_no (int): Początkowa liczba podziałów przedziału.
        acc (float): Pożądana dokładność całkowania.

    Returns:
        float: Przybliżona wartość całki funkcji 'f'.
    """
    h = (b - a)/start_no
    k = start_no//2
    odd = 4 * sum(f((2*i-1)*h)*exp(-1*((2*i-1)*h)) for i in range(1, k+1, 1))
    #for i in range(1, k + 1, 1):
        #print("o: " + str(2*i-1))
        #print("ov" + str((2 * i - 1) * h))
    even = 2 * sum(f(2*i*h)*exp(-1*(2*i*h)) for i in range(1, k, 1))
    #for i in range(1, k, 1):
        #print("e: " + str(2*i))
        #print("ev" + str((2 * i * h)))
    #print(str(odd))
    #print(str(even))
    integral = (h/3) * (f(a)*exp(-1*a) + f(b)*exp(-1*b) + odd + even)

    no = start_no
    while True:
        no = no * 2
        old_integral = integral
        h = (b - a) / no
        k = no // 2
        odd = 4 * sum(f((2 * i - 1) * h + a) * exp(-1 * ((2 * i - 1) * h + a)) for i in range(1, k + 1, 1))
        even = 2 * sum(f(2 * i * h + a) * exp(-1 * (2 * i * h + a)) for i in range(1, k, 1))
        integral = (h / 3) * (f(a) * exp(-1 * a) + f(b) * exp(-1 * b) + odd + even)
        if(abs(integral-old_integral)<acc):
            #print("no: " + str(no))
            break
    return integral

def newton_cotes_integration(f, acc, lim_acc, a = 10, jump = 5):
    """
    Oblicza przybliżoną wartość całki funkcji 'f' przy użyciu metody Newtona-Cotesa z automatycznym dostosowaniem kroku.

    Parameters:
        f (function): Funkcja, której całkę chcemy obliczyć.
        acc (float): Pożądana dokładność całkowania.
        lim_acc (float): Graniczna dokładność, przy której zatrzymywane jest całkowanie.
        a (float): Początek przedziału całkowania.
        jump (float): Długość skoku.

    Returns:
        float: Przybliżona wartość całki funkcji 'f'.
    """
    integral = newton_cotes(0, a, f, 3, acc)
    print('1: '+str(integral))
    print('2: ' + str(newton_cotes(a, a+jump, f, 3, acc)))
    poczatek_przedzialu = a
    while True:
        new_integral = newton_cotes(poczatek_przedzialu, poczatek_przedzialu+jump, f, 3, acc)
        print(str(new_integral))
        if(abs(new_integral)<lim_acc):
            #print("ostatni zakres: " + str(a) + " " + str(a+jump))
            break
        poczatek_przedzialu += jump
        integral += new_integral
    return integral

def plot_integration_method(f, result, method_name, start, end, num_points, parameters):
    """
    Generuje wykres funkcji oraz przybliżonej całki dla danej metody całkowania.

    Parameters:
        f (function): Funkcja, której całkę chcemy obliczyć.
        result (float): Przybliżona wartość całki.
        method_name (str): Nazwa metody całkowania.
        start (float): Początek przedziału wykresu.
        end (float): Koniec przedziału wykresu.
        num_points (int): Liczba punktów do wygenerowania na wykresie.
        parameters (list): Lista zawierająca parametry metody całkowania.
    """
    x = np.linspace(start, end, num_points)
    y = f(x) * np.exp(-x)

    plt.plot(x, y, label='Funkcja całkowana')
    plt.title(f'Wykres funkcji oraz przybliżona całka ({method_name})')
    plt.xlabel('x')
    plt.ylabel('y')

    if method_name == "Gaussa-Laguerre'a":
        nodes, weights = roots_laguerre(parameters[0])
        plt.scatter(nodes, f(nodes) * np.exp(-1*nodes), color='green', label=f'Wagi uwzględnione we wzorze funkcji')
        plt.scatter(nodes, weights, color='red', label=f'Wagi')
        plt.legend(title=f'Liczba węzłów: {parameters[0]}')
    else:
        a = parameters[2]
        jumps = []
        values = []
        while a < end:
            a += parameters[3]
            jumps.append(a)
            values.append(0)


        plt.scatter(parameters[2], 0, color='red', label='Punkt początkowy')
        plt.scatter(jumps, values, color='green', label='Skoki')
        plt.legend(title=f'Dokładność całkowania: {parameters[0]}')
        plt.legend(title=f'Dokładność granicy: {parameters[1]}')
        plt.legend(title=f'Punkt początkowy: {parameters[2]}')
        plt.legend(title=f'Skok: {parameters[3]}')

    plt.legend(title=f'Wynik: {result:.5f}')
    plt.show()
def main():
    """
    Główna funkcja programu, odpowiedzialna za wybór metody całkowania i funkcji oraz wygenerowanie wyników i wykresów.
    """
    print("Wybierz metodę całkowania:")
    print("1. Gaussa-Laguerre'a")
    print("2. Newtona-Cotesa")
    choice = input("Twój wybór: ")

    #print(nazwy_funkcji)
    j = 0
    for i in nazwy_funkcji:
        print(str(j) + ". " + i)
        j+=1
    choice_function = int(input("Podaj numer odpowiedni danej funkcji: "))

    if choice == "1":
        n = int(input("Podaj liczbę węzłów kwadratury Gaussa-Laguerre'a: "))
        start_time = time.time()
        result = gauss_laguerre_integration(funkcje_matematyczne[choice_function], n)
        end_time = time.time()
        print("Przybliżona wartość całki gaussa:", result)
        print("Czas wykonania: ", end_time - start_time, "sekundy")
        plot_integration_method(funkcje_matematyczne[choice_function], result, "Gaussa-Laguerre'a", 0, 25, 100000, [n])

    elif choice == "2":
        acc = float(input("Podaj dokładność całkowania dla metody Newtona-Cotesa: "))
        lim_acc = float(input("Podaj limit dokładności dla metody Newtona-Cotesa: "))
        a = float(input("Podaj początek przedziału całkowania: "))
        jump = float(input("Podaj długość skoku dla metody Newtona-Cotesa: "))
        start_time = time.time()
        result = newton_cotes_integration(funkcje_matematyczne[choice_function], acc, lim_acc, a, jump)
        end_time = time.time()
        print("Przybliżona wartość całki newtona-cotesa:", result)
        print("Czas wykonania: ", end_time - start_time, "sekundy")
        plot_integration_method(funkcje_matematyczne[choice_function], result, "Newtona-Cotesa", 0, 25, 100000, [acc, lim_acc, a, jump])

    else:
        print("Niepoprawny wybór")

if __name__ == "__main__":
    main()