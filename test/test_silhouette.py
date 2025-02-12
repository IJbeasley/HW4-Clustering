# write your silhouette score unit tests here
import pytest
import numpy as np
from cluster import utils, silhouette 
from sklearn.metrics import silhouette_score

def test_silhouette_score():
    """
    Unit test that checks compares the Silhouette scoring function in our cluster module
    to `sklearn.metrics.silhouette_score`. 
    """
    
    # Firstly, let's make dataset to compare silhouette score with
    
    # Test dataset of 10 observations, measured in 4 dimensions, with sd of 1
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
