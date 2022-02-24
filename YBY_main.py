import pandas as pd
import numpy as np
import os

def yby_csv_writer():
    years = list(range(2000, 2022))


    for year in years:
        df = pd.DataFrame()
        arqv = os.listdir('dados\\%s'%(year))
        for filecsv in arqv:
            stid =  pd.read_csv('dados\\%s\\'%(year)+filecsv, sep = ';', usecols=[1], skiprows=1, nrows=3, names= ['Valor'], decimal=',', encoding='mbcs')
            id = stid['Valor'].values

            stcoords = pd.read_csv('dados\\%s\\'%(year)+filecsv, sep = ';', usecols=[1], skiprows=4, nrows=3, names= ['Valor'], decimal=',', encoding='mbcs')
            coords = stcoords['Valor'].values

            dados = pd.read_csv('dados\\%s\\'%(year)+filecsv, sep=';', header=8, usecols=[0,1,2], decimal=',', encoding='mbcs', names= ['Data', 'Hora', id[1]+' - '+id[0]])

            dados [id[1]+' - '+id[0]] = dados[id[1]+' - '+id[0]].replace(-9999,np.nan)

            if (pd.isnull(dados[id[1]+' - '+id[0]]).all()):
                next
            else:
                count = pd.DataFrame(dados[id[1]+' - '+id[0]].value_counts(normalize= True))
                count.reset_index(inplace= True)
                df = pd.concat([df, count], axis=1)     


        df.to_csv('%s.csv'%(year), sep=';', decimal = ',')


def station_21y_csv_writer():
    
    years = list(range(2021, 1999, -1))
    for year in years:
        df = pd.read_csv('%s.csv'%(year))

    return (df)

if __name__ == "__main__":

    yby_csv_writer()
    # df = station_21y_csv_writer()
    # df = pd.read_csv('%s.csv'%(2000), sep = ';', decimal=',')
print('breakpoint')