from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from collections import Counter
import pandas as pd
import time

# data = "Este es un ejemplo de remocion de palabras a ver que pasa con las palabras y la remocion"
articles = pd.read_csv("articles1.csv", usecols=[1,2,9])
ids = articles['id'].values
titles = articles['title'].values
content = articles['content'].values
stopWords = set(stopwords.words('english'))
index = {}
sub_index = {}
start = time.time()
for r in range(len(ids)):
        data = titles[r].lower() + content[r].lower()
        words = word_tokenize(data)
        wordsFiltered = []
        
        for w in words:
                if w not in stopWords and len(w)!=1:
                        wordsFiltered.append(w)
        c = Counter(wordsFiltered) 
        for s,r in c.items():
                sub_index[s] = r
        index[ids[r]]=sub_index
        sub_index={}
        data = ""
end =time.time()
print(index[17284])
print(end-start)
