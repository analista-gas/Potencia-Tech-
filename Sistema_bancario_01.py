
volta = 1
opcao = 0
valor = 0.0
saldo = 0.0
extrato = ""
numero_saques = 0

while volta == 1:
    print("Qual operação?\n1 - DEPOSITAR\n2 - SACAR\n3 - EXTRATO")
    opcao = int(input("Digite aqui: "))
    if opcao == 1:
        valor = float(input("Informe o valor do depósito: "))
        if valor > 0:
            saldo = saldo + valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        else:
            print("Operação falhou! Valor digitado é inválido.")    
    elif opcao == 2:
        valor = float(input("Informe o valor do saque: "))
        #excedeu saldo
        if valor > saldo:
            print("Operação falhou! Você não tem saldo suficiente. ")
        #excedeu limite
        elif valor > 500:
            print("Operação falhou! O valor do saque excede o limite.")
        #excedeu saque
        elif numero_saques >= 3:
            print("Operação falhou! Número máximo de saques excedidas.")
        elif valor > 0:
            saldo = saldo - valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
        else:
            print("Operação falhou! O valor informado é inválido.")
    elif opcao == 3:
        print("\n=======================================================\n")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("\n=======================================================\n")
    else:
        print("Essa operação não existe.")    

    print("Deseja fazer novamente?\n1 - SIM\n2 - NÃO")
    volta = int(input("Digite aqui: "))
