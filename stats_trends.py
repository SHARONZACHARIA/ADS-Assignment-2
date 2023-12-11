import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


dataUri = 'DataSet/Gender_StatsData.csv'
pivoted_data_uri = 'DataSet/PivotedDataset.csv'
cleaned_data_uri = 'DataSet/CleanedDataset.csv'

def getDataset(dataUrl):
    dataset = pd.read_csv(dataUrl)
    return dataset

""" Defining Feature codes and country names to analyse """

COLUMN_CODES = ['Country Name', 'Country Code', 'Year', 'SP.POP.TOTL', 'SP.POP.TOTL.FE.IN', 'SP.POP.TOTL.MA.IN',
                'SP.DYN.CBRT.IN', 'SP.DYN.CDRT.IN',
                'SL.IND.EMPL.ZS', 'SL.AGR.EMPL.ZS', 'SL.AGR.EMPL.FE.ZS', 'SL.IND.EMPL.FE.ZS', 'SL.UEM.TOTL.ZS',
                'NY.GDP.MKTP.CD',
                'NY.ADJ.NNTY.PC.KD.ZG','SE.ADT.1524.LT.FE.ZS','SE.ADT.1524.LT.MA.ZS']

featureMap = {
    "SP.POP.TOTL": "Total Population",
    "SP.POP.TOTL.FE.IN": "Female Population",
    "SP.POP.TOTL.MA.IN": "Male Population",
    "SP.DYN.CBRT.IN": "Birth Rate",
    "SP.DYN.CDRT.IN": "Death Rate",
    "SL.IND.EMPL.ZS": "Employment in Industry(%)",
    "SL.AGR.EMPL.ZS": "Employment in Agriculture(%)",
    "SL.AGR.EMPL.FE.ZS": "Female Employment in Agriculture(%)",
    "SL.IND.EMPL.FE.ZS": "Female Employment in Industry(%)",
    "SL.UEM.TOTL.ZS": "Unemployment(%)",
    "NY.GDP.MKTP.CD": "GDP in USD",
    "NY.ADJ.NNTY.PC.KD.ZG": "National Income per Capita",
    "SE.ADT.1524.LT.MA.ZS" : "Literacy rate % male (ages 15-24)",
    "SE.ADT.1524.LT.FE.ZS" : "Literacy rate % 'female (ages 15-24)"
}

countryMap = {
    "US": "USA",
    "IN": "India",
    "CHN": "China",
    "JP": "Japan",
    "CA": "Canada",
    "GBR": "United Kingdom",
    "ZAF": "South Africa"
}


# melting the dataset
melted_df = getDataset(dataUri).melt(id_vars=[
    'Country Name', 'Country Code', 'Indicator Name', 'Indicator Code'], var_name='Year', value_name='Value')

# Pivot the table to have Indicator Names as columns
pivoted_df = melted_df.pivot_table(
    index=['Country Name', 'Country Code', 'Year'], columns='Indicator Code', values='Value').reset_index()
# pivoted_df.to_csv('DataSet/PivotedDataset.csv')

filtered_columns = [col for col in pivoted_df.columns if col in COLUMN_CODES]
df_filtered = pivoted_df[filtered_columns]

# cleaning the transformed data set
# Fill missing values with the mean of the column
df_cleaned = df_filtered.fillna(df_filtered.mean())
df_cleaned.to_csv('Dataset/CleanedDataset.csv')


# Applying Statistical Methods on cleaned dataset
copy_df_cleaned = df_cleaned.drop(['Year', 'Country Name'], axis='columns')
print(copy_df_cleaned.describe())


df_IND = df_cleaned[df_cleaned["Country Name"] == "India"]
df_UK = df_cleaned[df_cleaned["Country Name"] == "United Kingdom"]
df_ZAF = df_cleaned[df_cleaned["Country Name"] == "South Africa"]

# Correlation Matrix and Heat map for India 
correaltion_matrix_IND = df_IND.corr(numeric_only=True)
correaltion_matrix_IND = correaltion_matrix_IND.rename(columns=featureMap)
correaltion_matrix_IND = correaltion_matrix_IND.rename(index=featureMap)
plt.figure(1,figsize=(10,10))
heatmap_data = sns.heatmap(correaltion_matrix_IND , annot=True,fmt=".1g", vmax=1, vmin=0) 
plt.title('Correlation Matrix for India')
plt.show()

# Correlation Matrix and Heat map for United Kingdom 
correaltion_matrix_UK = df_UK.corr(numeric_only=True)
correaltion_matrix_UK = correaltion_matrix_UK.rename(columns=featureMap)
correaltion_matrix_UK = correaltion_matrix_UK.rename(index=featureMap)
plt.figure(2,figsize=(10,10))
heatmap_data = sns.heatmap(correaltion_matrix_UK , annot=True,fmt=".1g", vmax=1, vmin=0) 
plt.title('Correlation Matrix for United Kingdom')
plt.show()

#Correlation Matrix and Heat map for South Africa
correaltion_matrix_ZAF = df_ZAF.corr(numeric_only=True)
correaltion_matrix_ZAF = correaltion_matrix_ZAF.rename(columns=featureMap)
correaltion_matrix_ZAF = correaltion_matrix_ZAF.rename(index=featureMap)
plt.figure(3,figsize=(10,10))
heatmap_data = sns.heatmap(correaltion_matrix_ZAF , annot=True,fmt=".1g", vmax=1, vmin=0) 
plt.title('Correlation Matrix for South Africa')
plt.show()

# # bar graphs 
# # Filtering for India and China for the years 1960 and 2022
cleaned_df = pd.read_csv(cleaned_data_uri)

filtered_population = cleaned_df[
    ((cleaned_df['Country Name'] == 'India') | (cleaned_df['Country Name'] == 'China') | 
    (cleaned_df['Country Name'] == 'United Kingdom') | (cleaned_df['Country Name'] == 'South Africa')) &
    ((cleaned_df['Year'] == 1960) | (cleaned_df['Year'] == 1990) | (cleaned_df['Year'] == 2022))]

filtered_population = filtered_population[["Country Name","Year","SP.POP.TOTL"]]
pivoted_population_df = filtered_population.pivot(index='Country Name', columns='Year', values='SP.POP.TOTL').reset_index()
pivoted_population_df.plot(kind='bar',x='Country Name',y=[1960, 1990, 2022])
plt.xticks(rotation=30, horizontalalignment="center")
plt.show()


#line graphs 
literacy_FE_India = cleaned_df[cleaned_df['Country Name']=="India"]
literacy_FE_China = cleaned_df[cleaned_df['Country Name']=="China"]
plt.plot(literacy_FE_China["Year"],literacy_FE_China["SE.ADT.1524.LT.FE.ZS"])
plt.plot(literacy_FE_India["Year"],literacy_FE_India["SE.ADT.1524.LT.FE.ZS"])
plt.show()