#idade = input('qual a sua idade')
#    if idade <= 11:
#       print('você é crianca')
#    elif idade

# Crie um programa que peça peso (kg) e altura (m), 
# calcule o IMC (peso / altura²) e 
# exiba a classificação: abaixo do peso (< 18.5), peso normal (18.5 - 24.9), sobrepeso (25.0 - 29.9), obesidade (≥ 30.0). 


def calcule_imc(peso, altura):
    imc = peso / (altura*altura)
    return imc

def classificacao(imc):
    if imc < 18.5:
        return "abaixo do peso"
    elif imc > 18.5 and imc < 24.9:
        return "peso normal"
    elif imc > 25.0 and imc < 29.9:
        return "sobrepeso"
     
    return "obesidade"

peso = float(input("qual eh o seu peso? "))
altura = float(input("qual eh o seu altura? "))

imc = calcule_imc(peso, altura)
classificacao = classificacao(imc)

print(f'Seu IMC eh {imc}')
print(f'classificacao: {classificacao}')