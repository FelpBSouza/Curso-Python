class Calculadora:
    def __init__(self,num1,num2):
        self.valor_a = num1
        self.valor_b = num2

    def soma(self):
        return self.valor_a + self.valor_b

    def subtracao(self):
        return self.valor_a - self.valor_b

"""  print (soma(1,2))
    print (soma(3,4))
    print(subtracao(10,2)) """

calculadora = Calculadora(10,2)
print (calculadora.valor_a)
print (calculadora.soma())
print (calculadora.subtracao())