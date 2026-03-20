#Crie um programa que peça a idade do usuário
# e exiba se ele é criança (0-11),
# adolescente (12-17), 
#adulto (18-59) ou 
#idoso (60+). 
#Se a idade for negativa ou maior que 120, exiba "Idade inválida".



def resultado(idade):
    if idade > 0 and idade < 11:
        return "criança"
    elif idade > 12 and idade < 17:
        return "adolescente"
    elif idade > 18 and idade < 59:
        return "adulto"
    elif idade > 60 and idade < 120:
        return "idoso"
    return "idade invalida"

idade = int(input("qual a sua idade? "))

idade_em_anos = resultado(idade)

print(f'{idade_em_anos}')
