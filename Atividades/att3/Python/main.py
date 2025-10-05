import merge_sort as m, bubble_sort as b
import time, tracemalloc

unsorted = list()
element = "text"
value = 0

with open("../arq.txt", "r") as lista:
    while element != "":
        element = lista.readline()
        try:
            value = int(element)
        except:
            break
        unsorted.append(value)

tracemalloc.start()
inic = time.time()
sorted_bubble = b.bubble_sort(list(unsorted))
fim = time.time()
tempo = round( (fim - inic), 2)
mem = tracemalloc.get_traced_memory()[1]
tracemalloc.stop()
print(f"tempo do bubble sort :{tempo}\n memoria utilizada {mem}")

tracemalloc.start()
inic = time.time()
sorted_merge = m.merge_sort(list(unsorted))
fim = time.time()
tempo = round( (fim - inic) * 1000, 2)
mem = tracemalloc.get_traced_memory()[1]
tracemalloc.stop()

print(f"tempo do merge sort {tempo}\n memoria utilizada {mem}")

