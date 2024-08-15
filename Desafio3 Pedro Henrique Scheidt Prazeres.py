import pandas as pd

'''
3 - Criação de Função para Processamento de Dados Elétricos

Crie uma função chamada calcular_fator_potencia que receba um arquivo CSV chamado medicoes_potencia.csv e um intervalo de tempo em minutos. A função deve:

a) Ler o arquivo CSV.

b) Filtrar os registros dentro do intervalo de tempo fornecido.

c) Calcular o fator de potência médio durante o período, usando a fórmula: Fator de Potência = Potencia_W / (Tensao_V * Corrente_A).

d) Criar a função para retornar o fator de potência médio calculado para a primeira leitura do csv usando a função criada.

'''

