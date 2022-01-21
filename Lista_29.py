produtos = int(input("Digite a quantidade de produtos: "))
while produtos > 50:
    produtos = int(input("Digite a quantidade de produtos[menos que 50]: "))


precos = []
numero_produto = 1
count = 0

for i in range(produtos):
    print("Produto N° ", numero_produto)
    preco = precos.append(float(input("Digite o preco do produto: ")))
    numero_produto += 1

numero_produto = 1
for j in range(produtos):
    print("Produto N° ", numero_produto, "= ", precos[count])
    count += 1
    numero_produto += 1
