import pandas as pd
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

from matplotlib import pyplot as plt


class LinearRegression:
    def __init__(self, epochs: int = 1000, lr: float = 1e-3):
        self.epochs=epochs
        self.lr=lr


    iris = load_iris()
    df = pd.DataFrame(iris.data, columns=iris.feature_names)

    X = df['petal width (cm)'].values
    y = df['sepal length (cm)'].values

    def fit(self, X: np.array, y: np.array):

        
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Building the model
        m = 0
        c = 0

        L = 0.0001  # The learning Rate
        epochs = 1000  # The number of iterations to perform gradient descent

        n = float(len(self.X_train)) # Number of elements in X

        # Performing Gradient Descent 
        losses = []
        for i in range(epochs): 
            y_pred = m*self.X_train + c  # The current predicted value of Y

            residuals = self.y_pred - self.y_train
            loss = np.sum(residuals ** 2)
            losses.append(loss)
            D_m = (-2/n) * sum(self.X_train * residuals)  # Derivative wrt m
            D_c = (-2/n) * sum(residuals)  # Derivative wrt c
            m = m + L * D_m  # Update m
            c = c + L * D_c  # Update c
            if i % 100 == 0:
                print(np.mean(self.y_train-self.y_pred))


    def predict(self, X):
        pred = []
        for X in self.X_test:
            y_pred = m*self.X + c
            pred.append(y_pred)
