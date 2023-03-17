# Set_Instant_ngp

https://github.com/NVlabs/instant-ngp#building-instant-ngp-windows--linux

Installed all requirements also the (Optional).
Follow closely the section "Building instant-ngp (Windows & Linux)" and this guide -> https://bipul-mohanto.github.io/posts/2022/06/How%20to%20Install%20OptiX%20on%20Ubuntu%2020.04.01/

I had problems in installing Optix, especially because of the NVIDIA signing key that need to be updated -> https://developer.nvidia.com/blog/updating-the-cuda-linux-gpg-repository-key/. In my case I had to follow the seciton "Alternate method: Manually install the new signing key" because funny enough, the command "apt-key" is deprecated and I am not able to delete the old signing key.

To install the NVIDIA-Toolkit I followed -> https://developer.nvidia.com/cuda-downloads?target_os=Linux&target_arch=x86_64&Distribution=Ubuntu&target_version=22.04&target_type=deb_local and preferred to install the deb local installer

For the cmake of Optix you need to go inside the folder extracted and then in SDK. There run "cmake .." and then "make -j 8" (or more cores).

The nvcc command was not installed until I followed this link -> https://askubuntu.com/questions/885610/nvcc-version-command-says-nvcc-is-not-installed where you have to add it in the .bashrc file to make it visible.

Once Optix was installed I followed the instructions on the instant-ngp repo and managed to build it; now time to test!
