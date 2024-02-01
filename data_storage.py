# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 14:41:16 2024

@author: User
"""

"""
storing data in python
1. Lists
2. Dictionaries
3. Data frames - specific to pandas
"""
import pandas

import pandas as pd

file1 = pandas.read_csv("country_data.csv")

print(file1.head())

age1 = 30
age2 = 25
age3 = 29

age = [30,25,29,46,22]

print(age)

"""
[30,25,29,46,22]
"""

print(age[0])

"""
30
"""

print (age[1])

print(min(age))

"""
22
"""

print(max(age))

print(sum(age))

print(len(age))

"""
[30, 25, 29, 46, 22]
"""
avg = sum(age)/len(age)

print(avg)



"""
30.4
"""

g1 = "M"
g2 = "F"
g3 = "M"

gender = ["M","F","F"]

c1 = "South Africa"
c2 = "lesotho"

print(age[0:3])

"""
[30, 25, 29, 46, 22]
"""

"""
[30, 25]
"""

age.append(100)

print(age)

"""
[30, 25, 29, 46, 22, 100]
"""

print(age)
age.insert(0,100)

"""
Dictionaries - key:value pairs

cat: "a cute animal"

"""

mammals = {"cat":"a cute animal","lion":"king of the jungle","elephant":"a gigantic herbivore"}
    
               
print(mammals["cat"])

fruits =  ["apples", "banana", "orange", "grape", "kiwi"]

size_nm = [9.8, 10.1, 13.2, 8.7, 20.5]

fruit_sizes = {
    'fruits':fruits,
    'sizes':size_nm
    
    }

"""
df = dataframe
"""

import pandas

import pandas as pd

#df = dataframe

df = pd.DataFrame(fruit_sizes)

print(df['fruits'])

print(df['sizes'])

print(df['sizes'].min())

print(df['sizes'].mean())

print(df.describe())

print(df[df["sizes"]>10])

print(df[1:3])

prices = [10.00, 12.50, 16.00, 23.00, 7.00]

df['prices'] = prices

df.drop(columns=["sizes"], inplace=True)


import pandas as pd

data = {
        'age': [30, 40, 30, 49, 22, 35, 22, 46, 29, 25, 39],
        'gender':["M", "M", "F", "M", "F", "F", "F", "M", "M", "F", "M"],
        'country': ["South Africa", "Botswana", "South Africa", "South Africa", "Kenya", "Mozambique", "Lesotho", "Kenya", "Kenya", "Egypt", "Sudan"]
        }

#df = data frame

df = pd.DataFrame(data)

print(df)

print(df['age'])

print(df['gender'])

print(df['age'].min())

print(df['age'].max())

print(df['age'].mean())

print(df[df['age'] > 30])

print(df[1:4])


import pandas as pd


df['new_column'] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

print(df)

df.drop(columns=["new_column"], inplace=True)

print(df)






 

























