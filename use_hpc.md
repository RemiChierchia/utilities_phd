# Use HPC

Clone your conda env -> `conda env export > environment.yml`

Copy files to remote folder -> `scp -r /path/to/local/dir user@remotehost:/path/to/remote/dir` to copy the code

Re-create on remote folder -> `conda env create --prefix -f environment.yml`

`get_project_codes` to see on bracewell which codes I have. 
Use one to ask a `sinteractive` node `sinteractive -A your_code_from_get_project_code -n 1 -c 8 -m 24GB -t 3:59:00 -g gpu:1`

Follow the instructions in run_job.q file to `sbatch` a job.
Then `sbatch -A your_code_from_get_project_code run_job.q`

To see the job running or in the queue `squeue -u my_ident` or `slurmtop -u my_ident`

`scancel job_id` to cancel a job

## Run a Job Script

Example:
```
#!/bin/bash

#SBATCH --time=166:00:00 # walltime
#SBATCH --nodes=1 # Number of computer nodes
#SBATCH --ntasks-per-node=1 # number of process per node
#SBATCH --cpus-per-task=4 # number of threads per process
#SBATCH --mem-per-cpu=16G # memory per node
#SBATCH --gres=gpu:1 # number of gpus

cd /scratch2/chi215/geoneus_transfer

module load miniconda3

source ~/.bashrc

conda activate /scratch2/chi215/geoneus_transfer/geoneus_env

python exp_runner.py --mode train --conf ./confs/womask.conf --case DTU/scan63

python exp_runner.py --mode validate_mesh --conf ./confs/womask.conf --case DTU/scan63 --is_continue
```
With `#SBATCH` you can set the settings of the `sinteractive` node, so you can just run the command `sbatch -A your_code_from_get_project_code run_job.q`.
When using a `conda` environment, you need firstly to explicit `--prefix` when creating it to install the environment in the local (on `/scratch2/my_ident/<current_folder>`) current folder.
Then it is important to use `source ~/.bashrc` before activating the environment so the node knows where to find the installed libraries. Then the conda environment can be correctly activated.
