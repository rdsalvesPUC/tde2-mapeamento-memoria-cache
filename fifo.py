dados_a = [4,3,25,8,19,6,25,8,16,35,45,22,8,3,16,25,7]
dados_b = [4,5,7,9,46,45,14,4,64,7,65,2,1,6,8,45,14,11]
dados_c = [4,6,7,8,1,6,10,15,16,4,2,1,4,6,12,15,16,11]

qtd_paginas = 8
memoria_vazia = []
pf_contador = 0

def fifo(dados, memoria, paginas, pf):
	for i in dados:
		if len(memoria) < paginas:
			if i not in memoria: 
				memoria.append(i)
				pf += 1
			else:
				print ("dado já alocado")
	return print(memoria, pf)

fifo(dados_a, memoria_vazia, qtd_paginas, pf_contador)
	 