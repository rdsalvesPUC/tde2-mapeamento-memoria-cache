def lru(sequencia: list[int], tamanho: int):
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
                lru_pagina = min(ultimo_uso, key=ultimo_uso.get)
                memoria[memoria.index(lru_pagina)] = pagina
                del ultimo_uso[lru_pagina]
        ultimo_uso[pagina] = tempo
        print(f"Passo {tempo + 1}: Página {pagina}, Memória: {memoria}")


sequencia = [4, 3, 25, 8, 19, 6, 25, 8, 16, 35, 45, 22, 8, 3, 16, 25, 7]
tamanho = 8
lru(sequencia, tamanho)
