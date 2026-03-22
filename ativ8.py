def calcular_estacionamento():
    print("--- SISTEMA DE TARIFAÇÃO DE ESTACIONAMENTO ---")
    
    h_entrada = int(input("Hora de entrada (0-23): "))
    h_saida = int(input("Hora de saída (0-23): "))
    ultimo_digito = int(input("Último dígito da placa: "))
    dia_semana = input("Dia da semana (ex: segunda, terca...): ").strip().lower()

    if h_saida > h_entrada:
        total_horas = h_saida - h_entrada
    elif h_saida < h_entrada:
        total_horas = (24 - h_entrada) + h_saida
    else:
        total_horas = 1 

    valor_base = 10.00
    if total_horas > 1:
        valor_base += (total_horas - 1) * 5.00

    adicional_noturno = 0.0
    periodo_noturno = False
    
    h_atual = h_entrada
    for _ in range(total_horas + 1):
        if h_atual >= 22 or h_atual < 6:
            periodo_noturno = True
            break
        h_atual = (h_atual + 1) % 24

    if periodo_noturno:
        adicional_noturno = valor_base * 0.50

    subtotal = valor_base + adicional_noturno

    desconto_segunda = 0.0
    if dia_semana == "segunda" and ultimo_digito % 2 == 0:
        desconto_segunda = subtotal * 0.10

    valor_final = subtotal - desconto_segunda

    print("\n" + "="*30)
    print(f"Tempo de permanência: {total_horas}h")
    print(f"Tarifa Base:        R$ {valor_base:>7.2f}")
    
    if adicional_noturno > 0:
        print(f"Adicional Noturno:  R$ {adicional_noturno:>7.2f} (50%)")
    
    if desconto_segunda > 0:
        print(f"Desconto (Placa Par):-R$ {desconto_segunda:>7.2f} (10%)")
        
    print("-" * 30)
    print(f"VALOR TOTAL:        R$ {valor_final:>7.2f}")
    print("="*30)
