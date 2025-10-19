# Sequências de páginas para teste
dados_a = [4,3,25,8,19,6,25,8,16,35,45,22,8,3,16,25,7]
dados_b = [4,5,7,9,46,45,14,4,64,7,65,2,1,6,8,45,14,11]
dados_c = [4,6,7,8,1,6,10,15,16,4,2,1,4,6,12,15,16,11]

# Controle da posição na memória
reg_posicao = 0
# Quantidade máxima de quadros na memória
qtd_paginas = 8
# Lista que representa a memória
memoria_vazia = []
# Contador de page faults
pf_contador = 0 

def fifo(dados, memoria, paginas, pf, registrador):
    for i in dados:
        # Se a página não está na memória
        if i not in memoria:
            # Se ainda há espaço
            if registrador < paginas:
                # Caso a memória ainda não esteja cheia
                if len(memoria) < paginas:
                    memoria.append(i)
                    pf += 1
                    registrador += 1
                else:
                    # Substitui página antiga
                    memoria[registrador] = i
                    pf += 1
                    registrador += 1
            else:
                # Reinicia posição ao chegar no fim
                registrador = 0
                memoria[registrador] = i
                pf += 1
                registrador +=1
        else:
            print ("dado já alocado")

    # Exibe resultado final
    return print(f'\nResultado: {memoria}, \nTotal Page Fault: {pf}, \nValor alvo na Página: {registrador}\n')

# Execução dos testes
fifo(dados_a, memoria_vazia, qtd_paginas, pf_contador, reg_posicao)
fifo(dados_b, memoria_vazia, qtd_paginas, pf_contador, reg_posicao)
fifo(dados_c, memoria_vazia, qtd_paginas, pf_contador, reg_posicao)
