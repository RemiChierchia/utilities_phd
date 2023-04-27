import numpy as np
import argparse
import os
import trimesh

import read_write_colmap_model as read_model

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Collect points and view_id')

    parser.add_argument('--data_dir', required=True, type=str, help='data directory.')

    args = parser.parse_args()

    model_dir = os.path.join(args.data_dir, 'sparse/0')

    try:
        os.path.exists(model_dir)
    except os.error:
        print(model_dir + ' doesn\'t exist!')
    
    cameras, images, points3D = read_model.read_model(model_dir)

    all_points = np.empty((len(points3D), 3))
    view_id = [[] for i in range(len(images))]

    #for i, j in zip(points3D, range(len(points3D))):
        #all_points[j] = points3D[i][1]

        #print(points3D[i][4])
        #print(len(points3D[i][4]))
        #for p in range(len(points3D[i][4])):
            #print(points3D[i][4][p])
            #view_id[points3D[i][4][p]-1].append(points3D[i][0])
    
    sparse_points = trimesh.load(os.path.join(args.data_dir, "sparse_points_interest.ply"), process=False)
    sparse = []
    for i in sparse_points:
        sparse.append(i)

    for i in range(len(sparse)):
        #for j in range(len(all_points)):
        #point_found = False
        for p in points3D:
            #while point_found != True:
                # if sparse[i].all() == points3D[p][1].all():
            if np.allclose(sparse[i], points3D[p][1]):
                #print(sparse[i])
                #print(points3D[p][1])
                #breakpoint()
                #point_found = True
                for v in range(len(points3D[p][4])):
                    view_id[points3D[p][4][v]-1].append(i)
            #break
            # print(sparse[i])
            # print
            # breakpoint()
            # point_found = False
            # j = 0
            # while point_found != True:
            #     if model_sparse_points[i][:3] == all_points[j]:
            #         point_found == True
            #     else:
            #         j=j+1

    # Normalize
    print(np.max(sparse, axis=0))
    print(np.min(sparse, axis=0))
    bbox_max = np.max(sparse, axis=0)
    bbox_min = np.min(sparse, axis=0)
    center = (bbox_max + bbox_min) * 0.5
    radius = np.linalg.norm(sparse - center, ord=2, axis=-1).max()
    pcl = (1./radius)*(sparse - center)
    sparse = pcl
    print(np.max(sparse, axis=0))
    print(np.min(sparse, axis=0))

    with open(os.path.join(model_dir, 'points.npy'), 'wb') as f:
        np.save(f, sparse)
    with open(os.path.join(model_dir, 'view_id.npy'), 'wb') as f:
        np.save(f, view_id)
        