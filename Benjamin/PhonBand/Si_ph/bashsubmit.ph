#!/bin/bash
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=2
#SBATCH --job-name=scf
#SBATCH --mem-per-cpu=4000M
#SBATCH --time=00:30:00
#SBATCH --mail-user=
#SBATCH --mail-type=ALL
#SBATCH --partition=Def

module purge
source /home/ucl/naps/gbrunin/SetEnv.sh intel13_intel

export OMP_NUM_THREADS=1
unset SLURM_CPUS_PER_TASK

MPI="mpirun"
MPIOPT="-np 2"
QE="/home/ucl/naps/gbrunin/q-e/bin/ph.x"

${MPI} ${MPIOPT} ${QE} < ph.Si.in > ph.Si.out

echo "--"
