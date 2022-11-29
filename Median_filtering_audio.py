# Pre defined modules
import numpy as np
import scipy as sci
from playsound import playsound
from scipy.io import wavfile
import matplotlib.pyplot as plt
from tqdm import tqdm

# Custom modules
from medianFilter import medianFilter

# Inputs

samplerate, data = wavfile.read('degraded.wav')
sr, clicks = wavfile.read('detectionfile.wav')
sr1, org = wavfile.read('clean.wav')

filterlength = 11

# Converting the inputs to numpy arrays

# data: Array containing the degraded signal
data = np.array(data)

# clicks: array containing locations of the clicks
clicks = np.array(clicks)

# org: array containing the uncorrupted signal
org = np.array(org)

for i in range(0, len(clicks)):
    if clicks[i] != 0:
        clicks[i] = 1

# Creating an array of zeros for storing the restored signal

# Median filtered data
y = medianFilter(data, filterlength)
y = np.array(y)

# Restoring the signal by replacing the clicks with the median filtered data
print("Restoring the signal")
for i in tqdm(range(100)):
    r = (1 - clicks) * data + clicks * y
print("Done")

# Declaring the array 'r' as dtype np.int16 inorder to avoid issues with memory
#r = np.array(r,dtype=np.int16)

# Output
wavfile.write("outputfile.wav", samplerate, r)

# Playing the restored sound
playsound("outputfile.wav")

# Plotting the signals

fig, axs = plt.subplots(3)
plt.subplots_adjust(hspace=0.9)
for ax in axs.flat:
    ax.set(xlabel='time', ylabel='amplitude')

axs[0].plot(data)
axs[0].set_title("Degraded signal")

axs[1].plot(clicks)
axs[1].set_title("Location of clicks")

axs[2].plot(r)
axs[2].set_title("Restored signal")

plt.show()


# Defining a function to calculate MSE

def mse(a, b):
    """
    Takes in two arrays and gives the Mean squared error 

    Args:
        a (numpy.ndarray) : a numpy array
        b (numpy.ndarray) : a numpy array

    Returns:
        mse1 (numpy.float64) : Returns the Mean square error between arrays a and b

    """
    a, b = a.astype(np.float64), b.astype(np.int64)
    diff = np.subtract(a, b)
    squares = np.square(diff)
    mse1 = np.mean(squares)

    return mse1


# Calculating MSE between restored and original signals
M = []
I = []

print("Calculating MSEs")
for i in tqdm(range(3, 35, 2)):
    y = medianFilter(data, i)
    y = np.array(y)

    r = (1 - clicks) * data + clicks * y

    M.append(mse(r, org))
    I.append(i)
print("Done")
print(min(M))

# Plotting the MSE Values
plt.figure(2)
plt.plot(I, M)
plt.xlabel('Index')
plt.ylabel('MSE')
plt.title("MSE for different filter length")
plt.show()
