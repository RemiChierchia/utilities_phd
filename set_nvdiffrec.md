# Set nvdiffrec

Basically follow nerfstufio -> https://docs.nerf.studio/en/latest/quickstart/installation.html.
To install CUDA ToolKit I use conda `conda install -c "nvidia/label/cuda-11.7.0" cuda-toolkit`.
Probably nerfstudio is also downloading some additional libraries to make it work.

Still tho, I cannot run the train. At first I got an error and followed this solution -> https://github.com/NVlabs/nvdiffrast/issues/92.
Now I have another error and probably the previous fix didn't work.
One strategy could be to follow -> https://nvlabs.github.io/nvdiffrast/#linux for nvdiffrast and running it on a Docker. <- No it didn't work.

I did 2 modifications to make it work:
 - first I noticed `import nvdiffrast.torch as dr` wasn't the correct folder structure, probably I messed up something. My folder structure was `nvdiffrast>nvdiffrast>torch`. So I just copied the content of the second `nvdiffrast` in its parent dir.
 - second, I saw the code was pointing for the libraries to `/home/miniconda3/envs/test/lib64` that surprise I did't have as a folder at all in `test` environment. However, I have the folder `lib`, so I manually created a folder `lib64` and copied the content from `lib`.\
Now it is training! Later I will check if I can reproduce it.
