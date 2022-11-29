from scipy.io import wavfile
import numpy as np
from tqdm import tqdm
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline
from playsound import playsound

# Inputs
samplerate, data = wavfile.read('degraded.wav')
sr, clicks = wavfile.read('detectionfile.wav')
sr1, org = wavfile.read('clean.wav')

# Converting the inputs to numpy arrays

# data: Array containing the degraded signal
data = np.array(data)

# clicks: array containing locations of the clicks
clicks = np.array(clicks)

# org: array containing the uncorrupted signal
org = np.array(org)

fig, axs = plt.subplots(3)
plt.subplots_adjust(hspace=0.9)

for ax in axs.flat:
    ax.set(xlabel='time', ylabel='amplitude')

axs[0].plot(data)
axs[0].set_title("Degraded signal")

for i in range(0, len(clicks)):
    if clicks[i] != 0:
        clicks[i] = 1

# Creating inputs for CubicSplines function
x = []
y = []


for i in range(len(data)):
    if clicks[i] == 0:
        x.append(i)
        y.append(data[i])

# CubicSplines filter
c = CubicSpline(x, y, axis=0, bc_type='not-a-knot', extrapolate=None)

# Restoring the signal
r = data

for i in tqdm(range(len(clicks))):
    if clicks[i] == 1:
        r[i] = c(i)
    else:
        r[i] = data[i]

print("Done")

# Output
wavfile.write("output_cubicSplines.wav", samplerate, r)

# Playing the restored sound
playsound("output_cubicSplines.wav")


axs[1].plot(clicks)
axs[1].set_title("Location of clicks")

axs[2].plot(r)
axs[2].set_title("Restored signal")

# Plotting the signals
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


# MSE for cubic splines
mse1 = mse(r, org)
print("MSE for Cubic splines filtering is :" + str(mse1))
