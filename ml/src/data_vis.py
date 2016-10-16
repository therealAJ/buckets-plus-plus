# -*- coding: utf-8 -*-
"""
Created on Sat Oct 15 14:17:21 2016

@author: Pedro
"""

"""
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


sns.pairplot(data, vars=['loc_x', 'loc_y', 'shot_distance'], hue='shot_made_flag', size=3)
plt.show()

desc = data.describe(include=['number'])
desc = data.describe(include=['object', 'category'])


f, axarr = plt.subplots(2, 2)                                

sns.boxplot(x='loc_x', y='shot_made_flag', data=data, showmeans=True, ax=axarr[0,0])
sns.boxplot(x='loc_y', y='shot_made_flag', data=data, showmeans=True, ax=axarr[0,1])
sns.boxplot(x='shot_distance', y='shot_made_flag', data=data, showmeans=True, ax=axarr[1,0])
sns.boxplot(x='time_remaining', y='shot_made_flag', data=data, showmeans=True, ax=axarr[1,1])

plt.tight_layout()
plt.show()
"""