import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from collections import OrderedDict

from sklearn.preprocessing import MinMaxScaler
from sklearn.feature_selection import VarianceThreshold, RFE, SelectKBest, chi2
from sklearn.cross_validation import KFold, cross_val_score
from sklearn.grid_search import GridSearchCV

from pandas import DataFrame
from sklearn.pipeline import Pipeline, FeatureUnion
from sklearn.linear_model import LogisticRegression
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.ensemble import BaggingClassifier, ExtraTreesClassifier, GradientBoostingClassifier, VotingClassifier, RandomForestClassifier, AdaBoostClassifier
from sklearn.externals import joblib

raw_data = pd.read_csv("../csv/data.csv", usecols=["loc_x",
                                                      "loc_y",
                                                      #"shot_distance",
                                                      #"combined_shot_type",
                                                      "minutes_remaining",
                                                      "seconds_remaining",
                                                      #"period",
                                                      #"season",
                                                      #"game_date",
                                                      #"playoffs",
                                                      #"opponent",
                                                      #"action_type",
                                                      #"shot_type",
                                                      #"period",
                                                      "shot_made_flag",
                                                      "matchup"])

#remove columns with missing data                                                  
data = raw_data.dropna() 

##new features#################################################################

#time remaining in period
data["time_remaining"] = data["minutes_remaining"] * 60 + data["seconds_remaining"]
data.drop("minutes_remaining", axis=1, inplace=True)
data.drop("seconds_remaining", axis=1, inplace=True)


#is this shot clutch af?
#data["clutch_shot"] = data["time_remaining"] < 5
#data.drop("time_remaining", axis=1, inplace=True)


#is this game at home
#data['home_game'] = data['matchup'].str.contains('vs').astype('int')
data.drop("matchup", axis=1, inplace=True)

#game date feature?? TBD


#convert to polar
zero = data['loc_x'] == 0
data['angle'] = np.arctan(data['loc_y'][~zero] / data['loc_x'][~zero])
data['angle'][zero] = np.pi / 2

data['distance'] = np.sqrt(data['loc_y'] ** 2 + data['loc_x'] ** 2)


#data['loc_x'] = pd.cut(data['loc_x'], 25)
#data['loc_y'] = pd.cut(data['loc_y'], 25)
data.drop('loc_x', axis=1, inplace=True)
data.drop('loc_y', axis=1, inplace=True)


#convert categorical data to one-hot encoding
categories = []

for k in categories:
    onehot = pd.get_dummies(data[k])
    data.drop(k, axis=1, inplace=True)
    data = data.join(onehot)
    
###############################################################################
target = data["shot_made_flag"].copy()                                              
data.drop("shot_made_flag", axis=1, inplace=True) #remove labels from data

##ML analysis
X = data
Y = target


kfold = KFold(n=len(X), n_folds=3, random_state=7)
scoring = 'log_loss'

d = OrderedDict({'time_remaining': 1, 'angle': 622, 'distance': 10000})
df = DataFrame(d, index=[0])
print(X.head(2))
print(df)
model = GradientBoostingClassifier(n_estimators=100, random_state=7)

results = cross_val_score(model, X, Y, cv=kfold, scoring=scoring, n_jobs=1)
print("({0:.3f}) +/- ({1:.3f})".format(results.mean(), results.std()))



print(Y.shape)
model.fit(X, Y)
print(model.predict_proba(df))



print("done")



# save the model to disk
filename = 'finalized_model.sav'
joblib.dump(model, filename)

# loaded_model = pickle.load(open(filename, 'rb'))
# result = loaded_model.score(X_test, Y_test)
# print(result)