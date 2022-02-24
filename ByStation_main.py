from operator import index
import pandas as pd
import numpy as np
import os

def byStation_csv_writer():
    arqv = os.listdir('dados\\2021 - Copia')
    for filecsv in arqv:

        stid =  pd.read_csv('dados\\2021 - Copia\\'+filecsv, sep = ';', usecols=[1], skiprows=1, nrows=3, names= ['Valor'], decimal=',', encoding='mbcs')
        id = stid['Valor'].values

        stcoords = pd.read_csv('dados\\2021 - Copia\\'+filecsv, sep = ';', usecols=[1], skiprows=4, nrows=3, names= ['Valor'], decimal=',', encoding='mbcs')
        coords = stcoords['Valor'].values

        city_uf = id[1]+' - '+id[0]

        data1 = pd.read_csv('dados\\2021 - Copia\\'+filecsv, sep=';', header=8, usecols=[2], decimal=',', encoding='mbcs')

        data1.to_csv('byStation\\%s.csv'%(city_uf), sep=';', decimal = ',')

        add_yearofData(city_uf, id[2])
        
def add_yearofData(station, id):
    years = list(range(2020, 1999, -1))
    for year in years:
        arqv = os.listdir('dados\\%s'%(year))
        for filecsv in arqv:

            if id in filecsv:
                dados = pd.read_csv('dados\\%s\\'%(year)+filecsv, sep=';', header=8, usecols=[2], decimal=',', encoding='mbcs')

                dados.to_csv('byStation\\%s.csv'%(station), mode='a', header= False, sep=';', decimal = ',')
                exit
            else: next

def count_occurences():
    
    arqv = os.listdir('byStation')
    fob = pd.DataFrame()
    for filecsv in arqv:
        df = pd.read_csv('byStation\\'+filecsv, sep = ';', encoding= 'UTF-8', names=['%', filecsv])
        df[filecsv]  = df[filecsv].replace(-9999,np.nan)
        
        if (pd.isnull(df[filecsv]).all()):
            next
        else:
            count = pd.DataFrame(df[filecsv].value_counts(normalize= True))
            count.reset_index(inplace= True) 
            fob = pd.concat([fob, count], axis = 1)           
    
    fob.to_csv('Count.csv', sep=';', decimal=',')            

def Stations_ID():
    arqv = os.listdir('dados\\2021')
    df = pd.DataFrame(index= ['ESTAÇÃO', 'UF', 'CODIGO (WMO)', 'LAT', 'LONG', 'ALT'])
    for filecsv in arqv:

        stid =  pd.read_csv('dados\\2021\\'+filecsv, sep = ';', usecols=[1], nrows=7, decimal=',', encoding='mbcs', header= None)
        id = stid[1].values

        dfid = pd.Series([id[2], id[1], id[3], id [4], id[5], id[6]])
        
        df = pd.concat([df, dfid], axis = 1)
    
    df.to_csv('StationIDs.csv', sep=';', decimal = ',')

if __name__ == "__main__":

    # byStation_csv_writer()
    # count_occurences()
    Stations_ID()
    
print('breakpoint')