import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



dataUri = 'DataSet/Gender_StatsData.csv'

def getDataset(dataUrl):
    dataset = pd.read_csv(dataUrl)
    return  dataset


# """ Defining Feature codes and country names to analyse """

# INDICATOR_CODES=['SP.POP.TOTL', 'SP.POP.TOTL.FE.IN', 'SP.POP.TOTL.MA.IN',
#  'SP.DYN.CBRT.IN', 'SP.DYN.CDRT.IN',
#  'SE.COM.DURS',
#  'SL.IND.EMPL.ZS', 'SL.AGR.EMPL.ZS', 'SL.AGR.EMPL.FE.ZS', 'SL.IND.EMPL.FE.ZS', 'SL.UEM.TOTL.ZS',
#  'NY.GDP.MKTP.CD',
#  'NY.ADJ.NNTY.PC.KD.ZG', 'NY.GSR.NFCY.CD', 'NV.AGR.TOTL.CD',
#  'EG.USE.ELEC.KH.PC', 'EG.FEC.RNEW.ZS', 'EG.USE.COMM.FO.ZS']


# featureMap={
#     "SP.POP.TOTL": "Total Population",
#     "SP.POP.TOTL.FE.IN": "Female Population",
#     "SP.POP.TOTL.MA.IN": "Male Population",
#     "SP.DYN.CBRT.IN": "Birth Rate",
#     "SP.DYN.CDRT.IN": "Death Rate",
#     "SE.COM.DURS": "Compulsory Education Dur.",
#     "SL.IND.EMPL.ZS":"Employment in Industry(%)",
#     "SL.AGR.EMPL.ZS": "Employment in Agriculture(%)",
#     "SL.AGR.EMPL.FE.ZS": "Female Employment in Agriculture(%)",
#     "SL.IND.EMPL.FE.ZS": "Female Employment in Industry(%)",
#     "SL.UEM.TOTL.ZS": "Unemployment(%)",
#     "NY.GDP.MKTP.CD": "GDP in USD",
#     "NY.ADJ.NNTY.PC.KD.ZG":"National Income per Capita",
#     "NY.GSR.NFCY.CD":"Net income from Abroad",
#     "NV.AGR.TOTL.CD":"Agriculture value added(in USD)",
#     "EG.USE.ELEC.KH.PC":"Electric Power Consumption(kWH per capita)",
#     "EG.FEC.RNEW.ZS":"Renewable Energy Consumption (%)",
#     "EG.USE.COMM.FO.ZS":"Fossil Fuel Consumption (%)"
# }


# countryMap={
#     "US": "USA",
#     "IN":"India",
#     "CN": "China",
#     "JP": "Japan",
#     "CA": "Canada",
#     "GB": "Great Britain",
#     "ZA": "South Africa"
# }

# # def remove_missing_features(df):
    
# #     if df is None:
# #         print("No DataFrame received!")
# #         return
    
# #     updated_df=df.copy()
# #     print("Removed missing features for: " + updated_df.iloc[0]['Country Name'])
# #     no_missing_vals=df.isnull().sum()
# #     n_missing_index_list = list(no_missing_vals.index)
# #     missing_percentage = no_missing_vals[no_missing_vals!=0]/df.shape[0]*100
# #     cols_to_trim=[]
    
    
# #     for i,val in enumerate(missing_percentage):
# #         if val > 75:
# #             cols_to_trim.append(n_missing_index_list[i])


# #     if len(cols_to_trim) > 0:
# #         updated_df=updated_df.drop(columns=cols_to_trim)
# #         print("Dropped Columns:" + str(cols_to_trim))
# #     else:
# #         print("Nothing  dropped")
# #     return updated_df



# # def fill_missing_values(df):
    
# #     if df is None:
# #         print("No DataFrame received")
# #         return

# #     df_cp=df.copy()
    
# #     # print("Filling missing features for: " + df_cp.iloc[0]['Country Name'])
    
# #     cols_list=list(df_cp.columns)
# #     cols_list.pop()

# #     df_cp.fillna(value=pd.np.nan, inplace=True)
    
# #     for col in cols_list:
# #         df_cp[col].fillna((df_cp[col].mean()), inplace=True)

# #     print("Filling missing values completed")
# #     return df_cp

# # updated_df = remove_missing_features(getDataset(dataUri))
# # updated_df = fill_missing_values(updated_df)
# # print(updated_df)

# pivotTable = getDataset(dataUri).pivot_table(index='Country Name',columns='Indicator Name',dropna=False)
# pivotTable.to_csv('pivotted.csv')



melted_df = getDataset(dataUri).melt(id_vars=['Country Name', 'Country Code', 'Indicator Name', 'Indicator Code'], var_name='Year', value_name='Value')

# Pivot the table to have Indicator Names as columns
pivoted_df = melted_df.pivot_table(index=['Country Name', 'Country Code', 'Year'], columns='Indicator Name', values='Value').reset_index()
pivoted_df.to_csv('pivotted.csv')
