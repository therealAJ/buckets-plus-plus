import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

raw_data = pd.read_csv("../../csv/data.csv", usecols=["loc_x",
                                                      "loc_y",
                                                      "shot_distance",
                                                      "combined_shot_type",
                                                      "minutes_remaining",
                                                      "seconds_remaining",
                                                      "period",
                                                      #"season",
                                                      #"game_date",
                                                      
                                                      "opponent",
                                                      "shot_made_flag",
                                                      "matchup"])

#remove columns with missing data                                                  
data = raw_data.dropna() 

#format data
data["shot_made_flag"] = data["shot_made_flag"].astype('category')
data["combined_shot_type"] = data["combined_shot_type"].astype('category')
data["period"] = data["period"].astype('object')

##new features#################################################################

#time remaining in period
data["time_remaining"] = data["minutes_remaining"] * 60 + data["seconds_remaining"]
data.drop("minutes_remaining", axis=1, inplace=True)
data.drop("seconds_remaining", axis=1, inplace=True)

#is this shot clutch af?
#data["clutch_shot"] = data["time_remaining"] < 5

#is this game at home
data['home_game'] = data['matchup'].str.contains('vs').astype('int')
data.drop("matchup", axis=1, inplace=True)

#game date feature?? TBD

#do one-hot encoding for categorical feature
cst_onehot = pd.get_dummies(data['combined_shot_type'])
data.drop('combined_shot_type', axis=1, inplace=True)
data = data.join(cst_onehot)
print(cst_onehot.shape)
###############################################################################

X_minmax = 
                                                 
target = data["shot_made_flag"].copy() 
                                                  
data.drop("shot_made_flag", axis=1, inplace=True) #remove labels from data

print("done")

