numero = int(input('Factorial de:'))

resultado = 1
for a in range(1, numero + 1):
   resultado *=  a

print('O factorial de {} é igual a {}'.format(numero, resultado))
