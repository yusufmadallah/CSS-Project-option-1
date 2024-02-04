#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 20:34:48 2024

@author: yusuf
"""

import pandas as pd

# Load the dataset
file_path = "/home/yusuf/movies/movie_dataset.csv" 
df = pd.read_csv(file_path)

df.columns = df.columns.str.replace(' ', '_')

df.fillna(df.mean(), inplace=True)
df.dropna(inplace=True)
summary_stats = df.describe()
print(summary_stats)

df.to_csv("cleaned_movie_dataset.csv", index=False)

file_path = "/home/yusuf/movies/cleaned_movie_dataset.csv"  
df = pd.read_csv(file_path)
highest_rated_movie = df.loc[df['Rating'].idxmax()]
print("Highest Rated Movie:")
print(highest_rated_movie[['Title', 'Rating']])

file_path = "/home/yusuf/movies/cleaned_movie_dataset.csv" 
df = pd.read_csv(file_path)

average_revenue = df['Revenue_(Millions)'].mean()

print("Average Revenue of All Movies:", average_revenue)

file_path = "/home/yusuf/movies/cleaned_movie_dataset.csv"  
df = pd.read_csv(file_path)

df['Year'] = pd.to_datetime(df['Year'], format='%Y')

filtered_df = df[df['Year'].dt.year.isin([2015, 2016, 2017])]

average_revenue_2015_2017 = filtered_df['Revenue_(Millions)'].mean()


print("Average Revenue of Movies from 2015 to 2017:", average_revenue_2015_2017)

file_path = "/home/yusuf/movies/cleaned_movie_dataset.csv"  
df = pd.read_csv(file_path)

df['Year'] = pd.to_datetime(df['Year'], format='%Y')

movies_2016 = df[df['Year'].dt.year == 2016]
num_movies_2016 = movies_2016.shape[0]


print("Number of Movies Released in 2016:", num_movies_2016)

file_path = "/home/yusuf/movies/cleaned_movie_dataset.csv"  
df = pd.read_csv(file_path)


nolan_movies = df[df['Director'] == 'Christopher Nolan']

num_nolan_movies = nolan_movies.shape[0]


print("Number of Movies Directed by Christopher Nolan:", num_nolan_movies)

file_path = "/home/yusuf/movies/cleaned_movie_dataset.csv"  
df = pd.read_csv(file_path)
high_rated_movies = df[df['Rating'] >= 8.0]

num_high_rated_movies = high_rated_movies.shape[0]

print("Number of Movies with a Rating of at Least 8.0:", num_high_rated_movies)


file_path = "/home/yusuf/movies/cleaned_movie_dataset.csv"  
df = pd.read_csv(file_path)


nolan_movies = df[df['Director'] == 'Christopher Nolan']


median_rating_nolan_movies = nolan_movies['Rating'].median()

print("Median Rating of Movies Directed by Christopher Nolan:", median_rating_nolan_movies)

file_path = "/home/yusuf/movies/cleaned_movie_dataset.csv"  
df = pd.read_csv(file_path)

average_rating_by_year = df.groupby('Year')['Rating'].mean()

year_highest_average_rating = average_rating_by_year.idxmax()

print("Year with the Highest Average Rating:", year_highest_average_rating)

file_path = "/home/yusuf/movies/cleaned_movie_dataset.csv"  
df = pd.read_csv(file_path)

df['Year'] = pd.to_datetime(df['Year'], format='%Y')


movies_2006_2016 = df[df['Year'].dt.year.isin(range(2006, 2017))]


num_movies_2006 = movies_2006_2016[df['Year'].dt.year == 2006].shape[0]
num_movies_2016 = movies_2006_2016[df['Year'].dt.year == 2016].shape[0]

percentage_increase = ((num_movies_2016 - num_movies_2006) / num_movies_2006) * 100

print("Percentage Increase in Number of Movies between 2006 and 2016:", percentage_increase)

file_path = "/home/yusuf/movies/cleaned_movie_dataset.csv"  
df = pd.read_csv(file_path)
all_actors = df['Actors'].str.split(', ', expand=True)

all_actors_long = all_actors.melt(value_name='Actor').dropna()['Actor']

most_common_actor = all_actors_long.value_counts().idxmax()

print("Most Common Actor in All Movies:", most_common_actor)


file_path = "/home/yusuf/movies/cleaned_movie_dataset.csv"  
df = pd.read_csv(file_path)

all_genres = df['Genre'].str.split(', ', expand=True)

all_genres_long = all_genres.melt(value_name='Genre').dropna()['Genre']

num_unique_genres = all_genres_long.nunique()

print("Number of Unique Genres in the Dataset:", num_unique_genres)

file_path = "/home/yusuf/movies/cleaned_movie_dataset.csv"  
df = pd.read_csv(file_path)

numerical_features = df.select_dtypes(include=['float64', 'int64'])

correlation_matrix = numerical_features.corr()
print("Correlation Matrix:")
print(correlation_matrix)
insight_1 = "Positive correlation between X1 and X2 indicates a potential relationship."
insight_2 = "Negative correlation between X3 and X4 suggests an inverse relationship."
insight_3 = "Close to zero correlation between X5 and X6 implies a weak linear relationship."
insight_4 = "High correlation between X7 and X8 suggests a strong linear relationship."
insight_5 = "Correlation does not imply causation; further analysis is needed to establish causative relationships."

print("\nInsights:")
print(insight_1)
print(insight_2)
print(insight_3)
print(insight_4)
print(insight_5)
