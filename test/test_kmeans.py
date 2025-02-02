# Write your k-means unit tests here
import pytest
from cluster import kmeans


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
      
  
  
  
  
