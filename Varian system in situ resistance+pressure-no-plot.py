# -*- coding: utf-8 -*-
"""
Created on Mon May 30 15:28:41 2016

@author: feliciaullstad

set to local network only
sudo ifconfig eth0 169.254.1.2 broadcast 169.254.255.255 netmask 255.255.0.0
telnet 169.254.1.1 3490

run PfiefferVacuum
"""

from PfeifferVacuum import *

filename='trial1.txt'


m=MaxiGauge('/dev/ttyUSB0') #Opens the usb port that pressure gauge RS232 is connected to
print m.pressure(1) #Prints the current status of the pressure gauge

import telnetlib
import time

#set to local network only
# sudo ifconfig eth0 169.254.1.2 broadcast 169.254.255.255 netmask 255.255.0.0
# telnet 169.254.1.1 3490


starttime=time.time()   #Saves the start time

host='169.254.1.1'  #ip address of multimeter

telnet=telnetlib.Telnet()   #Setup telnet

telnet.open(host, port=3490, timeout=3) #Sets up telnet connection to multimeter
telnet.write('SYST:REM\n')  #Set multimeter into remote mode

f=open(filename,'w')    
f.write("Index\Time(s)\tResistance (Ohm)\tPressure (mbar)\n")
n=0
k=1



time.sleep(1)

while k>0:
    telnet.write('MEAS:RES?\n') #Asks multimeter to measure the resistance
    #print n
    resistance=telnet.read_eager()  #Read resistance from multimeter
    #print resistance
    pressure=m.pressure(1).pressure #Measures pressure
    #print pressure
    current_time=time.time()-starttime  #Calculates time since start of script
    time.sleep(0.2)
    f.write( "%d\t%f\t%s\t%f\n" % (n,current_time,resistance.strip(),pressure) )    #Writes data to file
    f.flush()   #Flushes data out to file to make sure it writes
    n=n+1


telnet.close()  #Closes telnet connection to multimeter
f.close()   #Closes file

"""
Press ctrl+c to interrupt data sampling
type telenet.close() and
f.close()
in console
"""
