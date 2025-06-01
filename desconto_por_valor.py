valortotal = []
descontototal = []
print("*"*23,"SALDÃO DE DESCONTO","*"*22)
print("*"*65)

while True:
    valor = float(input("Digite o valor do produto(R$): "))
    if valor < 100:
        valortotal.append(valor)
        desconto = valor*5/100
        descontototal.append(desconto)
        print()
        print("VOCÊ ACABA DE GANHAR 5% DE DESCONTO NESSE PRODUTO -> ")
        print(f"- O valor original é R$ {valor:.2F} \n- O valor do desconto é de R$ {desconto:.2f} \n- O valor COM DESCONTO APLICADO é de R$ {valor-desconto:.2f} ")
    elif valor >= 100 and valor <500:
        valortotal.append(valor)
        desconto = valor*10/100
        descontototal.append(desconto)
        print()
        print("VOCÊ ACABA DE GANHAR 10% DE DESCONTO NESSE PRODUTO -> ")
        print(f"- O valor original é de R$ {valor:.2f} \n- O valor do desconto é de R$ {desconto:.2f} \n- O valor COM DESCONTO APLICADO é de R$ {valor-desconto:.2f}")
    else:
        valortotal.append(valor)
        desconto = valor*15/100
        descontototal.append(desconto)
        print()
        print("VOCÊ ACABA DE GANHAR 15% DE DESCONTO NESSE PRODUTO -> ")
        print(f"- O valor original é de R$ {valor:.2f} \n- O valor do desconto é de R$ {desconto:.2f} \n- O valor COM DESCONTO APLICADO é de R$ {valor-desconto:.2f} ")
    print()   
    opc = str(input("Deseja calcular outro produto [S/N]: ")).strip().upper()
    print("="*40)
    if opc not in "SsNn":
        print("ERRO! Digite uma opção válida")
    elif opc == "N":
        break
print()
total = sum(valortotal)
totdesconto = sum(descontototal)
print(f"O valor total da compra foi R$ {total:.2f}")
print(f"O valor total do desconto foi R$ {totdesconto:.2f}")
print(f"O valor TOTAL COM DESCONTO foi de R$ {total - totdesconto:.2f}")