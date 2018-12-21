"""
Script to find out the angle at a given time for 12 hours format
# -----------------------------------------------------------
# Original Author: Subhashini Tatipamula
# Created Date : 12-Dec-2018
# ------------------------------------------------------------
"""
minutes_angle_dict = {}
hours_angle_dict = {1: 30}

for i in range(1, 61):
    minutes_angle_dict[i] = i * 6
print("Angle at each Minute: " + str(minutes_angle_dict))

for i in range(1, 13):
    hours_angle_dict[i + 1] = hours_angle_dict[i] + 30

print("Angle at each Hour: " + str(hours_angle_dict))
time = input("Enter time in h:m format ")
hour, minute = time.split(':')
print('Angle for %s is %d' % (time, (hours_angle_dict[int(hour)] - minutes_angle_dict[int(minute)])))
