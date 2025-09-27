public class Elemento {
    public Elemento Proximo;
    public int Valor;

    public Elemento(Elemento proximo, int valor) {
        Proximo = proximo;
        Valor= valor;
    }
    public Elemento( int valor) {
        Proximo = null;
        Valor= valor;
    }
}
