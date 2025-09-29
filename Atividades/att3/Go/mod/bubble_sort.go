package sorters

func Bubble_sort(lista []int) []int {
	// é ideal que a lista seja retornada ordenada em vez de ordenar a lista diretamente
	array := lista
	tr := 0
	tam := len(lista)

	for i := 0; i < tam; i++ {
		for j := 1; j < tam; j++ {

			if array[j] < array[j-1] {
				tr = array[j]
				array[j] = array[j-1]
				array[j-1] = tr
			}

		}
	}
	return array
}
