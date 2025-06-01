print("="*55)
print(" "*13,"PAR, ÍMPAR E DIVISÍVEL POR 5")
print("="*55)
numeropar = []
numeroimpar = []
while True:
    numero = int(input("Digite um número: "))
    if numero % 2 == 0:
        print(f"O número {numero} é PAR!")
        numeropar.append(numero)
        if numero % 5 == 0:
            print(" - E também é divisível por 5!")
        else:
            print(" - Porém, não é divisível por 5!")
    else:
        print(f"O número {numero} é ímpar!")
        numeroimpar.append(numero)
        if numero % 5 == 0:
            print(" - E também é divisível por 5!")
        else:
            print(" - Porém, não é divisível por 5!")
    opc = str(input("Deseja continuar [S/N]: ")).upper().strip()
    print()
    if opc not in "NnSs":
        print("ERRO! Tente novamente")
    if opc == "N":
        print("Encerrando...")
        break
numeroimpar.sort()
numeropar.sort()
print("="*40)
print(f"Os números PARES foram: {numeropar}.")
print(f"Os números ÍMPARES foram: {numeroimpar}.")
