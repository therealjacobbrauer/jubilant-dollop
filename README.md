# jubilant-dollop

Credits:
I mainly modified the code from Paul McWhorter's youtube video:
"Arduino with Python LESSON 11: Graphing and Plotting Live Data from Arduino with Matplotlib" 
which was very helpful, but used a single temperature sensor of a different type along with a pressure sensor. 
-------------

This repository is for the purpose of making real time data displays and simultaneously can write a csv file of the data points. 

The LivePlots.py script was setup to be ran on MacOS from terminal. 
It depends on the libraries: PySerial, time, CSV, NumPy, Matplotlib.pyplot, and drawnow. 

It relys on having the physical connection from an Arduino (I used an arduino Nano) to the main computer that is running the LivePlots.py script. 

The Arduino .ino code uses four max6675 chips with one type-K thermocouple each to plot the four temperatures live using the LivePlots.py script. 

<img src="jubilant-dollop/Four_temps_fig.png" class="img-responsive" alt=""> </div>
