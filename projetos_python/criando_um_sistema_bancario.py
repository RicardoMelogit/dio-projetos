def cabecalho(nome, simbolo):
    nome = nome.center(30, f"{simbolo}")
    return nome

menu_principal= f'''
{cabecalho(" MENU PRINCIPAL ", "=")}

(1) Depósito
(2) Saque
(3) Saldo
(4) Extrato

(0) Sair

Digite uma das opcoes=> '''

saldo = 0
extrato = ""
valor_limite = 500
numero_saques = 0
LIMITE_DE_SAQUES = 3
movimentacao = ""

while True:
    
    opcao = input(menu_principal)

    if opcao == "1":
        print(cabecalho(" DEPÓSITO ", "+"))
        print("")
        valor = float(input("Informe o valor do depósito R$ "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print("Depósito efetuado")
            input("Digite 1 para voltar ao Menu Principal: ")
            continue
        else:
            print("Operação falhou! O valor é invalido. ")
    
    elif opcao == "2":
        print(cabecalho(" SAQUE ", "-" ))
        print("")
        valor = float(input("Informe o valor do saque R$ "))
        
        excedeu_saldo = valor > saldo

        excedeu_saques = numero_saques >= LIMITE_DE_SAQUES

        excedeu_limite = valor > valor_limite

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
            print("")
            input("Digite 1 para voltar ao Menu Principal: ")
            continue
        
        elif excedeu_saques:
            print("Operação falhou! Limite de saques excedido.")
            print("")
            input("Digite 1 para voltar ao Menu Principal: ")
            continue

        elif excedeu_limite:
            print("Operação falhou! Valor excede o limite")
            print("")
            input("Digite 1 para voltar ao Menu Principal: ")
            continue

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print("Operação efetuada retire seu dinheiro.")
            print("")
            input("Digite 1 para voltar ao Menu Principal: ")
            continue

        else:
            print("Operação falhou! O valor informado é inválido")
            print("")
            input("Digite 1 para voltar ao Menu Principal: ")
            continue

    elif opcao == "3":
        print(cabecalho(" SALDO ", "_" ))
        print("")
        print(f"Seu saldo é de: R$ {saldo:.2f}\n")
        print("")
        input("Digite 1 para voltar ao Menu Principal: ")
        continue

    elif opcao == "4":
        print(cabecalho(" Extrato ", "#"))
        print("")
        print("Naõ foram reaizadas movimentações." if not extrato else extrato)
        for movimentacoes in extrato:
            movimentacoes = movimentacao
            print(movimentacao)
            print(f"Saldo atual: R$ {saldo:.2f}\n")
            print("")
            input("Digite 1 para voltar ao Menu Principal: ")
            break
           
    elif opcao == "0":
        break

    else:
        print("Opção invalida! Digite uma opção de válida.")
        continue
