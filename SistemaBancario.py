menu = '''

[1] Deposito
[2] Saque
[3] Extrato
[4] Sair

=> '''

saldo = 0 
limite = 500
extrato = ""
num_saque = 0
LIMITE_SAQUE = 3

while True:

    opcao = int(input(menu))

    if opcao == 1:
        valor = float(input("Digite o valor que será depositado: "))

        if valor > 0:
            saldo += valor
            extrato += f'Deposito no valor de: R$ {valor:.2f}\n'

        else:
            print("Falha na opração! O valor Informado é invalido.")
    
    elif opcao == 2:
        valor = float(input("Quanto deseja sacar? "))

        ex_saldo = valor > saldo

        ex_limite = valor > limite

        ex_saque = num_saque >= LIMITE_SAQUE

        if ex_saldo:
            print ("Não foi possivel finalizar a operação! Saldo insuficiente")

        elif ex_limite:
            print ("Não foi possivel finalizar a operação! valor do saque excede o limite")

        elif ex_saque:
            print ("Não foi possivel finalizar a operação! você já realizzou todos os saques permitidos")

        elif valor > 0:
            saldo -= valor
            extrato += f'Saque no valor de: R$ {valor:.2f}\n'
            num_saque +=1

        else:
            print("Falha na opração! O valor Informado é invalido.")

    elif opcao == 3:
        print ("\n","="*15,"EXTRATO","="*15)
        print ("não foram realizadas movimentações." if not extrato else extrato)
        print (f"\n saldo: R$ {saldo:.2f}")
        print ("="*37)

    elif opcao == 4:
        break

    else: 
        print("opção invalida, por favor selecione novamente a opção desejada")



    


