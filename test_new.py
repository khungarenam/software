from ase.constraints import FixAtoms
from ase import Atoms
from mace.calculators import mace_mp
from ase.optimize import BFGS
import matplotlib.pyplot as plt
from ase.io.trajectory import Trajectory
from ase.io import read
from ase.visualize import view
from ase.build import bulk, molecule, add_adsorbate
from ase.filters import ExpCellFilter
from ase.build import surface
import numpy as np
from ase.io import read
from ase.build import surface
import numpy as np

#comment in branch number_two
#adding a second comment

geo_files = ['geometry_1_layer_fixed.in', 'geometry_2_layer_fixed.in', 'geometry_3_layer_fixed.in']

calc = mace_mp(model='large', device='cuda', default_dtype='float64', dispersion=True)
for file in geo_files:
    optimised_energy = read(file)
    optimised_energy.calc = calc
    opt = BFGS(optimised_energy)
    opt.run(fmax=0.01)
    print(f"{file}: Energy = {optimised_energy.get_potential_energy()} eV")
