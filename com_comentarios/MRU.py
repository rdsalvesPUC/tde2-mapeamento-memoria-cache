# sequencia = a lista de paginas que vão chegar 4, 3, 25, ...
# tamanho = quantas caixinhas temos 8 no caso
# memoria = lista das páginas que estão nas caixinhas
# faltas = contador de quantas vezes a página não estava na memoria
# ultimo_uso = dicionario que guarda o tempo da última vez que cada pagina foi usada

def mru(sequencia: list[int], tamanho: int):
    memoria = []
    faltas = 0
    ultimo_uso = {}
    
    # tempo = numero de passos 0, 1 ...
    for tempo in range(len(sequencia)):
        
        # pagina = valor naquele passo guardado
        pagina = sequencia[tempo]

        # verifica se a pagina ja esta na memoria
        if pagina not in memoria:
            faltas += 1 # incrementa o contador de faltas

            if len(memoria) < tamanho: # se ainda tem caixa vazia apenas incrementa
                memoria.append(pagina)
                
            else:  # memoria cheia e a pagina nao esta na memoria, precisa substituir
                mru_pagina = max(ultimo_uso, key=ultimo_uso.get) # encontra a pagina que foi usada mais recentemente (maior valor no dicionario ultimo_uso)
                memoria[memoria.index(mru_pagina)] = pagina # procura em qual posicao (quadro) essa pagina esta na memoria e troca pela nova pagina
                del ultimo_uso[mru_pagina] # remove a pagina expulsa do dicionario de ultimo uso, pois ela nao esta mais na memoria
        ultimo_uso[pagina] = tempo # registra o tempo atual em que a pagina foi usada
        print(f"Passo {tempo + 1}: Página {pagina}, Memória: {memoria}") # mostra o estado atual da memoria para acompanhar passo a passo
    print(f"Faltas: {faltas}")
    return memoria # retorna o estado final dos quadros da memoria


if __name__ == "__main__":
    sequencia = [4, 3, 25, 8, 19, 6, 25, 8, 16, 35, 45, 22, 8, 3, 16, 25, 7] # sequencia a
    tamanho = 8 # tamanho da memoria (quantidade de quadros)
    memorias = mru(sequencia, tamanho)
    print(f"A página 7 está no quadro: {memorias.index(7) + 1}")
    sequencia = [4, 5, 7, 9, 46, 45, 14, 4, 64, 7, 65, 2, 1, 6, 8, 45, 14, 11] # sequencia b
    memorias = mru(sequencia, tamanho)
    print(f"A página 11 está no quadro: {memorias.index(11) + 1}")
    sequencia = [4, 6, 7, 8, 1, 6, 10, 15, 16, 4, 2, 1, 4, 6, 12, 15, 16, 11] # sequencia c
    memorias = mru(sequencia, tamanho)
    print(f"A página 11 está no quadro: {memorias.index(11) + 1}")