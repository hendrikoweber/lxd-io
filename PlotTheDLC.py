from lxd_io import Dataset
import matplotlib.pyplot as plt
import numpy as np

dataset_path = "/home/hendrik/data/highD-dataset-v1.0"
dataset = Dataset(dataset_path)
recording = dataset.get_recording(12)

plt.rcParams['axes.prop_cycle'] = plt.cycler(color=['#803dc0', '#803dc0', '#8080ff', '#ff8080'])  # Custom color list
plot_file = recording.plot_track([1009, 1016, 1115, 1110], ".")

im = plt.imread(plot_file)
plt.imshow(im)
plt.show()

t_ego = recording.get_track(1115)
t_1 = recording.get_track(1110)
t_2 = recording.get_track(1109)
t_3 = recording.get_track(1116)

f_ego = t_ego.get_data('frame')
f_1 = t_1.get_data('frame')
f_2 = t_2.get_data('frame')
f_3 = t_3.get_data('frame')

b_1 = np.logical_and(f_1 >= f_ego[0], f_1 <= f_ego[-1])
b_2 = np.logical_and(f_2 >= f_ego[0], f_2 <= f_ego[-1])
b_3 = np.logical_and(f_3 >= f_ego[0], f_3 <= f_ego[-1])

x_ego = t_ego.get_data('x')
y_ego = t_ego.get_data('y')

x_1= t_1.get_data('x')
y_1= t_1.get_data('y')

x_2= t_2.get_data('x')
y_2= t_2.get_data('y')

x_3= t_3.get_data('x')
y_3= t_3.get_data('y')

plt.rcParams['axes.prop_cycle'] = plt.cycler(color=[ '#8080ff', '#ff8080', '#803dc0', '#803dc0'])
plt.plot(x_ego, y_ego)
plt.plot(x_1[b_1], y_1[b_1])
plt.plot(x_2[b_2], y_2[b_2])
plt.plot(x_3[b_3], y_3[b_3])
plt.show()