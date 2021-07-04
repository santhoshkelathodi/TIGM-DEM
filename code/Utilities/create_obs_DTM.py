import cv2
import os
import numpy as np
import matplotlib.pyplot as plt
import glob

trajectory_path = './gKLT_GT_100_ALL_REINDEXED'

# main program
path = os.path.join(trajectory_path, '*.txt')#specify the kind of files if * is used all will be added
#print path
files = glob.glob(path)
#print files
#print np.sort(files)
file_indices=[]
for fl in files:
	file_name = fl.split('/')[2]
	#print file_name
	file_indices.append(int(file_name.split('.')[0]))

#print file_indices
numpy_file_array = np.vstack(file_indices)
#print numpy_file_array
sorted_file_indices = np.sort(numpy_file_array, axis=None)
#print sorted_file_indices
tid_list = []
x1_list = []
y1_list = []
x2_list = []
y2_list = []
t_list = []
t1_list = []
t2_list = []
for idx in sorted_file_indices:
	file_name = str(idx) + '.txt'
	print file_name
	file_path = os.path.join(trajectory_path, file_name)
	#print file_path
	all_cols = np.loadtxt(file_path)
	x_coord, y_coord, t_coord = np.loadtxt(file_path, usecols=(0, 1, 2), unpack=True, dtype='int')
	print x_coord.shape
	length = len(all_cols)
	#length = len(x_coord)
	if length < 50:
		continue    # continue here
	tid_list.append(idx)
	x1 = x_coord[0]
	x1_list.append(x1)
	y1 = y_coord[0]
	y1_list.append(y1)
	t1 = t_coord[0]
	t1_list.append(t1)
	x2 = x_coord[length - 1]
	x2_list.append(x2)
	y2 = y_coord[length - 1]
	y2_list.append(y2)
	t2 = t_coord[length - 1]
	t2_list.append(t2)
	#print length
	t_list.append(length)

#print x1_list
tid_numpy = np.vstack(tid_list)
x1_numpy = np.vstack(x1_list)
y1_numpy = np.vstack(y1_list)
x2_numpy = np.vstack(x2_list)
y2_numpy = np.vstack(y2_list)
t_numpy = np.vstack(t_list)
t1_numpy = np.vstack(t1_list)
t2_numpy = np.vstack(t2_list)

track_obs = np.c_[x1_numpy, y1_numpy, x2_numpy, y2_numpy, t_numpy, tid_numpy, t1_numpy, t2_numpy]
print track_obs
np.savetxt('track_obs_gKLT_DTM.txt', track_obs, fmt="%i", delimiter='\t')
#print label





