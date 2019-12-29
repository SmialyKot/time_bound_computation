# Made by Looter
import time
from random import randint
import numpy as np
import matplotlib.pyplot as plt


def matrix_gen(n):
    def rand_num():
        return randint(1, 99)

    matrix = []
    for i in range(n):
        x = []
        for j in range(n):
            x.append(rand_num())
        matrix.append(x)
    return matrix


# std lib way of multiplication
def matrix_multiplication(matrix):
    result = [[sum(a*b for a, b in zip(X_row, X_col)) for X_col in zip(*matrix)] for X_row in matrix]
    return result


# numpy way of multiplication
def numpy_matrix_mul(matrix):
    return np.dot(matrix, matrix)


def solver(type_):
    results = {}
    n = 10
    if type_ == 'std':
        while n <= 1250:
            matrix = matrix_gen(n)
            t = time.process_time()
            matrix_multiplication(matrix)
            elapsed_time = time.process_time() - t
            results[n] = elapsed_time
            n *= 5
    else:
        while n <= 1250:
            matrix = matrix_gen(n)
            t = time.process_time()
            numpy_matrix_mul(matrix)
            elapsed_time = time.process_time() - t
            results[n] = elapsed_time
            n *= 5
    return results


def plot_graphs(title, save_name, data):
    s = []
    t = []
    for key, value in data.items():
        t.append(float(round(value, 4)))
        s.append(int(key))
    plt.plot(s, t, label='Time(s)', color='b')
    plt.legend()
    plt.grid(True)
    plt.xlabel('Matrix side(n)')
    plt.title(title)
    plt.ylabel('Execution time in seconds')
    plt.savefig(save_name, dpi=200)
    plt.close()


print("The program is running...\n"
      "Please wait. It can take some time\n"
      "Graphs will be saved to current dir")

plot_graphs("Matrix multiplication: Time vs Matrix size, in python std library", "std_graph.png", solver('std'))
plot_graphs("Matrix multiplication: Time vs Matrix size, in python NumPy library", "numpy_graph.png", solver('numpy'))
