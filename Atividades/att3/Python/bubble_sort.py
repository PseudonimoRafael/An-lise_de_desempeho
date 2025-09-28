def bubble_sort(lista):
    tam = len(lista)
    val = 0 ## apenas uma variável temporaria para a troca
    for _ in range(tam):
        for j in range(1, tam):
            if lista[j - 1] > lista[j]:
                val = lista[j-1]
                lista[j-1] = lista[j]
                lista[j] = val

    return lista
