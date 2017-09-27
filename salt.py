from ase.build import molecule
atoms = molecule('NaCl')
atoms.write('salt.traj')