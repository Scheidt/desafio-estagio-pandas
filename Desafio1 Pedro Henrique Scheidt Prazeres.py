import pandas as pd

ARQUIVO_CSV = 'medicoes_eletricas.csv'

'''
1 - Leitura e Análise de Arquivo CSV:
Dado um arquivo CSV chamado medicoes_eletricas.csv contendo as colunas Data, Potencia_W, Tensao_V, Corrente_A, Frequencia_Hz, Requisitos do exercício:

a) Ler o arquivo CSV com qualquer biblioteca, função nativa...

b) Exibir as 5 primeiras linhas do arquivo.

c) Calcular e exibir a média da potência (Potencia_W) durante o período registrado no CSV.

d) Identificar e exibir o valor máximo de tensão (Tensao_V) registrado e em que data ocorreu.

'''

data = pd.read_csv(ARQUIVO_CSV)
print(data.head(5))

potencia_media = data["Potencia_W"].mean()
print(f"A potência média foi de {potencia_media:.2f} Watts")

tensao_maxima = data.iloc[data["Tensao_V"].idxmax()]
print(f"Valor máximo de tensão V: {tensao_maxima["Tensao_V"]} Volts, lido em {tensao_maxima["Data"]}")