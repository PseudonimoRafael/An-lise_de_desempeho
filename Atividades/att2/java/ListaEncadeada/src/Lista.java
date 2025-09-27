    /*
    public int achar(int valor) {
        return recAchar(valor, Cabeca);
    }
    private int recAchar(int valor, Elemento el) {
        if (el.Valor == valor){
            return valor;
        } else if (el.Proximo == null) {
            return 0;
        } else {
            return recAchar(valor, el.Proximo);
        }
    }
    */


public class Lista {
    public Elemento Cabeca = null;

    public void push(int valor) {
    if (Cabeca == null)
        primeiroValor(valor);
    Valor(valor);
    }

    private void primeiroValor(int valor) {
        Cabeca = new Elemento(valor);
    }
    private void Valor(int valor) {
        Elemento anterior = Cabeca;
        Cabeca = new Elemento(anterior, valor);
    }

    public void imprimeLista() {
        recLista(Cabeca);
    }
    private void recLista(Elemento proximo) {
        if (proximo.Proximo != null) {

            System.out.print(proximo.Valor); System.out.printf(" "); 
            recLista(proximo.Proximo);
        }
    }

        public int remove(int valor) {
            Elemento anterior = Cabeca;
            Elemento defasado;
            if (anterior.Valor == valor) {
                    Cabeca = anterior.Proximo;
                    return anterior.Valor;
                }
            
            while (anterior.Proximo != null) {
                defasado = anterior.Proximo;
                if (defasado.Valor == valor)
                    {
                    anterior.Proximo = defasado.Proximo;
                    return anterior.Valor;
                    }
                anterior = anterior.Proximo;
            } return 0;
        }
}
