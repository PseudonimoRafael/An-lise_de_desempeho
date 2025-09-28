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
    
    def remove(self, valor):
        anterior = self.elemento
        defasado = anterior ## apenas criando a variável
        if anterior.valor == valor:
            self.elemento = anterior.elemento
            return anterior.valor
        
        while anterior.elemento != None:
            defasado = anterior.elemento
            if defasado.valor == valor:
                anterior.elemento = defasado.elemento
                return anterior.valor
            
            anterior = anterior.elemento
        
        return 0
    

chain = fila()

for n in range(12):
    chain.push(n)

chain.print()

chain.pop()
chain.remove(2)

chain.print()
