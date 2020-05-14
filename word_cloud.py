#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 12 16:28:24 2020

@author: ornwipa
"""

import os
import re
import string
from wordcloud import WordCloud
import nltk
# nltk.download('stopwords')
import matplotlib.pyplot as plt

def readText():
    ''' read text file, one file per one item in the list '''
    extractedText = []
    filepath = 'text'
    for filename in os.listdir(filepath):
        file = open(filepath + '/' + filename, 'r')
        extractedText.append(file.read())
        file.close()
    return extractedText

def splitParts(text):
    ''' this function is specific to the book L’ÉTRANGER,
    split between PREMIÈRE PARTIE et DEUXIÈME PARTIE,
    return a list of two elements of string '''
    tokens = text.split()
    for index in range(len(tokens)):
        if tokens[index] == 'PREMIÈRE':
            beg1 = index + 3
        if tokens[index] == 'DEUXIÈME':
            end1 = index
            beg2 = index + 3
        if tokens[index] == 'électronique': # the end of the ebook
            end2 = index - 5 
            break
    return [' '.join(tokens[beg1:end1]), ' '.join(tokens[beg2:end2]) ]

def splitParagraphs(text):
    ''' \n is a line break as read (not new paragraph), so should be kept together;
    \n\n is a new paragraph, so will be used as splitting indicator;
    \n\n\n is a page break in the book (not new paragraph), so should be together '''
    text = text.replace('\n\n\n', ' ') # connect the page break as entire text
    textList = []
    beg_index = 1
    for char in range(len(text) - 2):
        if text[char] == '\n' and text[char+1] == '\n':
            end_index = char
            textList.append(text[beg_index:end_index])
            beg_index = char + 2
        if beg_index > len(text):
            break        
    return textList # total of 221 paragraphs in the book
    
def processText(text):
    ''' text is a string type, make all characters lowercase, 
    remove '\n' of new paragraph (not necessary for one paragraph text),
    remove all punctuations, non-alphabets, and extra space '''
    text = text.lower()
    text = text.replace('\n', ' ')
    text = text.translate(str.maketrans('','',string.punctuation))
    text = re.sub(' +', ' ', text)
    return text

def removeWords(text):
    ''' split the entire text into a list of one words '''
    tokens = text.split() # fulltext has 31997 words     
    ''' define and manually remove french stopwords '''
    arrêt = set(nltk.corpus.stopwords.words('french')) # 'stopwords' en français
    tokens_wo_arrêt = []
    for token in tokens:
        if (token not in arrêt):
            tokens_wo_arrêt.append(token)
    cloudText = ' '.join(tokens_wo_arrêt) # for the whole book, 18645 words left
    return cloudText

def wordcloudFromOneWord():
    ''' pre-process input text '''
    textList = readText()
    for text in textList:
        [part1, part2] = splitParts(text)
    [part1processed, part2processed] = [processText(part1), processText(part2)]    
    [cloudtext1, cloudtext2] = [removeWords(part1processed), removeWords(part2processed)]
    ''' create word clouds, separate between two parts '''
    arrêt = set(nltk.corpus.stopwords.words('french')) # 'stopwords' en français
    cloud1 = WordCloud(background_color = "white", max_words = 200, stopwords = arrêt).generate(cloudtext1)
    part1 = cloud1.to_array()
    plt.figure()
    plt.title("PREMIÈRE PARTIE")
    plt.imshow(part1, interpolation="bilinear")
    plt.axis("off")
    plt.show()
    cloud2 = WordCloud(background_color = "white", max_words = 200, stopwords = arrêt).generate(cloudtext2)
    part2 = cloud2.to_array()
    plt.figure()
    plt.title("DEUXIÈME PARTIE")
    plt.imshow(part2, interpolation="bilinear")
    plt.axis("off")
    plt.show()


if __name__ == "__main__":
    wordcloudFromOneWord()
