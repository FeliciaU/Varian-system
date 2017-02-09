# -*- coding: utf-8 -*-
"""
Created on Mon May 30 15:28:41 2016

@author: feliciaullstad

For manually keeping track of the thickness, rate and time
when doing an iin-situ resistance growth.
"""


filename='SmN-in-situ-F24-160928-thickness.txt'



import time

#set to local network only
# sudo ifconfig eth0 169.254.1.2 broadcast 169.254.255.255 netmask 255.255.0.0
# telnet 169.254.1.1 3490


starttime=time.time()   #Saves the start time

f=open(filename,'w')
f.write("Index\tTime(s)\tN2massflow(sccm)\tThickness(Å)\tRate(Å/s)\n")
n=0
k=1



time.sleep(1)

while k>0:
    N2_flow=input('N2 mass flow:')
    thickness=input('Thickness:')
    rate=input('Rate:')
    current_time=time.time()-starttime  #Calculates time since start of script
    time.sleep(0.1)
    f.write( "%d\t%f\t%s\t%s\t%s\n" % (n,current_time,N2_flow,thickness,rate) )    #Writes data to file
    f.flush()   #Flushes data out to file to make sure it writes
    n=n+1


f.close()   #Closes file

"""
f.close()
in console
"""
