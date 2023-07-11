import numpy as np
import multiprocessing as mp

def multiply_row(row, matrix1, matrix2, result):
    for col in range(len(matrix2[0])):
        result[row][col] = sum(matrix1[row][k] * matrix2[k][col] for k in range(len(matrix2)))

def multiply_matrices(matrix1, matrix2):
    result = mp.Array('d', [0] * (len(matrix1) * len(matrix2[0])))
    result = np.frombuffer(result.get_obj(), dtype=np.float64).reshape((len(matrix1), len(matrix2[0])))

    processes = []

    for row in range(len(matrix1)):
        process = mp.Process(target=multiply_row, args=(row, matrix1, matrix2, result))
        process.start()
        processes.append(process)

    for process in processes:
        process.join()

    return result

# Exemplo de uso
matrix1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matrix2 = np.array([[9, 8, 7], [6, 5, 4], [3, 2, 1]])

result = multiply_matrices(matrix1, matrix2)
print(result)
