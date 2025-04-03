#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 21:56:10 2025
@author: xydong


"""

# ****************
# MODULE IMPORTS
# ****************

from scipy.io import FortranFile
import numpy as np

# ****************
# FUNCTIONS
# ****************

def read_bptnr_file(bptnr_file, n_beads):
    '''
    Reads in files with .bptnr extension produced from DMD/PRIME20 simulations.
    

    Parameters
    ----------
    bptnr_file : unformatted binary file
        First value is collision number, followed by hydrogen bonding partners
    n_beads : integer
        Total number of coarse-grained beads in simulation.

    Returns
    -------
    bptnr : TYPE
        Column 1 is the bead number. Column 2 is the hydrogen bonding partner.

    '''

    dtype=[('col','i8'),('hb','i4',((n_beads)) )]
    collision_num=0 
    
    with FortranFile(bptnr_file,'r') as f:
      while (( collision_num%1e7) != 1.0):
        record=f.read_record(dtype)
        collision_num=record['col'][0]
        
    bptnr = np.vstack((np.linspace(1,n_beads,n_beads,dtype=int), record['hb'][0])).T

    return bptnr        
