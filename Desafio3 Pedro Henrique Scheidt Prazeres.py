import pandas as pd
from datetime import timedelta

# O enunciado pede para verificar "monitoramento_eletrico.csv", assumo que isso é um erro, pois o nome do csv fornecido é "medicoes_eletricas.csv"
# portanto, eu modifiquei para "medicoes_eletricas.csv"
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
    calcula o fator de potência média em um intervalo, com base em um arquivo csv.
    A função assume o inicio do intervalo como o primeiro registro do csv, e o final como a ultima leitura antes do limite do intervalo fornecido
    
    Parameters
    ----------
    file_path : str
        string contendo o diretorio do arquivo .csv
    intervalo_minutos : int
        int representando o período que deve ser analisado

    Return
    ------
    retorna a média do fator potência do intervalo fornecido (int)
    """

    # Ler o arquivo CSV
    if intervalo_minutos < 0:
        raise Exception("ERRO! Valor do intervalo fornecido não pode ser negativo")
    try:
        dados = pd.read_csv(ARQUIVO_CSV)
    except FileNotFoundError:
        print(f"Arquivo não encontrado, verifique o nome do arquivo. Nome do arquivo fornecido: {ARQUIVO_CSV}")
    else:
        # datas
        datas = pd.to_datetime(dados["Data"])
        data_inicial = datas.min() # Foi considerado que a data inicial seja a data mais antiga do .csv

        # Filtrar os registros dentro do intervalo de tempo fornecido
        intervalo_final = data_inicial + timedelta(minutes=intervalo_minutos)
        df_filtrado = dados[(datas <= intervalo_final)]

        #print(df_filtrado)

        # Calcular o fator de potência e a média
        media = (df_filtrado['Potencia_W'] / (df_filtrado['Tensao_V'] * df_filtrado['Corrente_A'])).mean()
        
        return media

print(calcular_fator_potencia(ARQUIVO_CSV, 5))