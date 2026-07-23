#Sistema de caixa eletronico simples em Python
saldo = 1000.00
extrato = ""

def menu():
    while True:
        print("\n========== CAIXA ELETRÔNICO ==========")
        print("1 - Ver saldo")
        print("2 - Depositar")
        print("3 - Sacar")
        print("4 - Ver extrato")
        print("5 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            ver_saldo()

        elif opcao == "2":
            depositar()

        elif opcao == "3":
            sacar()

        elif opcao == "4":
            ver_extrato()

        elif opcao == "5":
            print("Obrigado por utilizar nosso caixa eletrônico!")
            break

        else:
            print("Opção inválida!")
    
    def ver_saldo():
        print(f"\nSeu saldo é R$ {saldo:.2f}")
    
    def depositar():
        global saldo
        global extrato

    valor = float(input("Valor do depósito: R$ "))

    if valor > 0:
        saldo += valor
        extrato += f"Depósito: +R$ {valor:.2f}\n"
        print("Depósito realizado com sucesso!")
    else:
        print("Valor inválido.")
        
    def sacar():
        global saldo
        global extrato

    valor = float(input("Valor do saque: R$ "))

    if valor <= 0:
        print("Valor inválido.")

    elif valor > saldo:
        print("Saldo insuficiente.")

    else:
        saldo -= valor
        extrato += f"Saque: -R$ {valor:.2f}\n"
        print("Saque realizado com sucesso!")
    
    def ver_extrato():
            print("\n========== EXTRATO ==========")

    if extrato == "":
        print("Nenhuma movimentação.")

    else:
        print(extrato)

        print(f"Saldo atual: R$ {saldo:.2f}")
        