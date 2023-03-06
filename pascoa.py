tamanho = int(input("1-Pequeno - R$7.80\n2-Médio - R$12.90\n3-Grande - R$23.95\nEscolha o tamanho: "))
if tamanho == 1:
    valor = 7.80
elif tamanho == 2:
    valor = 12.90
else:
    valor = 23.95
sabor = int(input("1-Chocolate preto - R$9.67\n2-Chocolate branco - R$4.50\n3-Chocolate ao leite - R$9.32\nEscolha o recheio: "))
if sabor == 1:
    valor2 = 9.67
elif sabor == 2:
    valor2 = 4.50
else:
    valor2 = 9.32
outro = int(input("1-sim\n2-não\nQuer outro recheio: "))
if outro == 1:
    sabor2 = int(input("1-Chocolate preto - R$9.67\n2-Chocolate branco - R$4.50\n3-Chocolate ao leite - R$9.32\nEscolha o recheio: "))
    if sabor2 == 1:
        valor3 = 9.67
    elif sabor2 == 2:
        valor3 = 4.50
    else:
        valor3 = 9.32
    valor4 = (valor2 + valor3)/2
else:
    valor3 = 0
    valor4 = valor2
adicional = int(input("1-sim\n2-não\nQuer um adicional: "))
if adicional == 1:
    adicional2 = int(input("1-KitKat - R$4.67\n2-MM'S - R$5.43\nQual adicional: "))
    if adicional2 == 1:
        valor5 = 4.67
        valor7 = valor5
    else:
        valor5 = 5.43
        valor7 = valor5
    adicional3 = int(input("1-sim\n2-não\nQuer outro adicional: "))
    if adicional3 == 1:
        adicional4 = int(input("1-KitKat - R$4.67\n2-MM'S - R$5.43\nQual adicional: "))
        if adicional4 == 1:
            valor6 = 4.67
            valor7 = valor5 + valor6
        else:
            valor6 = 5.43
            valor7 = valor5 + valor6
else:
    valor7 = 0
presente = int(input("1-sim\n2-não\nÉ presente: "))
if presente == 1:
    valor8 = 2.50
else:
    valor8 = 0
entrega = int(input("1-sim\n2-não\nÉ para entregar: "))
if entrega == 1:
    valor9 = 5.00
else:
    valor9 = 0
valor10 = valor +valor4 + valor7 + valor8 + valor9
pagamento = int(input("1-cartão de crédito (+R$3.30 do valor)\n2-dinheiro ou PÍX (-10 porcento do valor)\nEscolha a forma de pagamento: "))
if pagamento == 1:
    valor11 = valor10 + 3.30
else:
    valor11 = valor10 * 0.10
quantidade = int(input("Quantos ovos: "))
valorfinal = valor11 * quantidade
print(f"R${valorfinal:.2f}")