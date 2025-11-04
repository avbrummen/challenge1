import numpy as np

def vector_mean(vector):
    """arithmetic mean of a series meow meow

    Parameters
    ----------
    vector : array-like
        A vector or series of numbers
  
    Returns
    -------
    mean
        Arithmetic mean
    
    """

    mean = np.sum(vector) / len(vector)

    return mean
