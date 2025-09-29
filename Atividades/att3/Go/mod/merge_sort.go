package sorters

func MergeSort(arr []int) []int {
	if len(arr) <= 1 {
		return arr
	}

	mid := len(arr) / 2
	left := MergeSort(arr[:mid])
	right := MergeSort(arr[mid:])

	return merge(left, right)
}

func merge(a, b []int) []int {
	lena := len(a)
	lenb := len(b)
	res_list := make([]int, 0, lena+lenb)
	i, j := 0, 0
	for i < lena || j < lenb {
		if i == lena {
			res_list = append(res_list, b[j])
			j++
		} else if j == lenb {
			res_list = append(res_list, a[i])
			i++
		} else if a[i] < b[j] {
			res_list = append(res_list, a[i])
			i++
		} else {
			res_list = append(res_list, b[j])
			j++
		}
	}
	return res_list
}
