dados_a = [4,3,25,8,19,6,25,8,16,35,45,22,8,3,16,25,7]
dados_b = [4,5,7,9,46,45,14,4,64,7,65,2,1,6,8,45,14,11]
dados_c = [4,6,7,8,1,6,10,15,16,4,2,1,4,6,12,15,16,11]

qtd_paginas = 8
memoria = []
pf_contador = 0

def fifo(dados, paginas):
	for i in dados:
		if len(memoria) < paginas:
			memoria.append(i)
	return memoria

fifo(dados_a, qtd_paginas)

print(memoria)
	