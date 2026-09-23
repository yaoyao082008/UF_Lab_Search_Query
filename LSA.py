import numpy as np
from sklearn.feature_extraction.text import ENGLISH_STOP_WORDS

class LSA:
    def __init__(self,k=2):

        self.k = k 
        self.vocabulary = []
        self.U=None
        self.sigma = None
        self.vT= None
    

    def strip(self,corpus):

        new_corpus = corpus.copy()
        stop = ENGLISH_STOP_WORDS

        for i in range(len(new_corpus)):

            text = list(new_corpus[i])
            new_text=[]

            for j in range(len(text)):
                text[j] = text[j].lower()
                if text[j].isalpha() or text[j] == " ":
                    new_text.append(text[j])
            
            new_corpus[i] = "".join(new_text)

        for i in range(len(new_corpus)):

            words = new_corpus[i].split(" ")
            new_words = []

            for j in range(len(words)):
                word = words[j]

                if word not in stop:
                    new_words.append(word)

            new_corpus[i] = " ".join(new_words)



        
                

        return new_corpus
    


        
