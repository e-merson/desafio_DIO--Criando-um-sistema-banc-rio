menu = """ 
[1] DEPOSITAR 
[2] SACAR
[3] EXTRATO
[4] SAIR
=> """

saldo = 0
limite = 500
extrato = ''
numero_saque = 0
LIMITE_SAQUE = 3

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
        print("Saindo...")
        break
        
    else:
        print('Operação inválida')
