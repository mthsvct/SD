from multiprocessing import Process, Value
from time import time

# Programa que conta ocorrências de palavras em um texto com paralelismo utilizando Process do módulo multiprocessing
# O programa lê um arquivo texto.txt e conta ocorrências de palavras em uma lista de palavras
# O programa imprime o resultado da contagem de ocorrências de cada palavra da lista de palavras
# O programa utiliza o módulo multiprocessing para realizar a contagem de ocorrências de cada palavra em paralelo

def busca(texto, palavra, result):
    palavras = texto.split(' ')
    count = 0
    for p in palavras:
        if p == palavra:
            count += 1
    with result.get_lock():
        result.value += count


if __name__ == '__main__':

    with open('texto.txt', 'r') as file:
        texto = file.read().lower()
        plvs = ["mas", "passado", "a", "poderia", "semana", "creio", "casa", "e"]
        resultados = [{'plv': x, 'count': Value('i', 0)} for x in plvs]

        inicio = time()

        processos = [Process(target=busca, args=(texto, r['plv'], r['count'])) for r in resultados]

        for p in processos:
            p.start()
        
        for p in processos:
            p.join()

        fim = time() - inicio

        for r in resultados:
            print(f"Palavra: {r['plv']}, Ocorrências: {r['count'].value}")
        
        print(f"Tempo de execução usando paralelismo: {fim} segundos")


# Tempo de execução sem paralelismo: 0.030971050262451172 segundos
# Tempo de execução com paralelismo: 0.014852046966552734 segundos
# Fórmula da porcentagem = ( 0.014852046966552734 / 0.030971050262451172 ) * 100
# Total: 47.95461193823036 de redução.


