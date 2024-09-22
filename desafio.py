import locale
locale.setlocale(locale.LC_ALL,'pt_BR.UTF-8')
menu = '''
-----MENU-----
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
--------------

Selecione a opção:
'''

saldo = 0
limite = 500
extrato = ""
numero_saque = 0
opcoes = 'qQdDsSeE'
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if(opcao in opcoes):

        if(opcao == 'q' or opcao == 'Q'):
            break

        elif(opcao == 'd' or opcao == 'D'):
            valor = locale.atof(input('Digite o valor a depositar:'))
            if(valor > 0):
                saldo+=valor
                extrato += f"Deposito: R$ {valor:.2f}\n"
            else:
                print('Valor inválido.')
        
        elif(opcao == 's' or opcao == 'S'):
            if(numero_saque >= LIMITE_SAQUES):
                print('Limite de saque diário excedido.')
            else:
                valor = locale.atof(input('Digite o valor de saque:'))
                if(valor > limite):
                    print('Limite para saque é de R$ 500,00.')
                elif(valor > saldo):
                    print('Saldo insulficiente.')
                else:
                    saldo -= valor
                    numero_saque+=1
                    extrato += f"Saque: R$ {valor:.2f}\n"

        elif(opcao == 'e' or opcao == 'E'):
            print(extrato.replace(",",'').replace(".",","))
            print(f"Saldo R$ {saldo:.2f}".replace(",",'').replace(".",","))
    else:
        print("opção inválida.")
