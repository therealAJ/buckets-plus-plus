from sklearn.externals import joblib
import numpy as np
import pandas as pd
from pandas import DataFrame
from collections import OrderedDict

def _predict(time_remaining, loc_x, loc_y, model):
	angle = np.pi/2 if loc_x == 0 else np.arctan(loc_y / loc_x)
	distance = np.sqrt(loc_x ** 2 + loc_y ** 2)
	obs_d = OrderedDict({'time_remaining': time_remaining, 
						 'angle': 	angle,
						 'distance': distance})
	obs_df = DataFrame(obs_d, index=[0])
	return model.predict_proba(obs_df)	


def makeprediction(time_remaining, loc_x, loc_y):
	time_remaining = int(time_remaining)
	loc_x = int(loc_x)
	loc_y = int(loc_y)
	filename = 'finalized_model.sav'
	loaded_model = joblib.load(filename)
	result = _predict(time_remaining, loc_x, loc_y, loaded_model)
	return result[0][1]
	
