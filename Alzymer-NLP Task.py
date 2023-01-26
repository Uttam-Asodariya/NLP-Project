from transformers import RobertaConfig, RobertaModel, RobertaModel, RobertaTokenizer
import pandas as pd
import numpy as np
import nltk
from sklearn.metrics.pairwise import cosine_similarity
import torch
from sentence_transformers import SentenceTransformer, util
import os, glob

roberta= SentenceTransformer('sentence-transformers/stsb-roberta-base-v2')

AD_embedding=[]
file_embedding=[]
def encodding(path): 

    for f in csv_files:
        df=pd.read_csv(f)
        df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
        for i in df['sentence']:
            embedding=roberta.encode(i)
            file_embedding.append(embedding)
            print(file_embedding)
            print('new_file')
     



path=r"C:\Users\uttam\OneDrive\Desktop\NLP Project\Data\AD"
csv_files=glob.glob(path+'/*.csv')
if __name__=='__main__':
    encodding(path)



