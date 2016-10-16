from sklearn.externals import joblib
import numpy as np
import pandas as pd
from pandas import DataFrame
from collections import OrderedDict

def _predict(time_remaining, loc_x, loc_y, model):
	angle = np.pi/2 if loc_x == 0 else np.arctan(loc_y / loc_x)
	distance = np.sqrt(loc_x ** 2 + loc_y ** 2)

	obs_d = OrderedDict.fromkeys(('time_remaining', 'angle', 'distance'))
	obs_d['time_remaining'] = time_remaining
	obs_d['angle'] = angle
	obs_d['distance'] = distance

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

def makegridprediction(time_remaining, locs_x, locs_y):
	time_remaining = int(time_remaining)

	x_arr = locs_x.split(',')
	x_arr = [int(val) for val in x_arr]

	y_arr = locs_y.split(',')
	y_arr = [int(val) for val in y_arr]	

	filename = 'finalized_model.sav'
	loaded_model = joblib.load(filename)
	
	results = [_predict(time_remaining, x_arr[i], y_arr[i], loaded_model)[0][1] for i in range(len(x_arr))]
	return ','.join(str(val) for val in results)
