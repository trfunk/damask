#!/usr/bin/python3
import damask
import numpy as np

result = damask.Result('50_64x64x64_pc_vor_tension.hdf5')

res.add_stress_Cauchy()
res.add_strain()
res.add_strain('F_p')
res.add_equivalent_Mises('sigma')
res.add_equivalent_Mises('epsilon_V^0.0(F)')

res.add_IPF_color([1,0,0])
res.add_IPF_color([0,1,0])
res.add_IPF_color([0,0,1])
res.add_IPF_color([1,1,0])
res.add_IPF_color([1,0,1])
res.add_IPF_color([0,1,1])
res.add_IPF_color([1,1,1])
