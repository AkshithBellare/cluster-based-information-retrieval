import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import string
import re
from nltk.stem.wordnet import WordNetLemmatizer

df = pd.read_csv('.\\data.csv')
df.dropna()

ps = PorterStemmer()
lemma = WordNetLemmatizer()
punct = set(string.punctuation)
stopwords = set(stopwords.words('english'))

def clean(doc):
    processed_list = []
    stop_free = " ".join([i for i in doc.lower().split() if i not in stopwords])
    punc_free = ''.join(ch for ch in stop_free if ch not in punct)
    
    normalized_lemmatized = " ".join(lemma.lemmatize(word) for word in punc_free.split())
    processed_lemmatized = re.sub(r"\d+", "", normalized_lemmatized)
    y = processed_lemmatized.split()
    processed_list.append(y)

    normalized_stemmed = " ".join(ps.stem(word) for word in punc_free.split())
    processed_stemmed = re.sub(r"\d+", "", normalized_stemmed)
    y = processed_stemmed.split()
    processed_list.append(y)
    return processed_list

df_to_list = df.values.tolist()
for i in range(len(df_to_list)):
    cleaned = clean(df_to_list[i][1])
    df_to_list[i][1] = cleaned[0]
    df_to_list[i].append(cleaned[1])
df = pd.DataFrame(df_to_list)
df.to_csv('preprocessed-data.csv', header=['Doc Name', 'Lemmatized', 'Stemmed'])
