

def entrada(mensagem):
    return input(mensagem)

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

    opcao = entrada(menu)

    if opcao == "d":
        valor_deposito = float(entrada("Digite o valor do seu depósito: "))

        if valor_deposito <0:
            print("Valor errado, por favor tente novamente")
        else:
            saldo += valor_deposito
            extrato += f"Depósito: R$ {valor_deposito: 0.2f} | Saldo final: R$ {saldo: 0.2f}\n"
            print("Valor depositado, Tenha um bom dia !!")
        
    elif opcao == "s":

        """Autorização de Saque """
        autorizacao_saque = numero_saques < LIMITE_SAQUES and saldo > 0

        if autorizacao_saque:
            valor_saque = float(entrada("""Saque autorizado !!! Coloque o valor a ser sacado: """))

            if valor_saque <= 500 and valor_saque <= saldo:
                saldo -= valor_saque
                numero_saques += 1
                extrato += f"Saque: {numero_saques} | Valor sacado : R$ {valor_saque:0.2f} | Saldo final: R$ {saldo:0.2f}\n"

                print("Operação bem-sucedida, Obrigado por ter escolhido nosso banco")


            else:

                print("Valor excedeu o valor máximo a sacar ou não possui saldo o suficiente")

        else:
            print('Saque não autorizado !! Número de saques já atingiu o limite ou não possui saldo')


    elif opcao == "e":
        print('Extrato'.center(30,'*'))
        if extrato:
            print(extrato)
        else:
            print("Sem movimentações a mostrar !\n")
        print(f"{'Saldo Atual'.center(30,'*')}\n R$ {saldo:0.2f}\n")
    
    elif opcao == "q":
        break
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")