import random

def jogar_big_bang():
    opcoes = {
        1: "Pedra",
        2: "Papel",
        3: "Tesoura",
        4: "Lagarto",
        5: "Spock"
    }

    regras = {
        "Tesoura": {"Papel": "corta", "Lagarto": "decapita"},
        "Papel": {"Pedra": "cobre", "Spock": "refuta"},
        "Pedra": {"Lagarto": "esmaga", "Tesoura": "quebra"},
        "Lagarto": {"Spock": "envenena", "Papel": "come"},
        "Spock": {"Tesoura": "derrete", "Pedra": "vaporiza"}
    }

    print("--- PEDRA, PAPEL, TESOURA, LAGARTO, SPOCK ---")
    print("1. Pedra\n2. Papel\n3. Tesoura\n4. Lagarto\n5. Spock")
    
    try:
        escolha_usuario = int(input("Escolha sua jogada (1-5): "))
        if escolha_usuario not in opcoes:
            print("Opção inválida! Escolha de 1 a 5.")
            return
    except ValueError:
        print("Entrada inválida! Digite apenas o número.")
        return

    escolha_comp = random.randint(1, 5)

    usuario = opcoes[escolha_usuario]
    computador = opcoes[escolha_comp]

    print(f"\nVocê escolheu: {usuario}")
    print(f"O computador escolheu: {computador}")
    print("-" * 30)

    if usuario == computador:
        print("Empate! Ambos escolheram o mesmo.")
    
    elif computador in regras[usuario]:
        motivo = regras[usuario][computador]
        print(f"VOCÊ GANHOU! {usuario} {motivo} {computador}.")
    
    else:
        motivo = regras[computador][usuario]
        print(f"VOCÊ PERDEU! {computador} {motivo} {usuario}.")