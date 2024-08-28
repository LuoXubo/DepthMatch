"""
@Description :   点云可视化
@Author      :   Xubo Luo 
@Time        :   2024/08/28 09:52:28
"""

import numpy as np
import open3d as o3d
 
print("Load a ply point cloud, print it, and render it")
pcd = o3d.io.read_point_cloud("outputs/groot2.ply")
print(pcd)
print(np.asarray(pcd.points))
o3d.visualization.draw_geometries([pcd])