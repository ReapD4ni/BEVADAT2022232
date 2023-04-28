import numpy as np
from sklearn.cluster import KMeans
from sklearn.datasets import load_digits
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix


class KMeansOnDigits:

    def __init__(self,n_clusters, random_state) -> None:
        self.n_clusters=n_clusters
        self.random_state=random_state

    def load_dataset(self):
        self.digits=load_digits()

    def predict(self):
        model=KMeans(n_clusters=self.n_clusters,random_state=self.random_state)
        self.clusters=model.fit_predict(self.digits.data)

    def get_labels(self):
        result=np.zeros_like(self.clusters)
        for cluster in range(self.n_clusters):
            mask= self.n_clusters == cluster
            cluster_label=self.digits.target[mask]
            mode=np.bincount(cluster_label).argmax()
            result[mask]=mode
        self.labels=result

    def calc_accuracy(self):
        self.accuracy=accuracy_score(self.digits.target,self.labels)

    def confusion_matrix(self):
        self.mat=confusion_matrix(self.digits.target, self.labels)
