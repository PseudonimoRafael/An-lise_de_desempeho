def merge(a, b):
    lena = len(a)
    lenb = len(b)
    index1, index2 = 0, 0

    res_list = list()

    while index1 < lena and index2 < lenb:
        if a[index1] < b[index2]:
            res_list.append(a[index1])
            index1 += 1
        
        else:
        # elif a[index1] >= b[index2]:
            res_list.append(b[index2])
            index2 += 1
    
    while index1 < lena:
        res_list.append(a[index1])
        index1 += 1

    while index2 < lenb:
        res_list.append(b[index2])
        index2 += 1
    
    return res_list

def half(n): return int(n / 2)

def merge_sort(lista):
    l = len(lista)
    ## uma implementação recursiva do merge_sort
    if l > 1:
        l2 = half(l)

        # particionando
        a1 = merge_sort(lista[0: l2])
        a2 = merge_sort(lista[l2: l])

        return merge(a1, a2)
    
    return lista
