import serial
import time
import csv
import numpy as np

import matplotlib.pyplot as plt 
from drawnow import *
from datetime import datetime

now = datetime.now()
 
dt_string = now.strftime("%d/%m/%Y %H:%M:%S.%f")

ser = serial.Serial('/dev/cu.usbserial-1410', 115200)
time.sleep(2)

# Read and record the data
data =[]                       # empty list to store the data
t_inc1 = "Time"
TN1 = "Temp. inlet coil"
TN2 = "Temp. outlet coil"
TN3 = "Temp. inlet radiator"
TN4 = "Temp. outlet radiator"

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
with open('Temperature_file.csv', mode='w') as Temperature_file:
    Temperature_writer = csv.writer(Temperature_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    Temperature_writer.writerow([t_inc1, TN1, TN2, TN3, TN4])

while True:
    try:
        with open('Temperature_file.csv', mode='a') as Temperature_file:
            Temperature_writer = csv.writer(Temperature_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

            for i in range(50):
                b = ser.readline()         # read a byte string
                string_n = b.decode()  # decode byte string into Unicode  
                string = string_n.rstrip() # remove \n and \r
                Tarr = string.split(",")
                T1.append(Tarr[0])
                T2.append(Tarr[1])
                T3.append(Tarr[2])
                T4.append(Tarr[3])

                Temperature_writer.writerow([dt_string, Tarr[0], Tarr[1], Tarr[2], Tarr[3]])
                now = datetime.now()
                dt_string = now.strftime("%d/%m/%Y %H:%M:%S.%f")
                print(dt_string, T1, T2, T3, T4)

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

