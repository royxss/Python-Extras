# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 20:44:19 2016

@author: SROY
"""

from IPython.display import HTML
HTML('')

from sklearn.datasets import load_iris
from sklearn import tree
iris=load_iris()
type(iris)

print(iris.data)
print(iris.feature_names)
print(iris.target)
print(iris.target_names)
print(type(iris.data))
print(type(iris.target))
print(iris.data.shape)
print(iris.target.shape)
print(iris.data[<indices>])
print(iris.target[<indices>])

x=iris.data
y=iris.target

clf = tree.DecisionTreeClassifier()
clf = clf.fit(iris.data, iris.target)
clf.predict(iris.data[:1, :])
clf.predict_proba(iris.data[:1, :])



