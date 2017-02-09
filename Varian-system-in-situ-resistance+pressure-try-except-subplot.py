# -*- coding: utf-8 -*-
"""
Created on Mon May 30 15:28:41 2016

@author: feliciaullstad

set to local network only
sudo ifconfig eth0 169.254.1.2 broadcast 169.254.255.255 netmask 255.255.0.0 (not neccassary)
telnet 169.254.1.1 3490 (not neccessary)

run PfiefferVacuum
"""

from PfeifferVacuum import *

filename='Test-interactive-plotting.txt'


m=MaxiGauge('/dev/ttyUSB1') #Opens the usb port that pressure gauge RS232 is connected to
print m.pressure(1) #Prints the current status of the pressure gauge

import telnetlib
import time
import matplotlib.pyplot as plt
import sys # For try-except

#set to local network only
# sudo ifconfig eth0 169.254.1.2 broadcast 169.254.255.255 netmask 255.255.0.0
# telnet 169.254.1.1 3490


starttime=time.time()   #Saves the start time

host='169.254.1.1'  #ip address of multimeter

telnet=telnetlib.Telnet()   #Setup telnet

telnet.open(host, port=3490, timeout=3) #Sets up telnet connection to multimeter
telnet.write('SYST:REM\n')  #Set multimeter into remote mode

f=open(filename,'w')    
f.write("Index\tTime(s)\tResistance (Ohm)\tPressure (mbar)\n")
n=0
k=1


timelist=[]
resistancelist=[]
pressurelist=[]

time.sleep(1)
plt.ion()
while k>0:
    telnet.write('MEAS:RES?\n') #Asks multimeter to measure the resistance
    #print n
    time.sleep(0.5)
    resistance=telnet.read_eager()  #Read resistance from multimeter
    #print resistance
    #resistancelist.append(resistance)
    pressure=m.pressure(1).pressure #Measures pressure
    #print pressure
    #pressurelist.append(pressure)
    current_time=time.time()-starttime  #Calculates time since start of script
    time.sleep(1)
    f.write( "%d\t%f\t%s\t%.10f\n" % (n,current_time,resistance.strip(),pressure) )    #Writes data to file
    f.flush()   #Flushes data out to file to make sure it writes
    n=n+1

    try:
	fig1=plt.figure(1)
	ax=fig1.add_subplot(211)
	plot1=plt.plot(current_time,resistance.strip(),'b.')
	plt.yscale('log', nonposy='clip')
	plt.ylim(10**-3,10**10)	#Resistance range to be displayed
	plt.xlabel('Time (s)')
	plt.ylabel('Resistance (Ohm)')
	plt.title('In-situ measurements of '+filename)
	plt.subplot(212)
	plot2=plt.plot(current_time,pressure,'r.')
	plt.yscale('log', nonposy='clip')
	plt.ylabel('Pressure (mbar)')
	plt.pause(0.05) 
    except:
	print('Overload')

telnet.close()  #Closes telnet connection to multimeter
f.close()   #Closes file

"""
Press ctrl+c to interrupt data sampling
type telnet.close() and
f.close()
in console
"""
