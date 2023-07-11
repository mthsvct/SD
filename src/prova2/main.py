from random import randint
from threading import Thread
from time import sleep, time
from multiprocessing import Process, Manager


def linha(m1, m2, l, resultante):
    # print(f'Calculando linha {l} da matriz resultante: {resultante}')
    for i in range(len(m2)):
        for j in range(len(m2)):
            resultante[l][i] += m1[l][j] * m2[j][i]

def multThrd(m1, m2, n):
    resultante = criaMatriz(n, z=True)
    lista = [Thread(target=linha, args=(m1, m2, i, resultante)) for i in range(n)]
    [t.start() for t in lista]
    [t.join() for t in lista]
    print(resultante)
    return resultante

def multProcss(m1, m2, n):
    with Manager() as manager:
        resultante = manager.list(criaMatriz(n, z=True))
        lista = [Process(target=linha, args=(m1, m2, i, resultante)) for i in range(n)]
        for t in lista:
            t.start()
        for t in lista:
            t.join()
        return list(resultante)

criaMatriz = lambda n, z=False: [[0 if z else randint(0, 99) for _ in range(n)] for _ in range(n)]

n = 3
m1, m2 = criaMatriz(n), criaMatriz(n)

t = time()
aux2 = multProcss(m1, m2, n)
print(f"Tempo de execução: {time() - t}")
print(aux2)