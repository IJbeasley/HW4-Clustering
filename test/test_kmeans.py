# Write your k-means unit tests here
import pytest
import numpy as np
from cluster import utils, kmeans as km


def test_kmeans_predict():
    """
    
    Unit test that checks that our KMeans cluster label predictions are accurate on example data
    * to add: within expected accurarcy / misclassification?
    
    """
    
    # Create test dataset of 100 observations, measured in 2 dimensions, with small sd
    test_clusters, test_cluster_labels  =  utils.make_clusters(n=100,
                                                               m=2,
                                                               scale = 0.001,
                                                               k = 2
                                                               )

    # save visualisation of this dataset
    utils.plot_clusters(mat = test_clusters,
                        labels = test_cluster_labels,
                        filename = "figures/unit_test_data_2d.png")
    
    # run kmeans model fitting and prediction: 
    kmeans_model = km.KMeans(k = 2)
    kmeans_model.fit(mat = test_clusters)
    predicted_labels = kmeans_model.predict(mat = test_clusters)
    
    # assert np.sum(predicted_labels) == np.sum(test_cluster_labels), "KMeans predict is not returning expected labels"
    # 
    # assert np.allclose(predicted_labels, test_cluster_labels) or np.allclose(np.abs(predicted_labels - 1), test_cluster_labels), "KMeans predict is not returning expected labels"
    # 
    pass

#################### Unit test of initalization variables #####################

def test_invalid_k_init():
    """
    
    Unit test to check whether KMeans initalisation correctly fails when k=0 is provided. 
    
    """
    
    try:
      
      km.KMeans(k = 0)
      assert False, "Problem: no error"
    
    except ValueError as e:
      assert str(e) == "The number of requested clusters (k) must be a positive integer >= 1.", "Problem: wrong error"
      
  
def test_invalid_tol_init():
    """
    
    Unit test to check whether Kmeans initalisation correctly fails when tol=0 is provided
    
    """
    
    try: 
      km.KMeans(k=2, tol=0)
      
      assert False, "Problem: no error"
    
    except ValueError as e:
      assert str(e) == "The minimum error tolerance (tol) must be positive",  "Problem: wrong error"
      
def test_invalid_max_iter():
    """
    
    Unit test to check whether Kmeans initalisation correctly fails when max_iter=0 is provided
    
    """
    
    try:
      km.KMeans(k=2, max_iter=0)
      
      assert False,  "Problem: no error"

    except ValueError as e:
      assert str(e) == "The maximum number of iterations (max_iter) must be a positive integer >= 1."  
      
##################### Unit tests of valid matrix format #######################

def test_invalid_mat_dim():
     """
     
     Unit test to check whether Kmeans fitting correctly fails when provided matrix dimensions are
     inappropriate (e.g. 3D rather than 2D)
     
     """
     pass
     
     #test_mat = 
     
     # try:
     #   kmeans = KMeans(k=2)
     #   kmeans.fit()
     
  
def test_incompatible_mat_k():
     """
     
     Unit test to check whether Kmeans fitting correctly fails when requested number of clusters is > 
     number of observations in provided matrix (mat).
     
     
     """
     
     pass
   
   
