import pytest
import mpi4py
from dolfin import *
from mpi4py.MPI import COMM_WORLD as comm
import h5py

def test_mpi4py():
    assert True
    
def test_h5py():
    f = h5py.File('tmp.h5', 'w', driver='mpio', comm=comm)
