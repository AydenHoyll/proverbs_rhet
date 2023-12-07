from nltk import *
from nltk.corpus import stopwords
import numpy as np
import pandas as pd
import nltk
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
from nltk.sentiment import SentimentIntensityAnalyzer
import string
from tabulate import tabulate
from docx import Document

with open('/Users/aydenhoyll/desktop/proverbs.txt', 'r') as proverb_file:
    text_file = proverb_file.read()
stopwords = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't", "n't", "'s", "'d", 'the', 'a', 'ca', 'if', "'ll", 'when']

# print(stopwords)
sentences = sent_tokenize(text_file)
english_punctuation = list(string.punctuation)
tokenized_sentences = [word_tokenize(sentence) for sentence in sent_tokenize(text_file)]
# all_words = [word.lower() for word in tokenized_words if word.lower() not in english_punctuation and word.lower() not in stopwords and word.isalpha()]
# print(english_punctuation)
all_words = [word.lower() for sentence in tokenized_sentences for word in sentence
             if word.lower() not in english_punctuation and word.lower() not in stopwords and word.isalpha()]
words_str = ' '.join(all_words)


# print('allwords', all_words) 
# freq_dist = FreqDist(all_words)
# print("Word Frequency Distribution:")
# freq_dist.plot(50, cumulative=False)
# plt.show()
# freq_dist.tabulate(50)
# print(freq_dist.tabulate(50))
print(len(sentences))
# wordcloud = WordCloud(stopwords=STOPWORDS, background_color="black", max_words=200, width=1920, height=1080).generate(words_str)
# plt.figure(1, figsize=(15,10))
# plt.clf()
# plt.imshow(wordcloud)
# plt.axis('on')
# plt.show()

# sia = SentimentIntensityAnalyzer()

# # print(sia.polarity_scores(text_file))
# sents_sentiments = [sia.polarity_scores(sentence) for sentence in sentences]

