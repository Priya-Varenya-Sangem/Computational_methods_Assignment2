# Pre defined modules
import numpy as np
import scipy as sci
from playsound import playsound
from scipy.io import wavfile
import matplotlib.pyplot as plt
from tqdm import tqdm

#Custom modules
from medianFilter import medianFilter

#Inputs

samplerate, data = wavfile.read('degraded.wav')
sr, clicks = wavfile.read('detectionfile.wav')
sr1, org = wavfile.read('clean.wav')
filterlength = 5

#Converting the inputs to numpy arrays

data = np.array(data)
clicks = np.array(clicks)
org = np.array(org)

#Creating an array of zeros for storing the restored signal

r = np.zeros(len(data))

for i in tqdm(range(0,len(clicks))):
    #print("hello1")
    if clicks[i] != 0:
        med = medianFilter(data[i - (filterlength//2): i + (filterlength//2)], filterlength)
        #print(med)
        r[i] = med[len(med)//2]
    else:
        r[i] = data[i]

print("Done")

#Declaring the array 'r' as dtype np.int16 inorder to avoid issues with memory
r = np.array(r,dtype=np.int16)

#Output
wavfile.write("outputfile.wav", samplerate, r)

#Playing the restored sound
playsound("outputfile.wav")

#Plotting the signals
fig, axs = plt.subplots(3)
plt.subplots_adjust(hspace= 0.7)

axs[0].plot(data)
axs[0].set_title("Degraded signal")

axs[1].plot(clicks)
axs[1].set_title("Location of clicks")

axs[2].plot(r)
axs[2].set_title("Restored signal")

plt.show()


#Defining a function to calculate MSE

def mse(a, b):
    """
    Takes in two arrays and gives the Mean squared error 
    
    Args:
        a (numpy.ndarray) : a numpy array
        b (numpy.ndarray) : a numpy array

    Returns:
        mse1 (numpy.float64) : Returns the Mean square error between arrays a and b
    
    """
    diff = np.subtract(a,b)
    squares = np.square(diff)
    mse1 = np.mean(squares)
    
    return mse1

#Calculating MSE between restored and original signals
mse1 = mse(r, org)
print(abs(mse1))




