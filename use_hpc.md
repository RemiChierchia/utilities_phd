# Use HPC

Clone your conda env -> `conda env export > <env_name>.yml`

Copy files to remote folder -> `scp -r /path/to/local/dir user@remotehost:/path/to/remote/dir` to copy the code

Re-create on remote folder -> `conda env create -f <env_name>.yml --prefix <env_name>`

`get_project_codes` to see on bracewell which codes I have. 
Use one to ask a `sinteractive` node `sinteractive -A OD-225414 -n 1 -c 8 -m 24GB -t 3:59:00 -g gpu:1`

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

When using a `conda` environment, you need firstly to explicit `--prefix` when creating it to install the environment in the local (on `/scratch2/my_ident/<current_folder>`) current folder (`conda create --prefix <env_name> python=<version>`).
Then it is important to use `source ~/.bashrc` before activating the environment so the node knows where to find the installed libraries. Then the conda environment can be correctly activated.

## Mount Remote Folder

`sshfs chi215@bracewell.hpc.csiro.au:/scratch2/chi215/<folder_to_mount> /home/chi215/<name_to_mount>`

## Recreating Venvs/Testing Papers' Code

Refer to this `.sh`
```
# Set root directory
CFPP_ROOT_DIR=<CFPP_ROOT_DIR>
cd CFPP_ROOT_DIR

# Load modules
module load miniconda3/4.9.2
conda deactivate

# Create conda enviroment
mkdir ./CONDA_PKGS/
export CONDA_PKGS_DIRS=${CFPP_ROOT_DIR}/CONDA_PKGS/ #important step to do also after each conda activation, else it installs in the home dir
conda create python=<VERSION> --prefix ./CONDA_ENV/
conda activate ./CONDA_ENV/

# Load more Modules
module load <GCC>
module load <CMAKE>
module load <CUDA>

# Install pip stuff
pip install <>

# Install conda stuff
conda install <>
```

It is important also to check with `module list` or `conda list` the modules loaded, sometimes might have other CUDA modules loaded which crash when trying to call CUDA libs; otherwise try to load already existing modules. For example if needed to build from source code you might need to load `gcc` and `cmake` modules.

## Set SSH key
`ssh-keygen -t rsa -b 2048` if you don't have a key yet

`ssh-copy-id id@server` and insert password

## Use non-server HPCs (sleipnir, shazza, ...)
`screen -S <process_name>` to create a virtual screen to keep the job running when disconnecting from ssh
Then activate your conda env etc like normally and run your script.
To exit the screen bash do `ctrl+A ctrl+D` in sequence.
