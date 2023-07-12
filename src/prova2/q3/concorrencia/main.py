from threading import Thread
from time import time, sleep
import random


# Este programa cria 5 threads que executam a função busca da 444ª aparição de uma palavra no texto.
# Além disso, a cada 100 aparições da palavra no texto, a thread deve aguardar meio segundo antes de continuar a busca.
# O programa deve imprimir o tempo de execução de cada thread.
# O programa deve imprimir a ordem das threads que terminaram a execução.


def busca(texto, palavra, resultado):
    
    palavras = texto.split(' ')
    count = 0
    i = 0
    block = False

    inicio = time()
    
    while count < 444:
        
        if count % 100 == 0 and count != 0 and not block:
            sleep(0.5)
            block = True
        
        if palavras[i] == palavra:
            count += 1
            block = False
        
        i += 1

    resultado['tempo'] = time() - inicio


if __name__ == '__main__':
    palavra = "mas"
    with open('texto.txt', 'r') as file: texto = file.read().lower()
    
    tempo_total = time()
    tempos = [{'thread': x, 'tempo': 0} for x in range(5)]
    thrs = [Thread(target=busca, args=(texto, palavra, x), name=f"T{x['thread']}") for x in tempos]
    
    for t in thrs:
        print(f"Iniciando thread {t.name}")
        t.start()
    for t in thrs:
        t.join()
    
    tempo_total = time() - tempo_total

    print("\nTempo de execução de cada thread:")
    for t in tempos:
        print(f"Thread {t['thread']}: {t['tempo']} segundos")
    
    print("\nOrdem de término das threads:")
    for index, t in enumerate(sorted(tempos, key=lambda x: x['tempo'])):
        print(f"{index}º - Thread {t['thread']}")

    print(f"\nTempo de execução total: {tempo_total} segundos")

