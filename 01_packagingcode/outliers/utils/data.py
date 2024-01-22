from sklearn.datasets import make_blobs

def create_data():
    '''
    imports the make_blobs function from the sklearn.datasets module. 
    the make_blobs function is used to generate synthetic data with clusters of points.
    '''
    n_samples = 300                                         # total number of samples in the dataset
    outliers_fraction = 0.15                                # proportion of outliers in the dataset
    n_outliers = int(outliers_fraction * n_samples)         # generate total number of outliers
    n_inliers = n_samples - n_outliers                      # generate total number of non-outliers

    blobs_params = dict(random_state=0, 
                        n_samples=n_inliers, 
                        n_features=2)
    data = make_blobs(centers=[[0, 0], [0, 0]], 
                      cluster_std=0.5, 
                      **blobs_params)[0]
    return data