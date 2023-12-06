import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


dataUri = 'DataSet/Gender_StatsData.csv'

def getDataset(dataUrl):
    dataset = pd.read_csv(dataUrl)
    return  dataset


"""Defining Feature codes and country named to analyse """

INDICATOR_CODES=['SP.POP.TOTL', 'SP.POP.TOTL.FE.IN', 'SP.POP.TOTL.MA.IN',
 'SP.DYN.CBRT.IN', 'SP.DYN.CDRT.IN',
 'SE.COM.DURS',
 'SL.IND.EMPL.ZS', 'SL.AGR.EMPL.ZS', 'SL.AGR.EMPL.FE.ZS', 'SL.IND.EMPL.FE.ZS', 'SL.UEM.TOTL.ZS',
 'NY.GDP.MKTP.CD',
 'NY.ADJ.NNTY.PC.KD.ZG', 'NY.GSR.NFCY.CD', 'NV.AGR.TOTL.CD',
 'EG.USE.ELEC.KH.PC', 'EG.FEC.RNEW.ZS', 'EG.USE.COMM.FO.ZS']

countryMap={
    "US": "USA",
    "IN":"India",
    "CN": "China",
    "JP": "Japan",
    "CA": "Canada",
    "GB": "Great Britain",
    "ZA": "South Africa"
}

def remove_missing_features(df):
    
    if df is None:
        print("No DataFrame received!")
        return
    
    updated_df=df.copy()
    print("Removed missing features for: " + updated_df.iloc[0]['Country'])
    no_missing_vals=df.isnull().sum()
    n_missing_index_list = list(no_missing_vals.index)
    missing_percentage = no_missing_vals[no_missing_vals!=0]/df.shape[0]*100
    cols_to_trim=[]
    
    
    for i,val in enumerate(missing_percentage):
        if val > 75:
            cols_to_trim.append(n_missing_index_list[i])


    if len(cols_to_trim) > 0:
        updated_df=updated_df.drop(columns=cols_to_trim)
        print("Dropped Columns:" + str(cols_to_trim))
    else:
        print("Nothing  dropped")
    return updated_df


def fill_missing_values(df):
    
    if df is None:
        print("No DataFrame received")
        return

    df_cp=df.copy()
    
    print("Filling missing features for: " + df_cp.iloc[0]['Country'])
    
    cols_list=list(df_cp.columns)
    cols_list.pop()

    df_cp.fillna(value=pd.np.nan, inplace=True)
    
    for col in cols_list:
        df_cp[col].fillna((df_cp[col].mean()), inplace=True)

    print("Filling missing values completed")
    return df_cp