# Frequent issues

__glibc==x.xx=0 conflict is due to cuda-toolkit=11.3 version and gcc probably or something with conda, however running conda install -c conda-forge cudatoolkit=11.3 it worked. 
But, It doesen't install nvcc and other libraries but to run pytorch seems sufficient.
