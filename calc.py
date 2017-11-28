from ase.io import read
from espresso import espresso
from ase.optimize import QuasiNewton


traj_list = ['Pt+CO','Pt_111','ads_CO']

energy_list = []
for traj_name in traj_list:
    slab_ads=read(traj_name+'.traj')
    slab_ads.calc=espresso(pw=400,
            dw=4500,
            kpts=(5,5,1),
            xc='PBE',
            outdir='E_slab_ads',
            convergence={'energy':1e-6,
                'mixing':0.05,
                'mixing_mode':'local-TF',
                'maxsteps':1000,
                'diag':'cg'})
    relax_slab_ads=QuasiNewton(slab_ads,
            logfile='opt_'+traj_name+'.log',
            trajectory='opt_'+traj_name+'.traj',
            restart='opt_'+traj_name+'.pckl')
    relax_slab_ads.run(fmax=0.05)
    E_slab_ads=slab_ads.get_potential_energy()
    energy_list.append(E_slab_ads)
    print(E_slab_ads)

print(energy_list[0]-energy_list[1]-energy_list[2])
