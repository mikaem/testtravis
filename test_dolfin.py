import pytest
import mpi4py
from dolfin import *
from mpi4py.MPI import COMM_WORLD as comm
import h5py

def test_dolfin():
    mesh = UnitSquareMesh(4, 4)
    V = FunctionSpace(mesh, 'CG', 1)
    u = interpolate(Expression("x[0]"), V)
    
def test_h5py():
    f = h5py.File('tmp.h5', 'w', driver='mpio', comm=comm)
