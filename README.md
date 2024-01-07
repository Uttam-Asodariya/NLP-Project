## Table of Contents
- [Description](#Description)
- [Getting Started](#Getting-Started)
- [Methodology](#Methodology)
  - [Dataset](#Dataset)
  - [Pre-processing](#pre-processing)
  - [Roberta model](#roberta-model)
  - [Classification Model](#classification-model)
  - [Disclaimer](#disclaimer)


# Description
- Nowadays, natural language processing (NLP) has become a hot topic of research as it is useful in text processing. NLP can also be used in word embedding. where the representation of words becomes a vector of real numbers. It is multidimensional, and good model values lie between 50 and 500. There are also different methods for word embedding. EX:Bag of Word, TF-IDF, Word2Vec, GloVe, Transformer, BERT

- BERT has an advantage compared to other methods. Bert creates word representations that are dynamically informed by their surrounding words. On the other hand, methods like Word2Vec have only similar representations for words.

- Let's take an example. 1) The new lamp had good light for reading.
                         2) Magnesium is a light metal.

- Here, Word2Vec create same embedding for "light" word, Whereas the meaning is different. On the other hand, BERT creates varying embeddings for each sentence. Therefore, BERT word embedding captures good information about content that results in more accurate feature representations, which in the end helps the model perform better.

- This project mostly focused on the word embedding of sentences of an Alzheimer's patient by using Roberta, which is a variation of BERT. Classification can be done by using these embeddings.


# Getting Started
- For this task, the following basic Python libraries are required: In addition, it is important to load a Word embedding model such as Roberta, Electra, and so on.

- 1.[Pandas](https://pandas.pydata.org/docs/)
- 2.[Numpy](https://numpy.org/doc/stable/)
- 3.[Pytorch](https://pytorch.org/tutorials/)
- 4.[Sklaern](https://scikit-learn.org/stable/user_guide.html)
- 5.[Hugging Face](https://huggingface.co/docs)
- 6.[Scipy](https://docs.scipy.org/doc/scipy/)


# Methodology

## Dataset

- There are two different formats for datasets. The first is a description of a cookie theft picture, and the second is a patient health report. These two datasets were collected based on AD (Alzheimer Disease) and HC (Healthy Control).

## Pre-processing

- For the classification task, we take the first type of data. Where each csv file contains a sentence. We need to combine sentences from each of the csv files for AD and HC. So we can process further. Meanwhile also add extra column about label so easily can be identified sentence origin.

- Note: For the test set, we cannot take mixed sentences from different files. So initially, we isolated 20% of the csv files into a newly created test folder.


## Word Embedding: Roberta Model 
- Now, tokenizers help tokenize the words of each sentence and use the Roberta model to convert each tokenized sentence to get the word embedding of it. The architecture of the Roberta model is as follows: Base: Number of transformer blocks: 12, Hidden layer size: 768, Attention heads: 12. The total length of each token embedding is 768. Robrta has 12 layers, so there are a total of 12 different representations of each token with 768 bytes.


- The sum of the last six encoders gives good word embedding. This can be deduced by trying a couple of combinations. Currently there is 47*768; 47 is words/tokens in sentence. Mean/Entropy is useful to convert 47*768 dim tensor to 1*768 .

 ```
 tokenizer=RobertaTokenizer.from_pretrained('roberta-base')
 ```

 ```
 Roberta= RobertaModel.from_pretrained('roberta-base',output_hidden_states=True)
 ```
 
 ## Classification Model
 - These word embeddings can be used for our classification task. We already have our dataset split into trains and tests. Good classification model can be identified by evaluating couple of models on test set. A  AdaBoostClassifier is useful in this uncertain environment.

 ```
Classification_model = AdaBoostClassifier(n_estimators=100, random_state=0)
model = make_pipeline(MinMaxScaler(), Classification_model)
 ```
- Model result can be observed by using metrics of accuracy score.
```
 metrics.accuracy_score(y_test,y_pred)

 #Accuracy: ~ 57%
```
# Feature Importance

- Analysis.ipynb notebook is the second part of this project. where the second data type is used. The dataset is located in the Data folder with the names AD-Description and HC-Description. The same methods previously mentioned were used for classification, including cross-validation.

- Using the permutation importance library, connected parameters with Alzeihmer can be observed. In addition, scatter plots provide important visualizations relating to AD and HC.

```
# Accuracy: ~ 90%

# output of weight Permutation importance
Weight         | Feature
0.4681 ± 0.1132| MMSE_Pitt
0.0585 ± 0.0117| Age
```

# Disclaimer
- The notebook is created based on current information and available sources. There are still chances for improvement in the future. Any feedback regarding this notebook is more than welcome.