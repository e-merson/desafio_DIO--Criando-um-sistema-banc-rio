menu = """ 
[1] DEPOSITAR 
[2] SACAR
[3] EXTRATO
[4] ADICIONAR USUÁRIO
[5] ADICIONAR CONTA
[6] SAIR
=> """

saldo = 0
limite = 500
extrato = ''
numero_saque = 0
LIMITE_SAQUE = 3


usuarios = {}

def adicionar_usuario():
    nome = input("Informe o nome do usuário: ")
    data_nascimento = input("Informe a data de nascimento (formato dd/mm/aaaa): ")
    cpf = input("Informe o CPF do usuário (somente números): ")
    endereco = input("Informe o endereço completo do usuário (cidade, estado): ")

    if cpf in usuarios:
        print("CPF já cadastrado. Por favor, insira um CPF diferente.")
        return

    usuarios[cpf] = {
        "nome": nome,
        "data_nascimento": data_nascimento,
        "endereco": endereco,
        "saldo": 0  # Saldo inicial zerado
    }

    print("Usuário cadastrado com sucesso.")


def adicionar_conta(cpf):
    if cpf in usuarios:
        saldo_inicial = float(input("Informe o saldo inicial da conta: "))
        usuarios[cpf]["saldo"] += saldo_inicial  # Atualiza o saldo da conta ao adicionar o saldo inicial
    else:
        print("Usuário não encontrado.")

def depositar(valor):
    global saldo, extrato
    if valor > 0:
        saldo += valor
        extrato += f'Depósito de R$ {valor:.2f}\n'
    else:
        print("O valor informado não é válido")

def sacar(valor):
    global saldo, extrato, numero_saque
    saldo_excedido = valor > saldo
    limite_excedido = valor > limite
    saque_excedido = numero_saque >= LIMITE_SAQUE
    
    if saldo_excedido:
        print('Não há saldo suficiente para concluir a operação')
    elif limite_excedido:
        print(f'Você excedeu o limite de R$ {limite:.2f}')
    elif saque_excedido:
        print(f'Você já efetuou o limite de {LIMITE_SAQUE} saques')
    elif valor > 0:
        saldo -= valor
        extrato += f'Saque de R$ {valor:.2f}\n'
        numero_saque += 1

def mostrar_extrato():
    print("\n=================EXTRATO==================")
    print(" Não foram realizadas movimentações" if not extrato else extrato)
    print(f'\nSaldo R$ {saldo:.2f}')
    print('##############################################')

while True:
    opcao = input(menu).strip()
    
    if opcao == '1':
        valor = float(input("Informe o valor do depósito: "))
        depositar(valor)
            
    elif opcao == '2':
        valor = float(input("Informe o valor do saque: "))
        sacar(valor)
            
    elif opcao == '3':
        mostrar_extrato()
    
    elif opcao == '4':
        adicionar_usuario()
        
    elif opcao == '5':
        cpf = input("Informe o CPF do usuário para adicionar a conta: ")
        adicionar_conta(cpf)
        
    elif opcao == '6':
        print("Saindo...")
        break
        
    else:
        print('Operação inválida')
