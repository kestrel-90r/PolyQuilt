import numpy as np


def Cross2D( a , b ) :
    """Return the scalar cross product of 2D vectors.

    NumPy 2.x no longer accepts 2D vectors in ``np.cross``.  Keeping the
    operation explicit preserves the old 2D result for both single vectors
    and arrays of vectors.
    """
    return a[..., 0] * b[..., 1] - a[..., 1] * b[..., 0]


def IntersectPointInSphere( point , points , radius ) :
    rt = np.sum( (points - point) ** 2 , axis = -1 )

    rr = np.float32( radius * radius )
    ri = np.where( rt <= rr )

    return ri[0]

def DistancePointToLine2D( co , lines , radius , isRetPoint = True ) :
    lnum = lines.shape[0]
    a = lines[:,0:1].reshape(lnum,2)
    b = lines[:,1:2].reshape(lnum,2)

    ab = a - b
    ba = -ab
    pa = co - a 
    pb = co - b

    t0 = (ba[:,None,:] @ pa[...,None]).ravel()
    t1 = (ab[:,None,:] @ pb[...,None]).ravel()
    idx = np.where( (t0 > 0) & (t1 > 0) )

    ba = ba[idx]
    pa = pa[idx]
    dist = np.abs( Cross2D( ba , pa ) / np.linalg.norm( ba , axis=-1 ) )

    return idx[0][ dist < radius ]

def IntersectLine2DLines2D( line , lines , isRetPoint = True ) :
    nline = lines.shape[0]
    p1 = line[0].reshape(2)
    p2 = line[1].reshape(2)
    p3 = lines[:,0:1].reshape(nline,2)
    p4 = lines[:,1:2].reshape(nline,2)

    t21 = p2 - p1
    t43 = p4 - p3
    t31 = p3 - p1

    d = Cross2D( t21 , t43 )

    with np.errstate(divide='ignore'):
        u = Cross2D( t31 , t43 ) / d
        v = Cross2D( t31 , t21 ) / d

    hit = (d != 0) & (u > 0) & (u < 1) & (v > 0) & (v < 1)
    idx = np.where( hit == True )[0]

    if isRetPoint :
        pts = p1 + u[idx].reshape( idx.shape[0] , 1 ) * t21.reshape(1,2)
        return idx , pts
    else :
        return idx
