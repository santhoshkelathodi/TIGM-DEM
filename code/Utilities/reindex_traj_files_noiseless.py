import cv2
import os
import numpy as np
import matplotlib.pyplot as plt
import shutil

from shutil import copyfile

MAX_TRAJ_IDX = 8821

trajectory_path = 'gKLT_GT_100_ALL_REINDEXED_NOISELESS'
new_trajectory_path = 'gKLT_GT_100_ALL_REINDEXED_NOISELESS_REINDEXED'
#shutil.rmtree(new_trajectory_path) #to empty directory if it exists
if not os.path.exists(new_trajectory_path):
	os.makedirs(new_trajectory_path)
new_file_idx = 0
# For each trajectory plot datapoints on image plane
for idx in range(1,MAX_TRAJ_IDX):
	#print idx, t, label
	file_name = str(idx)+'.txt'
	file_path = os.path.join(trajectory_path, file_name)
	#print file_path
	if not os.path.isfile(file_path):#if file does not exist go to the next index
		continue
	file_name = str(idx)+'.txt'
	
	dest_file_name = str(new_file_idx)+'.txt'
	dest_file_path = os.path.join(new_trajectory_path, dest_file_name)
	#copyfile(src, dst)
	print(file_path,dest_file_path)
	copyfile(file_path, dest_file_path)
	new_file_idx=new_file_idx+1



