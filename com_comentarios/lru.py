#sequencia é a lista de páginas que irão ser acessadas
#tamanho é a quantidade de quadros de memória disponíveis
def lru(sequencia: list[int], tamanho: int):
    #memoria é a lista que representa os quadros de memória (cada item é uma página)
    memoria = []
    #faltas é o contador de page faults
    faltas = 0
    #ultimo_uso é o dicionário mapeando página para o último tempo em que foi acessada
    ultimo_uso = {}

    for tempo in range(len(sequencia)):
        #percorre a sequência usando o índice tempo para registrar o momento do acesso
        pagina = sequencia[tempo]
        #valor da página acessada no passo atual
        if pagina not in memoria:
            #se a página não está em memória: incrementa 'faltas' (page fault)
            faltas += 1
            if len(memoria) < tamanho:
                #se há espaço (len(memoria) < tamanho) insere a página no próximo quadro livre
                memoria.append(pagina)
            else:
                #caso contrário, procura a página na memória que foi usada há mais tempo (LRU), logo o menor ultimo_uso[pagina]
                lru_pagina = min(ultimo_uso, key=ultimo_uso.get)
                #substitui essa página pelo novo valor e remove seu registro de 'ultimo_uso'
                memoria[memoria.index(lru_pagina)] = pagina
                del ultimo_uso[lru_pagina]
        #sempre que uma página é acessada (hit ou after insert), atualiza ultimo_uso[pagina] = tempo
        ultimo_uso[pagina] = tempo
        #imprime o estado por passo
        print(f"Passo {tempo + 1}: Página {pagina}, Memória: {memoria}")
    #imprime o total de faltas
    print(f"Faltas: {faltas}")
    #retorna a memória no final do processo
    return memoria

#bloco principal
#contém as sequências pedidas no enunciado e localiza as páginas pedidas
#o índice retornado é incrementado em 1 para exibir a posição humana
#o numero de páginas foi settado como 8 igual pedido no enunciado
if __name__ == "__main__":
    sequencia = [4, 3, 25, 8, 19, 6, 25, 8, 16, 35, 45, 22, 8, 3, 16, 25, 7]
    tamanho = 8
    memorias = lru(sequencia, tamanho)
    print(f"A página 7 está no quadro: {memorias.index(7) + 1}")
    sequencia = [4, 5, 7, 9, 46, 45, 14, 4, 64, 7, 65, 2, 1, 6, 8, 45, 14, 11]
    memorias = lru(sequencia, tamanho)
    print(f"A página 11 está no quadro: {memorias.index(11) + 1}")
    sequencia = [4, 6, 7, 8, 1, 6, 10, 15, 16, 4, 2, 1, 4, 6, 12, 15, 16, 11]
    memorias = lru(sequencia, tamanho)
    print(f"A página 11 está no quadro: {memorias.index(11) + 1}")