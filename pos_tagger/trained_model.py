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
		    self.tagged_data_path = "C:\\Users\\"+getpass.getuser()+"\\bnltk_data\\pos_da