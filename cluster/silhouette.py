import numpy as np
from scipy.spatial.distance import cdist


class Silhouette:
    def __init__(self):
        """
        inputs:
            none
        """

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
        
  
      
      cluster_labels = np.unique(y)
      
      cluster_dict = {
                      label: np.where(y == label)[0].tolist() for label in cluster_labels
                      }

                     
      # Distance between every point in this dataset 
      all_distances = cdist(X, X)
      
      # Initialize matrix of average distance to points in a cluster, per point: 
      avg_clust_distance = np.zeros(
                                    (len(y), len(cluster_labels))
                                   )
      
      # Initialize array of silhoutte scores
      score = np.zeros(len(y))
                     
      # For a given point, calculate score: 
      for observation in range(0, len(y)):
      
      # Calculate the mean distance from this point to points for each cluster
          for cluster_id in cluster_labels: 
            
              cluster_points = cluster_dict.get(cluster_id, [])
              
              #if observation is in cluster_points, then remove it from cluster_points
              if observation in cluster_points:
                 
                 cluster_points = cluster_points.remove(observation)
              
              # How far is observation from points in this cluster on average?
              avg_clust_distance[observation, cluster_id] = all_distances[observation, cluster_points].mean()
          
          observation_cluster = y[observation]
          
          # How far is that point from other points in the same cluster (on average)?
          # Intra-cluster distance from this point:
          intra_dist = avg_clust_distance[observation, observation_cluster]
          
          # How far is the smallest mean distance to a different cluster?
          # Inter-cluster distance from this point: 
          inter_dist = np.delete(
                                 avg_clust_distance[observation], 
                                 observation_cluster
                                 )
          
          min_inter_dist = inter_dist.min()
          
          score[observation] = (min_inter_dist - intra_dist) / max(min_inter_dist, intra_dist)
      
      return score
                                 
          
          # 
          # 
          # 
          # intra_dist = all_distances[observation, cluster].mean()
          # 
          # # intra_dist = cdist(X[observation, ], 
          #                    np.delete(X[cluster,], observation, axis = 0)
          #                    )
          #                    
          # mean_intra_dist = intra_dist.mean()
          

          
          
          
          
          

