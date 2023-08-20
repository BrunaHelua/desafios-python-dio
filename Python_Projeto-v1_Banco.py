menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0.0
limite = 500.0
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)
    
    if opcao.lower() == 'd':
        valor = float(input("Informe o valor do depósito: "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print(extrato)
        else:
            print("Valor de depósito inválido")
    
    elif opcao.lower() == 's':
        valor = float(input("Informe o valor do saque: "))
        
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_numero_saques = numero_saques >= LIMITE_SAQUES
        
        if excedeu_saldo:
            print("Saldo insuficiente")
        elif excedeu_limite:
            print("Valor do saque maior que o limite permitido")
        elif excedeu_numero_saques:
                print("Limite do número de saques atingido")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque no valor de R$: {valor:.2f}\n"
            numero_saques += 1
            print(extrato)
        else:
            print("Valor de saque inválido. Digite novamente.")
            
    elif opcao.lower() == 'e':
        print("\n====Extrato====")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo R$: {saldo:.2f}")
        print(f"Número de saques até o momento: {numero_saques}")
        
    elif opcao.lower() == 'q':
        break
    
    else:
        print("Opção inválida, por favor selecione novamente a operação desejada.")