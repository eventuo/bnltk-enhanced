# Bangla Natural Language Toolkit: Parts of Speech Tagger
#
# Copyright (C) 2019 BNLTK Project
# Author: Ashraf Hossain <asrafhossain197@gmail.com>



import string
import numpy as np
from keras.models import load_model
from sklearn.feature_extraction import DictVectorizer
from sklearn.preprocessing import L