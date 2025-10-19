dados_a = [4,3,25,8,19,6,25,8,16,35,45,22,8,3,16,25,7]
dados_b = [4,5,7,9,46,45,14,4,64,7,65,2,1,6,8,45,14,11]
dados_c = [4,6,7,8,1,6,10,15,16,4,2,1,4,6,12,15,16,11]

reg_posicao = 0
qtd_paginas = 8
pf_contador = 0	

def fifo(dados, memoria, paginas, pf, registrador):
	for i in dados:
		if i not in memoria:
			if registrador < paginas:
				if len(memoria) < paginas:
					memoria.append(i)
					pf += 1
					registrador += 1
				else:
					memoria[registrador] = i
					pf += 1
					registrador += 1
			else: 
				registrador = 0
				memoria[registrador] = i
				pf += 1
				registrador +=1
		else:
			print ("dado já alocado")

	return print(f'\nResultado: {memoria}, \nTotal Page Fault: {pf}, \nValor alvo na Página: {registrador}\n')

fifo(dados_a, [], qtd_paginas, pf_contador, reg_posicao)
fifo(dados_b, [], qtd_paginas, pf_contador, reg_posicao)
fifo(dados_c, [], qtd_paginas, pf_contador, reg_posicao)




	 