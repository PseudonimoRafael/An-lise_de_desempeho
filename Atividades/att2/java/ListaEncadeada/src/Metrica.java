import java.time.Duration;
import java.time.Instant;

public class Metrica {
    /*
        métodos:
        start -> começa a registrar (Void)
        stop -> para de registar  (Void)
        show -> mostra resultados (String)
    */
    private float mem0, mem;
    private Instant inic, fim;

    private Duration tempo;
    private float memUtilizada;

    private Runtime runtime = Runtime.getRuntime();


   public void start() {
        // limpar o garbage Collector
        System.gc();

        mem0 = runtime.totalMemory() - runtime.freeMemory();
        inic = Instant.now();
   }
   public void stop() {
        mem = runtime.totalMemory() - runtime.freeMemory();
        fim = Instant.now();
        tempo = Duration.between(inic, fim);
        memUtilizada = mem - mem0;
   }

   public String show() {
    return "\nTempo: " + tempo.toMillis() + "ms\nMemoria: " + memUtilizada + "kB\n";
   }
}
