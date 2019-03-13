# -*- coding: utf-8 -*-
"""
Created on Wed Mar 13 11:03:56 2019

@author: ameli
"""
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

def plot_accuracy():
    '''
    Plot actual food insecurity versus predicted
    '''
    test_outcome = pd.read_csv('./data/prepped/test_outcome.csv', sep=',')
    tree_pred = pd.read_csv('./data/prepped/predictions.csv', sep=',')['0']
    sns.regplot(test_outcome['18'], tree_pred[1:], line_kws={"color": "black"}, 
                scatter_kws={'alpha':0.3})
    plt.title("Actual Child Food Insecurity versus Predicted Food Insecurity")
    plt.xlabel("Actual")
    plt.ylabel("Predicted")
    plt.savefig("accuracy")

plot_accuracy()
