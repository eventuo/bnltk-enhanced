# Bangla Natural Language Toolkit: Parts of Speech Tagger
#
# Copyright (C) 2019 BNLTK Project
# Author: Ashraf Hossain <asrafhossain197@gmail.com>


from keras.models import load_model
from string import punctuation
import numpy as np
from sklearn.feature_extraction import DictVectorizer
from sklearn.preprocessing import LabelEncoder
import platform
import getpass
import os
import sys

import logging
logging.getLogger('tensorflow').disabled = True

import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'


class Loader:

	texts = ''
	sentences = []
	model = ''

	model_path = None
	tagged_data_path = None

	def __init__(self):
		self.texts = ''
		self.sentences = []
		self.model = None
		self.model_path = None
		self.tagged_data_path = None

	def path_generator(self):

		isFiles_exist = True

		if platform.system() == 'Windows':
		    self.model_path = "C:\\Users\\"+getpass.getuser()+"\\bnltk_data\\pos_data\\keras_mlp_bangla.h5"
		    self.tagged_data_path = "C:\\Users\\"+getpass.getuser()+"\\bnltk_data\\pos_data\\bn_tagged_mod.txt"
		else:
		    self.model_path = "/Users/"+getpass.getuser()+"/bnltk_data/pos_data/keras_mlp_bangla.h5"
		    self.tagged_data_path = "/Users/"+getpass.getuser()+"/bnltk_data/pos_data/bn_tagged_mod.txt" 
			

	def load_keras_model(self):

		self.path_generator()

		self.model = load_model(self.model_path)
		self.model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

		self.load_corpus()
		self.data_manipulator()

	def load_corpus(self):
		#file = '/Users/ashrafhossain/bnltk_data/pos_data/bn_tagged_mod.txt'
		self.texts = open(self.tagged_data_path, encoding="utf8").readlines()

	def tuple_maker(self, line):
	    line = line.split(' ')
	    sentence = []
	    
	    for x in line:
	        
	        if x == '':
	            continue
	        else:
	            x = x.split('\\')
	            tup = []
	            for y in x:
	                tup.append(y);
	            sentence.append(tuple(tup))
	    return sentence            

	def data_manipulator(self):
		for i in self.texts:
			self.sentences.append(self.tuple_maker(i))


class BanglaPosTagger:

	sentences = []
	mod_elements = []
	model = ''
	dict_vectorizer = None
	label_encoder = None


	def __init__(self):
		self.sentences = []
		self.mod_elements = []
		self.model = ''
		self.dict_vectorizer = DictVectorizer(sparse=False)
		self.label_encoder = LabelEncoder()

	def load(self):

		loader_ = Loader()
		loader_.load_keras_model()
		self.model = loader_.model
		self.sentences = loader_.sentences
		#print(self.sentences[0])
		#print(self.mod_elements)


		train_test_cutoff = int(.80 * len(self.sentences))
		training_sentences = self.sentences[:train_test_cutoff]
		testing_sentences = self.sentences[train_test_cutoff:]
		train_val_cutoff = int(.25 * len(training_sentences))
		validation_sentences = training_sentences[:train_val_cutoff]
		training_sentences = training_sentences[train_val_cutoff:]

		X_train, y_train = self.transform_to_dataset(training_sentences)
		X_test, y_test = self.transform_to_dataset(testing_sentences)
		X_val, y_val = self.transform_to_dataset(validation_sentences)

		#dict_vectorizer = DictVectorizer(sparse=False)
		self.dict_vectorizer.fit(X_train + X_test + X_val)
		self.label_encoder.fit(y_train + y_test + y_val)	
			

	def bn_pos_tag(self, input):

		self.load()

		self.bn_tokenizer(input)

		t_list = self.training