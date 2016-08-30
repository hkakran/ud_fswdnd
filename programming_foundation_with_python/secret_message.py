import os
import re

def remove_numbers(name):
	return re.sub('[0-9]','',name)


def rename_files():
	# 1. get all the photos
	files = os.listdir(os.getcwd()+'/prank')

	# 2. rename the files
	for fileName in files:
		print fileName
		print remove_numbers(fileName)
		os.rename(os.getcwd()+'/prank/'+fileName, os.getcwd()+'/prank/'+remove_numbers(fileName))

rename_files()

