package sorters

func Bubble_sort(lista []int) []int {
	// é ideal que a lista seja retornada ordenada em vez de ordenar a lista diretamente
	array := lista
	tr := 0
	tam := len(lista)
	var swap bool
	for i := 0; i < tam; i++ {
		swap = false
		for j := 0; j < tam-1; j++ {
			if array[j+1] < array[j] {
				tr = array[j]
				array[j] = array[j+1]
				array[j+1] = tr
				swap = true
			}
		}
		if !swap {
			break
		}
	}
	return array
}
