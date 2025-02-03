# Write your k-means unit tests here
import pytest
import numpy as np
from cluster import utils, kmeans


def test_kmeans():
    """
    """
    
    pass

#################### Unit test of initalization variables #####################

def invalid_k_init():
    """
    
    Unit test to check whether KMeans initalisation correctly fails when k=0 is provided. 
    
    """
    
    try:
      
      KMeans(k = 0)
      assert False, "Problem: no error"
    
    except ValueError as e:
      assert str(e) == "The number of requested clusters (k) must be a positive integer >= 1.", "Problem: wrong error"
      
  
def invalid_tol_init():
    """
    
    Unit test to check whether Kmeans initalisation correctly fails when tol=0 is provided
    
    """
    
    try: 
      KMeans(k=2, tol=0)
      
      assert False, "Problem: no error"
    
    except ValueError as e:
      assert str(e) == "The minimum error tolerance (tol) must be positive",  "Problem: wrong error"
      
def invalid_max_iter():
    """
    
    Unit test to check whether Kmeans initalisation correctly fails when max_iter=0 is provided
    
    """
    
    try:
      KMeans(k=2, max_iter=0)
      
      assert False,  "Problem: no error"

    except ValueError as e:
      assert str(e) == "The maximum number of iterations (max_iter) must be a positive integer >= 1."  
      
##################### Unit tests of valid matrix format #######################

def invalid_mat_dim():
     """
     
     Unit test to check whether Kmeans fitting correctly fails when provided matrix dimensions are
     inappropriate (e.g. 3D rather than 2D)
     
     """
     pass
     
     #test_mat = 
     
     # try:
     #   kmeans = KMeans(k=2)
     #   kmeans.fit()
     
  
def incompatible_mat_k():
     """
     
     Unit test to check whether Kmeans fitting correctly fails when requested number of clusters is > 
     number of observations in provided matrix (mat).
     
     
     """
     
     pass
   
   
