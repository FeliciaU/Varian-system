
import matplotlib.pyplot as plt
plt.interactive(True)
import pandas as pd
import os
import re



plt.close("all")    #Closes plots from previous run

#######################################################
#Settings for the SQUID data
filename_res='F20-SmN-pumping1-060916.txt'    #Base name of files that need to be read

file_location='/home/feliciaullstad/Desktop/Google_Drive/PhD/SmN data/Varian/F20'
Sample_name='F20'
Comment='Pressure+resistance-venting-backing'


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

for column in Res_data:
    for item in Res_data[column]:
        if isinstance(item,str):
            item=float(item)
        elif isinstance(item,int):
            item=float(item)
print('Resistance data')
print(Res_data)

xmin=72000
xmax=74500

fig1=plt.figure()
ax=fig1.add_subplot(211)
plot1=plt.plot(Res_data["Time(s)"],Res_data["Resistance (Ohm)"],'.')
plt.xlim(xmin,xmax)
plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
plt.ylim(1*10**8,2.5*10**8)

plt.annotate('Backing pump off', xy=(73320, 2.1*10**8),
            xycoords='data',
            xytext=(73320, 2.3*10**8), arrowprops=dict(facecolor='black', shrink=0.5),
            horizontalalignment='center', verticalalignment='bottom',
            )

plt.annotate('Nitrogen off', xy=(1000, 1200000),
            xycoords='data',
            xytext=(1000, 1350000), arrowprops=dict(facecolor='black', shrink=0.5),
            horizontalalignment='center', verticalalignment='bottom',
            )

#plt.yscale('log', nonposy='clip')
plt.xlabel('Time (s)')
plt.ylabel('Resistance (Ohm)')
plt.title('In-situ measurements of '+Sample_name)
#plt.title('Resistance vs time for F21')
plt.subplot(212)
plot2=plt.plot(Res_data["Time(s)"],Res_data["Pressure (mbar)"],'r.')
plt.xlim(xmin,xmax)
plt.ylim(10**-3,10**4)
#plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
plt.yscale('log', nonposy='clip')
plt.xlabel('Time (s)')
plt.ylabel('Pressure (mbar)')
#plt.title('Pressure vs time for F21')

plt.annotate('Pressure gauge max', xy=(73610, 0.9*10**3),
            xycoords='data',
            xytext=(73610, 10**1.7), arrowprops=dict(facecolor='black', shrink=0.5),
            horizontalalignment='left', verticalalignment='bottom',
            )


save_location=file_location+'-python/'+Sample_name+'_'+Comment+'_plot_Resistance_vs_time.pdf'
plot1=plt.savefig(save_location, format='pdf', dpi=1200)
