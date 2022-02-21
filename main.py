from numpy import NaN
import pandas as pd
import numpy as np

import os

arqv = os.listdir('dados')
df = pd.DataFrame()
fname = 'dados\{}'
for filecsv in arqv:
    # f= 'dados\INMET_SE_SP_A771_SAO PAULO - INTERLAGOS_01-01-2021_A_31-12-2021.CSV'

    stid =  pd.read_csv('dados\\'+filecsv, sep = ';', usecols=[1], skiprows=1, nrows=3, names= ['Valor'], decimal=',', encoding='mbcs')
    id = stid['Valor'].values

    stcoords = pd.read_csv('dados\\'+filecsv, sep = ';', usecols=[1], skiprows=4, nrows=3, names= ['Valor'], decimal=',', encoding='mbcs')
    coords = stcoords['Valor'].values


    dados = pd.read_csv('dados\\'+filecsv, sep=';', header=8, usecols=[0,1,2], decimal=',', encoding='mbcs', names= ['Data', 'Hora', id[1]+' - '+id[0]])

    if (pd.isnull(dados[id[1]+' - '+id[0]]).all()):
        next
    else:
        count = pd.DataFrame(dados[id[1]+' - '+id[0]].value_counts(normalize= True, bins = 8))
        count.reset_index(inplace= True)
        df = pd.concat([df, count], axis=1) #.IntervalIndex.get_indexer_non_unique()
    # df = pd.concat([df, ct.reindex(df.index)], axis=1)
    # df = pd.merge(df, ct, how='outer')
    


# print(id)
# print (coords)
# print (dados)
df.to_csv('ano.csv', sep=';')
print(df)
print('breakpoint')