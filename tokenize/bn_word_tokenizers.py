# Bangla Natural Language Toolkit: Tokenizers
#
# Copyright (C) 2019 BNLTK Project
# Author: Ashraf Hossain <asrafhossain197@gmail.com>

import string 
import re
from string import punctuation

class Tokenizers:
	def __init__(self):
		pass

	def bn_word_tokenizer(self, input_):
		tokenize_list = []
		r 