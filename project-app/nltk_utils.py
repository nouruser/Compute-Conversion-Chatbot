import nltk
from nltk.stem.porter import PorterStemmer 
import numpy as np
# nltk.download('punkt')


stemmer=PorterStemmer()
def tokenize(sentence):
    return nltk.word_tokenize(sentence)

def stem(word):
     return stemmer.stem(word.lower())

def bag_of_words(token,all_words):
    tokenize_sentence=[stem(w) for w in token]
    bag=np.zeros(len(all_words),dtype=np.float32)
    for idx ,w in enumerate(all_words):
        if w in tokenize_sentence:
            bag[idx]=1.0
    return bag

# print (stem("cooking"))