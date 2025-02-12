# write your silhouette score unit tests here
import pytest
import numpy as np
from cluster import utils, silhouette 
from sklearn.metrics import silhouette_score

def test_silhouette_score():
    """
    Unit test that compares the Silhouette scoring function in our cluster module
    to `sklearn.metrics.silhouette_score`. 
    """
    
    # Firstly, let's make dataset to compare silhouette score with
    
    # Test dataset of 10 observations, measured across 4 features, with sd of 1
    test_clusters, test_cluster_labels  =  utils.make_clusters(n=10,
                                                               m=4,
                                                               scale = 1,
                                                               k = 3
                                                               )
    
    
    # # Calculate sklearn silhouette scores
    sklearn_scores = silhouette_score(test_clusters, test_cluster_labels)
    
    # Calulate our cluster module silhouette scores
    cluster_silhouette = silhouette.Silhouette()
    cluster_silhouette_scores = cluster_silhouette.score(test_clusters, test_cluster_labels)
    
    assert np.allclose(sklearn_scores, cluster_silhouette_scores.mean()), "cluster module silhouette scores are not similar to sklearn scores"



def test_invalid_n_labels_silhouette_score():
    """
    Unit test that checks that silhouette_score correctly fails when number of labels is < 2. 
    """
    # Test dataset of 10 observations, measured across 4 features, with sd of 1
    # Just one cluster
    test_clusters, test_cluster_labels  =  utils.make_clusters(n=10,
                                                               m=4,
                                                               scale = 1,
                                                               k = 1
                                                               )
    
    try:
        # Calulate our cluster module silhouette scores
        cluster_silhouette = silhouette.Silhouette()
        cluster_silhouette_scores = cluster_silhouette.score(test_clusters, test_cluster_labels)
        
        assert False, "silhouette_score function should have failed as number of clusters is < 2"
    
    except ValueError as e:
        
        assert str(e) == "Number of clusters must be >= 2",  "silhouette_score function should have failed with a different error as number of clusters is < 2"
      
