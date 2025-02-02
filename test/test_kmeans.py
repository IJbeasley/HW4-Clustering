# Write your k-means unit tests here
import pytest
from cluster import kmeans.KMeans


def bad_k_value_init()
    """
    
    """
    
    try:
      
      KMeans(k = 0)
      assert False, "Problem: no error"
    
    except ValueError as e:
      assert str(e) == "The number of requested clusters (k) must be a positive integer >= 1.", "Problem: wrong error"
      
  
