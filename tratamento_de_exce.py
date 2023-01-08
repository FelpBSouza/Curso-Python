lista = [1,10]







try:
    divisao = 10/1
    numero = lista[1]
    x = a
except BaseException as ex:
    print ('erro desconhecido.Erro:{}'.format(ex))
except ZeroDivisionError:
    print ('Não é possivel realizar uma divisão por 0')
except IndexError:
    print ('Erro ao acessar um indice invalido da lista')
