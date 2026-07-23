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
    