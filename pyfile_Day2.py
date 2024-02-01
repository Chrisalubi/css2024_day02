# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 09:51:41 2024

@author: User
"""

import pandas as pd

file = pd.read_csv("iris.csv")

file = pd.read_csv("data_02/iris.csv")

file = pd.read_csv("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data")

url = ("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data")


column_names = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class']

file = pd.read_csv(url, header=None, names = column_names)

df = pd.read_csv("data_02/Geospatial Data.txt",sep=";")

file = pd.read_excel("residentdoctors.xlsx")

print(file)

file = pd.read_json("data_02/student_data.json")

print(file)



# df = dataframe

# df = pd.read_csv(url)

# print(df.info())
# print(df.describe())




"""
Working with dates

10-01-2024 - UK

01-10-2024 - US

"""

df = pd.read_csv("time_series_data.csv",index_col=0)

print(df.info())

# df['Date'] = pd.to_datetime(df['Date'], formart="%d-%m-%Y")

df['Date'] = pd.to_datetime(df['Date'])

# df['Date'] = pd.to_datetime(df['Date'], formart="%d-%m-%Y")

print(df.info())

df['Year'] = df['Date'].dt.year


df = pd.read_csv("patient_data_dates.csv")

df = pd.read_csv("patient_data_dates.csv", index_col=0)

df.drop(index=26, inplace=True)

df['Date'] = pd.to_datetime(df['Date'])

print(df.info())

avg_cal = df["Calories"].mean()

df["Calories"].fillna(avg_cal, inplace=True)


"""
Best practice
"""

df.dropna(inplace = True)

df = df.reset_index(drop=True)

#df.loc[7, 'duration'] = 45

df['Duration'] = df['Duration'].replace([450], 50)

print(df)

# pd.set_option('display.max_rows',None)

##########################################


df = pd.read_csv("iris.csv")


df["sepal_length_sq"] = df["sepal_length"]**2

df["sepal_length_sq_2"] = df["sepal_length"].apply(lambda x: x**2)

##################################

df1 = pd.read_csv("data_02/person_split1.csv")
df2 = pd.read_csv("data_02/person_split2.csv")

df = pd.concat([df1, df2], ignore_index=True)

###################################

df1 = pd.read_csv('data_02/person_education.csv')
df2 = pd.read_csv('data_02/person_work.csv')

# inner join

#df_merge = pd.merge(df1,df2,on='id')

#df_merge = pd.merge(df1, df2, on='id', how='outer')

print(df)

df = pd.read_csv("iris.csv")



url = "https://raw.githubusercontent.com/alexandrehsd/Predicting-Pulsar-Stars/master/pulsar_stars.csv"

df = pd.read_csv(url)

df.to_csv("data_02/output/iris_data_cleaned.csv")










































































