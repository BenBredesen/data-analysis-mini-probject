import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def plotEvent(data,event,gender,medal):

    thisData = data[data['Event']==event+' '+gender]
    thisData = thisData[thisData['Medal']==medal]
    thisData = thisData.sort_values('Year')
    x=thisData['Year'].to_list()
    y=thisData['Result'].to_list()
    x.reverse()
    y.reverse()
    for i in range(len(y)):
        
        num = y[i]
        if type(num)!=type('abc'):
            continue
        num = num.replace('h',':')
        num = num.replace('-',':')
        if (num.count(':')<=1 and num[:num.find(':')+1]=='0') or (num.count(':')==0): #if it doesn't have or need anything other than seconds
            num = num[num.find(':')+1:]
            y[i] = float(num)
        else: #if it uses minutes/hours
            time = num.split(':')
            time.reverse()
            totalTime = 0
            for v in range(len(time)):
                totalTime += float(time[v])*(60**v)
                y[i] = totalTime
    return x,y

print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
data = pd.read_csv('data/results.csv')

numPlots = int(input('How many events would you like to view: '))

fig, axs = plt.subplots(numPlots)
if numPlots==1:
    axs = [axs]

for i in range(numPlots):
    print('\n')
    event = input("Which event would you like to view: ")
    gender = input("Which gender of the "+event+" would you like to view? Enter 'M' or 'W': ")
    if gender=='M':
        gender = 'Men'
    else:
        gender = 'Women'
    x,y = plotEvent(data,event,gender,'G')
    axs[i].plot(x,y,label='Gold',c='#FFD700')
    x,y = plotEvent(data,event,gender,'S')
    axs[i].plot(x,y,label='Silver',c='#C0C0C0')
    x,y = plotEvent(data,event,gender,'B')
    axs[i].plot(x,y,label='Bronze',c='#CD7F32')

    axs[i].set(title=f'{gender}\'s {event.lower()}',ylabel='Time (s)')
    axs[i].legend()
    axs[i].grid()

plt.grid()
fig.tight_layout()
plt.show()