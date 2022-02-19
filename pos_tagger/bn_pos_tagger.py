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


        train_test_cutoff = int(.80 * len(sentence