import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class Main {
    
    public static void main(String[] args)
    {
        Metrica med = new Metrica();
        
        // abrindo arquivo para leitura
        String[] cont = readFile("../../../arq-novo.txt");
        ListaOperavel chain = new ListaOperavel();
        
        // pondo os elementos na lista
        String[] numeros = cont[0].split(" ");
        int tam_inic = numeros.length;
        int tam = Integer.parseInt(cont[1]);
        int casting;

        med.start();
        // obs: o for tem que ser invertido para a lista ser indexada na ordem correta.
        for (int i = tam_inic -1; i > -1; i--) {
            casting = Integer.parseInt(numeros[i]);
            chain.push(casting);
        }
        
        for (int com = 0; com < tam; com++) {
            chain.executaComando(cont[com + 2]);
        }
        med.stop();

        System.out.println(med.show());
    }


        public static String[] readFile(String path) {
        File arq = new File(path);
        String[] lista = new String[1024*1024];
        int len = 0; 
        try (Scanner Dados = new Scanner(arq)){
            while (Dados.hasNext()){
                lista[len] = Dados.nextLine();
                len++;
            }
        } catch (FileNotFoundException e) {
            System.err.println(e);
        }
        return lista;
        }
}