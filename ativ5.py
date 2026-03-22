 #Crie um programa para uma loja que aplica descontos baseados no valor da compra:
#até R$ 100 não tem desconto,
#  de R$ 100.01 a R$ 300 tem 10% de desconto,
#  de R$ 300.01 a R$ 500 tem 15%,
# acima de R$ 500 tem 20%.
#  Além disso, se o cliente for VIP (pergunte sim ou não),
#  ganha 5% extra em qualquer faixa.
#  Exiba o valor original,
# o desconto aplicado, 
# o desconto VIP (se houver)
#  e o valor final.


def calcular_venda():
    valor_original = float(input("Digite o valor da compra (R$): "))
    
    if valor_original < 0:
        print("Valor inválido.")
        return

    ser_vip = input("O cliente é VIP? (sim/não): ").strip().lower()

    if valor_original <= 100:
        percentual_base = 0.0
    elif valor_original <= 300:
        percentual_base = 0.10  
    elif valor_original <= 500:
        percentual_base = 0.15 
    else:
        percentual_base = 0.20 

    
    desconto_loja = valor_original * percentual_base
    
    
    desconto_vip = 0.0
    if ser_vip == "sim":
        desconto_vip = valor_original * 0.05

    valor_final = valor_original - desconto_loja - desconto_vip

    print("\n--- RESUMO DA COMPRA ---")
    print(f"Valor Original:    R$ {valor_original:>8.2f}")
    print(f"Desconto da Loja:  R$ {desconto_loja:>8.2f} ({percentual_base*100:.0f}%)")
    
    if desconto_vip > 0:
        print(f"Desconto VIP:      R$ {desconto_vip:>8.2f} (5%)")
    
    print("-" * 25)
    print(f"VALOR TOTAL:       R$ {valor_final:>8.2f}")

