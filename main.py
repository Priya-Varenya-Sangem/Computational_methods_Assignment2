# Pre defined modules
import numpy as np
import scipy as sci
import playsound
from scipy.io import wavfile
import matplotlib.pyplot as plt


#Custom modules
from medianFilter import medianFilter

#Function to calculate mse
def mse(a, b):
    diff = np.subtract(a,b)
    squares = np.square(diff)
    mse1 = np.mean(squares)
    return mse1

#Inputs
samplerate, data = wavfile.read('degraded.wav')
sr, clicks = wavfile.read('detectionfile.wav')
sr1, org = wavfile.read('original.wav')

data = np.array(data)
clicks = np.array(clicks)
org = np.array(org)

print(clicks)


filterlength = 5

t = range(0,samplerate * len(data))

#Plotting graphs for input signals
#plt.plot(t,data,label = "Degraded signal")
#plt.plot(t,clicks,label = "Locations of corrupted data")

#print(len(data))
#print(len(clicks))

#Median filtered signal
y = medianFilter(data, filterlength)

y = np.array(y)

r = (1- clicks) * data + clicks * y



wavfile.write("restored.wav", samplerate, r)

mse1 = mse(org,r)
print(mse1)

#plt.show()