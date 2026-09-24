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

            new_corpus[i] = new_words
                

        return new_corpus
    
    def term_doc_matrix(self,docs):
        vocab = []

        for words in docs:
            for word in words:
                if word not in vocab:
                    vocab.append(word)
        vocab.sort()

        term_to_row = {}

        for row in range(len(vocab)):
            term_to_row[vocab[row]] = row

        num_terms = len(vocab)

        num_docs=len(docs)

        TDM = np.zeros((num_terms,num_docs))

        for col in range(len(docs)):
            for word in docs[col]:
                row = term_to_row[word]
                TDM[row,col] = TDM[row,col]+1

        return TDM

    


        
