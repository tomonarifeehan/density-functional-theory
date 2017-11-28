#!/bin/bash
#PBS -l nodes=1:ppn=14
#PBS -l walltime=5:00:00
#PBS -q joe-fast
#PBS -N test
#PBS -o stdout
#PBS -e stderr

cd $PBS_O_WORKDIR
source  /gpfs/pace1/project/chbe-medford/medford-share/envs/espresso-5.1.r11289-pybeef_ase3.13_cust_esp


python calc.py