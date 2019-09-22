from math import sqrt
import matplotlib.pyplot as plt

no_of_steps = 278

EKF_file = open("data/EKF_SLAM_error.txt",'r')
Fast_file = open("data/fast_SLAM_error.txt",'r')


ekf_errors = [float(error[:-1]) for error in EKF_file.readlines()]
fast_errors = [float(error[:-1]) for error in Fast_file.readlines()]

print(ekf_errors[:5])
print('===============')
print(fast_errors[:5])

"""
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
"""

plt.plot([i for i in range(no_of_steps)], ekf_errors, label = 'EKF SLAM Error')
plt.plot([i for i in range(no_of_steps)], fast_errors, label = 'Fast SLAM Error')
# plt.axhline(y=overall_error, color='r', linestyle='-', label = 'Average Error')
plt.xlabel('Number of Steps')
plt.ylabel('Error (in mm)')
plt.title('Comparison of error in EKF SLAM and Fast SLAM')
plt.legend()
plt.show()

