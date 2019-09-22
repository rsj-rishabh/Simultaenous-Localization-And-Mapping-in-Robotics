from math import sqrt
import matplotlib.pyplot as plt

no_of_steps = 278

measured_file = open("data/fast_slam_counter.txt",'r')
actual_file = open("data/robot4_reference.txt",'r')
error_file = open('fast_SLAM_error.txt', 'w')

measured_poses = []
actual_poses = []

# Store measured poses
for l in measured_file:
    pose = l.split()
    if pose[0] == 'F':
        measured_poses.append((float(pose[1]), float(pose[2])))

# Store actual poses
for l in actual_file:
    pose = l.split()
    actual_poses.append((float(pose[2]), float(pose[3])))

print(measured_poses[:5])
print('===============')
print(actual_poses[:5])

# Calculate error
overall_error = 0.0
error_at_each_step = []
for measured_pose, actual_pose in zip(measured_poses, actual_poses):
    error = sqrt((measured_pose[0] - actual_pose[0])**2 + (measured_pose[1] - actual_pose[1])**2)
    overall_error += error
    error_at_each_step.append(error)
    error_file.write(str(error)+'\n')

overall_error = overall_error/no_of_steps

print('The overall error is: {}'.format(overall_error))

plt.plot([i for i in range(no_of_steps)], error_at_each_step, label = 'Error')
plt.axhline(y=overall_error, color='r', linestyle='-', label = 'Average Error')
plt.xlabel('Number of Steps')
plt.ylabel('Error (in mm)')
plt.title('Error in Fast SLAM')
plt.legend()
plt.show()
