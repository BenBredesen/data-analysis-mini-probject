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
        num = num[num.find(':')+1:]
        y[i] = float(num)
    return x,y


x,y = plotEvent(data,'400M','Men','G')
ax1.plot(x,y,label='Gold',c='#FFD700')
x,y = plotEvent(data,'400M','Men','S')
ax1.plot(x,y,label='Silver',c='#C0C0C0')
x,y = plotEvent(data,'400M','Men','B')
ax1.plot(x,y,label='Bronze',c='#CD7F32')

x,y = plotEvent(data,'400M','Women','G')
ax2.plot(x,y,label='Gold',c='#FFD700')
x,y = plotEvent(data,'400M','Women','S')
ax2.plot(x,y,label='Silver',c='#C0C0C0')
x,y = plotEvent(data,'400M','Women','B')
ax2.plot(x,y,label='Bronze',c='#CD7F32')

ax1.set(title='Men\'s 400m',ylabel='Time (s)')
ax1.legend()
ax2.set(title='Women\'s 400m',ylabel='Time (s)')
ax2.legend()
fig.tight_layout()
plt.show()