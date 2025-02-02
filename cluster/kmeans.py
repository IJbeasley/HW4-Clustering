import numpy as np
from scipy.spatial.distance import cdist
import warnings


class KMeans:
    def __init__(self, k: int, tol: float = 1e-6, max_iter: int = 100):
        """
        In this method you should initialize whatever attributes will be required for the class.

        You can also do some basic error handling.

        What should happen if the user provides the wrong input or wrong type of input for the
        argument k?

        inputs:
            k: int
                the number of centroids to use in cluster fitting
            tol: float
                the minimum error tolerance from previous error during optimization to quit the model fit
            max_iter: int
                the maximum number of iterations before quitting model fit
        """
        
        if k < 1: 
          raise ValueError("The number of requested clusters (k) must be a positive integer >= 1.")
        
        if tol <= 0:
            raise ValueError("The minimum error tolerance (tol) must be positive")
          
        if max_iter < 1:
            raise ValueError("The maximum number of iterations (max_iter) must be a positive integer >= 1.")

        
        

    def fit(self, mat: np.ndarray):
        """
        Fits the kmeans algorithm onto a provided 2D matrix.
        As a bit of background, this method should not return anything.
        The intent here is to have this method find the k cluster centers from the data
        with the tolerance, then you will use .predict() to identify the
        clusters that best match some data that is provided.

        In sklearn there is also a fit_predict() method that combines these
        functions, but for now we will have you implement them both separately.

        inputs:
            mat: np.ndarray
                A 2D matrix where the rows are observations and columns are features
        """
        
        n_observations = mat.shape[0]
        n_features = mat.shape[1]
        
        if n_observations <= 1 or n_features < 1:
            raise ValueError("Check input matrix: the number of observations (rows) should be > 1 " + 
                             "and the number of features should be >= 1.")
        
        # is there sufficent number of observations for 
        # the number of requested clusters
        if self.k > n_observations:
           raise ValueError("The number of requested clusters" + k + 
                            "is > than the number of observations (rows) in mat " + mat.shape[0]
                            )

        
        # Check in case user has put  
        if n_observations < n_features: 
           warnings.warn("The number of features" + n_features +  
                         " is greater than the number of observations"  + n_observations + 
                         " in provided mat. " + 
                         "Check that the rows in mat correspond to observations.")
                         
        
                         
        # Initialize m to k random values
        # For each data point x, find the closest m_i.
        # Compute new m_i’s to be the centroid (average) of the closest points found in (2).
        #Compute max change in an m_i from the previous m_i.
        #Repeat (2) through (4) until the change in centroid is less than some epsilon.

        

    def predict(self, mat: np.ndarray) -> np.ndarray:
        """
        Predicts the cluster labels for a provided matrix of data points--
            question: what sorts of data inputs here would prevent the code from running?
            How would you catch these sorts of end-user related errors?
            What if, for example, the matrix is of a different number of features than
            the data that the clusters were fit on?

        inputs:
            mat: np.ndarray
                A 2D matrix where the rows are observations and columns are features

        outputs:
            np.ndarray
                a 1D array with the cluster label for each of the observations in `mat`
        """

    def get_error(self) -> float:
        """
        Returns the final squared-mean error of the fit model. You can either do this by storing the
        original dataset or recording it following the end of model fitting.

        outputs:
            float
                the squared-mean error of the fit model
        """

    def get_centroids(self) -> np.ndarray:
        """
        Returns the centroid locations of the fit model.

        outputs:
            np.ndarray
                a `k x m` 2D matrix representing the cluster centroids of the fit model
        """
