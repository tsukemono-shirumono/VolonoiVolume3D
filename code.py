import numpy as np
import random
from scipy.spatial import Voronoi, ConvexHull

def VolonoiVolumes(rs,periodic_boundary=None):
    N=len(rs)
    if periodic_boundary is not None:
        X_MAX,Y_MAX,Z_MAX=periodic_boundary
        boundarys=np.array( [[x,y,z] for x in [0,X_MAX,-X_MAX] for y in [0,Y_MAX,-Y_MAX] for z in [0,Z_MAX,-Z_MAX]] )
        rs_replica=np.concatenate([boundary+rs for boundary in boundarys])
    else:
        rs_replica=rs
    
    vor = Voronoi(rs_replica)
    volumes=[]
    for reg_num in vor.point_region[:N]:
        indices = vor.regions[reg_num]
        if -1 in indices:
            volumes.append(np.nan)
        else:
            polygon=vor.vertices[indices]
            volumes.append( ConvexHull(polygon).volume )
    return np.array(volumes)
