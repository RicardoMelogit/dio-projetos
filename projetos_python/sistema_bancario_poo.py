# Sistema bancário orientado a objetos simples somente com funções essenciais.

from typing import List, Optional


class Cliente:
    def __init__(self, nome: str, cpf: str):
        self.nome = nome
        self.cpf = cpf

    def __str__(self):
        return f"{self.nome} (CPF: {self.cpf})"


class ContaBancaria:
    proximo_numero = 1

    def __init__(self, cliente: Cliente):
        self.cliente = cliente
        self.numero = ContaBancaria.proximo_numero
        self.saldo = 0.0
        self.historico: List[str] = []
        ContaBancaria.proximo_numero += 1

        self.registrar_movimentacao("Conta criada")

    def registrar_movimentacao(self, descricao: str):
        self.historico.append(descricao)

    def depositar(self, valor: float) -> bool:
        # Deposita um valor se ele for válido
        if valor <= 0:
            return False

        self.saldo += valor
        self.registrar_movimentacao(f"Depósito de R$ {valor:.2f}")
        return True

    def sacar(self, valor: float) -> bool:
        # Realiza saque apenas se houver saldo suficiente
        if valor <= 0 or valor > self.saldo:
            return False

        self.saldo -= valor
        self.registrar_movimentacao(f"Saque de R$ {valor:.2f}")
        return True

    def transferir(self, valor: float, destino: "ContaBancaria") -> bool:
        # Tenta sacar e depois envia para outra conta
        if self.sacar(valor):
            destino.depositar(valor)
            self.registrar_movimentacao(
                f"Transferência de R$ {valor:.2f} para conta {destino.numero}"
            )
            destino.registrar_movimentacao(
                f"Transferência recebida de R$ {valor:.2f} da conta {self.numero}"
            )
            return True
        return False

    def extrato(self):
        # Exibe histórico e saldo
        print(f"\n=== Extrato da conta {self.numero} ===")
        print(f"Titular: {self.cliente.nome}")
        for mov in self.historico:
            print(f"- {mov}")
        print(f"Saldo atual: R$ {self.saldo:.2f}")
        print("=====================================\n")


class Banco:
    def __init__(self, nome: str):
        self.nome = nome
        self.contas: List[ContaBancaria] = []

    def criar_conta(self, nome_cliente: str, cpf_cliente: str) -> ContaBancaria:
        # Cria cliente e conta
        cliente = Cliente(nome_cliente, cpf_cliente)
        conta = ContaBancaria(cliente)
        self.contas.append(conta)
        return conta

    def buscar_conta(self, numero: int) -> Optional[ContaBancaria]:
        # Procura conta pelo número
        for conta in self.contas:
            if conta.numero == numero:
                return conta
        return None

    def listar_contas(self):
        # Exibe todas as contas cadastradas
        if not self.contas:
            print("Nenhuma conta cadastrada.\n")
            return

        print(f"\n=== Contas cadastradas no {self.nome} ===")
        for conta in self.contas:
            print(
                f"Conta {conta.numero} | Titular: {conta.cliente.nome} | "
                f"Saldo: R$ {conta.saldo:.2f}"
            )
        print("========================================\n")


def menu():
    print("===== SISTEMA BANCÁRIO =====")
    print("1 - Criar conta")
    print("2 - Listar contas")
    print("3 - Depositar")
    print("4 - Sacar")
    print("5 - Transferir")
    print("6 - Extrato")
    print("0 - Sair")
    print("============================")


def main():
    banco = Banco("Banco Python")

    while True:
        menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Nome do cliente: ")
            cpf = input("CPF do cliente: ")
            conta = banco.criar_conta(nome, cpf)
            print(f"Conta criada! Número: {conta.numero}\n")

        elif opcao == "2":
            banco.listar_contas()

        elif opcao == "3":
            try:
                numero = int(input("Número da conta: "))
                valor = float(input("Valor do depósito: R$ "))
            except ValueError:
                print("Dados inválidos.\n")
                continue

            conta = banco.buscar_conta(numero)
            if conta and conta.depositar(valor):
                print("Depósito realizado.\n")
            else:
                print("Erro ao depositar.\n")

        elif opcao == "4":
            try:
                numero = int(input("Número da conta: "))
                valor = float(input("Valor do saque: R$ "))
            except ValueError:
                print("Dados inválidos.\n")
                continue

            conta = banco.buscar_conta(numero)
            if conta and conta.sacar(valor):
                print("Saque realizado.\n")
            else:
                print("Erro ao sacar.\n")

        elif opcao == "5":
            try:
                origem = int(input("Conta de origem: "))
                destino = int(input("Conta de destino: "))
                valor = float(input("Valor da transferência: R$ "))
            except ValueError:
                print("Dados inválidos.\n")
                continue

            c_origem = banco.buscar_conta(origem)
            c_destino = banco.buscar_conta(destino)

            if c_origem and c_destino and c_origem.transferir(valor, c_destino):
                print("Transferência realizada.\n")
            else:
                print("Erro na transferência.\n")

        elif opcao == "6":
            try:
                numero = int(input("Número da conta: "))
            except ValueError:
                print("Número inválido.\n")
                continue

            conta = banco.buscar_conta(numero)
            if conta:
                conta.extrato()
            else:
                print("Conta não encontrada.\n")

        elif opcao == "0":
            print("Encerrando o sistema...")
            break

        else:
            print("Opção inválida.\n")


if __name__ == "__main__":
    main()
