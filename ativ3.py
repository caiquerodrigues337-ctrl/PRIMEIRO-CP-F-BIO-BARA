#Crie um programa que exiba um menu com 3 opções de conversão:
#Real → Dólar,
#Real → Euro,
#Real → Libra.
#O usuário escolhe a opção, 
#digita o valor em reais e o programa exibe o valor convertido com 2 casas decimais
#Se o usuário escolher uma opção inválida, exiba "Opção inválida". 
#Se digitar um valor negativo, exiba "Valor inválido".

def conversor_moedas():
    TAXA_DOLAR = 5.15
    TAXA_EURO = 5.55
    TAXA_LIBRA = 6.45

    print("MENU DE CONVERSÃO")
    print("1. Real → Dólar")
    print("2. Real → Euro")
    print("3. Real → Libra")
    
    opcao = input("Escolha uma opção: ")


    if opcao not in ['1', '2', '3']:
        print("Opção inválida.")
        return 

    valor_real = float(input("Digite o valor em Reais (R$): "))

   
    if valor_real < 0:
        print("Valor inválido.")
        return

   
    if opcao == '1':
        resultado = valor_real / TAXA_DOLAR
        moeda = "Dólares"
    elif opcao == '2':
        resultado = valor_real / TAXA_EURO
        moeda = "Euros"
    elif opcao == '3':
        resultado = valor_real / TAXA_LIBRA
        moeda = "Libras"

    print(f"O valor convertido é: {resultado:.2f} {moeda}")
