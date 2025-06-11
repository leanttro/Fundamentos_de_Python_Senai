# Projeto de Exercícios Senai 
# Sem uso de parâmetros
# Sem correção de erros

def l():
  print("="*40)

def e():
  print("ERRO! DIGITE NOVAMENTE!")

while True:
  l()
  print('EXERCÍCIOS - FUNDAMENTOS DE PYHTON I ')
  l()

  print('[1] - LOOP WHILE')
  print('[2] - LISTAS')
  print('[3] - LOOP FOR')
  print('[4] - SAIR')
  menu1 = str(input('Digite a opção desejada: '))
  while True:
    if menu1 == '1':
                  l()
                  print('EXERCÍCIOS DE LOOP WHILE')
                  l()

                  print('[1] - EXERCÍCIO LOOP ERRO')
                  print('[2] - EXERCÍCIO MÉDIA ARITMÉTICA')
                  print('[3] - MÉDIA ALUNO POR TURMA')
                  print('[4] - CONTAGEM DE DÍGITOS')
                  print("[5] - CONFERÊNCIA DE SENHAS")
                  print("[6] - SOMA DE NÚMEROS ALEATÓRIOS")
                  print("[7] - VOLTAR AO MENU")
                  menu2 = str(input('Opção escolhida: '))

                  if menu2 == '1':
                      while True:
                          l()
                          nota1 = float(input('Digite uma nota entre 0 e 10:'))
                          if nota1 < 0 or nota1 > 10:
                            e()
                          else:
                            print(f'NOTA {nota1} REGISTRADO COM SUCESSO!')
                            menu3 = str(input('[1] REGISTRAR OUTRA NOTA [2] RETORNAR AO MENU'))
                            if menu3 == "1":
                              continue
                            elif menu3 == '2':
                              break
                            else:
                              e()
                  elif menu2 == "2":
                    while True:
                      l()
                      cont = 0
                      soma = 0
                      notas2 = int(input('QUANTIDADE DE NOTAS: '))
                      while cont < notas2:
                        nota = int(input(f'Digite a {cont+1} nota: '))
                        cont += 1
                        soma += nota
                      print(f'A quantidade de notas foi: {cont}')
                      print(f'A média das notas foi {soma/cont:.2f}')
                      menu4 = str(input('[1] VER OUTRA MÉDIA [2] RETORNAR AO MENU: '))
                      if menu4 == '1':
                        continue
                      elif menu4 =='2':
                        break
                      else:
                        e()

                  elif menu2 == '3':
                    while True:
                      cont= soma = 0
                      l()
                      quant = int(input('QUANTIDADE DE TURMAS: '))
                      while cont < quant:
                        turma = int(input(f'Quantidade de alunos da {cont+1} turma: '))
                        if turma > 40:
                          print("ERRO! Máximo 40 alunos por turma")
                        else:
                          cont = cont + 1
                          soma += turma
                      print(f"O total de turmas válidas foi: {cont}")
                      print(f'A média de alunos por turma válida foi {soma/cont:.2f}')
                      menu5 = str(input("[1] CALCULAR OUTRA MÉDIA [2] RETORNAR AO MENU PRINCIPAL: "))
                      if menu5 == "1":
                        continue
                      elif menu5 == '2':
                        break
                      else:
                        e()
                  elif menu2 == "4":
                    while True:
                        l()
                        num = int(input("Digite um número: "))
                        numm = str(num)
                        print(f"O número digitado tem {len(numm)} dígitos ")
                        menu15 = str(input("[1] VER OUTRA CONTAGEM [2] VOLTAR AO MENU: "))
                        if menu15 == "1":
                            continue
                        elif menu15 =="2":
                            break
                        else:
                            e()
                
                  elif menu2 == "5":
                    while True:
                        opc1 = str(input("DIGITE SUA SENHA: "))
                        opc2 = str(input("DIGITE SUA SENHA NOVAMENTE: "))
                        if opc1 != opc2:
                            print("ERRO! SENHAS NÃO CONFEREM")
                            continue
                        else:
                            print("Cadastro realizado com sucesso!")
                            menu6 = str(input("[1] CADASTRAR NOVA SENHA [2] VOLTAR AO MENU"))
                            if menu6 == "2":
                               break
                  elif menu2 == "6":
                    while True:
                        soma = 0
                        while True:
                            num1 = int(input("DIGITE UM NÚMERO ([00] PARA PARAR): "))
                            if num1 == 00:
                                break
                            else:
                                soma += num1
                        print(f"A soma dos números digitados é {soma} ")
                        menu18 = str(input("[1] SOMAR OUTROS NÚMEROS [2] VOLTAR AO MENU: "))
                        if menu18 == "1":
                            continue
                        elif menu18 == "2":
                            break
                        else:
                            e()
                  elif menu2 == "7":
                     break
                  else:
                     e()
                
    elif menu1 == "2":
        l()
        print('EXERCÍCIOS DE LISTA')

        print('[1] - 5 NÚMEROS VETORES')
        print('[2] - ORDEM REVERSA LISTA')
        print('[3] - LISTA DE NOTAS E MÉDIA')
        print('[4] - VOLTAR AO MENU')
        menu7 = str(input('Opção escolhida: '))

        if menu7 == '1':
           while True:
            l()
            lista = []
            num2 = cont = 0
            while cont < 5:
                cont += 1
                num2 = int(input(f"Digite o {cont}° número: "))
                lista.append(num2)
            print(f"Os números digitados foram {lista}")
            menu8 = str(input("[1] ADICIONAR MAIS PRODUTOS [2] VOLTAR AO MENU"))
            if menu8 == "1":
               continue
            elif menu8 == "2":
               break
            else:
               e()
        elif menu7 =="2":
           while True:
            l()
            cont = 0
            listanum = []
            while cont <10:
                cont += 1
                num3 = int(input(f"DIGITE O {cont}° NUMERO: "))
                listanum.append(num3)
            listanum.reverse() 
            print(f"A lista digitada ao contrário é {listanum}")
            menu9 = str(input("[1] CRIAR OUTRA LISTA [2] VOLTAR AO MENU: "))
            if menu9 == "1":
               break
            elif menu9 == "2":
               continue
            else:
               e()
        elif menu7 == "3":
           while True:
            l()
            cont = soma = 0
            listanota = []
            while cont < 4:
                nota3 = float(input(f"DIGITE A {cont+1}° NOTA: "))
                listanota.append(nota3)
                cont +=1
                soma += nota3
            print(f"As notas informadas foram {listanota} e a média delas é {soma/4}")
            menu10 = str(input("[1] ADICIONAR OUTRA MÉDIA [2] VOLTAR AO MENU: "))
            if menu10 == "1":
               continue
            elif menu10 == "2":
               break
            else:
               e()
        elif menu7 == "4":
           break

        else:
           e()
    elif menu1 == "3":
        l()
        print('EXERCÍCIOS DE LOOP FOR')
        l()

        print('[1] - CADASTRO DE HOMENS')
        print('[2] - ORDEM REVERSA LISTA')
        print('[3] - LISTA DE NOTAS E MÉDIA')
        print('[4] - VOLTAR AO MENU')
        menu11 = str(input('Opção escolhida: '))

        if menu11 == "1":
           while True:
            pessoas = 0
            masc = 0
            quant_pessoas = int(input("QUANTIDADE DE PESSOAS: "))
            for pessoas in range(quant_pessoas):
                sexo = str(input("SEXO DA PESSOA [M/F]: ")).upper().strip()
                if sexo == "M":
                    masc += 1
            print(f"A quantidade de pessoas do masculino é {masc}")
            menu12 = str(input("[1] REFAZER ANÁLISE [2] VOLTAR AO MENU: "))
            if menu12 == "1":
               continue
            elif menu12 == "2":
               break
            else:
               e()
        
        elif menu11 == "2":
            while True:
                for k in range(2,101,2):
                    print(k,end=" ")
                menu13 = str(input("[1] Rever Números Pares [2] Voltar ao Menu: "))
                if menu13 == "1":
                    break
                elif menu13 == "2":
                    continue
                else:
                    e()
        elif menu11 == "3":
            l()
            for k in range(100000):
                senha = str(input("Digite sua senha: "))
                senha1 = str(input("Digite sua senha novamente: "))
                if senha != senha1:
                   e()
                   continue
                else:
                   print("SENHAS CADASTRADAS COM SUCESSO!")
                   menu14 = str(input("[1] CADASTRAR NOVA SENHA [2] VOLTAR AO MENU"))
                   if menu14 == "1":
                      continue
                   elif menu14 =="2":
                      break
                   else:
                      e()
        else:
           e()
    elif menu1 == "4":
        exit()              
    else:
        e()
        break            

