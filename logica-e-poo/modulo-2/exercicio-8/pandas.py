import pandas as pd

df = pd.read_csv("notas_alunos.csv")
df["media"] = (df["nota_1"] + df ["nota_2"])/2
df.loc[((df["media"] >=7) & (df["faltas"] <=5)) , "situacao"] = "APROVADO"
df.loc[((df["media"] <7) | (df["faltas"] >5)) , "situacao"] = "REPROVADO"

df.to_csv('alunos_situacao.csv', index = False)

print(df.head())

print("\n")
print("Maior número de Faltas: "+str(df["faltas"].max()))
print("Média da Turma: "+str(df["media"].mean()))
print("Maior Média: "+str(df["media"].max()))
