passos = []
def l():
    print("="*50)
"""def l():
    print("="*50)

def eh_primo(n):
    if n == 2 or n == 3:
        passos.append(n)
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    else:
        passos.append(n)
        return True

def somaa(n):
    if len(n) == 1:
        cm = int(n)
        if cm % 2 ==0:
            passos.append(cm)
            return True
        else:
            return False
    elif len(n) == 2:
        d = int((n[0]))
        e = int((n[1]))
        soma1 = d + e
        if soma1 % 2 == 0:
            passos.append(n)
            return True
        else:
            return False
    
    elif len(n) == 3:
        f = int((n[0]))
        g = int((n[1]))
        h = int((n[2]))
        soma2 = f + g + h 
        if soma2 % 2 == 0:
            passos.append(n)
            return True
        else:
            return False

a = int(input("DIGITE UM NÚMERO: "))
print(eh_primo(a))
a2 = (input("DIGITE UM NÚMERO:"))
print(passos)
print(somaa(a2))
"""

passos = []
def l():
    print("="*50)
#MENU PRINCIPAL
l()
print(" "*5,"JOGO DE PRIMOS E SOMAS DE DÍGITOS PARES")
l()
print()
print("REGRAS: O jogador deverá andar somente nos números que forem PRIMOS ou que soma de seus dígitos seja ÍMPAR!")

n = (input("DIGITE ATÉ QUAL NÚMERO, DE 1 ATÉ 1000, O JOGADOR DEVERÁ ANDAR: "))
for k in range(1,int(n),1):
    if n == 2 or n == 3:
        passos.append(n)

    if int(n) > 3:
        if int(n) % 2 == 0 or int(n) % 3 == 0:
            print()
        else:
            passos.append(n)
    if len(n) == 1:
        cm = int(n)
        if cm % 2 ==0:
            passos.append(cm)
    if len(n) == 2:
        d = int((n[0]))
        e = int((n[1]))
        soma1 = d + e
        if soma1 % 2 == 0:
            passos.append(n)
    
    if len(n) == 3:
        f = int((n[0]))
        g = int((n[1]))
        h = int((n[2]))
        soma2 = f + g + h 
        if soma2 % 2 == 0:
            passos.append(n)
print(passos)
