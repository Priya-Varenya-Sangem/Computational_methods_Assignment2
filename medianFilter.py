import numpy as np
import scipy 

def medianFilter(a, win_length):

    # Checkingif the window length is odd
    if (win_length % 2) == 0:
        print("window length must be an odd number")
        return 1

    a = np.array(a) #array with the degraded signal
    #clicks = np.array(clicks)#array with location of clicks

    # Padding zeros on either ends of the list a
    zpad = int((win_length - 1)/2)
    win_length = int(win_length)
    #apad = np.concatenate([np.zeros(zpad), a, np.zeros(zpad)])

    apad = np.pad(a, (zpad, zpad), 'constant', constant_values=(0, 0))

    for i in range(0, len(a) - 1):
        w = apad[i:(i + win_length)]
        w = np.sort(w)
        #print(w)
        if w[(win_length + 1)//2 - 1] != a[i]: #& clicks[i] == 1:
            a[i] = w[(win_length + 1)//2 - 1]

    return a





#a = [1, 2, 3, 6, 10, 7, 2, 1]
#m = medianFilter(a, 3)
#o = scipy.ndimage.median_filter(a,3)
#if np.array_equal(m,o):
#    print("The function passed the check")

#print(m)