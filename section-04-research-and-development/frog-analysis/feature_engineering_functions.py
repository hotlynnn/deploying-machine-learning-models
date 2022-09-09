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


class ConvertDate(BaseEstimator, TransformerMixin):
    # function should replace one value in a specific column with another value
    def __init__(self, variables):

        if not isinstance(variables, list):
            raise ValueError('variables should be a list')

        self.variables = variables

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        
        # copy data frame inorder not to override original dataframe
        X = X.copy()

        for variable in self.variables:
            X[variable] = pd.to_datetime(X[variable])

        return X


class ExtractMonth(BaseEstimator, TransformerMixin):
    # function should replace one value in a specific column with another value
    def __init__(self, variables, column_name = 'Month'):

        if not isinstance(variables, list):
            raise ValueError('variables should be a list')

        self.variables = variables
        self.column_name = column_name

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        
        # copy data frame inorder not to override original dataframe
        X = X.copy()

        for variable in self.variables:
            X[self.column_name] = X[variable].dt.month

        return X


class MonthImputer(BaseEstimator, TransformerMixin):
    # function should replace one value in a specific column with another value
    def __init__(self, variables, column_name = 'Month'):

        if not isinstance(variables, list):
            raise ValueError('variables should be a list')

        self.variables = variables
        self.column_name = column_name

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        
        # copy data frame inorder not to override original dataframe
        X = X.copy()

        for variable in self.variables:
            X[variable] = X[variable].fillna(np.random.choice(X[X[variable].notnull()][self.column_name].unique(), 1)[0])

        return X 



