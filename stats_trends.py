import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



dataUri = 'DataSet/Gender_StatsData.csv'
pivoted_data_uri = 'DataSet/PivotedDataset.csv'

def getDataset(dataUrl):
    dataset = pd.read_csv(dataUrl)
    return  dataset


""" Defining Feature codes and country names to analyse """

INDICATOR_CODES=['SP.POP.TOTL', 'SP.POP.TOTL.FE.IN', 'SP.POP.TOTL.MA.IN',
 'SP.DYN.CBRT.IN', 'SP.DYN.CDRT.IN',
 'SE.COM.DURS',
 'SL.IND.EMPL.ZS', 'SL.AGR.EMPL.ZS', 'SL.AGR.EMPL.FE.ZS', 'SL.IND.EMPL.FE.ZS', 'SL.UEM.TOTL.ZS',
 'NY.GDP.MKTP.CD',
 'NY.ADJ.NNTY.PC.KD.ZG', 'NY.GSR.NFCY.CD', 'NV.AGR.TOTL.CD',
 'EG.USE.ELEC.KH.PC', 'EG.FEC.RNEW.ZS', 'EG.USE.COMM.FO.ZS']


featureMap={
    "SP.POP.TOTL": "Total Population",
    "SP.POP.TOTL.FE.IN": "Female Population",
    "SP.POP.TOTL.MA.IN": "Male Population",
    "SP.DYN.CBRT.IN": "Birth Rate",
    "SP.DYN.CDRT.IN": "Death Rate",
    "SE.COM.DURS": "Compulsory Education Dur.",
    "SL.IND.EMPL.ZS":"Employment in Industry(%)",
    "SL.AGR.EMPL.ZS": "Employment in Agriculture(%)",
    "SL.AGR.EMPL.FE.ZS": "Female Employment in Agriculture(%)",
    "SL.IND.EMPL.FE.ZS": "Female Employment in Industry(%)",
    "SL.UEM.TOTL.ZS": "Unemployment(%)",
    "NY.GDP.MKTP.CD": "GDP in USD",
    "NY.ADJ.NNTY.PC.KD.ZG":"National Income per Capita",
    "NY.GSR.NFCY.CD":"Net income from Abroad",
    "NV.AGR.TOTL.CD":"Agriculture value added(in USD)",
    "EG.USE.ELEC.KH.PC":"Electric Power Consumption(kWH per capita)",
    "EG.FEC.RNEW.ZS":"Renewable Energy Consumption (%)",
    "EG.USE.COMM.FO.ZS":"Fossil Fuel Consumption (%)"
}


countryMap={
    "US": "USA",
    "IN":"India",
    "CN": "China",
    "JP": "Japan",
    "CA": "Canada",
    "UK": "United Kingdom",
    "ZA": "South Africa"
}



melted_df = getDataset(dataUri).melt(id_vars=['Country Name', 'Country Code', 'Indicator Name', 'Indicator Code'], var_name='Year', value_name='Value')

# Pivot the table to have Indicator Names as columns
pivoted_df = melted_df.pivot_table(index=['Country Name', 'Country Code', 'Year'], columns='Indicator Code', values='Value').reset_index()
pivoted_df.fillna()
pivoted_df.to_csv('DataSet/PivotedDataset.csv')
