import textwrap

def menu():
    menu = """\n
    *****************  MENU  *****************
    (1)\t DEPOSITAR
    (2)\t SACAR
    (3)\t EXTRATO
    (4)\t NOVA CONTA
    (5)\t LISTAR CONTAS
    (6)\t NOVO USUÁRIO
    (0)\t SAIR
    """
    return input(textwrap.dedent(menu))

def depositar(saldo,valor,extrato,/):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito:\tR$ {valor:.2f}\n"
        print("\nDepósito realizado com sucesso!")
    else:
        print("\nO valor informado é inválido")
    return saldo,extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    if valor > saldo:
        print("\nVocê não tem saldo suficiente.")

    elif valor > limite:
        print("\nO valor do saque passou o limite.")

    elif numero_saques >= limite_saques:
        print("\nNúmero máximo de saques excedido.")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\t\tR$ {valor:.2f}\n"
        numero_saques += 1
        print("\n=== Saque realizado com sucesso! ===")

    else:
        print("\nO valor informado é inválido.")

    return saldo, extrato

def extrato_conta(saldo,/,*,extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("==========================================")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)
    if usuario:
        print("\nJá existe usuário com esse CPF!")
        return
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")
    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    print("=== Usuário criado com sucesso! ===")

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)
    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    print("\nUsuário não encontrado.")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))

def main():
    LIMITE_SAQUE =3
    AGENCIA = "001"
    saldo = 0
    limite = 500
    extrato = ""
    saque = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()
        if opcao == "1":
            valor  = float(input("Digite o valor para o depósito: "))
            saldo, extrato = depositar(saldo,valor,extrato)
        elif opcao == "2":  
            valor = float(input("Informe o valor do saque: "))
            saldo, extrato = sacar(saldo=saldo,valor=valor,extrato=extrato,limite=limite,numero_saques=saque,limite_saques=LIMITE_SAQUE)
        elif opcao == "3":  
            extrato_conta(saldo, extrato=extrato)
        elif opcao == "4":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            if conta:
                contas.append(conta)
        elif opcao == "5":
            listar_contas(contas)
        elif opcao == "6": 
            criar_usuario(usuarios)
        elif opcao == "0":
            break 
        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")   
main()