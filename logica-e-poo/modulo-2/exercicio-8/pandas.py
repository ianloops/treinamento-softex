import pandas as pd

df = pd.read_csv("notas_alunos.csv")
df["media"] = (df["nota_1"] + df ["nota_2"])/2
df.loc[df["media"] >=7 and df["faltas"] <=5 , "situacao"] = "APROVADO"
df.loc[df["media"] <7 or df["faltas"] >5, "situacao"] = "REPROVADO"

df.to_csv('alunos_situacao.csv', index = False)

print(df["faltas"].max())
print(df["media"].median())
print(df["media"].max())
