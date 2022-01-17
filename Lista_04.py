pais_a = 80000
pais_b = 200000
ano = 0

while pais_b > pais_a:
    pais_a += pais_a * 0.03
    pais_b += pais_b * 0.015
    ano += 1

print("Quantidade de anos: ", ano)
