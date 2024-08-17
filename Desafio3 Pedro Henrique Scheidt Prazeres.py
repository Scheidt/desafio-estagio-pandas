import pandas as pd
from datetime import datetime, timedelta

ARQUIVO_CSV = 'medicoes_eletricas.csv'

'''
3 - Criação de Função para Processamento de Dados Elétricos

Crie uma função chamada calcular_fator_potencia que receba um arquivo CSV chamado medicoes_potencia.csv e um intervalo de tempo em minutos. A função deve:

a) Ler o arquivo CSV.

b) Filtrar os registros dentro do intervalo de tempo fornecido.

c) Calcular o fator de potência médio durante o período, usando a fórmula: Fator de Potência = Potencia_W / (Tensao_V * Corrente_A).

d) Criar a função para retornar o fator de potência médio calculado para a primeira leitura do csv usando a função criada.

'''


def calcular_fator_potencia(file_path: str, intervalo_minutos: int):
    """
    calcula o fator de potência média
    
    Parameters
    ----------
    file_path : str
        string contendo o diretorio do arquivo .csv
    intervalo_minutos : int
        minutos...

    Return
    ------
    retorna a média...
    """
    # Ler o arquivo CSV
    df = pd.read_csv(file_path)

    # datas
    datas = pd.to_datetime(df["Data"])
    data_inicial = datas.min() # Foi considerado que a data inicial seja a data mais antiga do .csv

    # Filtrar os registros dentro do intervalo de tempo fornecido
    intervalo_final = data_inicial + timedelta(minutes=intervalo_minutos)
    df_filtrado = df[(datas <= intervalo_final)]
    
    # Calcular o fator de potência
    media = (df_filtrado['Potencia_W'] / (df_filtrado['Tensao_V'] * df_filtrado['Corrente_A'])).mean()
    
    # Calcular o fator de potência médio
    return media

print(calcular_fator_potencia(ARQUIVO_CSV, 5))