import pickle

def predict(combined_shot_type, loc_x, loc_y, seconds_remaining, period, season, shot_made, shot_type, game_date, opponent):
	filename = 'finalized_model.sav'
	loaded_model = pickle.load(open(filename, 'rb'))
	#result = loaded_model.score(combined_shot_type, loc_x, loc_y, seconds_remaining, period, shot_made, shot_type, game_date, opponent)
	#print(result)
	#result = loaded_model.score([0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0])
	#print(result)
	return combined_shot_type
