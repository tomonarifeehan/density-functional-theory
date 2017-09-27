from espresso import espresso
from ase.io import read
from ase.optimize import QuasiNewton
atoms = read('water.traj')
atoms.set_pbc([1,1,1])
atoms.set_cell([10,10,10])
calc = espresso()
atoms.set_calculator(calc)
relax = QuasiNewton(atoms)
relax.run()