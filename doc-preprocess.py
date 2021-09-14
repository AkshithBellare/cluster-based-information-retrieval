import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import string
import re
from nltk.stem.wordnet import WordNetLemmatizer

df = pd.read_csv('.\\data.csv')
df.dropna()

def clean(doc):
    stop_free = " ".join([i for i in doc.lower().split() if i not in stopwords])
    punc_free = ''.join(ch for ch in stop_free if ch not in punct)
    
    normalized = " ".join(lemma.lemmatize(word) for word in punc_free.split())
    processed = re.sub(r"\d+", "", normalized)
    y = processed.split()
    return y

stem = PorterStemmer()
lemma = WordNetLemmatizer()
punct = set(string.punctuation)
stopwords = set(stopwords.words('english'))

df_to_list = df.values.tolist()
for i in range(len(df_to_list)):
    cleaned = clean(df_to_list[i][1])
    df_to_list[i][1] = cleaned
df = pd.DataFrame(df_to_list)
df.to_csv('preprocessed-data.csv')
