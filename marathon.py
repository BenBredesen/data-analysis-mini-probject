import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
data = pd.read_csv('data/results.csv')



fig, (ax1,ax2) = plt.subplots(2)

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


x,y = plotEvent(data,'Marathon','Men','G')
ax1.plot(x,y,label='Gold',c='#FFD700')
x,y = plotEvent(data,'Marathon','Men','S')
ax1.plot(x,y,label='Silver',c='#C0C0C0')
x,y = plotEvent(data,'Marathon','Men','B')
ax1.plot(x,y,label='Bronze',c='#CD7F32')

x,y = plotEvent(data,'Marathon','Women','G')
ax2.plot(x,y,label='Gold',c='#FFD700')
x,y = plotEvent(data,'Marathon','Women','S')
ax2.plot(x,y,label='Silver',c='#C0C0C0')
x,y = plotEvent(data,'Marathon','Women','B')
ax2.plot(x,y,label='Bronze',c='#CD7F32')

ax1.set(title='Men\'s 10,000m',ylabel='Time (s)')
ax1.legend()
ax2.set(title='Women\'s 10,000m',ylabel='Time (s)')
ax2.legend()
fig.tight_layout()
plt.show()