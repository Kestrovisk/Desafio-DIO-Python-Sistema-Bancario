import textwrap


def menu():
    menu = """\n
    =============== MENU ==============
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo usuário
    [q]\tSair
    ==> """
    return input(textwrap.dedent(menu))


def depositar(saldo,valor,extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f'Deposito:\tR$ {valor:.2f}\n'
        print("\n=== Deposito realizado com sucesso! ===")
    else:
        print("\n@@@ Operação falhou! O valor informado é invalido. @@@")
 
    return saldo, extrato


def sacar(*, saldo, valor, extrato, limite, numero_saque, limite_saque):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numeoro_saque > limilites_saque

    if excedeu_saldo:
        print("\n@@@ Operação falhou! Você não tem saldo suficiente. @@@")
    
    elif excedeu_limite:
        print("\n@@@ Operação falhou! O valor do saque excede o limite. @@@")

    elif excedeu_saques:
        print("\n Operação falohu! Numero maximo de saques excedido. @@@")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque\t\tR$ {valor:.2f}\n"
        numero_saques += 1
        print("\n=== Saque realizado com sucesso! ===")

    else:
        print("\n@@@ Operação Falhou! O valor informado é invalido. @@@")

    return saldo, extrato


def exibir_extrato(saldo, / ,*, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")


def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n@@@ Já existe um usuario com esse CPF! @@@")

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereço = input("Informe o endereço(logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome,"data_nascimento": data_nascimento, "cpf": cpf, "endereço": endereço})

    print("=== Usuario criado com sucesso! ===")



def filtrar_usuarios(cpf, usuarios):
    usuarios_filtrados = [usuario for usuarios in usuarios if usuarios["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_contas(contas):
    cpf = input("Informe o CPF do usuario: ")
    usuario = filtrar_usuarios(cpf, usuarios)

    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta,"usuario": usuario}
                
    print("\n@@@ Usuario não encontrado, fluxo de criação de conta encerrada! @@@")
          

def listar_contas(contas):
    for contas in contas:
        linha = f"""\
            Agencia:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
    print("=" * 100)
    print(textwrap.dedent(linha))


def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opção = menu()

        if opção == "d":
            valor = float(input("informe o valor depoistado. "))

            saldo, extrato = depositar(saldo, valor, extrato)

        elif opção == "s":
            valor = float(input("Informe o valor do saque: "))

            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )

        elif opção == "e":
            exibir_extrato(saldo, extrato=extrato)

        elif opção == "nu":
            criar_usuario(usuarios)

        elif opção == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                conta.append(conta)

        elif opção == "lc":
            listar_contas(contas)
        
        elif opção == "q":
            break

        else:
            print("Operação invalida, por favor selecione a operação desejada. ")


main()
