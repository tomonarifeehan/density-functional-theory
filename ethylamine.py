from ase.build import molecule
atoms = molecule('CH3CH2NH2')
atoms.write('ethylamine.traj')