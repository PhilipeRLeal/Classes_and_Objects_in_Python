# -*- coding: utf-8 -*-
"""
Created on Sat Jun  2 17:41:39 2018

@author: Philipe_Leal
"""

import numpy as np
from math import sqrt
import matplotlib.pyplot as plt
import warnings
from collections import Counter

dataset = {'k': [[1,2], [2,3], [3,1]], 'r':[[6,5], [7,7], [8,6]]}


dataset['k'] += [1,1]
new_features = [5,7]

for i in dataset:
    for ii in dataset[i]:
        
        plt.scatter(ii[0], ii[1], s=100, color=i)
plt.grid(True)
plt.show()


def KNN_object (data, predict, K=3):
    if len(data) >=K:
        
        K = len(data)
        warnings.warn("O dataset inicial já contém mais de k classes! \
                      k será estabelecido conforme número mínimo do dataset inserido")

    else:
        distances = []
        for group in data:
            for features in data[group]:
                features = np.array(features)
                predict = np.array(predict)
                euclidean_distance = np.linalg.norm(features - predict)
                distances.append([euclidean_distance, group])
        
        votes = []        
        for i in sorted(distances)[:K]:
            votes.append(i[1])
            
        print("Menor distancia (mais votado): ", Counter(votes).most_common(1))
        vote_result = Counter(votes).most_common(1)[0][0]
        
        return vote_result
    
result = KNN_object(dataset, new_features, 3)
print(result)