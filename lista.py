lista  = [1,3,5,7]
lista_animal =['cachorro','gato','elefante']

nova_lista = lista_animal * 3
print (nova_lista)

print (lista_animal[1])

for x in lista_animal:
    print (x)
    
    
print (sum(lista))
print (max(lista))
print (min(lista))

if 'lobo' in lista_animal:
    print ('existe um gato na lista')
else:
    print ('não existe um gato na lista')
    lista_animal.append ('lobo')
    print (lista_animal)

lista_animal.pop()
print (lista_animal)

lista_animal.remove('lobo')
print (lista_animal)

""" ordenar lista """
lista.sort()
lista_animal.sort()
print (lista_animal)
print (lista)

""" reverter lista """
lista_animal.reverse()
print (lista_animal)