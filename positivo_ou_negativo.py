from time import sleep
numerosposi = []
numerosnega = []
opc = 0
print("=*"*35)
print(" "*18,"POSITIVO, NEGATIVO OU NULO")
print("=*"*35)
sleep(0.5)
while True:
    numero = float(input("Digite um número: "))
    if opc == "N":
         break
    if numero > 0:
        print("Número Positivo! [Maior que 0]")
        numerosposi.append(numero)
    elif numero < 0:
        print("Número Negativo! [Menor que 0]")
        numerosnega.append(numero)
    else:
        print("Número Nulo! [Igual a 0]")
    opc = str(input("Deseja continuar [S/N]: ")).upper().strip()
    print()
    if opc not in "SsNn":
        print("Erro! Digite S ou N, por favor.")
    elif opc == "N":
        break
print("="*40)
print(" "*14,"RESULTADO")
print("="*40)
numerosnega.sort()
numerosposi.sort()
sleep(0.5)
print(f"Os números POSITIVOS foram: {numerosposi}")
print(f"Os números NEGATIVOS foram: {numerosnega}")   