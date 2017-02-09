
import matplotlib.pyplot as plt
plt.interactive(True)
import pandas as pd
import os
import re
import numpy as np
import scipy.interpolate as sp



plt.close("all")    #Closes plots from previous run

#######################################################
#Settings for the SQUID data
filename_res='F22-SmN-In-situ-160921-final.txt'    #Base name of files that need to be read
filename_thickness='SmN-in-situ-F22-160921-thickness-cleaned.txt'

file_location='/home/felicia/Desktop/GoogleDrive/PhD/SmN data/Varian/F22'
Sample_name='F22'
Comment='Thickness+resistance-SEMguess80nm'
SEM_thickness=80  #SEM measured thickness in nm

Inf_res=10**35
#trimstart=4
#trimend=-16


######################################################
if not os.path.exists(file_location+'-python'):     #Checks if the python folder exists
    os.makedirs(file_location+'-python')            #If not, it makes it
#######################################################
#Importing and plotting the SQUID data


Res_data_raw=pd.read_csv(file_location+'/'+filename_res, header=0, sep='\t',skiprows=0)
Res_data_2=Res_data_raw[Res_data_raw["Resistance (Ohm)"] < Inf_res]    # Filters away data with fit values under Fit_value
Res_data=Res_data_2[Res_data_2["Time(s)"] < 900]    # Filters away data with fit values under Fit_value

for column in Res_data:
    for item in Res_data[column]:
        if isinstance(item,str):
            item=float(item)
        elif isinstance(item,int):
            item=float(item)
print('Resistance data')
print(Res_data)

Thick_data_raw=pd.read_csv(file_location+'/'+filename_thickness, header=0, sep='\t',skiprows=0)
Thick_data=Thick_data_raw['Thickness(Å)']*SEM_thickness/100/390
Thick_data_time=Thick_data_raw[Thick_data_raw['Time(s)'] < 900]
print(Thick_data,Thick_data_time)

#Now interpolate the data so they can be plotted against each other. From time 0 to
new_time=np.linspace(30,800,1000)
f_Res_data_interp=sp.interp1d(Res_data['Time(s)'], Res_data['Resistance (Ohm)'],assume_sorted=False)
fig1=plt.figure()
plot1=plt.plot(Res_data['Time(s)'],Res_data['Resistance (Ohm)'],'.', Res_data['Time(s)'], f_Res_data_interp(Res_data['Time(s)']))
Res_data_interp=f_Res_data_interp(new_time)
f_Thick_data_interp=sp.interp1d(Thick_data_raw['Time(s)'], Thick_data)
Thick_data_interp=f_Thick_data_interp(new_time)

print(Res_data_interp)
print(Thick_data_interp)

fig2=plt.figure()
plot2=plt.plot(Res_data['Time(s)'],Res_data['Resistance (Ohm)'],'.')

fig3=plt.figure()
plot3=plt.plot(1/Thick_data_interp,Res_data_interp,'.')
#plt.xlim(xmin,xmax)
plt.xlabel('1/Thickness (1/nm)')
plt.ylabel('Resistance (Ohm)')
plt.yscale('log', nonposy='clip')
plt.title('Resistance vs inverse thickness for '+Sample_name)

data=np.vstack((Thick_data_interp,Res_data_interp)).T
save_location=file_location+'-python/'+Sample_name+'_'+Comment+'_plot.pdf'

with open('F22-Thickness-resistance-interpolated.txt', 'wb') as f:
    f.write(b'Thickness(nm) Resistance(Ohm)\n')
    np.savetxt(f, data, delimiter=' ')
#data.to_csv('test_F21.txt', header=headers, index=None, sep=' ', mode='w')


plot3=plt.savefig(save_location, format='pdf', dpi=1200)
