a = int(input('Entre com o numero:'))

div = 0
for x in range(1, a + 1):
    resto = a % x
    print(a,resto)

    if resto == 0:
        div += 1

if div == 2:
    print('numero {} é primo'.format(a))
else:
    print('numero {} não é primo'.format(a))
