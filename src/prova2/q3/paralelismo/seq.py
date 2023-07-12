from time import time

# Programa que conta ocorrências de palavras em um texto sem paralelismo
# O programa lê um arquivo texto.txt e conta ocorrências de palavras em uma lista de palavras
# O programa imprime o resultado da contagem de ocorrências de cada palavra da lista de palavras

def busca(texto, palavra):
    palavras = texto.split(' ')
    count = 0
    for p in palavras:
        if p == palavra:
            count += 1
    return count


if __name__ == '__main__':
    with open('texto.txt', 'r') as file:
        texto = file.read().lower()
        plvs = ["mas", "passado", "a", "poderia", "semana", "creio", "casa", "e"]
        resultados = [{'plv': x, 'count': 0} for x in plvs]

        inicio = time()

        for r in resultados:
            r['count'] = busca(texto, r['plv'])

        for r in resultados:
            print(f"Palavra: {r['plv']}, Ocorrências: {r['count']}")
        
        fim = time() - inicio

        print(f"Tempo de execução usando sequencial: {fim} segundos")
    