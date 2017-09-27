from ase import Atoms
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms
from ase.optimize import QuasiNewton
from ase.build import surface, fcc111, add_adsorbate
from ase.spacegroup import crystal
from ase.visualize import view
from ase.io import write
from ase.io import read

#the paths to your .traj file
Pt_slab_path = 'Pt_111.traj'
ads_CO_path = 'ads_CO.traj'

#the height in angstroms the gas will be above the slab
h = 1.85

#read in the .traj files and put them into variables
Pt_slab = read(Pt_slab_path)
CO_molecule = read(ads_CO_path)

#these following lines will perform a calculation to slightly optimize the #position of the gas on the slab, but is no substitute for DFT calculations
CO_molecule.set_calculator(EMT())
Pt_slab.set_calculator(EMT())

#add the adsorbate to the slab. Change the position numbers for putting the gas in #a different spot
add_adsorbate(Pt_slab, CO_molecule, h, position=(1, 1))

constraint = FixAtoms(mask=[a.symbol != 'H' for a in Pt_slab])
Pt_slab.set_constraint(constraint)
#run the EMT optimization and write to a file
dyn = QuasiNewton(Pt_slab, trajectory='Pt+CO.traj')
dyn.run(fmax=0.05)

#open a GUI to inspect the adsorbed gas
view(Pt_slab)