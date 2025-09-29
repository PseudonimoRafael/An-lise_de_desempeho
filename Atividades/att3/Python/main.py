import merge_sort as m, bubble_sort as b
from dados import unsorted
import time, tracemalloc

tracemalloc.start()
inic = time.time()
sorted_bubble = b.bubble_sort(list(unsorted))
fim = time.time()
tempo = round( (fim - inic), 2)
mem = tracemalloc.get_traced_memory()[1]
tracemalloc.stop()
print(f"tempo do bubble sort :{tempo}\n memoria utilizada{mem}")

tracemalloc.start()
inic = time.time()
sorted_merge = m.merge_sort(list(unsorted))
fim = time.time()
tempo = round( (fim - inic) * 1000, 2)
mem = tracemalloc.get_traced_memory()[1]
tracemalloc.stop()

print(f"tempo do merge sort {tempo}\n memoria utilizada {mem}")

print(sorted_merge)
