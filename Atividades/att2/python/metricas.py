"""
Essa classe mede a quantidade de memória e tempo tudo
numa mesma instância
"""

import time, tracemalloc

class metricas:
    def __init__(self):
        """
        Para começar medida -> start()
        para acabar medida -> stop()
        Para mostrar informações -> show()
        """
        self.inic = 0
        self.tempo = 0
        self.memoria = 0
    
    def start(self):
        ## memŕia
        tracemalloc.start()

        ## tempo
        self.inic = time.time()

    def stop(self):
        ## memŕia
        self.memoria = tracemalloc.get_traced_memory()[1]
        tracemalloc.stop()

        ## tempo
        self.tempo  = time.time() - self.inic

    def show(self):
        # Pelo menos está formatado certinho 
        string = """
    Memória utilizada: {mem} KB
    Tempo decorrido : {time} s
""".format(mem= self.memoria, time=self.tempo)
        return string