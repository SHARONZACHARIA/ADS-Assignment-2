import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt



dataUri = 'DataSet/Gender_StatsData.csv'
pivoted_data_uri = 'DataSet/PivotedDataset.csv'

def getDataset(dataUrl):
    dataset = pd.read_csv(dataUrl)
    return  dataset


""" Defining Feature codes and country names to analyse """

COLUMN_CODES=[ 'Country Name','Country Code','Year','SP.POP.TOTL', 'SP.POP.TOTL.FE.IN', 'SP.POP.TOTL.MA.IN',
 'SP.DYN.CBRT.IN', 'SP.DYN.CDRT.IN',
 'SE.COM.DURS',
 'SL.IND.EMPL.ZS', 'SL.AGR.EMPL.ZS', 'SL.AGR.EMPL.FE.ZS', 'SL.IND.EMPL.FE.ZS', 'SL.UEM.TOTL.ZS',
 'NY.GDP.MKTP.CD',
 'NY.ADJ.NNTY.PC.KD.ZG']


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
    "NY.ADJ.NNTY.PC.KD.ZG":"National Income per Capita"
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


# melting the dataset 
melted_df = getDataset(dataUri).melt(id_vars=['Country Name', 'Country Code', 'Indicator Name', 'Indicator Code'], var_name='Year', value_name='Value')

# Pivot the table to have Indicator Names as columns
pivoted_df = melted_df.pivot_table(index=['Country Name', 'Country Code', 'Year'], columns='Indicator Code', values='Value').reset_index()
# pivoted_df.to_csv('DataSet/PivotedDataset.csv')

filtered_columns = [col for col in pivoted_df.columns if col in COLUMN_CODES]
df_filtered = pivoted_df[filtered_columns]


#cleaning the transformed data set 
# Fill missing values with the mean of the column
df_cleaned = df_filtered.fillna(df_filtered.mean())
df_cleaned.to_csv('Dataset/CleanedDataset.csv')


#Applying Statistical Methods on cleaned dataset
copy_us_df_cleaned = df_cleaned.drop(['Year', 'Country Name'], axis='columns')
print(copy_us_df_cleaned.describe())

#Plotting co relation graphs
fig, ax = plt.subplots(figsize=(10,10))
sns.heatmap(copy_us_df_cleaned.corr(), cmap='RdBu', center=0,ax=ax)
plt.savefig('correlation_us.png')
plt.show()