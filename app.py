import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# loading dataset
df = pd.read_csv("data/Air quality dataset.csv")
print(df.head())
print(df.shape)

#cheching basic info
print(df.info())
print(df.describe())

#Convert Date Column
df['last_update'] = pd.to_datetime(df['last_update'], format="%d-%m-%Y %H:%M:%S")
print(df['last_update'].head())

# Missing Value Check
print(df.isnull().sum())

#Remove Rows Where pollutant_avg is Missing
df_clean = df.dropna(subset=['pollutant_avg'])
print("Before:", df.shape)
print("After:", df_clean.shape)

#print("States:", df_clean['state'].nunique())
print("Cities:", df_clean['city'].nunique())
print("Stations:", df_clean['station'].nunique())
print("Pollutants:", df_clean['pollutant_id'].unique())

#Basic EDA Visualizations

# 1 -Distribution of pollutant_avg for each pollutant
plt.figure(figsize=(8,5))
df_clean.boxplot(column='pollutant_avg', by='pollutant_id')
plt.title("Pollutant-wise Distribution")
plt.xlabel("Pollutant")
plt.ylabel("Average Value")
plt.suptitle("")   # to remove extra title
plt.show()

#2) Average pollutant_avg per pollutant
mean_values = df_clean.groupby('pollutant_id')['pollutant_avg'].mean()

plt.figure(figsize=(8,5))
mean_values.plot(kind='bar')
plt.title("Average Value of Each Pollutant")
plt.xlabel("Pollutant Type")
plt.ylabel("Mean Pollutant Avg")
plt.xticks(rotation=45)
plt.show()

#3) Top 10 most polluted stations (max pollutant value)
top_stations = df_clean.groupby('station')['pollutant_avg'].max().sort_values(ascending=False).head(10)

plt.figure(figsize=(10,6))
top_stations.plot(kind='bar')
plt.title("Top 10 Polluted Stations")
plt.xlabel("Station Name")
plt.ylabel("Max Pollutant Value")
plt.xticks(rotation=45, ha='right')
plt.show()

