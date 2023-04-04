# Use HPC

Clone your conda env -> `conda env export > environment.yml`

Copy files to remote folder -> `scp -r /path/to/local/dir user@remotehost:/path/to/remote/dir` to copy the code

Re-create on remote folder -> `conda env create -f environment.yml`

`get_project_codes` to see on bracewell which codes I have. 
Use one to ask a `sinteractive` node `sinteractive -A your_code_from_get_project_code -n 1 -c 8 -m 24GB -t 3:59:00 -g gpu:1`

Follow the instructions in run_job.q file to `sbatch` a job.
Then `sbatch -A your_code_from_get_project_code run_job.q`

To see the job running or in the queue `squeue -u my_ident`
