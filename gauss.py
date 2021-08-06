# function to create random gaussian distribution over specified x

import numpy as np

def gauss(x, sigma, noise=False):
    # normalized gaussian density function
    g = (1/(sigma*np.sqrt(2*np.pi)))*np.exp((-1/2)*((x/sigma)**2))

    if noise is True:
        noise = np.random.normal(0, 0.005, len(x))
        g = g + noise
    return g

