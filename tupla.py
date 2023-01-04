""" TUPLA É IMUTAVEL """
lista  = [1,3,5,7]
lista_animal =['cachorro','gato','elefante']

tupla = (1,10,12,14)
print (tupla[0])

tupla[0] = 12   
""" QUANTOS ELEMENTOS TEM NA TUPLA OU LISTA """
print (len(tupla))

""" CONVERSÃO LISTA EM TUPLA """
tupla_animal = tuple(lista_animal)
print (tupla_animal)