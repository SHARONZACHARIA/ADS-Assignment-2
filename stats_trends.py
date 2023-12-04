import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


dataUri = 'DataSet/Gender_StatsData.csv'

def readDataset(dataUrl):
    dataset = pd.read_csv(dataUrl)
    return  dataset


genderdata = readDataset(dataUri)
print(genderdata.corr())

"""   Statistical Analysis on Expected years of schooling female """

year_of_schooling = genderdata.loc[genderdata['Indicator Code'] == 'SE.SCH.LIFE.FE']

describe_gender_female = year_of_schooling ["1990"].describe()
print ('skewness',describe_gender_female)

skew_gender_female = year_of_schooling ["1990"].skew()
print ('skewness',skew_gender_female)

stdev_gender_female = year_of_schooling ["1990"].std()
print ('standard deviation',stdev_gender_female)


""" Statistical Analysis  on  Expected years of schooling male """

year_of_schooling = genderdata.loc[genderdata['Indicator Code'] == 'SE.SCH.LIFE.MA']

describe_gender_male = year_of_schooling ["1990"].describe()
print ('skewness',describe_gender_male)

skew_gender_male = year_of_schooling ["1990"].skew()
print ('skewness',skew_gender_male)

stdev_gender_male = year_of_schooling ["1990"].std()
print ('standard deviation',stdev_gender_male)


""" Data analysis using plots """

print(genderdata.shape)