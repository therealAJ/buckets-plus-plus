import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("../../csv/data.csv", usecols=["loc_x",
                                                  "loc_y",
                                                  "shot_distance",
                                                  "combined_shot_type",
                                                  "minutes_remaining",
                                                  "seconds_remaining",
                                                  "period",
                                                  "season",
                                                  "game_date",
                                                  "opponent",
                                                  "shot_made_flag"])
                                                  
data = data.dropna() #remove columns with missing data

data["shot_made_flag"] = data["shot_made_flag"].astype('category')
data["combined_shot_type"] = data["combined_shot_type"].astype('category')
data["period"] = data["period"].astype('object')


data["time_remaining"] = data["minutes_remaining"] * 60 + data["seconds_remaining"]
data.drop("minutes_remaining", axis=1, inplace=True)
data.drop("seconds_remaining", axis=1, inplace=True)
                 

f, axarr = plt.subplots(2, 2)                                

sns.boxplot(x='loc_x', y='shot_made_flag', data=data, showmeans=True, ax=axarr[0,0])
sns.boxplot(x='loc_y', y='shot_made_flag', data=data, showmeans=True, ax=axarr[0,1])
sns.boxplot(x='shot_distance', y='shot_made_flag', data=data, showmeans=True, ax=axarr[1,0])
sns.boxplot(x='time_remaining', y='shot_made_flag', data=data, showmeans=True, ax=axarr[1,1])

plt.tight_layout()
plt.show()
                                                  
target = data["shot_made_flag"].copy() 
                                                  
data.drop("shot_made_flag", axis=1, inplace=True) #remove labels from data


print(data.dtypes)