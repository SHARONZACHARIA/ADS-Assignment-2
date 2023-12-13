import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import skew
from scipy.stats import kurtosis

# paths to datasets
Original_dataUri = 'DataSet/Gender_StatsData.csv'
pivoted_data_uri = 'DataSet/PivotedDataset.csv'
cleaned_data_uri = 'DataSet/CleanedDataset.csv'

# defining the column names as list  which will be used for analysis
COLUMN_CODES = ['Country Name', 'Country Code', 'Year', 'SP.POP.TOTL', 'SP.POP.TOTL.FE.IN', 'SP.POP.TOTL.MA.IN',
                'SP.DYN.CBRT.IN', 'SP.DYN.CDRT.IN',
                'SL.IND.EMPL.ZS', 'SL.AGR.EMPL.ZS', 'SL.AGR.EMPL.FE.ZS', 'SL.IND.EMPL.FE.ZS', 'SL.UEM.TOTL.ZS',
                'NY.GDP.MKTP.CD',
                'NY.ADJ.NNTY.PC.KD.ZG', 'SE.ADT.1524.LT.FE.ZS', 'SE.ADT.1524.LT.MA.ZS']

# defining the list of Indicatirs
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
    "SE.ADT.1524.LT.MA.ZS": "Literacy rate % male (ages 15-24)",
    "SE.ADT.1524.LT.FE.ZS": "Literacy rate % 'female (ages 15-24)"
}

# Mapping country codes to country names
countryMap = {
    "US": "United States",
    "IN": "India",
    "CHN": "China",
    "JP": "Japan",
    "CA": "Canada",
    "GBR": "United Kingdom",
    "ZAF": "South Africa"
}

# Function to Read a dataset and return the transposed dataset
def getDataset(dataUrl):
    dataset = pd.read_csv(dataUrl)
    melted_df = dataset.melt(id_vars=[
        'Country Name', 'Country Code', 'Indicator Name', 'Indicator Code'], var_name='Year', value_name='Value')
    Transposed_df = melted_df.pivot_table(
        index=['Country Name', 'Country Code', 'Year'], columns='Indicator Code', values='Value').reset_index()
    Transposed_df.to_csv('DataSet/PivotedDataset.csv')
    return Transposed_df



# Cleaning the Transposed Data set and saving cleaned dataset as a new csv file
def cleanDataSet(dataset):
    filtered_columns = [col for col in dataset.columns if col in COLUMN_CODES]
    df_filtered = getDataset(Original_dataUri)[filtered_columns]
    df_cleaned = df_filtered.fillna(df_filtered.mean())
    df_cleaned.to_csv('Dataset/CleanedDataset.csv')
    return cleaned_df


cleaned_df = pd.read_csv(cleaned_data_uri)
df_cleaned = cleanDataSet(getDataset(Original_dataUri))


df_IND = df_cleaned[df_cleaned["Country Name"] == "India"]
df_UK = df_cleaned[df_cleaned["Country Name"] == "United Kingdom"]
df_ZAF = df_cleaned[df_cleaned["Country Name"] == "South Africa"]

population_Canada_BDRate = cleaned_df[cleaned_df['Country Name'] == "Canada"]
population_Japan_BDRate = cleaned_df[cleaned_df['Country Name'] == "Japan"]
population_UK_BDRate = cleaned_df[cleaned_df['Country Name']
                                  == "United Kingdom"]

unemployment_India = cleaned_df[(cleaned_df['Country Name'] == "India") & (
    cleaned_df['Year'] >= cleaned_df['Year'].max() - 9)]
unemployment_Usa = cleaned_df[(cleaned_df['Country Name'] == "United States") & (
    cleaned_df['Year'] >= cleaned_df['Year'].max() - 9)]
unemployment_Sa = cleaned_df[(cleaned_df['Country Name'] == "South Africa") & (
    cleaned_df['Year'] >= cleaned_df['Year'].max() - 9)]


filtered_population = cleaned_df[
    ((cleaned_df['Country Name'] == 'India') | (cleaned_df['Country Name'] == 'China') |
     (cleaned_df['Country Name'] == 'United Kingdom') | (cleaned_df['Country Name'] == 'South Africa')) &
    ((cleaned_df['Year'] == 1960) | (cleaned_df['Year'] == 1990) | (cleaned_df['Year'] == 2022))]



population_Gender_China = cleaned_df[cleaned_df['Country Name']=="China"]
population_Gender_Usa = cleaned_df[cleaned_df['Country Name']=="United States"]
population_Gender_Sa = cleaned_df[cleaned_df['Country Name']=="South Africa"]
filtered_population = filtered_population[["Country Name","Year","SP.POP.TOTL"]]
years_to_plot = [1960, 1990, 2022]

