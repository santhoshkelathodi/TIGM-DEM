import time
import warnings
import cv2
import os
import numpy as np
import matplotlib.pyplot as plt

from sklearn import cluster, datasets, mixture
from sklearn.neighbors import kneighbors_graph
from sklearn.preprocessing import StandardScaler
from itertools import cycle, islice

np.random.seed(0)

# ============
# Set up cluster parameters
# ============

default_base = {'quantile': .07, #'quantile': .3, .0549
                'eps': .83,# smaller value more number of clusters Earlier value = 0.83
                'damping': 0.9, #'damping': .9,
                'preference': -1.4, #'preference': -200,
                'n_neighbors': 10,
                'n_clusters': 23} #'n_clusters': 3}



# update parameters with dataset-specific values
params = default_base.copy()

#print X
#np.savetxt('X.out',X)
#np.savetxt('y.out',y)
#X1 = np.loadtxt('src.txt')
#X1 = np.loadtxt('trackobs_QMUL_ECCV_2018_x1y1.txt')
#X2 = np.loadtxt('trackobs_QMUL_ECCV_2018_x1y1x2y2.txt')
#X3 = np.loadtxt('trackobs_QMUL_ECCV_2018_x1y1x2y2t.txt')
tid, x1, y1, x2, y2, t = np.loadtxt('track_obs.txt', usecols=(0, 1, 2, 3, 4, 5), unpack=True)

print tid
XObs = np.c_[x1, y1, x2, y2, t]
#print XObs
#np.savetxt('X1.out',X1)
# normalize dataset for easier parameter selection
#X = StandardScaler().fit_transform(X1) #2-D
#X = StandardScaler().fit_transform(X2) #4-D
#X = StandardScaler().fit_transform(X3) #5-D
X = StandardScaler().fit_transform(XObs) #5-D
#np.savetxt('X_normalized.out',X)	
# estimate bandwidth for mean shift
bandwidth = cluster.estimate_bandwidth(X, quantile=params['quantile'])

# connectivity matrix for structured Ward
connectivity = kneighbors_graph(
X, n_neighbors=params['n_neighbors'], include_self=False)
# make connectivity symmetric
connectivity = 0.5 * (connectivity + connectivity.T)

# ============
# Create cluster objects
# ============
#Meanshift
ms = cluster.MeanShift(bandwidth=bandwidth, bin_seeding=True)
#DBSCAN
#print 'eps = ',params['eps']
dbscan = cluster.DBSCAN(eps=params['eps'],min_samples=1)

#AP
affinity_propagation = cluster.AffinityPropagation(
damping=params['damping'], preference=params['preference'])

clustering_algorithms = (
#('AP', affinity_propagation),
('MS', ms),
#('DBSCAN', dbscan),
)

for name, algorithm in clustering_algorithms:

	# catch warnings related to kneighbors_graph
	with warnings.catch_warnings():
		warnings.filterwarnings(
		    "ignore",
		    message="the number of connected components of the " +
		    "connectivity matrix is [0-9]{1,2}" +
		    " > 1. Completing it to avoid stopping the tree early.",
		    category=UserWarning)
		warnings.filterwarnings(
		    "ignore",
		    message="Graph is not fully connected, spectral embedding" +
		    " may not work as expected.",
		    category=UserWarning)
		algorithm.fit(X)

	if hasattr(algorithm, 'labels_'):
		y_pred = algorithm.labels_.astype(np.int)
	else:
		y_pred = algorithm.predict(X)

	#print name,y_pred
	if not os.path.exists(name):
		os.makedirs(name)
	np.savetxt('cluster_label_'+name+'.out',y_pred, fmt='%i')
	print y_pred
	np.savetxt(name+'/'+name+'_cluster_result.out', np.c_[tid, x1, y1, x2, y2, t, y_pred], fmt="%i", delimiter='\t')



