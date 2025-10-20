import java.util.Scanner;

public class Fifo {
    public static void main(String[] args) {
        /* variável que armazena as paginas na memória*/
        int[] paginacao = new int[8];
        /* variável para definir quantos espaços já estão ocupados*/
        int paginas_ocupadas = 0;
        /* váriavel usada para definir qual página vai ser trocada depois que "paginas_ocupadas" estiver
        no máximo (8)*/
        int proxima_pagina = 0;
        /* variável que armazena quantas páginas foram trocadas*/
        int troca_de_pagina= 0;

        /* Inicia o leitor (Scanner) para que o usuário possa por a sequência e armazena na variável "entrada"*/
        Scanner leitor = new Scanner(System.in);
        System.out.println("Digite a sequência de páginas: ");
        String entrada = leitor.nextLine();

        /* utiliza o split para separar todos as páginas usando a vírgula como referencial
        para realizar a separação. Depois transforma de String para Int e armazena em uma terceira
        variável que tem o exato tamanho da "paginacao"*/
        String[] partes = entrada.split(",");
        int[] sequencia = new int[partes.length];
        for (int i = 0; i < partes.length; i++) {
            sequencia[i] = Integer.parseInt(partes[i].trim());
        }

        /* Pra cada item em "sequencia" verifica se já existe pra não ocorrer duplicação, se existir apenas
        * imprime a linha novamente. Se não existir verifica se todas as paginas já estão ocupadas
        * usando "paginas_ocupadas", se não estiverem apenas adiciona uma nova página, se estiverem
        * verifica qual a próxima pagina a ser trocada e troca ela. No final imprime as paginas que
        * estão atualmente na memória (representada por "paginacao"*/
        for (int pagina : sequencia) {
            if (!existe(paginacao, paginas_ocupadas, pagina)) {
                if (paginas_ocupadas < paginacao.length) {
                    paginacao[paginas_ocupadas] = pagina;
                    troca_de_pagina++;
                    paginas_ocupadas++;
                } else {
                    paginacao[proxima_pagina] = pagina;
                    proxima_pagina = (proxima_pagina + 1) % paginacao.length;
                    troca_de_pagina++;
                }
            }
            imprimir_linha(paginacao, paginas_ocupadas);
        }
        /* no final de tudo imprime quantas páginas foram trocadas/adicionadas*/
        System.out.println("Número de troca de páginas: " + troca_de_pagina);
    }

    /* Verifica se alguma das páginas já existe na memória */
    private static boolean existe(int[] paginacao, int paginas_ocupadas, int pagina) {
        for (int i = 0; i < paginas_ocupadas; i++) {
            if (paginacao[i] == pagina) {
                return true;
            }
        }
        return false;
    }

    /* imprime as linhas com as paginas que estão na memória e no final quebra a linha para gerar o
    * formato certo da impressão */
    private static void imprimir_linha(int[] paginacao, int paginas_ocupadas) {
        for (int i = 0; i < paginas_ocupadas; i++) {
            System.out.print(paginacao[i]);
            if (i < paginas_ocupadas - 1) System.out.print(" ");
        }
        System.out.println();
    }
}
