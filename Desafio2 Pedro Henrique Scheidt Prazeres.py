import pandas as pd

'''
2 - Manipulação de Dados com Pandas

Dado um arquivo CSV chamado monitoramento_eletrico.csv contendo as colunas Data, Potencia_W, Tensao_V, Corrente_A, Frequencia_Hz:

a) Ler o arquivo CSV com a biblioteca Pandas.

b) Exibir todos os registros onde a frequência (Frequencia_Hz) esteja fora da faixa normal de operação (assuma que a faixa normal é de 59.8 a 60.2 Hz).

'''

# O enunciado pede para verificar "monitoramento_eletrico.csv", assumo que isso é um erro, pois o nome do csv fornecido é "medicoes_eletricas.csv"
# portanto, eu modifiquei para "medicoes_eletricas.csv"

ARQUIVO_CSV = 'medicoes_eletricas.csv'
VAL_MIN = 59.8
VAL_MAX = 60.2


df = pd.read_csv(ARQUIVO_CSV)

filtros = (df['Frequencia_Hz'] < VAL_MIN) | (df['Frequencia_Hz'] > VAL_MAX)
outliers = df[filtros]
print(outliers)

