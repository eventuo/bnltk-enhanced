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
		    with open(file_name, "wb") as file:
		        # get request
		        print("Downloading....../"+tag)
		        response = get(url, stream=True)
		        # write to file
		        #file.write(response.content)
		        
		        
		        total_length = response.headers.get('content-length')

		        if total_length is None: # no content length header
		            file.write(response.content)
		        else:
		            dl = 0
		            total_length = int(total_length)
		            for data in response.iter_content(chunk_size=4096):
		                dl += len(data)
		                file.write(data)