import pandas as pd
import os

filename = sorted(os.listdir('weekly'))[-1]
df = pd.read_csv("weekly/" + filename)
df_photo = df[['id', 'photos']].drop('photos', axis=1).join(df['photos'].str.split(",", expand=True).stack().reset_index(level=1, drop=True).rename('photo'))
#df_photo = df[['id']]#.join(df['photos'].str.split('?im_w=720,', expand=True))
df_photo.set_index('id', inplace=True)
df_photo.to_csv("weekly/" + filename[:-4] + "-photo.csv")
