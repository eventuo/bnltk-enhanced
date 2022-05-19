
import unittest 
from bnltk.stemmer import BanglaStemmer 


class TestStemmer(unittest.TestCase):

	def setUp(self):
		print('Setup')
		self.t = BanglaStemmer()
