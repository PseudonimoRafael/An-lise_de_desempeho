from fila import Lista
from metricas import metricas
# Lista:
#     -- Adicionar(indice, valor)
#     -- Remover(valor)
#     -- Printar()
# 
# recebe do jeito que está formatado no arquivo -- Recebe o dado em String

# Abrindo Arquivo com dados

lista = Lista()
comandos = list()
index = 2 ## linha zero sempre tem a lista completa

with open("../arq-novo.txt", "r") as file:
    comandos = file.readlines()

# Pondo os números na lista
lista.generate_from_list(comandos[0].split(" "))
fim = int(comandos[1]) + 2
# Executando os comandos da lista.

Med = metricas()

Med.start()
while index < fim:
    lista.execute(comandos[index])
    index += 1

Med.stop()
print(Med.show())
