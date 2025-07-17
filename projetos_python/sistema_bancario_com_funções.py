from datetime import datetime, date

contas = {}

def cabecalho(nome, simbolo="="):
    print(simbolo * 50)
    print(nome.center(50, simbolo))
    print(simbolo * 50)

def gerar_numero_conta():
    numero = len(contas) + 1
    return f"{numero:04d}-0"

def verificar_cpf_existente(cpf):
    for conta in contas.values():
        if conta["dados"]["CPF"] == cpf:
            return True
    return False

def calcular_idade(data_nasc):
    hoje = date.today()
    return hoje.year - data_nasc.year - ((hoje.month, hoje.day) < (data_nasc.month, data_nasc.day))

def cadastrar_cliente():
    cabecalho("CADASTRO DE NOVA CONTA", "-")
    cpf = input("Digite o CPF (somente números): ").strip()
    if verificar_cpf_existente(cpf):
        print("Erro: CPF já cadastrado.")
        return

    try:
        data_nasc_str = input("Digite a data de nascimento (dd/mm/aaaa): ")
        data_nasc = datetime.strptime(data_nasc_str, "%d/%m/%Y").date()
    except ValueError:
        print("Data inválida.")
        return

    idade = calcular_idade(data_nasc)
    if idade < 18:
        print("Não é possível abrir a conta. O cliente deve ser maior de 18 anos.")
        return

    nome = input("Digite o nome completo: ")
    logradouro = input("Logradouro: ")
    bairro = input("Bairro: ")
    cidade = input("Cidade: ")
    estado = input("Estado (sigla): ")
    telefone = input("Telefone: ")

    while True:
        senha = input("Defina uma senha para a conta: ").strip()
        confirmacao = input("Confirme a senha: ").strip()
        if senha == confirmacao:
            break
        else:
            print("As senhas não coincidem. Tente novamente.")

    endereco = [logradouro, bairro, cidade, estado]
    numero_conta = gerar_numero_conta()

    contas[numero_conta] = {
        "dados": {
            "nome": nome,
            "CPF": cpf,
            "data_nascimento": data_nasc.strftime("%d/%m/%Y"),
            "endereco": endereco,
            "telefone": telefone,
            "senha": senha
        },
        "saldo": 0.0,
        "extrato": [],
        "movimentacoes": 0
    }

    print(f"\nConta criada com sucesso! Número da conta: {numero_conta}")

def depositar(conta, valor, /):
    cabecalho("DEPÓSITO")
    if valor <= 0:
        print("Valor deve ser positivo.")
        return
    contas[conta]["saldo"] += valor
    contas[conta]["extrato"].append(f"Depósito: +R$ {valor:.2f}")
    contas[conta]["movimentacoes"] += 1
    print("Depósito realizado com sucesso!")

def sacar(*, conta, valor):
    cabecalho("SAQUE")
    if valor <= 0:
        print("Valor deve ser positivo.")
        return
    if valor > contas[conta]["saldo"]:
        print("Saldo insuficiente.")
        return
    contas[conta]["saldo"] -= valor
    contas[conta]["extrato"].append(f"Saque: -R$ {valor:.2f}")
    contas[conta]["movimentacoes"] += 1
    print("Saque realizado com sucesso!")

def ver_extrato(conta, *, mostrar_saldo=True):
    cabecalho("EXTRATO")
    if contas[conta]["extrato"]:
        for movimento in contas[conta]["extrato"]:
            print(movimento)
    else:
        print("Nenhuma movimentação.")
    if mostrar_saldo:
        print(f"\nSaldo atual: R$ {contas[conta]['saldo']:.2f}")

def menu_conta(conta):
    while True:
        cabecalho(f"MENU CONTA {conta}", "=")
        print("1. Depositar")
        print("2. Sacar")
        print("3. Ver Extrato")
        print("4. Sair da Conta")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            try:
                valor = float(input("Digite o valor para depósito: R$ "))
                depositar(conta, valor)
            except ValueError:
                print("Valor inválido.")
        elif opcao == "2":
            try:
                valor = float(input("Digite o valor para saque: R$ "))
                sacar(conta=conta, valor=valor)
            except ValueError:
                print("Valor inválido.")
        elif opcao == "3":
            ver_extrato(conta, mostrar_saldo=True)
        elif opcao == "4":
            print("Saindo da conta...")
            break
        else:
            print("Opção inválida.")

def acessar_conta():
    cabecalho("ACESSAR CONTA", "-")
    conta = input("Digite o número da conta: ").strip()
    senha = input("Digite a senha: ").strip()

    if conta in contas:
        if contas[conta]["dados"]["senha"] == senha:
            print(f"Acesso autorizado. Bem-vindo(a), {contas[conta]['dados']['nome']}!")
            menu_conta(conta)
        else:
            print("Senha incorreta.")
    else:
        print("Conta não encontrada.")

def menu():
    while True:
        cabecalho("BANCO DIGITAL PYTHON", "*")
        print("1. Acessar conta existente")
        print("2. Criar nova conta")
        print("3. Sair")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            acessar_conta()
        elif opcao == "2":
            cadastrar_cliente()
        elif opcao == "3":
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")

def main():
    menu()

if __name__ == "__main__":
    main()
