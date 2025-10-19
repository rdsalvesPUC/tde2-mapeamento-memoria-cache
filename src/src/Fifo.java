import java.util.Scanner;

public class Fifo {
    public static void main(String[] args) {
        int[] paginacao = new int[8];
        int paginasOcupadas = 0;
        int proximaPagina = 0;

        Scanner leitor = new Scanner(System.in);
        System.out.println("Digite a sequência de páginas: ");
        String entrada = leitor.nextLine();

        String[] partes = entrada.split(",");
        int[] sequencia = new int[partes.length];
        for (int i = 0; i < partes.length; i++) {
            sequencia[i] = Integer.parseInt(partes[i].trim());
        }

        for (int pagina : sequencia) {
            if (!existe(paginacao, paginasOcupadas, pagina)) {
                if (paginasOcupadas < paginacao.length) {
                    paginacao[paginasOcupadas] = pagina;
                    paginasOcupadas++;
                } else {
                    paginacao[proximaPagina] = pagina;
                    proximaPagina = (proximaPagina + 1) % paginacao.length;
                }
            }
            imprimirLinha(paginacao, paginasOcupadas);
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
