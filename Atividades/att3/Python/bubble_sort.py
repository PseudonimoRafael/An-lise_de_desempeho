def bubble_sort(lista):
    tam = len(lista)
    val = 0 ## apenas uma variável temporaria para a troca
    swapped = False
    for i in range(tam):
        swapped = False
        for j in range(0, tam - i - 1):
            if lista[j + 1] < lista[j]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                swapped = True

        if not swapped:
            break

    return lista
