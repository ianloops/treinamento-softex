#Faça uma função calculadora que os números e as operações serão feitas
#pelo usuário. O código deve ficar rodando infinitamente até que o
#usuário escolha a opção de sair. No início, o programa mostrará a
#seguinte lista de operações:

#1: Soma
#2: Subtração
#3: Multiplicação
#4: Divisão
#0: Sair

#Digite o número para a operação correspondente e caso o usuário
#introduza qualquer outro, o sistema deve mostrar a mensagem “Essa opção
#não existe” e voltar ao menu de opções.

#Após a seleção, o sistema deve pedir para o usuário inserir o primeiro
#e segundo valor, um de cada. Depois precisa executar a operação e
#mostrar o resultado na tela. Quando o usuário escolher a opção “Sair”,
#o sistema irá parar.

def calcular(valor1, valor2, operacao):
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

def calculadora():
    operacao=-1
    while (operacao!=0):
        print("\n1: Soma")
        print("2: Subtração")
        print("3: Multiplicação")
        print("4: Divisão")
        print("0: Sair")
        operacao=int(input())
        if(operacao>0 and operacao<5):
            print("Valor 1: ")
            valor1=int(input())
            print("Valor 2: ")
            valor2=int(input())
            print("O resultado é : " + str(calcular(valor1, valor2, operacao)))
        elif (operacao==0):
            print("Calculadora finalizada")
        else:
            print("Essa opção não existe")

calculadora()
