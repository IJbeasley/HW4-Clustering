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
                     label: np.where(cluster_id == label)[0].tolist() for cluster_id in cluster_labels
                     }
                     
      # For a given point
      
      for observation in range(0, len(y)):
        
          # What cluster is that point in?
          cluster_id = y[observation]
          cluster = cluster_dict.get(cluster, [])
        
          # How far is that point from other points in the same cluster (on average)?
          # Intra-cluster distance from this point:
          
          intra_dist = cdist(X[observation, ], 
                             np.delete(X[cluster,], observation, axis = 0)
                             )
                             
          mean_intra_dist = intra_dist.mean()
          
          # How far is the smallest mean distance to a different cluster?
          # Inter-cluster distance from this point: 
          
          
          

