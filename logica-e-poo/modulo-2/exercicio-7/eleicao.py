#Desenvolva um código que simule uma eleição com três candidatos.
#- candidato_X => 889
#- candidato_Y => 847
#- candidato_Z => 515
#- branco => 0

#O código deve perguntar se deseja finalizar a votação depois do voto.
#Caso o número do voto não corresponda a nenhum candidato ou seja
#branco, ele deve ser tratado como nulo. Se for inserido um texto ao
#invés de número, o código deve retornar uma mensagem para votar
#novamente.

#Quando a votação for finalizada, o código deverá mostrar o vencedor,
#aquele com o maior número de votos e, também, a quantidade de votos de
#cada candidato, os brancos e nulos

#Trabalhe esse código em seu IDE, suba ele para sua conta no GitHub e
#compartilhe o link desse projeto no campo ao lado para que outros
#desenvolvedores possam analisá-lo.

votosCandidato_X = 0
votosCandidato_Y = 0
votosCandidato_Z = 0
votosBranco = 0

    
votacao=True
while votacao:
    voto = ''
    confirma = 'n'
    candidato_X = 889
    candidato_Y = 847
    candidato_Z = 515
    while(confirma=='n'):
        print("Insira o seu voto: ")
        voto = int(input())
        while((type(voto) is int)!=True):
            print("Erro: Insira apenas números: ")
            voto = int(input())
        print("Confirma o seu voto(s ou n): "+str(voto))
        confirma = input()
        if(confirma=='s'):
            print("Voto Confirmado")

        if(voto==candidato_X):
            votosCandidato_X += 1
        elif (voto == candidato_Y):
            votosCandidato_Y +=1
        elif (voto == candidato_Z):
            votosCandidato_Z +=1
        else:
            votosBranco += 1

        print("Deseja finalizar a votação(s ou n)?")
        resposta = input()

        while resposta!='s' and resposta!='n':
            print("Resposta inválida, responda com 's' ou 'n'")
            resposta==input()
         
        if resposta=="s":
            votacao= False
        elif resposta=="n":
            votacao = True

        
print("Candidato X: "+ str(votosCandidato_X))
print("Candidato Y: "+ str(votosCandidato_Y))
print("Candidato Z: "+ str(votosCandidato_Z))
print("Brancos e Nulos: "+ str(votosBranco))
