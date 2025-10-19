import java.util.Scanner;

public class Fifo {
    public static void main(String[] args) {
        int[] paginacao = new int[8];
        int paginas_ocupadas = 0;
        int proxima_pagina = 0;

        Scanner leitor = new Scanner(System.in);
        System.out.println("Digite a sequência de páginas: ");
        String entrada = leitor.nextLine();

        String[] partes = entrada.split(",");
        int[] sequencia = new int[partes.length];
        for (int i = 0; i < partes.length; i++) {
            sequencia[i] = Integer.parseInt(partes[i].trim());
        }

        for (int pagina : sequencia) {
            if (!existe(paginacao, paginas_ocupadas, pagina)) {
                if (paginas_ocupadas < paginacao.length) {
                    paginacao[paginas_ocupadas] = pagina;
                    paginas_ocupadas++;
                } else {
                    paginacao[proxima_pagina] = pagina;
                    proxima_pagina = (proxima_pagina + 1) % paginacao.length;
                }
            }
            imprimirLinha(paginacao, paginas_ocupadas);
        }
    }

    private static boolean existe(int[] paginacao, int paginas_ocupadas, int pagina) {
        for (int i = 0; i < paginas_ocupadas; i++) {
            if (paginacao[i] == pagina) {
                return true;
            }
        }
        return false;
    }

    private static void imprimirLinha(int[] paginacao, int paginas_ocupadas) {
        for (int i = 0; i < paginas_ocupadas; i++) {
            System.out.print(paginacao[i]);
            if (i < paginas_ocupadas - 1) System.out.print(" ");
        }
        System.out.println();
    }
}
