menu = """

[d] - Depositar
[s] - Sacar
[e] - Extrato
[q] - Sair

"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while(True):

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R${ valor:.2f}\n "
        else:
            print("Operação falhou.")

    elif opcao == "s":
        valor = float(input("Informe o valor para saque: "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > saldo
        excedeu_saques = numero_saques > LIMITE_SAQUES

        if excedeu_saldo:
            print("error")

        elif excedeu_limite:
            print("error 2")

        elif excedeu_saques:
            print("error 3")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R${ valor:.2f}\n "
            numero_saques += 1

    elif opcao == "e":
        print(extrato)

    elif opcao == "q":
        break

    else:
        print("Opção inválida, por favor selecione novamente a operação desejada.")