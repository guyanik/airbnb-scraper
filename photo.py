import os
import pandas as pd

filename = sorted(os.listdir('weekly'))[-1]
df = pd.read_excel("weekly/" + filename)

df.drop_duplicates(subset='id', inplace = True)
print(len(df["id"]))

df = df.replace('\u2028', ' ', regex=True).replace('\u2029', ' ', regex=True)
df = df.replace('\n', ' ', regex=True).replace('\r', ' ', regex=True).replace('\r\n', ' ', regex=True)

# create and save a file with reviews and IDs
df_reviews = df[['id', 'reviews']].drop('reviews', axis=1).join(df['reviews'].str.split("f07dy8y53xri9yk7zkin", expand=True).stack().reset_index(level=1, drop=True).rename('reviews'))
df_reviews[['text', 'date', 'language', 'score', 'response']] = df_reviews['reviews'].str.split("l1tl05cdej5bvhx5ypsr", expand=True)
df_reviews['id'] = df_reviews['id'].astype(str)
df_reviews = df_reviews.drop(['reviews'], axis=1)
df_reviews.to_csv("weekly/" + filename[:-5] + "-reviews.csv", index = False)
print(df_reviews.dtypes)

# create and save a file with only photos and IDs
df_photos = df[['id', 'photos']].drop('photos', axis=1).join(df['photos'].str.split(",", expand=True).stack().reset_index(level=1, drop=True).rename('photo'))
df_photos['id'] = df_photos['id'].astype(str)
df_photos.to_csv("weekly/" + filename[:-5] + "-photos.csv", index = False)
print(df_photos.dtypes)

# save the file without reviews and photos
df = df.drop(['photos'], axis=1)
df['id'] = df['id'].astype(str)
df.to_csv("weekly/" + filename[:-5] + "-clean.csv", index = False)
print(df.dtypes)
