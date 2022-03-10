# Bangla Natural Language Toolkit: Parts of Speech Tagger
#
# Copyright (C) 2019 BNLTK Project
# Author: Ashraf Hossain <asrafhossain197@gmail.com>



import string
import numpy as np
from keras.models import load_model
from sklearn.feature_extraction import DictVectorizer
from sklearn.preprocessing import LabelEncoder

import platform
import getpass
import sys

import logging
logging.getLogger('tensorflow').disabled = True

import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'


class PosTagger:
    
    def __init__(self):
        pass
    
    dict_vectorizer = None
    label_encoder = None
    model = None

    def loader(self):
        global dict_vectorizer
        global label_encoder
        global model

        model_path = None
        tagged_data_path = None

        if platform.system() == 'Windows':
            model_path = "C:\\Users\\"+getpass.getuser()+"\\bnltk_data\\pos_data\\keras_mlp_bangla.h5"
            tagged_data_path = "C:\\Users\\"+getpass.getuser()+"\\bnltk_data\\pos_data\\bn_tagged_mod.txt"
        else:
            model_path = "/Users/"+getpass.getuser()+"/bnltk_data/pos_data/keras_mlp_bangla.h5"
            tagged_data_path = "/Users/"+getpass.getuser()+"/bnltk_data/pos_data/bn_tagged_mod.txt" 

        model = load_model(model_path)
        model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
        #new_file = 'bn_tagged_mod.txt'
        texts = open(tagged_data_path, encoding='utf8').readlines()
        sentences = []
        for i in texts:
            sentences.append(self.tuple_maker(i))

        #print(sentences[0])


        train_test_cutoff = int(.80 * len(sentences)) 
        training_sentences = sentences[:train_test_cutoff]
        testing_sentences = sentences[train_test_cutoff:]

        train_val_cutoff = int(.25 * len(training_sentences))
        validation_sentences = training_sentences[:train_val_cutoff]
        training_sentences = training_sentences[train_val_cutoff:]

        X_train, y_train = self.transform_to_dataset(training_sentences)
        X_test, y_test = self.transform_to_dataset(testing_sentences)
        X_val, y_val = self.transform_to_dataset(validation_sentences)

        dict_vectorizer = DictVectorizer(sparse=False)
        dict_vectorizer.fit(X_train + X_test + X_val)

        label_encoder = LabelEncoder()
        label_encoder.fit(y_train + y_test + y_val)

    def tuple_maker(self, line):
        sentence = []
        line = line.split(' ')

        for x in line:

            if x == '':
                print("Yess")
            else:
                x = x.split('\\')
                tup = []
                for y in x:
                    tup.append(y);
                sentence.append(tuple(tup))    

        return sentence

    def tokenizer(self, input_):

        mod_elements = []

        words = input_.split(' ')
        words = [x.strip(' ') for x in words] 
        words = [i for i in words if i] 

        dict_ = {}
        dict_['।'] = True

        for p in string.punctuation:
            dict_[p] = True

        for n in words:
            if dict_.get(n[-1]):
                mod_elements.append(n[:-1])
                mod_elements.append(n[-1])
            else:
                mod_elements.append(n)
        mod_elements = [i for i in mod_elements if i]
        return mod_elements     

    def add_basic_features(self, sentence_terms, index):

        term = sentence_terms[index]
        return {
            'nb_terms': len(sentence_terms),
            'term': term,
            'is_first': index == 0,
            'is_last': index == len(sentence_terms) - 1,
            'prefix-1': term[0],
            'prefix-2': term[:2],
            'prefix-3': term[:3],
         