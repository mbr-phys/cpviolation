from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
#from shapely.ops import cascaded_union,polygonize
from scipy.spatial import Delaunay
#import shapely.geometry as geometry
#import pylab as pl
#import math

def exp_like(err,x,xt):
    like = 1
    for i in range(len(x)):
        like_i = (1/(np.sqrt(2*np.pi)*err[i]))*np.exp(-0.5*((x[i]-xt[i])/err[i])**2)
        like = like*like_i
    return like

def cov(x,y):
    xbar, ybar = x.mean(), y.mean()
    return np.sum((x-xbar)*(y-ybar))/(len(x)-1)

def cov_mat(X):
    return np.array([[cov(X[0],X[0]),cov(X[0],X[1])], \
                     [cov(X[1],X[0]),cov(X[1],X[1])]])

def cov_mat3(X):
    return np.array([[cov(X[0],X[0]),cov(X[0],X[1]),cov(X[0],X[2])], \
                     [cov(X[1],X[0]),cov(X[1],X[1]),cov(X[1],X[2])], \
                     [cov(X[2],X[0]),cov(X[2],X[1]),cov(X[2],X[2])]])

def chisq_simp(obs,the,sige,sigt):
    '''
        chisq val, all parameters lists of values, simple
    '''
    N = len(obs)
    chi = 0
    for i in range(N):
        sig = np.sqrt((sige[i]/1.96)**2 + (sigt[i]/1.96)**2)
        val = (obs[i]-the[i])/sig
        chi += val**2
    return chi

def chi_del2(chi_min,chis):
    '''
        computes delta chisq, for several CLs? so 2 sigma so 95.45 just now
    '''
    delt_chis = (chis-chi_min)
    hs = np.linspace(0,3.5,350)
    ts = np.linspace(-1,2,300)
    h_min,t_min = [],[]
    for i in range(len(hs)):
        for j in range(len(ts)):
            n = i*j
            if delt_chis[n] <= 5.99:
                h_min = np.append(h_min,hs[i])
                t_min = np.append(t_min,ts[j])

    return h_min, t_min

def alpha_shape(points, alpha, only_outer=True):
    """
    Compute the alpha shape (concave hull) of a set of points.
    :param points: np.array of shape (n,2) points.
    :param alpha: alpha value.
    :param only_outer: boolean value to specify if we keep only the outer border
    or also inner edges.
    :return: set of (i,j) pairs representing edges of the alpha-shape. (i,j) are
    the indices in the points array.
    """
    assert points.shape[0] > 3, "Need at least four points"

    def add_edge(edges, i, j):
        """
        Add an edge between the i-th and j-th points,
        if not in the list already
        """
        if (i, j) in edges or (j, i) in edges:
            # already added
            assert (j, i) in edges, "Can't go twice over same directed edge right?"
            if only_outer:
                # if both neighboring triangles are in shape, it's not a boundary edge
                edges.remove((j, i))
            return
        edges.add((i, j))

    tri = Delaunay(points)
    edges = set()
    # Loop over triangles:
    # ia, ib, ic = indices of corner points of the triangle
    for ia, ib, ic in tri.vertices:
        pa = points[ia]
        pb = points[ib]
        pc = points[ic]
        # Computing radius of triangle circumcircle
        # www.mathalino.com/reviewer/derivation-of-formulas/derivation-of-formula-for-radius-of-circumcircle
        a = np.sqrt((pa[0] - pb[0]) ** 2 + (pa[1] - pb[1]) ** 2)
        b = np.sqrt((pb[0] - pc[0]) ** 2 + (pb[1] - pc[1]) ** 2)
        c = np.sqrt((pc[0] - pa[0]) ** 2 + (pc[1] - pa[1]) ** 2)
        s = (a + b + c) / 2.0
        area = np.sqrt(s * (s - a) * (s - b) * (s - c))
        circum_r = a * b * c / (4.0 * area)
        if circum_r < alpha:
            add_edge(edges, ia, ib)
            add_edge(edges, ib, ic)
            add_edge(edges, ic, ia)
    return edges

def chi_del(chi_min,chis,hs,ts,parm):
    '''
        computes delta chisq, for several CLs? so 2 sigma so 95.45 just now
    '''
    h_min,t_min = [],[]
    for i in range(len(hs)):
        if (chis[i]-chi_min) <= parm:
            h_min = np.append(h_min,hs[i])
            t_min = np.append(t_min,ts[i])

    points = np.vstack([t_min,h_min]).T
    edges = alpha_shape(points,alpha=0.10,only_outer=True)

    return h_min, t_min, [edges,points]


