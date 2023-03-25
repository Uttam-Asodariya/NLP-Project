## Description
- Nowadays, Natural language processing(NLP) become hot topic of research, as it is useful in text processing. NLP has a also useful to transfer word to vector. It is known as word embedding.  In this project focused mostly on word embedding of alzheimer disease. we convert sentences of alzheimers'patient to vector. Classification can be done by using these embeddings.

## Getting Started
- For this task, the basic following python libraries are required.

1.[pandas](https://pandas.pydata.org/docs/)
2.[Numpy](https://numpy.org/doc/stable/)
3.[pytorch]()


## The word embedding

Where representation of words into vector of real numbers.
It is multidimensional and good model values lies between length of 50-500.
There are also different methods for word embedding. EX:Bag of Word, TF-IDF, Word2Vec, GloVe, Transformer, Bert

##Motivation

BERT has an advantage compared to other methods. BERT create word reperentation dynamically informed by it's surrounded words. On the other hand, methods like Word2Vec have only similar represenataion for words.

Let's take example. 1) "The new lamp had good light for reading"
                    2) "Magnesium is a light metal.

Here, Word2Vec create same embedding for "light" word, Whereas the meaning is different. On the otherhand BERT
create vary embedding for each sentence. Therefor BERT word embedding capture good information about content that result in more accurate feature representations, which in the end help to performe model better. 

##Model Description
: Base: Number of transformers block:12, Hidden layer size:768, Attention heads:12
        Large:

Bert need special kind of input format, with special tokens to mark beginnnin([CLS]) and seperation/end ([SEP])