public class Main {
    public static void main(String[] args)
    {
        Lista chain = new Lista();
        chain.push(10);
        chain.push(11);
        chain.push(12);
        chain.push(15);
        chain.push(14);
        chain.push(13);
        chain.imprimeLista();
        // System.out.println(chain.pop(11));
        chain.remove(11);
        chain.imprimeLista();
    }
}