# Bangla Natural Language Toolkit: DataFilles Downloader
#
# Copyright (C) 2019 BNLTK Project
# Author: Ashraf Hossain <asrafhossain197@gmail.com>

from requests import get  # to make GET request
import platform
import getpass
import os
import sys


class DataFiles:
	def __init__(self):
		pass

	def downloader(self, url, file_name, tag):
		if not os.path.exists(file_name):
				    # open in binary mode
		    wit