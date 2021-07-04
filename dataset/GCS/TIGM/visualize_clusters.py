import cv2
import os
import numpy as np
import matplotlib.pyplot as plt


trajectory_path = '/home/sk47/workspace/trackdata/Dataset/STATION/cust_trajectory_400'
bg_image_path = '../gcs.png'
cluster_file='TIGM_cluster_result.out'

image = cv2.imread(bg_image_path)
#cv2.imshow("ucf_bg",image)
x_max = image.shape[1]
y_max = image.shape[0]
#hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

common_cluster_folder = 'common_cluster_folder'
if not os.path.exists(common_cluster_folder):
	os.makedirs(common_cluster_folder)

def plot_trajectoy_gradient(cluster_name, src_path, filename, label, max_color):
	cluster_frame_name = 'grad_'+cluster_name+'_'+filename.split('.')[0]+'.png'
	#Always read the frame
	image = cv2.imread(bg_image_path)
	hsv_frame = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)


	file_path = os.path.join(src_path, filename)
	print file_path
	x_coord, y_coord = np.loadtxt(file_path, usecols=(0, 1), unpack=True, dtype='int') 

	#adjust outofbound values
	x_coord[x_coord >= x_max] = x_max-1
	x_coord[x_coord >= x_max] = x_max-1
	y_coord[y_coord >= y_max] = y_max-1
	y_coord[y_coord >= y_max] = y_max-1
	x_coord[x_coord < 0] = 0
	x_coord[x_coord < 0] = 0
	y_coord[y_coord < 0] = 0
	y_coord[y_coord < 0] = 0

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
	#cv2.imshow(cluster_frame_name, bgrcopy)
	#cv2.waitKey(0)
	cv2.imwrite(cluster_name+'/'+cluster_frame_name, bgrcopy)
	return

def plot_cluster_gradient(cluster_name, src_path, filename, label, max_color):
	cluster_frame_name = 'grad_'+cluster_name+'.png'
	if not os.path.isfile(cluster_frame_name):#read the frame
		image = cv2.imread(bg_image_path)
		hsv_frame = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
	else:#read the current cluster frame
		image = cv2.imread(cluster_frame_name)
		hsv_frame = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

	file_path = os.path.join(src_path, filename)
	print file_path
	x_coord, y_coord = np.loadtxt(file_path, usecols=(0, 1), unpack=True, dtype='int')

	#adjust outofbound values
	x_coord[x_coord >= x_max] = x_max-1
	x_coord[x_coord >= x_max] = x_max-1
	y_coord[y_coord >= y_max] = y_max-1
	y_coord[y_coord >= y_max] = y_max-1
	x_coord[x_coord < 0] = 0
	x_coord[x_coord < 0] = 0
	y_coord[y_coord < 0] = 0
	y_coord[y_coord < 0] = 0

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
	#cv2.imshow(cluster_frame_name, bgrcopy)
	#cv2.waitKey(0)
	cv2.imwrite(cluster_frame_name, bgrcopy)
	return

def plot_cluster(cluster_name, src_path, filename, label, max_color):
	cluster_frame_name = cluster_name+'.png'
	if not os.path.isfile(cluster_frame_name):#read the frame
		image = cv2.imread(bg_image_path)
		hsv_frame = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
	else:#read the current cluster frame
		image = cv2.imread(cluster_frame_name)
		hsv_frame = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

	file_path = os.path.join(src_path, filename)
	print file_path
	x_coord, y_coord = np.loadtxt(file_path, usecols=(0, 1), unpack=True, dtype='int')

	#adjust outofbound values
	x_coord[x_coord >= x_max] = x_max-1
	x_coord[x_coord >= x_max] = x_max-1
	y_coord[y_coord >= y_max] = y_max-1
	y_coord[y_coord >= y_max] = y_max-1
	x_coord[x_coord < 0] = 0
	x_coord[x_coord < 0] = 0
	y_coord[y_coord < 0] = 0
	y_coord[y_coord < 0] = 0

	num_data = len(x_coord)
	print num_data
	t = np.arange(len(x_coord))
	hue = []
	sat = []
	val = []

	hue[:] = [label*180.0/max_color for x in t] #going for a fixed color for this trajectory
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
	#cv2.imshow(cluster_frame_name, bgrcopy)
	#cv2.waitKey(0)
	cv2.imwrite(cluster_frame_name, bgrcopy)
	return
# main program

#Load the cluster results
tid, t, label = np.loadtxt(cluster_file, usecols=(0, 5, 6), unpack=True, dtype='int')

tid_t_label = np.c_[tid, t, label]
print tid_t_label
#print label

# For each trajectory plot datapoints on image plane
for idx,t,label in tid_t_label:
	#print idx, t, label
	cluster_name = 'cluster_'+str(label)
	print cluster_name
	if not os.path.exists(cluster_name):
		os.makedirs(cluster_name)
	file_name = str(idx) + '.txt'
	#file_path = os.path.join(trajectory_path, file_name)
	#print file_path
	max_color = len(np.unique(label))
	#plot_cluster(cluster_name, trajectory_path, file_name, label, max_color)
	#plot_cluster_gradient(cluster_name, trajectory_path, file_name, label, max_color)
	plot_trajectoy_gradient(cluster_name, trajectory_path, file_name, label, max_color)


