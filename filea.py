# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 12:52:23 2024

@author: user
"""

print("Your first python file")

import pandas

file = pandas.read_csv("diab_data.csv")

print(file)

print(file.info())

print(file.describe())

housing = pandas.read_csv("housing_data.csv")

housing.columns = ['A', 'B', 'C', "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N"]

housing = pandas.read_csv("housing_data.csv", )

print(housing)

print(housing.info())

print(housing.describe())

iris = pandas.read_csv("iris.csv")

print(iris)

print(iris.info())

insurance = pandas.read_csv("insurance_data.csv", skiprows=5)

print(insurance.info())

housing = pandas.read_csv("housing_data.csv")
#This command adds column names to the dataframe. 
housing.columns = ['A', 'B', 'C', "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N"]

print(housing)

print(housing.info())

print(housing.describe())

"""
Storing data in Python
1. Lists- uses square brackets to store multiple values in one object eg: colors = ["Red", "Blue", "Green"] or age = [2,4,6,8]
To access a value in the list, use its position in square brackets. The positions start from 0. so, print(colors[0]) will give Red. To get a range of values use a colon, and the last value should be the position of your last value + 1 eg print(age[0:3]) will give the values in list age in position 0,1 and 2.
You can get the descriptive statistics of lists. print(max(age)) gives the maximum value in the list named age. Can also be min for minimum,sum for the sum. 
append function adds values to the lists eg age.append(100) adds 100 to the list called age.
insert function inserts a value at a certain position in the list eg age.insert(0,100) inserts value 100 at position 0

2. Dictionaries
created using curly brackets with colons defining the variables.
mammals = {"cat":"a cute animal", "lion":"king of the jungle", "dolphin":"water based mammal"}
print(mammals["cat"])- accesses cat in the dictionary to print out its description

3. Data frames
Can be created from dictionaties.

fruit = ["apples", "kiwis", "pawpaw", "melon"]
sizes_nm = [3,4,5,6]

fruity = {"fruits":["apples", "kiwis", "pawpaw", "melon"], "sizes":[3,4,5,6]}
 
fruittty = pandas.DataFrame(fruity)

To access a column;
print(fruittty["fruits"])

To filter through data ie only show rows and columns whose sizes value is more than 4;
print(fruittty[fruittty["sizes"] > 4])

To select specific rows ie row 2 and 3;
print(fruittty[1:3])


To use data from a different directory, use the path eg: pandas.read_csv(NewDirectory/country_data.csv)
"""