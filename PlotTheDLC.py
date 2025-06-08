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

t_fields = ['frame', 'x', 'y']

ego = {}
ego['track'] = recording.get_track(1115)
for field in t_fields:
    ego[field] = ego['track'].get_data(field)

obj_ids = [1110, 1109, 1116]

objs = []
for id in obj_ids:
    obj = {}
    obj['track'] = recording.get_track(id)
    for field in t_fields:
        obj[field] = obj['track'].get_data(field)
        if field == 'frame':
            b_in = np.logical_and(obj['frame'] >= ego['frame'][0], obj['frame'] <= ego['frame'][-1])
        obj[field] = obj[field][b_in]
    objs.append(obj)

step = 100
plt.rcParams['axes.prop_cycle'] = plt.cycler(color=[ '#8080ff', '#ff8080', '#803dc0', '#803dc0'])
l_e, = plt.plot(ego['x'], ego['y'])
plt.plot(ego['x'][::step], ego['y'][::step], 'o', color=l_e.get_color(), label='Markers')

for obj in objs:
    l_o, = plt.plot(obj['x'], obj['y'])
    plt.plot(obj['x'][::step], obj['y'][::step], 'o', color=l_o.get_color(), label='Markers')

if ego['track'].get_data('xVelocity')[0] < 0:
    plt.gca().invert_xaxis()
    plt.gca().invert_yaxis()

plt.title('Absolute coordinates')

plt.show()


for obj in objs:
    # To get the matching pieces of the vecotors
    obj_in_ego = np.logical_and(obj['frame'] >= ego['frame'][0], obj['frame'] <= ego['frame'][-1])
    ego_in_obj = np.logical_and(ego['frame'] >= obj['frame'][0], ego['frame'] <= obj['frame'][-1])

    # Get the relative coordinates
    obj['x_rel'] = obj['x'][obj_in_ego] - ego['x'][ego_in_obj]
    obj['y_rel'] = obj['y'][obj_in_ego] - ego['y'][ego_in_obj]

    obj['x_in_ego'] = obj['x'][obj_in_ego]
    obj['y_in_ego'] = obj['y'][obj_in_ego]

plt.plot(0,0,'o')

for obj in objs:
    plt.plot(obj['x_rel'], obj['y_rel'])

if ego['track'].get_data('xVelocity')[0] < 0:
    plt.gca().invert_xaxis()
    plt.gca().invert_yaxis()   

plt.title('Relative coordinates')

plt.show()

plt.plot(np.zeros(np.shape(ego['y'])), ego['y'])
for obj in objs:
    plt.plot(obj['x_rel'], obj['y_in_ego'])


if ego['track'].get_data('xVelocity')[0] < 0:
    plt.gca().invert_xaxis()
    plt.gca().invert_yaxis()   

plt.title('x-rel, y-abs')

plt.show()