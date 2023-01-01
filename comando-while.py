a = float(input('Primeira nota:'))
while a >10:
    a = float(input('Você digitou errado a sua primeira nota.Digite novamente a primeira nota:'))

b = float(input('Segunda nota:'))
while b > 10:
    b = float(input('Você digitou errado a sua segunda nota.Digite novamente a segunda nota:'))

c = float(input('Terceira nota:'))
while c > 10:
    c = float(input('Você digitou errado a sua terceira nota.Digite novamente a terceira nota:'))

d = float(input('Quarta nota:'))
while d > 10:
    d = float(input('Você digitou errado a sua quarta nota.Digite novamente a quarta nota:'))
    

media = (a + b +c +d)/4
print ('media: {}'.format(media))