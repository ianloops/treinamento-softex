tup =[9,11,65,55,43,83,5,3,45,7,67,1,29,501,-61,13,467,8957,921,97,973,113,9465,99,63,247,561,3221,901]


def insertionSort(tup):
    for i in range(1,len(tup)):
        aux=tup[i]
        j=i-1

        while j>=0 and aux<tup[j]:
            tup[j+1]=tup[j]
            j-=1
        tup[j+1]=aux
    return tup

print(tup)
tup=insertionSort(tup)
print(tup)
                
