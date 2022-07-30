#Desenvolva um programa que recebe do usuário nome completo e ano de
#nascimento que seja entre 1922 e 2021. A partir dessas informações, o
#sistema mostrará o nome do usuário e a idade que completou, ou
#completará, no ano atual (2022).

#Caso o usuário não digite um número ou apareça um inválido no campo do
#ano, o sistema informará o erro e continuará perguntando até que um
#valor correto seja preenchido.

#Trabalhe esse código em seu IDE, suba ele para sua conta no GitHub e
#compartilhe o link desse projeto no campo ao lado para que outros
#desenvolvedores possam analisá-lo.

def nomeIdade():
    print("Informe o nome completo: ")
    nome = input()
    print("Informe o ano de nascimento: ")
    anoNascimento = int(input())

    while anoNascimento<1922 or anoNascimento>2021:
        print("Erro: Ano de Nascimento Inválido!!!")
        print("Informe o ano de nascimento: ")
        anoNascimento = int(input())
    idade = 2022-anoNascimento
    print(str(nome)+", "+str(idade)+" anos")
        




nomeIdade()
