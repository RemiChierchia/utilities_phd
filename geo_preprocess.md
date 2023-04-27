# Geo-NeuS Data Preprocessing

First of all you are required to run COLMAP on your custom dataset. 
### `cameras.npz`
Once the folder `image` and `sparse/0` get generated you need to NeuS data preprocess -> https://github.com/Totoro97/NeuS/tree/main/preprocess_custom_data
To polish the PointCloud use `meshlab` and delete the points further away. Then keep following NeuS instructions to get the file `cameras.npz`.
### `pairs.txt`
To generate the file `pairs.txt` use -> https://github.com/GhiXu/ACMP/blob/574c8e078b6f7bd93237bd180d46f5adf1169a19/colmap2mvsnet_acm.py#L304 and run it specifying
`--dense_folder` and `--save_folder`.
### `points.ply` and `view_id.ply`
Use the file I created `sfm_pts_process.py` specifying `--data_dir`.
