import pandas as pd
import matplotlib.pyplot as plt
import kagglehub
from kagglehub import KaggleDatasetAdapter

path = "Titanic-Dataset.csv"

df = kagglehub.dataset_load(
  KaggleDatasetAdapter.PANDAS,
  "yasserh/titanic-dataset",
  path
)

print("Quantidade de linhas e colunas: ", df.shape)
print("Colunas: ", df.columns)

#informacoes e tipos de dados
df.info()

#primeiras linhas
df.head(5)

#Homens e mulheres
homens = df[ (df["Sex"] == "male")  ].count().sum()
mulheres = df[ (df["Sex"] == "female")  ].count().sum()
print("Homens::", homens)
print("Mulheres:", mulheres)

valores = [homens, mulheres]
categorias = ['Homens', 'Mulheres']

plt.bar(categorias, valores, color='skyblue')
plt.show()

#Mortos e sobreviventes
mortos = df[ (df['Survived'] == 0)  ].count().sum()
sobreviventes = df[ (df['Survived'] == 1)  ].count().sum()

print("Mortos:", mortos)
print("Sobreviventes:", sobreviventes)

valores = [mortos, sobreviventes]
categorias = ['Mortos', 'Sobreviventes']

plt.bar(categorias, valores, color='skyblue')
plt.show()

#Idade
idades = df["Age"]
plt.hist(idades)
plt.show()

#Mortos e sobreviventes x idade
print(idades, valores)