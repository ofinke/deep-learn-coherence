# CLASS FOR IMPORTING DATA FROM MATLAB FUNCTIONS

import matlab.engine
import matlab
import numpy as np
import matplotlib.pyplot as plt
import time

class mb():
    # constructor
    def __init__(self):
        self.engine = matlab.engine.start_matlab()
        return

    # method acquire data
    def acqdata(self, x, sig):
        return self.engine.retgauss(x, sig)

def main():
    instance = mb()
    x = np.linspace(-15,15, 1000).tolist()
    sig = [1.0, 2.0, 3.0, 4.0]
    
    now = time.time()
    for i, val in enumerate(sig):
        plt.plot(np.squeeze(np.array(instance.acqdata(x, val))))
    print("Calculation took: " + str(np.round(time.time()-now, 3)) + " seconds.")

    plt.show()

    return

if __name__ == "__main__":
    main()