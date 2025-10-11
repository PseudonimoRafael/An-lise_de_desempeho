class Elemento:
    def __init__(self, valor, elemento):
        self.elemento = elemento
        self.valor = valor

class Linked_List:
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

    
class Lista(Linked_List):
    def __init__(self):
        super().__init__()

    def execute(self, string):
        comando = string.split(" ")
        comando[-1] = comando[-1][0:-1]
        
        # print(comando)
        if comando[0] == 'P':
            self.print()
        elif comando[0] == 'A':
            self.push(comando[1])
        elif comando[0] == 'R':
            self.remove(comando[1])

    def generate_from_list(self, lista):
        for V in lista:
            self.push(
                int(V)
                )