public class ListaOperavel extends Lista{
    public void executaComando(String comando)
    {
        int valor1;
        int valor2;

        String[] form = comando.split(" ");
        if (null != form[0]) switch (form[0]) {
            case "P":
                print();
                break;
            case "R":
                valor1 = Integer.parseInt(form[1]);
                remove(valor1);
                break;
            case "A":
                valor1 = Integer.parseInt(form[1]); // valor p ser adicionado
                valor2 = Integer.parseInt(form[2]); // posição
                adiciona(valor2, valor1);
                break;
            default:
                break;
        }
    }
}
