from Model import get_Model
import sys
import itertools
import cv2
import os
import numpy as np
from parameter import *

MAL_VECTOR = 'ംഃഅആഇഈഉഊഋഌഎഏഐഒഓഔകഖഗഘങചഛജഝഞടഠഡഢണതഥദധനഩപഫബഭമയരറലളഴവശഷസഹാിീുൂൃെേൈൊോൌ്ൎൗൺൻർൽൾ.,'

ASCII_VECTOR = '-+=!@#$%^&*(){}[]|\'"\\/?<>;:0123456789'

ENG_VECTOR = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'

model = get_Model(training=False)
model.load_weights(os.getcwd()+"/"+sys.argv[1])


def real(img,j,h,w,g): #input grayscale image specifying height, width, file to be written
	try:
		img = img.astype(np.float32)       # convert to float 32
		img = (img / 255.0) * 2.0 - 1.0    # normalising
		img_pred = img.T                   # (h,w) -> (w,h)
		img_pred = np.expand_dims(img_pred, axis=-1)  # (w,h,1)
		img_pred = np.expand_dims(img_pred, axis=0)   # (1,w,h,1)
		X_data = np.ones([img_w, img_h, 1])           # (w,h,1)
		X_data[:img_pred.shape[1]] = img_pred
		print(img_pred.shape[1])
		img_pred = np.expand_dims(X_data, axis=0)     # (1,w,h,1)
		out = model.predict(img_pred)                 # prediction
		letters = [letter for letter in CHAR_VECTOR]
		out_best = list(np.argmax(out[0, 2:], axis=1)) #ignore the first two outputs, and take the index of the maximum 
		out_best = [k for k, g in itertools.groupby(out_best)]
		outstr = ''
		for i in out_best:
			if i < len(letters):
				outstr += letters[i]           # conjoin each charto form the required string
		g.write(str(var)+ " = "+outstr+'-'+str(j)+"-"+str(h)+"-"+str(w)+'\n')
		print(str(var) +" = "+outstr)
	except:
		outstr = 'error on prediction'
	return outstr


