menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == 'd':
        valor = float(input("Informe o valor de depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f'Depósito: R$ {valor:.2f}\n'

        else:
            print("Não foi possível realizar a transação. Tente novamente")

    elif opcao == 's':
        valor = float(input("Informe o valor de saque: "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saque = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print('Saldo insuficiente!')

        elif excedeu_limite:
            print('Limite permitido atingido!')

        elif excedeu_saque:
            print('Número máximo de saques atingido')

        elif valor > 0:
            saldo -= valor 
            extrato += f'Saque: R$ {valor:.2f}\n'
            numero_saques += 1

        else:
            print("Não foi possível completar a transação! O valor digitado é inválido")

    elif opcao == 'e':
        print(10 * '#' + 'EXTRATO' + '#' * 10)
        print("Não foram realizadas movimntações" if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print(27 * '#')

    elif opcao == 'q':
        break

    else:
        print("Operação inválida. Por favor, digite novamente uma das opções acima")