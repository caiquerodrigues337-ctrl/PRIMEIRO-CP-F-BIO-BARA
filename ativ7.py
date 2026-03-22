def caixa_eletronico():
    print("--- SIMULADOR DE CAIXA ELETRÔNICO ---")
    
    try:
        saque = int(input("Digite o valor para saque (R$): "))
    except ValueError:
        print("Erro: Por favor, digite um número inteiro válido.")
        return

    if saque <= 0:
        print("Erro: O valor deve ser positivo.")
        return
    
    if saque % 10 != 0:
        print("Erro: Este caixa só possui cédulas de R$ 10, 20, 50, 100 e 200.")
        print("O valor deve ser múltiplo de 10.")
        return

    print(f"\nProcessando saque de R$ {saque}...")
    print("-" * 30)

    cedulas = [200, 100, 50, 20, 10]
    
    valor_restante = saque

    for nota in cedulas:
        quantidade_notas = valor_restante // nota
        
        if quantidade_notas > 0:
            print(f"Cédulas de R$ {nota:3}: {quantidade_notas}")
       
            valor_restante %= nota

    print("-" * 30)
    print("Saque realizado com sucesso!")
