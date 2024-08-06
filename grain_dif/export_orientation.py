import damask
import numpy as np


result_200grains = '20_32x32x32_pc_vor_tension2.5.hdf5'



def get_rotation(damask_result_file, increment = 0):
    result = damask.Result(damask_result_file)
    current_increment = result.view(increments=increment)
    return damask.Rotation(current_increment.get('O')).as_Euler_angles(degrees=True)


for i in range(0, 55, 5):
    with open("angles_200_{i}.txt".format(i = i), "w") as ori_file:
        for vector in get_rotation(result_200grains, i):
            ori_file.write("{x} {y} {z}\n".format(x=vector[0], y = vector[1], z = vector[2]))




