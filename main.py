# Pre defined modules
import numpy as np
import scipy as sci
from playsound import playsound
from scipy.io import wavfile
import matplotlib.pyplot as plt
from tqdm import tqdm
#from sklearn.metrics import mean_squared_error
from time import sleep



#Custom modules
from medianFilter import medianFilter

#Function to calculate mse
def mse(a, b):
    """
    Takes in two arrays and gives the Mean squared error 
    
    Args:
        a (numpy.ndarray) : a numpy array
        b (numpy.ndarray) : a numpy array
    
    """
    diff = np.subtract(a,b)
    squares = np.square(diff)
    mse1 = np.mean(squares)
    return mse1

#Inputs
samplerate, data = wavfile.read('degraded.wav')
sr, clicks = wavfile.read('detectionfile.wav')
sr1, org = wavfile.read('clean.wav')

print(type(data))

data = np.array(data)
clicks = np.array(clicks)
org = np.array(org)

#print(clicks)


filterlength = 5

r = np.zeros(len(data))
print("length of r"+ str(len(r)))
print(max(clicks))

for i in range(0,len(clicks)):
    #print("hello1")
    if clicks[i] != 0:
        clicks[i] = 1

for i in tqdm(range(0,len(clicks))):
    #print("hello1")
    if clicks[i] != 0:
        med = medianFilter(data[i - (filterlength//2): i + (filterlength//2)], filterlength)
        #print("hello2")
        #print(med)
        #r[i] = med[len(med)//2]
    #else:
        #print("hello3")
        #r[i] = data[i]

#r = np.array(r,dtype=np.int16)
#t = range(0,samplerate * len(data))

#Plotting graphs for input signals


#plt.plot(data)
#plt.label("Degraded signal")


#plt.plot(clicks)

#plt.show()
#plt.plot(t,data,label = "Degraded signal")
#plt.plot(t,clicks,label = "Locations of corrupted data")

#print(len(data))
#print(len(clicks))

#Median filtered signal
for i in tqdm(range(100)):
    y = medianFilter(data, filterlength)
    sleep(0.1)

y = np.array(y)

r = (1 - clicks) * data + clicks * y

#plt.rcParams["figure.figsize"] = [7.50, 3.50]
#plt.rcParams["figure.autolayout"] = True
#plt.xlabel("Time")

fig, axs = plt.subplots(3)
#fig.suptitle('Sharing both axes')
plt.subplots_adjust(hspace= 0.7)
axs[0].plot(data)
axs[0].set_title("Degraded signal")
axs[1].plot(clicks)
axs[1].set_title("Location of clicks")
axs[2].plot(r)
axs[2].set_title("Restored signal")
#axs[3].plot(y)

#plt.plot(r)
plt.show()

print(r)
print(r.dtype)
print(data)
print(type(data))
print(clicks.dtype)
print()
print(len(clicks))



wavfile.write("outputfile.wav", samplerate, r)
playsound("outputfile.wav")

mse1 = mse(org, r)
print(abs(mse1))
print(type(mse1))

#plt.show()