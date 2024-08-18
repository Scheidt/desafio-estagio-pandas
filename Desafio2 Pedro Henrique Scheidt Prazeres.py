import pandas as pd
from datetime import timedelta

ARQUIVO_CSV = 'medicoes_eletricas.csv'
FREQUENCIA_MIN = 59.8
FREQUENCIA_MAX = 60.2

'''
2 - Manipulação de Dados com Pandas

Dado um arquivo CSV chamado monitoramento_eletrico.csv contendo as colunas Data, Potencia_W, Tensao_V, Corrente_A, Frequencia_Hz:

a) Ler o arquivo CSV com a biblioteca Pandas.

b) Exibir todos os registros onde a frequência (Frequencia_Hz) esteja fora da faixa normal de operação (assuma que a faixa normal é de 59.8 a 60.2 Hz).

'''

# O enunciado pede para verificar "monitoramento_eletrico.csv", assumo que isso é um erro, pois o nome do csv fornecido é "medicoes_eletricas.csv"
# portanto, eu modifiquei para "medicoes_eletricas.csv"

try:
    data = pd.read_csv(ARQUIVO_CSV)
except FileNotFoundError:
    print(f"Arquivo não encontrado, verifique o nome do arquivo. Nome do arquivo fornecido: {ARQUIVO_CSV}")
else:

    frequencias = data["Frequencia_Hz"]

    filtros = (frequencias < FREQUENCIA_MIN) | (frequencias > FREQUENCIA_MAX)
    outliers = data[filtros]

    if len(outliers) > 0:
        print(outliers)
    else:
        print("Nenhuma medição está fora da faixa normal de operação.")
