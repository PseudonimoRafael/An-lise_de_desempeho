package main

import (
	sorters "att3/mod"
	"fmt"
	"io"
	"os"
	"runtime"
	"time"
)

// literalmente um copiar-colar do grok
// getMemStats captura estatísticas de memória
func getMemStats() runtime.MemStats {
	var memStats runtime.MemStats
	runtime.ReadMemStats(&memStats)
	return memStats
}

func ReadFile(filePath string) (lista []int) {
	fd, err := os.Open(filePath)
	if err != nil {
		panic(err)
	}
	var line int
	for {
		_, err := fmt.Fscanf(fd, "%d\n", &line)

		if err != nil {
			fmt.Print(err)
			if err == io.EOF {
				return
			}
			panic(fmt.Sprint("scan failed %s, %v", filePath, err))
		}
		lista = append(lista, line)
	}

}

func main() {

	lista := ReadFile("../arq.txt")

	inicioBubble := getMemStats()
	start := time.Now()
	sorters.Bubble_sort(lista)
	tempoBubble := time.Since(start)
	memBubble := getMemStats().TotalAlloc - inicioBubble.TotalAlloc

	inicioMerge := getMemStats()
	start = time.Now()
	sorters.MergeSort(lista)
	tempoMerge := time.Since(start)
	memMerge := getMemStats().TotalAlloc - inicioMerge.TotalAlloc

	fmt.Printf("tempo decorrido bubble\n: %v\n", tempoBubble)
	fmt.Printf("tempo decorrido Merge\n: %v\n\n", tempoMerge)

	fmt.Printf("memória alocada bubble\n: %v\n", memBubble)
	fmt.Printf("memória alocada Merge\n: %v\n\n", memMerge)

}
