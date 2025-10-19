def mru(sequencia: list[int], tamanho: int):
    memoria = []
    faltas = 0
    ultimo_uso = {}
    
    
    for tempo in range(len(sequencia)):
        
        
        pagina = sequencia[tempo]

        
        if pagina not in memoria:
            faltas += 1

            if len(memoria) < tamanho:
                memoria.append(pagina)
                
            else:
                mru_pagina = max(ultimo_uso, key=ultimo_uso.get)
                memoria[memoria.index(mru_pagina)] = pagina
                del ultimo_uso[mru_pagina]
        ultimo_uso[pagina] = tempo
        print(f"Passo {tempo + 1}: Página {pagina}, Memória: {memoria}")
    print(f"Faltas: {faltas}")
    return memoria


if __name__ == "__main__":
    sequencia = [4, 3, 25, 8, 19, 6, 25, 8, 16, 35, 45, 22, 8, 3, 16, 25, 7]
    tamanho = 8
    memorias = mru(sequencia, tamanho)
    print(f"A página 7 está no quadro: {memorias.index(7) + 1}")
    sequencia = [4, 5, 7, 9, 46, 45, 14, 4, 64, 7, 65, 2, 1, 6, 8, 45, 14, 11]
    memorias = mru(sequencia, tamanho)
    print(f"A página 11 está no quadro: {memorias.index(11) + 1}")
    sequencia = [4, 6, 7, 8, 1, 6, 10, 15, 16, 4, 2, 1, 4, 6, 12, 15, 16, 11]
    memorias = mru(sequencia, tamanho)
    print(f"A página 11 está no quadro: {memorias.index(11) + 1}")