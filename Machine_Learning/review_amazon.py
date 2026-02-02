import pandas as pd 
from google_trans_new import google_translator

df = pd.read_csv('reviews.csv')
print('O numero de reviews foi: ', len(df))
linhas, colunas = df.shape
print(f'O numero de colunas são: {colunas} e linhas: {linhas}')
print(df[['title', 'rating']].head(5))
detector= google_translator()
detector.detect('Good')