# Applying Statistical Methods on cleaned dataset
copy_df_cleaned = df_cleaned.drop(['Year', 'Country Name'], axis='columns')
# describe method()
stat_describe = copy_df_cleaned.describe()
print(stat_describe)
#skewness 
skewness_gender_china = skew(population_Gender_China["SP.POP.TOTL"])
print(f"skewnwss of chineese population data {skewness_gender_china}")
#kurtosis
kurtosis_gender_china = kurtosis(population_Gender_China["SP.POP.TOTL"])
print(f"kurtosis of chineese population data{kurtosis_gender_china}")



# Function to draw correlation heatmap
def drawCorrGraph(country_df, country_name):
    correaltion_matrix = country_df.corr(numeric_only=True)
    correaltion_matrix = correaltion_matrix.rename(columns=featureMap)
    correaltion_matrix = correaltion_matrix.rename(index=featureMap)
    plt.figure(1, figsize=(10, 5))
    sns.heatmap(correaltion_matrix, annot=True, fmt=".1g", vmax=1, vmin=0)
    plt.title('Correlation HeatMap - ' + country_name)
    plt.show()

#function to draw Bar graph
def drawBar(df_col1 , df_col2 , country , color):
    plt.bar(df_col1,df_col2,color=color)
    plt.title("Unemployment Rate - " + country)
    plt.xlabel("Year")
    plt.ylabel("Unemployment Rate - ")
    plt.show()

# Function to draw population Bar graph
def draw_population_growth(population_data, years):
    filtered_population = population_data[["Country Name", "Year", "SP.POP.TOTL"]]
    pivoted_population_df = filtered_population.pivot(
        index='Country Name', columns='Year', values='SP.POP.TOTL').reset_index()
    pivoted_population_df.plot(kind='bar', x='Country Name', y=years)
    plt.xticks(rotation=90, horizontalalignment="center")
    plt.title("Population Growth")
    plt.xlabel("Country")
    plt.ylabel("Population Rate")
    plt.legend(title='Year')
    plt.show()

# Function to plot line graphs -1 
def plot_birth_death_rates(country_data_list):
    num_countries = len(country_data_list)
    fig, axs = plt.subplots(num_countries, 1, figsize=(8, 6 * num_countries))
    plt.subplots_adjust(hspace=0.5)
    country_name = ["Canada","Japan","UK"]
    for i, country_data in enumerate(country_data_list):
        axs[i].set_xlabel("Year")
        axs[i].set_ylabel("Number of People")
        axs[i].plot(country_data["Year"], country_data["SP.DYN.CBRT.IN"], linestyle='-', color='#A569BD', label='Birth Rate')
        axs[i].plot(country_data["Year"], country_data["SP.DYN.CDRT.IN"], linestyle='-', color='b', label='Death Rate')
        axs[i].set_title(f"Birth Death Rate - " + country_name[i])  # Assuming a 'Country' column exists in the data
        axs[i].legend()
    
    plt.show()

# Function to plot line graphs -2
def plot_population_by_gender(country_data_list):
    num_countries = len(country_data_list)
    fig, axs = plt.subplots(num_countries, 1, figsize=(8, 6 * num_countries))
    plt.subplots_adjust(hspace=0.5)
    country_name = ["China","USA","South Africa"]
    for i, country_data in enumerate(country_data_list):
        axs[i].set_xlabel("Year")
        axs[i].set_ylabel("Population Rate")
        axs[i].plot(country_data["Year"], country_data["SP.POP.TOTL.FE.IN"], linestyle='-', color='#A569BD', label='Female')
        axs[i].plot(country_data["Year"], country_data["SP.POP.TOTL.MA.IN"], linestyle='-', color='b', label='Male')
        axs[i].set_title(f"Population by Gender - " + country_name[i])  # Assuming a 'Country' column exists in the data
        axs[i].legend()
    
    plt.show()


# Function Calls 
# drawCorrGraph(df_IND, " India")
# drawCorrGraph(df_ZAF, " South Africa")
# drawBar(unemployment_India["Year"],unemployment_India["SL.UEM.TOTL.ZS"],"India","#8E44AD")
# drawBar(unemployment_Usa["Year"],unemployment_Usa["SL.UEM.TOTL.ZS"],"USA","#F4D03F")
# drawBar(unemployment_Sa["Year"],unemployment_Sa["SL.UEM.TOTL.ZS"],"South Africa","#27AE60")
# draw_population_growth(filtered_population, years_to_plot)
# plot_birth_death_rates([population_Canada_BDRate,population_Japan_BDRate,population_UK_BDRate])
# plot_population_by_gender([population_Gender_China,population_Gender_Usa,population_Gender_Sa])
