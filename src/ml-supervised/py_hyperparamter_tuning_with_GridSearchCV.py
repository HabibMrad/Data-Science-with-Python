# Hyperparameter tuning with GridSearchCV
#
# Hugo demonstrated how to use to tune the n_neighbors parameter of the
# KNeighborsClassifier() using GridSearchCV on the voting dataset. You will now practice this yourself, but by using
# logistic regression on the diabetes dataset instead!
#
# Like the alpha parameter of lasso and ridge regularization that you saw earlier, logistic regression also has a
# regularization parameter: C. C controls the inverse of the regularization strength, and this is what you will tune
# in this exercise. A large C can lead to an overfit model, while a small C can lead to an underfit model.
#
# The hyperparameter space for C has been setup for you. Your job is to use GridSearchCV and logistic regression to
# find the optimal C in this hyperparameter space. The feature array is available as X and target variable array is
# available as y.
#
# You may be wondering why you aren't asked to split the data into training and test sets. Good observation! Here,
# we want you to focus on the process of setting up the hyperparameter grid and performing grid-search
# cross-validation. In practice, you will indeed want to hold out a portion of your data for evaluation purposes,
# and you will learn all about this in the next video!

import numpy as np
import pandas as pd
# Import necessary modules
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV

from helper import path

# Read the CSV file into a DataFrame: df
df = pd.read_csv(path + 'diabetes.csv')

# Create arrays for features and target variable
X = df.drop('diabetes', axis=1)
y = df['diabetes']

# Setup the hyperparameter grid
c_space = np.logspace(-5, 8, 15)
param_grid = {'C': c_space}

# Instantiate a logistic regression classifier: logreg
logreg = LogisticRegression()

# Instantiate the GridSearchCV object: logreg_cv
logreg_cv = GridSearchCV(logreg, param_grid, cv=5)

# Fit it to the data
logreg_cv.fit(X, y)

# Print the tuned parameters and score
print("Tuned Logistic Regression Parameters: {}".format(logreg_cv.best_params_))
print("Best score is {}".format(logreg_cv.best_score_))
