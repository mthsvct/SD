from threading import Thread
from time import time

def busca(texto, palavra, result):
    palavras = texto.split(' ')
    count = 0
    for p in palavras:
        if p == palavra:
            count += 1
    
    result['count'] += count


if __name__ == '__main__':

    with open('texto.txt', 'r') as file:
        texto = file.read().lower()
        plvs = ["mas", "passado", "a", "poderia", "semana", "creio", "casa", "e"]
        resultados = [{'plv': x, 'count': 0} for x in plvs]

        inicio = time()

        processos = [Thread(target=busca, args=(texto, r['plv'], r)) for r in resultados]

        for p in processos:
            p.start()
        
        for p in processos:
            p.join()

        fim = time() - inicio

        for r in resultados:
            print(f"Palavra: {r['plv']}, Ocorrências: {r['count']}")
        
        print(f"Tempo de execução usando concorrencia: {fim} segundos")