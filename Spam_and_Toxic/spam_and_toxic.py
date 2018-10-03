import sys
import pickle
import string
import nltk
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer

classifier = pickle.load(open('one_vs_rest_classifier.pkl', 'rb'))
vectorizer = pickle.load(open('vectorizer.pkl', 'rb'))

del_symbols = ['«', '»', '®', '´', '·', 'º', '½', '¾', '¿', '¡', '§', '£', '₤']


def remove_punc(txt):
    plain_txt = (ch for ch in txt if(
        ch not in string.punctuation and ch not in string.digits and ch not in del_symbols))
    plain_txt = ''.join(plain_txt)
    return plain_txt


def text_process(mess):
    '''
    Removing the punctuations
    Removing the common words 
    Returning the cleaned words
    '''
    nopunc = [char for char in mess if char not in string.punctuation]

    nopunc = ''.join(nopunc)

    return [word for word in nopunc.split() if word.lower() not in stopwords.words('english')]


spam_pipeline = pickle.load(open('spam_pipeline.pkl', 'rb'))

spam_input = user_input = sys.argv[1]
print(spam_input)
# For spam
spam_input = spam_input.rstrip()
f_user_msg = pd.Series(data=spam_input, index=[len(spam_input)])
result_spam = spam_pipeline.predict(f_user_msg)[0]
# print('\n---SPAM STATUS---\n')
if result_spam == 'spam':
    print('THE MESSAGE IS A SPAM ')
else:
    print('THE MESSAGE IS NOT A SPAM ')


# For toxicity
# user_input = remove_punc(user_input)
# user_input = pd.Series(user_input)
# user_input = vectorizer.transform(user_input)
# result = classifier.predict(user_input)
# # print(result[0],'\n')
# print('\n---TOXICITY STATUS---\n')
# count = 0
# if 1 not in result:
#     print("comment is fine")

# if(result[0][0] == 1):
#     print('Toxic')
# if(result[0][1] == 1):
#     print('severe toxic')
# if(result[0][2] == 1):
#     print('obscene')
# if(result[0][3] == 1):
#     print('threat')
# if(result[0][4] == 1):
#     print('insult')
# if(result[0][5] == 1):
#     print('identity hate')
