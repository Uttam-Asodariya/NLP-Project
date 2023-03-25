## Table of Contents
- [Description](#Description)
- [Getting Started](#Getting-Started)
- [Methodology](#Methodology)
  - [Dataset](#Dataset)


# Description
- Nowadays, Natural language processing(NLP) become hot topic of research, as it is useful in text processing. NLP can also be used in word embedding. Where representation of words into vector of real numbers. It is multidimensional and good model values lies between length of 50-500.
There are also different methods for word embedding. EX:Bag of Word, TF-IDF, Word2Vec, GloVe, Transformer, Bert.

- BERT has an advantage compared to other methods. BERT create word reperentation dynamically informed by it's surrounded words. On the other hand, methods like Word2Vec have only similar represenataion for words.

  Let's take example. 1) "The new lamp had good light for reading"
                    2) "Magnesium is a light metal.

- Here, Word2Vec create same embedding for "light" word, Whereas the meaning is different. On the otherhand BERT create vary embedding for each sentence. Therefor BERT word embedding capture good information about content that result in more accurate feature representations, which in the end help to performe model better. 

- This project mostly focused on word embedding of sentences of alzheimers' patient  by using Roberta which is variation of BERT.  Classification can be done by using these embeddings.


# Getting Started
- For this task, the basic following python libraries are required. In addition installation of Hugging Face is important to load Word embedding model such as Roberta, Electra, so on.

- 1.[Pandas](https://pandas.pydata.org/docs/)
- 2.[Numpy](https://numpy.org/doc/stable/)
- 3.[Pytorch](https://pytorch.org/tutorials/)
- 4.[Sklaern](https://scikit-learn.org/stable/user_guide.html)
- 5.[Hugging Face](https://huggingface.co/docs)
- 6.[Scipy](https://docs.scipy.org/doc/scipy/)


# Methodology

## Dataset

- There is two different format of datasets. Firstly, AD(Alzheimer Disease) and HC(Healthy Control). These two dataset contains excel files according patients id, which contains description of the 'Cookie theft' picture.

- On the other hand, there is also two csv files namely AD-Description and HC-Desciption which contains description of these patients.

## Pre-processing

- For classification task we take first type of data. Where each csv file contains sentences. We need to combine sentences from each csv files of AD and HC. So we can process further. Meanwhile also add column about label so easily can be identified sentence origin.

- Note: For test set, we can not take mixed senteces from different patients. So initially we store 20% csv files of total file into newly created testing folder.


## Roberta Model 
 - Now, tokenizer help to tokenize words of each sentence and use the roberta model to convert each tokenized sentence to get word embedding of it. Base: Number of transformers block:12, Hidden layer size:768, Attention heads:12. Total length of each token embedding is 768. Robrta has 12 layer so there is total 12 differnt representations of each token with 768 length. 

 - Sum of last six encoder gives good word embedding. This can be deduced by trying couple of combination. Currently there is n*768; n is words in sentence. Entropy is useful to convert n dim to 1*768. 

 '''
 tokenizer=RobertaTokenizer.from_pretrained('roberta-base')
 '''

 '''
 Roberta= RobertaModel.from_pretrained('roberta-base',output_hidden_states=True)
 '''
 ## Classification Model
 - These word embedding can be used for our classification task. We already have our dataset splited into train and test. Good classification model can be identified by evaluating couple of models on test set. Model result can be observed by using metrics of accuracy score.

 '''
 Gaussian = GaussianProcessClassifier(kernel=1.0 * RBF(0.7),random_state=0,max_iter_predict=500)
 '''

 '''
 metrics.accuracy_score(y_test,y_pred)

 #output: 0.65
 '''

# Desclaimer
- The notebook is created based on current information and available sources. There is still chances of improvment in the future. Any feedback regarding this note book is morethan welcome.