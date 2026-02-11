import pandas as pd
from googletrans import Translator

df = pd.read_csv('reviews.csv')
print('O numero de reviews foi: ', len(df))
linhas, colunas = df.shape
print(f'O numero de colunas são: {colunas} e linhas: {linhas}')
print(df[['title', 'rating']].head(5))
translator = Translator()
detection_result = translator.detect('Good')
print(f"Idioma detectado: {detection_result.lang}")
df['lang'] = df['title'].apply(lambda x: translator.detect(x).lang)
print(df[['title', 'rating', 'lang']])
df = df[df['lang'] == 'en']
print(len(x_train.toarray()))
print(len(x_test.toarray()))
print(len(x_train.toarray()[0]))
print(x_train.toarray())
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer

reviews = df['title'].values
ratings = df['rating'].values
reviews_train, reviews_test, y_train, y_test = train_test_split(reviews, ratings, test_size=0.2, random_state=1000)
vectorizer = CountVectorizer()
vectorizer.fit(reviews_train)
x_train = vectorizer.transform(reviews_train)
x_test = vectorizer.transform(reviews_test)

from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression()
classifier.fit(x_train, y_train)
import numpy as np
predictedTeste = classifier.predict(x_test)
predictedTreino = classifier.predict(x_train) 
accurayTreino = np.mean(predictedTreino == y_train) 
accuracy = np.mean(predictedTeste == y_test) 
print(f"Acurácia Teste: {round(accuracy,2)}")
print(f"Acurácia Treino: {round(accurayTreino,2)}")
from sklearn import metrics
import numpy as np

# Função para converter a string de rating para inteiro
def convert_rating_to_int(rating_str):
    return int(rating_str.split(',')[0])

# Converte y_test e predictedTeste para arrays numéricas
y_test_numeric = np.array([convert_rating_to_int(r) for r in y_test])
predictedTeste_numeric = np.array([convert_rating_to_int(r) for r in predictedTeste])

metrics.confusion_matrix(y_test_numeric, predictedTeste_numeric, labels=[1,2,3,4,5])
print(df.groupby('rating').size())
print(metrics.classification_report(y_test_numeric, predictedTeste_numeric, labels=[1,2,3,4,5]))