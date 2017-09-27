from ase.build import molecule
atoms = molecule('H2O')
atoms.write('water.traj')