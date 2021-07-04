import cv2
import os
import numpy as np
import matplotlib.pyplot as plt

MAX_TRAJ_IDX = 99656

trajectory_path = './gKLT_GT_50_ALL'
bg_image_path = './qmul_bg.jpg'
image = cv2.imread(bg_image_path)
cv2.imshow("qmul_bg",image)
x_max = image.shape[1]
y_max = image.shape[0]

def plot_trajectory_gradient(traj_image_name, src_path, filename):
	frame_name = traj_image_name+'.png'
	if not os.path.isfile(frame_name):#read the frame
		image = cv2.imread(bg_image_path)
		hsv_frame = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
	else:#read the cluster frame if already saved
		image = cv2.imread(frame_name)
		hsv_frame = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

	file_path = os.path.join(src_path, filename)
	print file_path
	x_coord, y_coord = np.loadtxt(file_path, usecols=(0, 1), unpack=True, dtype='int')

	'''
	#adjust outofbound values
	x_coord[x_coord >= x_max] = x_max-1
	x_coord[x_coord >= x_max] = x_max-1
	y_coord[y_coord >= y_max] = y_max-1
	y_coord[y_coord >= y_max] = y_max-1
	x_coord[x_coord < 0] = 0
	x_coord[x_coord < 0] = 0
	y_coord[y_coord < 0] = 0
	y_coord[y_coord < 0] = 0
	'''
	num_data = len(x_coord)
	print num_data
	t = np.arange(len(x_coord))
	hue = []
	sat = []
	val = []

	hue[:] = [x*180.0/num_data for x in t] #going for a fixed color for this trajectory
	sat[:] = [255 for x in t]
	val[:] = [255 for x in t]

	hsv_frame[y_coord[:],x_coord[:] ,0] = hue[:]
	hsv_frame[y_coord[:],x_coord[:] ,1] = sat[:]
	hsv_frame[y_coord[:],x_coord[:] ,2] = val[:]

	image = cv2.cvtColor(hsv_frame, cv2.COLOR_HSV2BGR)

	bgrcopy = image[:, :, :].copy() 
	prev_col = x_coord[0]
	prev_row = y_coord[0]
	print image[prev_row, prev_col]
	for i in range(1,num_data): 
		b = image[prev_row, prev_col, 0]
		g = image[prev_row, prev_col, 1]
		r = image[prev_row, prev_col, 2]
		cv2.line(bgrcopy,(prev_col, prev_row),(x_coord[i], y_coord[i]), (int(b),int(g),int(r)), 1, 8) # Point(row,col)
		prev_col = x_coord[i]
		prev_row = y_coord[i]
	#cv2.imshow(frame_name, bgrcopy)
	#cv2.waitKey(0)
	cv2.imwrite(frame_name, bgrcopy)
	return

# For each trajectory plot datapoints on image plane
for idx in range(1,MAX_TRAJ_IDX):
	#print idx, t, label
	file_name = str(idx)+'.txt'
	file_path = os.path.join(trajectory_path, file_name)
	print file_path
	if not os.path.isfile(file_path):#if file does not exist go to the next index
		continue
	file_name = str(idx) + '.txt'
	plot_trajectory_gradient('all_traj_frame', trajectory_path, file_name)


