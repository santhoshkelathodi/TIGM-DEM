import cv2
import os
import numpy as np
import matplotlib.pyplot as plt
import glob
import shutil
from shutil import copyfile

trajectory_path = 'gKLT_GT_100_ALL_REINDEXED_NOISELESS'

cluster_file_name = 'DTM_cluster_result.out'

bg_image_path = './qmul_bg.jpg'
image = cv2.imread(bg_image_path)
cv2.imshow("qmul_bg",image)
x_max = image.shape[1]
y_max = image.shape[0]


kill_start_x=0
kill_end_x= kill_start_x + 160
kill_start_y=150
kill_end_y= kill_start_y + 60



cv2.rectangle(image,(kill_start_x,kill_start_y),(kill_end_x,kill_end_y),(0,0,255),2)
'''
#Start:test code
cv2.imshow('track',image)
k = cv2.waitKey() & 0xff
cv2.destroyAllWindows()
cap.release()
#End:test code
'''


#Load the DTM cluster results
tid, x1, y1, x2, y2, label, state = np.loadtxt(cluster_file_name, usecols=(0, 1, 2, 3, 4, 8, 9), unpack=True, dtype='int')
#tid, x1, y1, x2, y2 = np.loadtxt(cluster_file_name, usecols=(0, 1, 2, 3, 4,), unpack=True, dtype='int')

tid_x1_y1_label = np.c_[tid, x1, y1, label, state]
print tid_x1_y1_label
#print label

# For each trajectory plot datapoints on image plane
for tid, x1, y1, label, state in tid_x1_y1_label:
	#if  (3 == label) and (kill_start_x < x1 < kill_end_x) and (kill_start_y < y1 < kill_end_y): # noisy trajectories, hence must not b copied
	if  (11 == label):
		#os.rename("path/to/current/file.foo", "path/to/new/destination/for/file.foo")
		#shutil.move("path/to/current/file.foo", "path/to/new/destination/for/file.foo")
		file_name = str(tid) + '.txt'
		file_path = os.path.join(trajectory_path, file_name)
		if os.path.isfile(file_path): # if the file exists
			print("Removing noisy trajectory:",tid)
			os.remove(file_path)

		

