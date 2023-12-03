import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


dataUri = 'Gender_Stats_Data.csv'

def readDataset(dataUrl):
    dataset = pd.read_csv(dataUrl)
    # country_transposed_data = dataset.set_index('Country Name')
    # year_transposed_data = dataset.transpose()
    # print(dataset.describe())
    # print(dataset.head(25))
    return  dataset


genderdata = readDataset(dataUri)

"""  Applying Statistical Methods on  Expected years of schooling female"""

year_of_schooling = genderdata.loc[genderdata['Indicator Code'] == 'SE.SCH.LIFE.FE']


describe_gender = year_of_schooling ["1975"].describe()
print ('skewness',describe_gender)

skew_gender = year_of_schooling ["1975"].skew()
print ('skewness',skew_gender)

stdev_gender = year_of_schooling ["1975"].std()
print ('standard deviation',stdev_gender)


"""  Applying Statistical Methods on  Expected years of schooling male """

