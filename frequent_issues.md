# Frequent issues

### Cannot install CUDA 11.3 + tiny cuda for some reason
Either ninja/cmake/gcc or I don't know.

`__glibc==x.xx=0` conflict is due to `cuda-toolkit=xx.x` version and gcc probably or something with conda, however running `conda install -c conda-forge cudatoolkit=xx.x` it worked. 
But, **it doesen't install nvcc nor other libraries** but to run pytorch seems sufficient.
