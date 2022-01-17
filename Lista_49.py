print('1-File Duplo: 4,90 por Kg')
print('2-Alcatra: 5,90 por Kg')
print('3-Picanha: 6,60 por Kg')
print()

opcao = input('Escolha uma das opcoes:')
if opcao == "1":
   quantidade = int(input('Qual quntidade deseja:'))
   if quantidade <= 5:
       cartao = input('Deseja usar o cartao ArrobaMZ[1-(SIM), 2-(NAO):')
       if cartao == "1":
         total = 4.90 * quantidade
         desconto = ((4.90 * quantidade) * 5 ) / 100
         novototal = total - desconto
         print()
         print('Tipo de Carne: File Duplo')
         print('Quantidade:',quantidade, 'Kg')
         print('Preco Total:',total,'Mts')
         print('Tipo de pagamento: Cartao ArrobaMZ')
         print('Valor do Desconto:',desconto)
         print('Valor a pagar:',novototal,'Mts')
       else:
           if cartao == "2":
             total = 4.90 * quantidade
             print()
             print('Tipo de Carne: File Duplo')
             print('Quantidade:',quantidade, 'Kg')
             print('Preco Total:',total,'Mts')
             print('Tipo de pagamento: Cash Out')
             print('Valor do Desconto: 0 Mts')
             print('Valor a pagar:',total,'Mts')
   if quantidade > 5:
       cartao = input('Deseja usar o cartao ArrobaMZ[1-(SIM), 2-(NAO):')
       if cartao == "1":
         total = 5.80 * quantidade
         desconto = ((5.80 * quantidade) * 5 ) / 100
         novototal = total - desconto
         print()
         print('Tipo de Carne: File Duplo')
         print('Quantidade:',quantidade, 'Kg')
         print('Preco Total:',total,'Mts')
         print('Tipo de pagamento: Cartao ArrobaMZ')
         print('Valor do Desconto:',desconto)
         print('Valor a pagar:',novototal,'Mts')
       if cartao == "2":
          total = 5.80 * quantidade
          print()
          print('Tipo de Carne: File Duplo')
          print('Quantidade:',quantidade, 'Kg')
          print('Preco Total:',total,'Mts')
          print('Tipo de pagamento: Cash Out')
          print('Valor do Desconto: 0 Mts')
          print('Valor a pagar:',total,'Mts')

elif opcao == "2":
    quantidade = int(input('Qual quntidade deseja:'))
    if quantidade <= 5:
       cartao = input('Deseja usar o cartao ArrobaMZ[1-(SIM), 2-(NAO):')
       if cartao == "1":
         total = 5.90 * quantidade
         desconto = ((5.90 * quantidade) * 5 ) / 100
         novototal = total - desconto
         print()
         print('Tipo de Carne: Alcatra')
         print('Quantidade:',quantidade, 'Kg')
         print('Preco Total:',total,'Mts')
         print('Tipo de pagamento: Cartao ArrobaMZ')
         print('Valor do Desconto:',desconto)
         print('Valor a pagar:',novototal,'Mts')
       else:
           if cartao == "2":
             total = 5.90 * quantidade
             print()
             print('Tipo de Carne: Alcatra')
             print('Quantidade:',quantidade, 'Kg')
             print('Preco Total:',total,'Mts')
             print('Tipo de pagamento: Cash Out')
             print('Valor do Desconto: 0 Mts')
             print('Valor a pagar:',total,'Mts')
    if quantidade > 5:
       cartao = input('Deseja usar o cartao ArrobaMZ[1-(SIM), 2-(NAO):')
       if cartao == "1":
         total = 6.80 * quantidade
         desconto = ((6.80 * quantidade) * 5 ) / 100
         novototal = total - desconto
         print()
         print('Tipo de Carne: Alcatra')
         print('Quantidade:',quantidade, 'Kg')
         print('Preco Total:',total,'Mts')
         print('Tipo de pagamento: Cartao ArrobaMZ')
         print('Valor do Desconto:',desconto)
         print('Valor a pagar:',novototal,'Mts')
       if cartao == "2":
          total = 6.80 * quantidade
          print()
          print('Tipo de Carne: File Duplo')
          print('Quantidade:',quantidade, 'Kg')
          print('Preco Total:',total,'Mts')
          print('Tipo de pagamento: Cash Out')
          print('Valor do Desconto: 0 Mts')
          print('Valor a pagar:',total,'Mts')
else:
    if opcao == "3":
       quantidade = int(input('Qual quntidade deseja:'))
    if quantidade <= 5:
       cartao = input('Deseja usar o cartao ArrobaMZ[1-(SIM), 2-(NAO):')
       if cartao == "1":
         total = 6.90 * quantidade
         desconto = ((6.90 * quantidade) * 5 ) / 100
         novototal = total - desconto
         print()
         print('Tipo de Carne: Picanha')
         print('Quantidade:',quantidade, 'Kg')
         print('Preco Total:',total,'Mts')
         print('Tipo de pagamento: Cartao ArrobaMZ')
         print('Valor do Desconto:',desconto)
         print('Valor a pagar:',novototal,'Mts')
       else:
           if cartao == "2":
             total = 6.90 * quantidade
             print()
             print('Tipo de Carne: File Duplo')
             print('Quantidade:',quantidade, 'Kg')
             print('Preco Total:',total,'Mts')
             print('Tipo de pagamento: Cash Out')
             print('Valor do Desconto: 0 Mts')
             print('Valor a pagar:',total,'Mts')
    if quantidade > 5:
       cartao = input('Deseja usar o cartao ArrobaMZ[1-(SIM), 2-(NAO):')
       if cartao == "1":
         total = 7.80 * quantidade
         desconto = ((7.80 * quantidade) * 5 ) / 100
         novototal = total - desconto
         print()
         print('Tipo de Carne: File Duplo')
         print('Quantidade:',quantidade, 'Kg')
         print('Preco Total:',total,'Mts')
         print('Tipo de pagamento: Cartao ArrobaMZ')
         print('Valor do Desconto:',desconto)
         print('Valor a pagar:',novototal,'Mts')
       if cartao == "2":
          total = 7.80 * quantidade
          print()
          print('Tipo de Carne: File Duplo')
          print('Quantidade:',quantidade, 'Kg')
          print('Preco Total:',total,'Mts')
          print('Tipo de pagamento: Cash Out')
          print('Valor do Desconto: 0 Mts')
          print('Valor a pagar:',total,'Mts')
