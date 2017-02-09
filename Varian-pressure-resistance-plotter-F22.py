
import matplotlib.pyplot as plt
plt.interactive(True)
import pandas as pd
import os
import re



plt.close("all")    #Closes plots from previous run

#######################################################
#Settings for the SQUID data
filename_res='F22-SmN-In-situ-160921.txt'    #Base name of files that need to be read

#file_location='/home/feliciaullsta/Desktop/Google_Drive/PhD/SmN data/Varian/F22'
file_location='/Users/Felicia/Desktop/Google_Drive/PhD/SmN data/Varian/F22'
Sample_name='F22'
Comment='Only_film_growth'


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

xmin=0
xmax=3000

fig1=plt.figure()
ax=fig1.add_subplot(211)
plot1=plt.plot(Res_data["Time(s)"],Res_data["Resistance (Ohm)"],'.')
plt.xlim(xmin,xmax)
plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
#plt.ylim(3*10**6,5*10**7)
"""
plt.annotate('Valve opened', xy=(84983, 5*10**6),
            xycoords='data',
            xytext=(84983, 7*10**6), arrowprops=dict(facecolor='black', shrink=0.5),
            horizontalalignment='right', verticalalignment='bottom',
            )

plt.annotate('Valve more opened', xy=(85141, 8*10**6),
            xycoords='data',
            xytext=(85141, 5*10**6), arrowprops=dict(facecolor='black', shrink=0.5),
            horizontalalignment='left', verticalalignment='bottom',
            )
"""
plt.yscale('log', nonposy='clip')
plt.xlabel('Time (s)')
plt.ylabel('Resistance (Ohm)')
plt.title('In-situ measurements of '+Sample_name)
#plt.title('Resistance vs time for F21')
plt.subplot(212)
plot2=plt.plot(Res_data["Time(s)"],Res_data["Pressure (mbar)"],'r.')
plt.xlim(xmin,xmax)
#plt.ylim(10**-4,10**4)
#plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))
plt.yscale('log', nonposy='clip')
plt.xlabel('Time (s)')
plt.ylabel('Pressure (mbar)')
#plt.title('Pressure vs time for F21')
"""
plt.annotate('Pressure gauge max', xy=(73610, 0.9*10**3),
            xycoords='data',
            xytext=(73610, 10**1.7), arrowprops=dict(facecolor='black', shrink=0.5),
            horizontalalignment='left', verticalalignment='bottom',
            )

"""
save_location=file_location+'-python/'+Sample_name+'_'+Comment+'_plot_Resistance_vs_time.pdf'
plot1=plt.savefig(save_location, format='pdf', dpi=1200)
