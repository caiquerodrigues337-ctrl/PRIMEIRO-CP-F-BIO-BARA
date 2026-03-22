def validar_data():
    dia = int(input("Digite o dia: "))
    mes = int(input("Digite o mês: "))
    ano = int(input("Digite o ano: "))

    bissexto = (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)

    if mes < 1 or mes > 12:
        print(f"Erro: Mês {mes} é inválido (deve ser entre 1 e 12).")
        return

    if mes in [1, 3, 5, 7, 8, 10, 12]:
        dias_no_mes = 31
    elif mes in [4, 6, 9, 11]:
        dias_no_mes = 30
    elif mes == 2:
        dias_no_mes = 29 if bissexto else 28

    if dia < 1 or dia > dias_no_mes:
        if mes == 2 and dia == 29 and not bissexto:
            print(f"Erro: O dia 29 é inválido porque o ano {ano} não é bissexto.")
        else:
            print(f"Erro: O dia {dia} é inválido para o mês {mes}.")
        return

    print(f"Data válida: {dia:02d}/{mes:02d}/{ano}")
    if bissexto:
        print(f"Nota: O ano {ano} é bissexto.")