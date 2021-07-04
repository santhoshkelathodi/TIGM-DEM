import cv2
import os
import numpy as np
import matplotlib.pyplot as plt
import glob
import shutil
from shutil import copyfile

trajectory_path = 'gKLT_GT_100_ALL_REINDEXED'
new_trajectory_path = 'gKLT_GT_100_ALL_REINDEXED_NOISELESS'

cluster_file_name = 'DTM_cluster_result.out'

bg_image_path = './qmul_bg.jpg'
image = cv2.imread(bg_image_path)
cv2.imshow("qmul_bg",image)
x_max = image.shape[1]
y_max = image.shape[0]


kill_start_x=0
kill_end_x= kill_start_x + 150
kill_start_y=150
kill_end_y= kill_start_y + 90



cv2.rectangle(image,(kill_start_x,kill_start_y),(kill_end_x,kill_end_y),(0,0,255),2)

#Start:test code
cv2.imshow('track',image)
k = cv2.waitKey() & 0xff
cv2.destroyAllWindows()
cap.release()
#End:test code


if not os.path.exists(new_trajectory_path):
	os.makedirs(new_trajectory_path)


#Load the DTM cluster results
tid, x1, y1, x2, y2, label, state = np.loadtxt(cluster_file_name, usecols=(0, 1, 2, 3, 4, 8, 9), unpack=True, dtype='int')
#tid, x1, y1, x2, y2 = np.loadtxt(cluster_file_name, usecols=(0, 1, 2, 3, 4,), unpack=True, dtype='int')

tid_x1_y1_label = np.c_[tid, x1, y1, label]
print tid_x1_y1_label
#print label

# For each trajectory plot datapoints on image plane
for tid, x1, y1, label in tid_x1_y1_label:
	if  (0 == label) and (kill_start_x < x1 < kill_end_x) and (kill_start_y < y1 < kill_end_y): # noisy trajectories, hence must not b copied
		#os.rename("path/to/current/file.foo", "path/to/new/destination/for/file.foo")
		#shutil.move("path/to/current/file.foo", "path/to/new/destination/for/file.foo")
		print("noisy trajectory:",tid)
		continue
	if  not(65535 == label):# There are labels with 65535. They should not be copied
		print("Non-noisy trajectory:",tid)
		file_name = str(tid) + '.txt'
		file_path = os.path.join(trajectory_path, file_name)

		new_file_name = str(tid) + '.txt'
		new_file_path = os.path.join(new_trajectory_path, new_file_name)
		copyfile(file_path, new_file_path)
		

