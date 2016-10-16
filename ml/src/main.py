import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.preprocessing import MinMaxScaler
from sklearn.feature_selection import VarianceThreshold, RFE, SelectKBest, chi2
from sklearn.cross_validation import KFold, cross_val_score
from sklearn.grid_search import GridSearchCV


from sklearn.pipeline import Pipeline, FeatureUnion
from sklearn.linear_model import LogisticRegression
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.ensemble import BaggingClassifier, ExtraTreesClassifier, GradientBoostingClassifier, VotingClassifier, RandomForestClassifier, AdaBoostClassifier


raw_data = pd.read_csv("../../csv/data.csv", usecols=["loc_x",
                                                      "loc_y",
                                                      #"shot_distance",
                                                      "combined_shot_type",
                                                      "minutes_remaining",
                                                      "seconds_remaining",
                                                      "period",
                                                      "season",
                                                      #"game_date",
                                                      "playoffs",
                                                      "opponent",
                                                      #"action_type",
                                                      #"shot_type",
                                                      "period",
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
data["clutch_shot"] = data["time_remaining"] < 5
#data.drop("time_remaining", axis=1, inplace=True)


#is this game at home
data['home_game'] = data['matchup'].str.contains('vs').astype('int')
data.drop("matchup", axis=1, inplace=True)

#game date feature?? TBD


#convert to polar
zero = data['loc_x'] == 0
data['angle'] = np.arctan(data['loc_y'][~zero] / data['loc_x'][~zero])
data['angle'][zero] = np.pi / 2

data['distance'] = np.sqrt(data['loc_y'] ** 2 + data['loc_x'] ** 2)


#data['loc_x'] = pd.cut(data['loc_x'], 25)
#data['loc_y'] = pd.cut(data['loc_y'], 25)
#data.drop('loc_x', axis=1, inplace=True)
#data.drop('loc_y', axis=1, inplace=True)


#convert categorical data to one-hot encoding
categories = ['opponent', 'combined_shot_type', 'period', 'season']

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

#X_norm = MinMaxScaler(feature_range=(0,1)).fit_transform(X)


models = []
models.append(('LR', LogisticRegression()))
models.append(('LDA', LinearDiscriminantAnalysis()))
models.append(('K-NN', KNeighborsClassifier(n_neighbors=5)))
models.append(('CART', DecisionTreeClassifier()))
models.append(('NB', GaussianNB()))


cv_scores = []
names = []

for name, model in models:
    cv_result = cross_val_score(model, X, Y, cv=kfold, scoring='log_loss', n_jobs=1)
    cv_scores.append(cv_result)
    names.append(name)
    print("{0}: ({1:.3f}) +/- ({2:.3f})".format(name, cv_result.mean(), cv_result.std()))


kfold = KFold(n=len(X), n_folds=3, random_state=7)
scoring = 'log_loss'

lr_grid = GridSearchCV(
    estimator = LogisticRegression(random_state=7),
    param_grid = {
        'penalty': ['l1', 'l2'],
        'C': [0.001, 0.01, 1, 10, 100, 1000]
    }, 
    cv = kfold, 
    scoring = 'log_loss', 
    n_jobs = 1)

lr_grid.fit(X, Y)

print(lr_grid.best_score_)
print(lr_grid.best_params_)



knn_grid = GridSearchCV(
    estimator = Pipeline([
        ('min_max_scaler', MinMaxScaler()),
        ('knn', KNeighborsClassifier())
    ]),
    param_grid = {
        'knn__n_neighbors': [25],
        'knn__algorithm': ['ball_tree'],
        'knn__leaf_size': [2, 3, 4],
        'knn__p': [1]
    }, 
    cv = kfold, 
    scoring = scoring, 
    n_jobs = 1)

knn_grid.fit(X, Y)

print(knn_grid.best_score_)
print(knn_grid.best_params_)

print("done")

