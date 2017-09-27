from ase.io import read
from espresso import espresso
from ase.optimize import QuasiNewton

slab_ads=read('slab_ads.traj')
slab_ads.calc=espresso(pw=450,
                       dw=4500,
                       kpts=(5,7,1),
                       xc='PBE',
                       outdir='E_slab_ads',#espresso outdirectory saved
                                            #here                                    
                       convergence={'energy':1e-6,                                                 
                                    'mixing':0.05,
                                    'mixing_mode':'local-TF',
                                    'maxsteps':1000,
                                    'diag':'cg'})

relax_slab_ads=QuasiNewton(slab_ads,
                           logfile='opt.log',
                           trajectory='opt.traj',
                           restart='opt.pckl') #ase output
relax_slab_ads.run(fmax=0.05)

E_slab_ads=slab_ads.get_potential_energy()

print(E_slab_ads)