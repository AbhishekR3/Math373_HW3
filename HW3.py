# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 22:44:01 2021

@author: Abhishek Ramesh
"""

#%% Import libraries
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris

#%% Binary Classification
#Sigmoid, softmax, cross-entropy loss for binary classification
def sigmoid_binary(realnumber):
    Sigmoid = np.exp(realnumber)/(1 + np.exp(realnumber))
    return(Sigmoid)

def crossentropy_binary(predictive, ground_truth):
    ce = ((-1*ground_truth) * np.log(predictive)) - ((1 - ground_truth) * np.log(1-predictive))
    return(ce)

#%% Multiclass Classification
#Softmax Function
def softmax(vector):
    softmaxed_vector = [1]*len(vector)
    for i in range(len(vector)):
        softmaxed_vector[i] = np.exp(vector[i])/sum(np.exp(vector))
    
    return(
        ed_vector)

#Cross-entropy loss for multiclass classification
def crossentropy_multiclass(predictive_vector, groundtruth_vector):
    minus_vector = 0
    
    for i in range(len(predictive_vector)):
        minus_vector = minus_vector + ((-predictive_vector[i]) * np.log10(groundtruth_vector[i]))
            
    return(minus_vector)
    

#%% Test
print("Example of Sigmoid Binary Classification: 5 converts to " 
      + str(sigmoid_binary(5)))

print("Example of Cross Entropy of Binary Classification: [0.6, 0.5] converts to " 
      + str(crossentropy_binary(0.6, 0.5)))

print("Example of Softmax: [1,2,3,4] converts into " 
      + str(softmax([1, 2, 3, 4])))

print("Example of Cross Entropy of Multiclass Classification: [0.1,0.2,0.3,0.4], [0.7,0.7, 0.7, 0.7] converts into " 
      + str(crossentropy_multiclass([0.1,0.2,0.3,0.4], [0.7,0.7, 0.7, 0.7])))


#%% Iris Dataset Test
iris = load_iris()
X = iris.data
Y = iris.target

#Logistic regression for the dataset
log_reg = LogisticRegression()

X = iris.data
Y = iris.target

X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size=0.4, random_state=3)

log_reg.fit(X_train, Y_train)

Y_pred = log_reg.predict(X_test)

#Convert to a list to run softmax function
Y_test = Y_test.tolist()
Y_pred = Y_pred.tolist()

Softmax_ypred = softmax_binary(Y_pred)
Softmax_ytest = softmax_binary(Y_test)

print("Iris dataset cross entropy loss function: " + str(crossentropy_multiclass(Softmax_ypred, Softmax_ytest)))
