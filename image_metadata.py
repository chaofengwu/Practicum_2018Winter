import numpy as np
import image_processing
from sklearn.decomposition import PCA
import json

def image_metadata(file_list):
	###### First get raw image data and then modify them
	raw_image_matadata = []
	dimension = []
	mode = []
	color = []
	histo = []
	square = []
	# pca_ima = []
	count = 1
	try:
		with open("data.json") as json_file:
			[dimension, color, histo, square] = json.load(json_file)
			# print([dimension, mode, color, histo, pca_ima, square])
			# print('\n\n\n\n\n\n\n\n')
			# print(color)
	except:
		for i in file_list:
			print(str(count) + i + "\n")
			[di, mo, co, hi, sq] = image_processing.pil_get_image_metadata(i, 2, int(100/2))
			dimension += [di]
			mode += [mo]
			color += [co]
			histo += [hi]
			square += [sq]
			# pca_ima += [pca_im]
			# image_processing.get_image_metadata(i, 2, 3)
			# print(type(histo[0][0][0]))
			count += 1
			# if count == 3:
			# 	break
		# print(pca_ima)
		with open('data.json', 'w') as outfile:
			json.dump([dimension, color, histo, square], outfile)
		# print(histo)
	
	return [dimension, mode, color, histo, square]