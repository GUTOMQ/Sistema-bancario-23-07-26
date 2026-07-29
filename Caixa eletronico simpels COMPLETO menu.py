import csv
import os
from datetime import datetime
import matplotlib.pyplot as plt

saldo = 100
extrato = []
ARQUIVO_CSV = "extrato.csv"

# Cria o arquivo CSV com cabeçalho, caso ele ainda não exista
if not os.path.exists(ARQUIVO_CSV):
    with open(ARQUIVO_CSV, mode="w", newline="", encoding="utf-8") as arquivo:
        escritor_csv = csv.writer(arquivo)
        escritor_csv.writerow(["Data/Hora", "Tipo", "Valor"])


def salvar_no_csv(tipo, valor):
    with open(ARQUIVO_CSV, mode="a", newline="", encoding="utf-8") as arquivo:
        escritor_csv = csv.writer(arquivo)
        escritor_csv.writerow([
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            tipo,
            f"{valor:.2f}"
        ])


def exibir_banco():
    print("\n===== CAIXA ELETRÔNICO =====")
    print("1 - Consultar Saldo")
    print("2 - Depositar Dinheiro")
    print("3 - Sacar Dinheiro")
    print("4 - Ver Extrato")
    print("5 - Ver movimentações")
    print("6 - Sair")

def consultar_saldo():
    print(f"\nSeu saldo atual é: R$ {saldo:.2f}")


def depositar_dinheiro():
    global saldo

    try:
        valor = float(input("\nDigite o valor a ser depositado: R$ "))

        if valor > 0:
            saldo += valor
            extrato.append(f"Depósito: R$ {valor:.2f}")
            salvar_no_csv("Depósito", valor)
            print(f"\nDepósito de R$ {valor:.2f} realizado com sucesso.")
        else:
            print("\nValor inválido.")

    except ValueError:
        print("\nDigite um valor numérico válido.")


def sacar_dinheiro():
    global saldo

    try:
        valor = float(input("\nDigite o valor a ser sacado: R$ "))

        if valor > 0 and valor <= saldo:
            saldo -= valor
            extrato.append(f"Saque: R$ {valor:.2f}")
            salvar_no_csv("Saque", valor)
            print(f"\nSaque de R$ {valor:.2f} realizado com sucesso.")
        elif valor > saldo:
            print("\nSaldo insuficiente.")
        else:
            print("\nValor inválido.")

    except ValueError:
        print("\nDigite um valor numérico válido.")


def ver_extrato():
    print("\n===== EXTRATO =====")

    if not extrato:
        print("Nenhuma movimentação realizada.")
    else:
        for movimentacao in extrato:
            print(movimentacao)

    print(f"\nSaldo atual: R$ {saldo:.2f}")

def ver_movimentacoes():
 # 1. Define your data
    x = [datetime.now().strftime("%d/%m/%Y")] #[1, 2, 3, 4, 5]
    y = [float(f"{saldo:.2f}")] #[2, 4, 6, 8, 10]

    # 2. Create the plot type
    plt.plot(x, y, color="red", linestyle="--", marker="o")

    # 3. Add titles and axis labels
    plt.title(f"HISTÓRICO DO SALDO ({datetime.now().strftime('%d/%m/%Y às %H:%M:%S')})")
    plt.xlabel("DATA")
    plt.ylabel("SALDO (R$)")

    # 4. Display the plot window
    plt.show()
    pass
                
def main():
    while True:
        exibir_banco()
        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            consultar_saldo()

        elif opcao == "2":
            depositar_dinheiro()

        elif opcao == "3":
            sacar_dinheiro()

        elif opcao == "4":
            ver_extrato()
            
        elif opcao == "5":
            ver_movimentacoes()
            
        elif opcao == "6":
            print("\nSaindo do sistema. Obrigado por utilizar o Caixa Eletrônico.")
            break

        else:
            print("\nOpção inválida. Tente novamente.")


if __name__ == "__main__":
    main()