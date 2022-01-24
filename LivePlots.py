import serial
import time
import csv
import numpy as np

import matplotlib.pyplot as plt 
from drawnow import *

ser = serial.Serial('/dev/cu.usbserial-1410', 115200)
time.sleep(2)

# Read and record the data
data =[]                       # empty list to store the data

TN1 = "temp. inlet coil"
TN2 = "temp. outlet coil"
TN3 = "temp. inlet radiator"
TN4 = "temp. outlet radiator"

Tarr = np.ones([])
"""
T1 = np.ones([])
T2 = np.ones([])
T3 = np.ones([])
T4 = np.ones([])
"""
T1 = []
T2 = []
T3 = []
T4 = []

cnt = 0
plt.ion()

def makeFig():
    plt.plot(T1, "ro-")
    plt.plot(T2, "ro-")
    plt.plot(T3, "b^-")
    plt.plot(T4, "b^-")
    plt.xlabel("time")
    plt.ylabel("Temp")

while True:
    try:
        with open('Temperature_file.csv', mode='w') as Temperature_file:
            Temperature_writer = csv.writer(Temperature_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            Temperature_writer.writerow([TN1, TN2, TN3, TN4])

            for i in range(50):
                b = ser.readline()         # read a byte string
                string_n = b.decode()  # decode byte string into Unicode  
                string = string_n.rstrip() # remove \n and \r
                Tarr = string.split(",")
                T1.append(Tarr[0])
                T2.append(Tarr[1])
                T3.append(Tarr[2])
                T4.append(Tarr[3])

                Temperature_writer.writerow([Tarr[0], Tarr[1], Tarr[2], Tarr[3]])
                print(T1, T2, T3, T4)

                data.append(string)           # add to the end of data list
                time.sleep(0.1)            # wait (sleep) 0.1 seconds
                drawnow(makeFig)
                plt.pause(0.0001)
                cnt = cnt + 1
                if (cnt > 60) :
                    T1.pop(0)
                    T2.pop(0)
                    T3.pop(0)
                    T4.pop(0)
                
        ser.close()
    except:
        print("err")
        ser.close()
        time.sleep(1)
        ser = serial.Serial('/dev/cu.usbserial-1410', 115200)

