#Construa um algoritmo de ordenação, utilizando o método bubble sort
#estudado. (Lembre-se que se trata de uma série de instruções que devem
#ser seguidas passo a passo). Para isso, você deve criar um método em
#que o tamanho do vetor seja dez e deve estar em ordem crescente.

#O vetor deverá:
#- comparar seus elementos dois a dois adjacentes;
#- se os elementos não estiverem em ordem, então ordenar;
#- senão, avançar para o próximo par;
#- repetir a operação até que nenhuma troca possa ser feita no vetor inteiro.

#Realize essa atividade no WORD ou no Bloco de Notas, suba esse arquivo
#para algum repositório e compartilhe o link no campo ao lado para que
#outros desenvolvedores possam analisá-lo.

tup = [9,8,5,3,4,7,6,1,2,0]
def bubbleSort(tup):
    for i in range(len(tup)):
        for j in range (len(tup)-i-1):
            if tup[j]>tup[j+1]:
                aux=tup[j+1]
                tup[j+1]=tup[j]
                tup[j]=aux
    return tup

print(tup)
tup=bubbleSort(tup)
print(tup)
                
