
import pandas as pd
import numpy as np

from sqlalchemy import create_engine, text

filename = 'https://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data'


headers = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
          "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
          "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
          "peak-rpm","city-mpg","highway-mpg","price"]

dict =     {

        "Name": [

            "Braund, Mr. Owen Harris",

            "Allen, Mr. William Henry",

            "Bonnell, Miss. Elizabeth",

            "Taylor, Miss. Jane"

        ],

        "Age": [22, 35, 58, 55],

        "Sex": ["male", "male", "female", "female"],

        "Location": ["Rome", "London", "Berlin", "New York"],

    }
 
df = pd.DataFrame(dict)
print("Un dataframe creato da un dizionario Python")
print(df)
print("\n")


# STORE DATA IN PostgreSQL DB
#Set up database connection (modify with your credentials)
engine = create_engine('postgresql+psycopg://postgres:postgres@postgresql:5432/prova_db')

# Prepare una tabella
passenger_info = df[['Name', 'Sex', 'Age', 'Location']]

# Store in PostgreSQL
passenger_info.to_sql('passenger_info', engine, if_exists='replace', index=False)

print("\nData stored in PostgreSQL database")
print("\n")