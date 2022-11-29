import numpy as np
import scipy 

def medianFilter(a, win_length):
    
    """
    Takes in an array and window length of median filter and performs median filtering based on the window length
    
    Args:
        a (numpy.ndarray) : a numpy array
        win_length (int) : an odd number

    Returns:
        Array after median filtering with the given window length
    
    """

    # Checkingif the window length is odd
    if (win_length % 2) == 0:
        print("window length must be an odd number")
        return 1

    a = np.array(a) 
    

    # Padding zeros on either ends of the list a
    zpad = int((win_length - 1)/2)
    win_length = int(win_length)
    

    apad = np.pad(a, (zpad, zpad), 'constant', constant_values=(0, 0))

    for i in range(0, len(a) - 1):
        w = apad[i:(i + win_length)]
        w = np.sort(w)
        #print(w)
        if w[(win_length + 1)//2 - 1] != a[i]: 
            a[i] = w[(win_length + 1)//2 - 1]

    return a
