class Elemento:
    def __init__(self, valor, elemento):
        self.elemento = elemento
        self.valor = valor

class fila:
    def __init__(self):
        self.elemento = Elemento(0, None)

    def push(self, valor):
        encadear = self.elemento
        self.elemento = Elemento(valor, encadear)
    
    def print(self):
        cadeia = self.elemento
        while cadeia.elemento != None:
            print("{0}".format(cadeia.valor), end=" ")
            cadeia = cadeia.elemento

    def pop(self):
        topo = self.elemento
        self.elemento = topo.elemento
        return topo.valor
    
chain = fila()
chain.push(1)
chain.push(2)
chain.push(3)

chain.print()

chain.pop()

chain.print()
