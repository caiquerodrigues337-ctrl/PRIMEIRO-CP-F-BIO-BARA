#Crie um programa que peça 3 valores representando os lados de um triângulo
#Primeiro, verifique se os valores formam um triângulo válido
#(a soma de dois lados deve ser maior que o terceiro —
#teste as 3 combinações). Se for válido, 
#classifique como equilátero (3 lados iguais), 
#isósceles (2 lados iguais) ou
#escaleno (3 lados diferentes). 
#Se não for válido, exiba "Não forma triângulo".


print("Descubra o triangulo")
a = float(input("digite o comprimento do lado a: "))
b = float(input("digite o comprimento do lado b: "))
c = float(input("digite o comprimento do lado c: "))

if a <= 0 or b <= 0 or c <= 0:
    print("Erro: Os lados devem ser maiores que zero.")
elif a == b == c:
        print("triângulo esquilátero")
elif a == b or a == c or b == c:
        print("triângulo isósceles")
elif a + b < c or b + c < a or c + a < b:
        print("não forma triangulo")
else:
        print("triângulo escaleno")
