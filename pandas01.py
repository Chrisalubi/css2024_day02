# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 12:12:57 2024

@author: User
"""

import pandas

file1 = pandas.read_csv("country_data.csv")
print("Country Data")
print(file1.head())


file2 = pandas.read_csv("insurance_data.csv",skiprows=5)
print("Insurance Data")
print(file2)

file3 = pandas.read_csv("housing_data.csv")
print("Housing Data")
print(file3)

file4 = pandas.read_csv("diab_data.csv")
print("Diab Data")
print(file4)

file5 = pandas.read_csv("iris.csv")
print("iris")
print(file5)

















