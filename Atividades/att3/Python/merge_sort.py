def merge(a, b):
    lena = len(a)
    lenb = len(b)
    index1, index2 = 0, 0

    res_list = list()

    while index1 < lena or index2 < lenb:
        
        if index1 == lena:
            res_list.append(b[index2])
            index2 += 1
        
        elif index2 == lenb:
            res_list.append(a[index1])
            index1 += 1
            
        elif a[index1] < b[index2]:
            res_list.append(a[index1])
            index1 += 1
        
        else:
        # elif a[index1] >= b[index2]:
            res_list.append(b[index2])
            index2 += 1
    
    return res_list

def half(n): return int(n / 2)

def merge_sort_rec(a, b):
    ## uma implementação recursiva do merge_sort
    if len(a) > 1 and len(b) > 1:
        halfa = half(len(a))
        halfb = half(len(b))

        # particionando
        a1 = a[0: halfa]
        a2 = a[halfa: len(a)]

        b1 = b[0: halfb]
        b2 = b[halfb: len(b)]

        lista1 = merge_sort_rec(a1, a2)
        lista2 = merge_sort_rec(b1, b2)

        return merge(lista1, lista2)
    
    return merge(a, b)
