
import matplotlib.pyplot as plt
plt.interactive(True)
import pandas as pd
import os
import re



plt.close("all")    #Closes plots from previous run

#######################################################
#Settings for the SQUID data
filename_res='F21-SmN-pumping1-130916final.txt'    #Base name of files that need to be read
filename_thick='SmN-in-situ-130916-thickness-cleaned.txt'
file_location='/home/feliciaullstad/Desktop/Google_Drive/PhD/SmN data/Varian/F21'
Sample_name='F21'
Comment='Final'


Inf_res=10**35
#trimstart=4
#trimend=-16


######################################################
if not os.path.exists(file_location+'-python'):     #Checks if the python folder exists
    os.makedirs(file_location+'-python')            #If not, it makes it
#######################################################
#Importing and plotting the SQUID data


Res_data_raw=pd.read_csv(file_location+'/'+filename_res, header=0, sep='\t',skiprows=0)
Res_data=Res_data_raw[Res_data_raw["Resistance (Ohm)"] < Inf_res]    # Fitlers away data with fit values under Fit_value

Thick_data=pd.read_csv(file_location+'/'+filename_thick, header=0, sep='\t',skiprows=0)
for column in Res_data:
    for item in Res_data[column]:
        if isinstance(item,str):
            item=float(item)
        elif isinstance(item,int):
            item=float(item)
print('Resistance data')
print(Res_data)
for column in Thick_data:
    for item in Thick_data[column]:
        if isinstance(item,str):
            print(column,item)
            item=float(item)
        elif isinstance(item,int):
            item=float(item)
        else:
            item=item
print('Thickness data')
print(Thick_data)
print(list(Thick_data.columns.values))

xmin=2900
xmax=4000

fig1=plt.figure()
plt.subplot(411)
plot1=plt.semilogy(Res_data["Time(s)"],Res_data["Resistance (Ohm)"],'.')
#plt.xlim(xmin,xmax)
#plt.ylim(ymin=350000)
plt.yscale('log', nonposy='clip')
plt.xlabel('Time (s)')
plt.ylabel('Resistance (Ohm)')
plt.title('In-situ measurements of '+Sample_name)
#plt.title('Resistance vs time for F21')
plt.subplot(412)
plot2=plt.semilogy(Res_data["Time(s)"],Res_data["Pressure (mbar)"],'r.')
#plt.xlim(xmin,xmax)
plt.yscale('log', nonposy='clip')
plt.xlabel('Time (s)')
plt.ylabel('Pressure (mbar)')
#plt.title('Pressure vs time for F21')
plt.subplot(413)
plot2=plt.plot(Thick_data["Time(s)"],Thick_data["N2massflow(sccm)"],'bs')
#plt.xlim(xmin,xmax)
#plt.yscale('log', nonposy='clip')
plt.xlabel('Time (s)')
plt.ylabel('Flow rate (sccm)')
#plt.title('N_2 Flow rate vs time for F21')
plt.subplot(414)
plot2=plt.plot(Thick_data["Time(s)"],Thick_data["Thickness(A)"],'gs')
#plt.xlim(xmin,xmax)
#plt.yscale('log', nonposy='clip')
plt.xlabel('Time (s)')
plt.ylabel('Thickness (A)')
#plt.title('Thickness vs time for F21')


save_location=file_location+'-python/'+Sample_name+'_'+Comment+'_plot_Resistance_vs_time.pdf'
plot1=plt.savefig(save_location, format='pdf', dpi=1200)
