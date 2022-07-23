#Faça uma função calculadora de dois números com três parâmetros: os
#dois primeiros serão os números da operação e o terceiro será a entrada
#que definirá a operação a ser executada. Considera a seguinte
#definição:
#1. Soma
#2. Subtração
#3. Multiplicação
#4. Divisão

#Caso seja inserido um número de operação que não exista, o resultado
#deverá ser 0.

#Trabalhe esse código em seu IDE, suba ele para sua conta no GitHub e
#compartilhe o link desse projeto no campo ao lado para que outros
#desenvolvedores possam analisá-lo.

def calculadora(valor1, valor2, operacao):
    if (operacao == 1):
        return valor1+valor2
    elif(operacao == 2):
        return valor1-valor2
    elif(operacao==3):
        return valor1*valor2
    elif(operacao==4):
        return valor1/valor2
    else:
        return 0

print(calculadora(10, 5, 1))
