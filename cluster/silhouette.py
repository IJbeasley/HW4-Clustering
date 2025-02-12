import numpy as np
import math
from scipy.spatial.distance import cdist


class Silhouette:
    def __init__(self, metric: str = "euclidean"):
        """
        inputs:
            metric: As per sklearn.metrics.silhouette_score, 
            'The metric to use when calculating distance between instances in a feature array.
            Must be one of the options allowed by sklearn.metrics.pairwise_distances'

        """
        
        self.metric = metric

    def score(self, X: np.ndarray, y: np.ndarray) -> np.ndarray:
        """
        calculates the silhouette score for each of the observations

        inputs:
            X: np.ndarray
                A 2D matrix where the rows are observations and columns are features.

            y: np.ndarray
                a 1D array representing the cluster labels for each of the observations in `X`

        outputs:
            np.ndarray
                a 1D array with the silhouette scores for each of the observations in `X`
        """
       
        # Are provided X and y arrays valid: checks?
        if X.ndim != 2:
          
           raise ValueError("Provided mat should be a 2D matrix")
        
        if y.ndim != 1:
          
           raise ValueError("Provided labels should be a 1D array")
        
        if len(y) != X.shape[0]:
         
           raise ValueError("Provided X and y arrays are not compatible. Number of rows in X should = number of elements in Y")
        
  
        # What are the clusters?
        cluster_labels = np.unique(y)
        cluster_labels = np.sort(cluster_labels)
        
        # Are cluster labels valid: checks? 
        if len(cluster_labels) < 2:
           
           raise ValueError("Number of clusters must be >= 2")
         
        
        if len(cluster_labels) > X.shape[0] - 1: 
          
           raise ValueError("Silhouette score is only defined if number of clusters is <= number of observations - 1")
      
        # Match each observation to a cluster
        cluster_dict = {
                        label: np.where(y == label)[0].tolist() for label in cluster_labels
                       }

                     
        # Find the distance between every point in this dataset 
        all_distances = cdist(X, X, metric = self.metric)
      
        # Initialize a matrix of average distance to points in a cluster, per point: 
        avg_clust_distance = np.zeros(
                                     (len(y), len(cluster_labels))
                                     )
      
        # Initialize array of silhoutte scores
        score = np.zeros(len(y))
                     
        # For a given point, calculate silhoutte score: 
        for observation in range(0, len(y)):
            
            observation_cluster = y[observation]
      
            # Calculate the mean distance from this point to points for each cluster
            for cluster_id in cluster_labels: 
            
                cluster_points = cluster_dict.get(cluster_id, [])
              
                # if observation is in cluster_points, then remove it from cluster_points
                # (don't care about the distance between a point and itself)
                if observation in cluster_points:
                 
                   #cluster_points.remove(observation)
                   cluster_points = [p for p in cluster_points if p != observation]

                # How far is observation from points in this cluster on average?
                
                # If the only point in the same cluster as the observation, then let's make silhouette score for
                # this observation point 0. 
                # Achieve this by setting average cluster distance to Inf. 
                if not cluster_points:
                   avg_clust_distance[observation, cluster_id] = float('inf')
                else:
                   avg_clust_distance[observation, cluster_id] = all_distances[observation, cluster_points].mean()
          
          
            # How far is that point from other points in the same cluster (on average)?
            # Intra-cluster distance from this point:
            intra_dist = avg_clust_distance[observation, observation_cluster]
          
            if math.isinf(intra_dist):
               score[observation] = 0
            
            else:
               # How far is the smallest mean distance to a different cluster?
               # Inter-cluster distance from this point: 
               inter_dist = np.delete(
                                      avg_clust_distance[observation], 
                                      observation_cluster
                                      )
          
               min_inter_dist = inter_dist.min()

               score[observation] = (min_inter_dist - intra_dist) / max(min_inter_dist, intra_dist)
        
        return score

          

          
          
          
          
          

