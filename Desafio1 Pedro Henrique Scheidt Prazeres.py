import csv

'''
1 - Leitura e Análise de Arquivo CSV:
Dado um arquivo CSV chamado medicoes_eletricas.csv contendo as colunas Data, Potencia_W, Tensao_V, Corrente_A, Frequencia_Hz, Requisitos do exercício:

a) Ler o arquivo CSV com qualquer biblioteca, função nativa...

b) Exibir as 5 primeiras linhas do arquivo.

c) Calcular e exibir a média da potência (Potencia_W) durante o período registrado no CSV.

d) Identificar e exibir o valor máximo de tensão (Tensao_V) registrado e em que data ocorreu.

'''

with open('medicoes_eletricas.csv', newline='') as database:
    dados = csv.reader(database, delimiter=',')

    nLinhas = 0 
    potenciaTotal = 0
    tensao_max = {"val": 0, "data": 0}

    titulo = True

        #Data,Potencia_W,Tensao_V,Corrente_A,Frequencia_Hz
    for linha in dados:
        print(f"{linha[0]:^20}|{linha[1]:^12}|{linha[2]:^14}|{linha[3]:^18}|{linha[4]:^16}" + '\n')
        if titulo: # Essa é uma escolha estilística e reduz a performance do programa, caso performance for prioridade, pode ser removida
            print("========================================================================================")
            titulo = False
        else:
            print("----------------------------------------------------------------------------------------")
        nLinhas += 1
        try:
            potenciaTotal += int(linha[1])
            if int(linha[2]) > tensao_max["val"]:
                tensao_max["val"] = int(linha[2])
                tensao_max["data"] = linha[0]
        except:
            pass
    print("---")
    print(f"A potência média foi de {potenciaTotal/nLinhas:.2f} Watts")
    print(f"Valor máximo de tensão V: {tensao_max["val"]} Volts, lido em {tensao_max["data"]}")
    