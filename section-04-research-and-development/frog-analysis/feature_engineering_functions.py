import pandas as pd
import numpy as np

from sklearn.base import TransformerMixin, BaseEstimator

class ValueReplacer(BaseEstimator, TransformerMixin):
    # function should replace one value in a specific column with another value
    def __init__(self, variables, original_value, replacer):

        if not isinstance(variables, list):
            raise ValueError('variables should be a list')

        self.variables = variables
        self.original_value = original_value
        self.replacer = replacer

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        
        # copy data frame inorder not to override original dataframe
        X = X.copy()

        for variable in self.variables:
            X[variable] = X[variable].replace(self.original_value, self.replacer)

        return X
