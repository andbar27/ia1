#!/usr/bin/env python3
# -*- coding: utf-8 -*-
print(
"""
Created on Mon Mar 31 15:31:24 2025

@author: stefano
"""
)

# Importare librerie necessarie
import pandas as pd

import os
# Get the directory where the script is located
script_dir = os.path.dirname(os.path.abspath(__file__))
# Construct the path to the data file
# data_path = os.path.join(script_dir, '../dati/SomeMusicAlbums.csv')
# df = pd.read_csv(data_path)

# print("ho letto il csv")
# print("df: \n", df.describe())
# # # Leggi data da un file CSV in un dataframe
# # df = pd.read_csv("../dati/SomeMusicAlbums.csv")
titanic = pd.read_csv("../dati/titanic.csv")
print("\n\nage.describe(): \n", titanic.Age.describe().head(2).tail(1))
print("\n\nsettimo dalla fine: \n", titanic.tail(7).head(1).Name)

print("\n\nage mean(): \n", titanic.Age.describe().iloc[[2]])
print("\n\nsettimo dalla fine: \n", titanic.iloc[[-7]].Name)

print("\n\nage mean(): \n", titanic.Age.describe().iloc[2])
print("\n\nsettimo dalla fine: \n", titanic.iloc[-7].Name)

titanic.set_index('Name', inplace=True)
print("\n\nkeys: \n", titanic.index)
print("\n\nCerca per nome\n", titanic.loc[['Dooley, Mr. Patrick']])


condition = titanic["Age"] > 40
print(condition)
print(type(condition))
print(titanic[condition])
print(type(titanic[condition]))
condition2 = titanic["Name"].cont
# # Scrvi la struttura del dataframe
# print(df.dtypes)

# # Scrvi le prime 5 righe del dataframe
# #df.head()

# # Valori unici in una colonna
# df_u = df['Released'].unique() 
# print(df_u)
# print(df_u.size)

# # Accesso alle colonne
# #x = df[['Artist','Genre','Length']]
# #x
# x = df[['Artist']] 
# # x = df['Artist']
# print(x)
# print(type(x))

# # Accesso alle righe
# print(df.loc[1])
# print(type(df.loc[0]))
# print(type(df.loc[[0]]))

# # Accesso ai valori di singole celle (incrocio riga, colonna)
# print(df.iloc[0,2])
# print(df.iloc[1,2])
# print(df.iloc[[0,2],[1,2]])
# print(df.iloc[0, 0])
# print(df.iloc[0])

# # Affettare un DataFrame
# iloc uses integer-based indexing (position-based)
# loc uses label-based indexing
# Row Selection:
#     iloc[0:2] → Rows 0 and 1 (excludes 2)
#     loc[0:2] → Rows 0, 1, and 2 (includes 2)
# Column Selection:
#     iloc[0:3] → Columns at positions 0, 1, 2 (all columns in this case)
#     loc['Name':'Sex'] → Columns from Name to Sex (also all columns here)
# print(df.loc[0:2])
# print(type(df.loc[0:2]))
# print(df.iloc[0:2, 0:3])
# print(df.loc[0:2, 'Artist':'Released'])

# # Esportazione del dataframe in un dizionario
# #print(df.to_dict())



