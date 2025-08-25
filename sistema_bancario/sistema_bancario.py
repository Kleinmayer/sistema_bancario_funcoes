from datetime import datetime

def deposito(valor, saldo, extrato_text, /):
    if valor > 0:
        saldo += valor
        extrato_text += f"[{datetime.now():%d/%m/%Y %H:%M}] Depósito: R$ {valor:.2f}\n"
    else:
        print("Operação falhou. O valor informado é inválido.")
    return saldo, extrato_text

def saque(*, saldo, valor, extrato_text, numero_saques, LIMITE_SAQUES):
    limite = 500

    excedeu_saque = valor > saldo

    excedeu_limite = valor > limite

    excedeu_saques =  numero_saques >= LIMITE_SAQUES

    if excedeu_saque:
            print("Falha na operação. \nVocê não tem saldo suficiente.")

    elif excedeu_limite:
            print("Falha na operação. \nO valor informado excede seu limite de saque.\nConsulte seu gerente para realizar atualização.")

    elif excedeu_saques:
            print("Falha na operação. \nVocê excedeu o limite de saque diário.\nConsulte seu gerente para realizar atualização.")

    elif valor > 0:
        saldo -= valor
        extrato_text += f"[{datetime.now():%d/%m/%Y %H:%M}] Saque: R$ {valor:.2f}\n"
        numero_saques += 1

    else:
        print("Operação falhou. O valor informado é inválido")

    return saldo, valor, extrato_text, numero_saques

def extrato(saldo, *, extrato):
        print("\n============== EXTRATO ==============")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("=====================================")

def criar_usuario():
     while True:
        nome = input("Informe o nome: ").strip()
        cpf = input("Informe o CPF (somente números): ").strip()
        cpf = "".join(c for c in cpf if c.isdigit())
        nascimento = input("Informe a data de nascimento: ").strip()
        endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/UF): ").strip()

        for u in usuarios:
                if u["cpf"] == cpf:
                    print("CPF já cadastrado!")
                    return 
     
        novo_usuario = {
            "nome": nome,
            "cpf": cpf,
            "nascimento": nascimento,
            "endereco": endereco,
         }
        usuarios.append(novo_usuario)
        print("Usuário criado com sucesso!")
        return

def criar_conta():
    cpf = input("Informe o CPF do usuário para vincular a conta: ")
    cpf = "".join(c for c in cpf if c.isdigit())

    usuario_encontrado = None
    for usuario in usuarios:
          if usuario["cpf"] == cpf:
               usuario_encontrado = usuario
               break
    
    if not usuario_encontrado:
        print("Usuário não encontrado. Crie o usuário primeiro.")
        return
          
    numero_conta = len(contas) + 1
    agencia = "0001"
          
    nova_conta = {
        "agencia": agencia,
        "numero_conta": numero_conta,
        "usuario": usuario_encontrado
    }

    contas.append(nova_conta)
    print(f"Conta criada com sucesso! Número da conta: {numero_conta}")

# programa principal

from datetime import datetime

contas = []
usuarios = []

menu = """
BEM VINDO AO BANCO PYTHON
                                                        
SELECIONE A OPÇÃO DESEJADA

    [1] Depósito
    [2] Saque
    [3] Extrato
    [4] Criar Usuário
    [5] Criar Conta
    [6] Sair
                                                        
  >> """
saldo = 0
extrato_text = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Informe o valor do depósito: "))
        saldo, extrato_text = deposito(valor, saldo, extrato_text)

    elif opcao == "2":
        valor = float(input("Informe o valor do saque: "))
        saldo, valor, extrato_text, numero_saques = saque(
             saldo=saldo,
             valor=valor,
             extrato=extrato_text,
             numero_saques=numero_saques,
             LIMITE_SAQUES=LIMITE_SAQUES

        )

    elif opcao == "3":
        extrato(saldo, extrato=extrato_text)
    
    elif opcao == "4":
        criar_usuario()
    
    elif opcao == "5":
        criar_conta()

    elif opcao == "6":
        print("Saindo do sistema...")
        break

    else:
        print("Opção inválida! Tente novamente.")