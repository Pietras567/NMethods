from itertools import permutations
import numpy as np
from matplotlib import pyplot as plt


def gauss_seidel(A, b, x0, tol=1e-6, max_iter=1000):
    if A.shape[0] != A.shape[1]:
        raise ValueError("Podana macierz A nie jest kwadratowa.")
    if A.shape[0] != len(b):
        raise ValueError("Wymiary macierzy A i wektora b nie są zgodne.")


    if (check_dominance_conditions(A) == False):
        print("Bazowe ustawienie nie jest dominujace przekatniowo")
        # Pobranie wszystkich możliwych permutacji
        all_permutations_A_rows, all_permutations_b_rows = permute_rows(A, b)
        #all_permutations_A_columns, all_permutations_b_columns = permute_columns(A, b)

        # Iteracja przez wszystkie możliwe permutacje wierszy
        for permuted_A, permuted_b in zip(all_permutations_A_rows, all_permutations_b_rows):
            if check_dominance_conditions(permuted_A) == True:
                A = permuted_A
                b = permuted_b
                print("Znalazlem dobre ustawienie wierszy")
                break
            print("Zle ustawienie wierszy")
        # Iteracja przez wszystkie możliwe permutacje kolumn
        #for permuted_A, permuted_b in zip(all_permutations_A_columns, all_permutations_b_columns):
        #    if check_dominance_conditions(permuted_A) == True:
        #        A = permuted_A
        #        print("Znalazlem kolumny")
        #        break
        #    print("Zle kolumny")

    n = len(b)
    x = np.array(x0)
    x_new = np.zeros(n)
    residuals = []  # Lista przechowująca normy residuów w kolejnych iteracjach
    for k in range(max_iter):
        for i in range(n):
            sum1 = np.dot(A[i, :i], x_new[:i])
            sum2 = np.dot(A[i, i + 1:], x[i + 1:])
            x_new[i] = (b[i] - sum1 - sum2) / A[i, i]
        residuals.append(np.linalg.norm(b - np.dot(A, x_new)))  # Obliczanie normy residuum

        if np.linalg.norm(x_new - x) < tol:
            print("Convergence achieved after", k + 1, "iterations.")
            plot_residuals(residuals)
            return x_new, residuals

        print(x_new)
        x = np.copy(x_new)
    print("Maximum number of iterations reached.")
    return x_new, residuals


def permute_rows(A, b):
    # Generowanie wszystkich możliwych permutacji indeksów wierszy
    n = A.shape[0]
    permutations_indices = permutations(range(n))

    # Lista przechowująca wszystkie możliwe permutacje
    all_permutations_A = []
    all_permutations_b = []

    # Iteracja przez wszystkie możliwe permutacje
    for indices in permutations_indices:
        permuted_A = A[list(indices)]
        permuted_b = b[list(indices)]
        all_permutations_A.append(permuted_A)
        all_permutations_b.append(permuted_b)

    return all_permutations_A, all_permutations_b


def permute_columns(A, b):
    n = A.shape[0]
    permutations_indices = permutations(range(n))

    all_permutations_A = []
    all_permutations_b = []

    for indices in permutations_indices:
        permuted_A = A[:, list(indices)]
        all_permutations_A.append(permuted_A)
        all_permutations_b.append(b)

    return all_permutations_A, all_permutations_b

def check_dominance_conditions(A):
    if check_strong_row_domination(A) or check_strong_column_domination(A) or check_weak_row_domination(A) or check_weak_column_domination(A):
        return True
    return False

def check_strong_row_domination(A):
    n = A.shape[0]
    for i in range(n):
        if np.abs(A[i, i]) <= np.sum(np.abs(A[i, :])) - np.abs(A[i, i]):
            return False
    return True

def check_strong_column_domination(A):
    n = A.shape[0]
    for j in range(n):
        if np.abs(A[j, j]) <= np.sum(np.abs(A[:, j])) - np.abs(A[j, j]):
            return False
    return True

def check_weak_row_domination(A):
    n = A.shape[0]
    strong_domination_found = False
    for i in range(n):
        if np.abs(A[i, i]) > np.sum(np.abs(A[i, :])) - np.abs(A[i, i]):
            strong_domination_found = True
            break
    if not strong_domination_found:
        return False
    for i in range(n):
        if np.abs(A[i, i]) < np.sum(np.abs(A[i, :])) - np.abs(A[i, i]):
            return False
    return True

def check_weak_column_domination(A):
    n = A.shape[0]
    strong_domination_found = False
    for j in range(n):
        if np.abs(A[j, j]) > np.sum(np.abs(A[:, j])) - np.abs(A[j, j]):
            strong_domination_found = True
            break
    if not strong_domination_found:
        return False
    for j in range(n):
        if np.abs(A[j, j]) < np.sum(np.abs(A[:, j])) - np.abs(A[j, j]):
            return False
    return True


def plot_residuals(residuals):
    plt.figure(figsize=(8, 6))
    plt.semilogy(range(1, len(residuals) + 1), residuals, marker='o', linestyle='-')
    plt.title('Norma residuów w kolejnych iteracjach')
    plt.xlabel('Iteracja')
    plt.ylabel('Norma residuów')
    plt.grid(True)
    plt.show()

def read_matrix_and_vector(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            matrix = []
            vector = []
            for line in lines:
                row = list(map(float, line.strip().split()))
                matrix.append(row[:-1])  # Wszystkie wartości oprócz ostatniej to współczynniki macierzy
                vector.append(row[-1])   # Ostatnia wartość to element wektora prawych stron
            return np.array(matrix), np.array(vector)
    except FileNotFoundError:
        print("Nie znaleziono pliku.")
        return None, None
    except ValueError:
        print("Błąd podczas przetwarzania danych w pliku.")
        return None, None

def get_settings_from_user():
    tol = float(input("Podaj tolerancję dla kryterium zbieżności: "))
    max_iter = int(input("Podaj maksymalną liczbę iteracji: "))
    return tol, max_iter

def main():
    # Wczytanie danych z pliku
    file_path = input("Podaj nazwę pliku zawierającego macierz i wektor prawych stron: ")
    A, b = read_matrix_and_vector(file_path)
    if A is None or b is None:
        return

    # Ustawienia algorytmu iteracyjnego
    tol, max_iter = get_settings_from_user()

    # Początkowe przybliżenie
    n = len(b)
    x0 = np.zeros(n)

    # Rozwiązanie układu równań
    try:
        solution, _ = gauss_seidel(A, b, x0, tol=tol, max_iter=max_iter)
        print("Rozwiązanie układu równań:", solution)
    except ValueError as e:
        print("Wystąpił błąd:", e)

if __name__ == "__main__":
    main()
