#!/usr/bin/python3

import damask
import numpy as np

# new material "material"
material = damask.ConfigMaterial()

# define isotrain Taylor 2 homogenization
material['homogenization']['sx'] = {'N_constituents':1, 'mechanical': {'type':'isostrain'}}

#define materials, Material A being Al (plastic)
material['phase']['A'] = damask.ConfigMaterial.load('phenopowerlaw_Al.yaml') 

# define microstructure, 50 grains of Al - creating random microstructure
O_A = damask.Rotation.from_random(50)


# add the materials
material = material.material_add(homogenization='sx', phase='A', O=O_A)

# export configurated material to material.yaml
material.save()

# setup polycrystal params, size in m, 128x128x128 cells, 50 grains
size = np.ones(3)*1e-5
cells = [128,128,128]
N_grains = 50

# random seeds for a voronoi tessellation
seeds = damask.seeds.from_random(size, N_grains, cells)
grid = damask.Grid.from_Voronoi_tessellation(cells, size, seeds)
 
# save grid as #grains_#resolution_pc.vti\n", w
grid.save(f'{N_grains}_{cells[0]}x{cells[1]}x{cells[2]}_pc_vor')
