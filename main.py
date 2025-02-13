import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
data = pd.read_csv('data/results.csv')



fig, ax = plt.subplots()

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
ax.plot(x,y,label='Gold',c='#FFD700')
x,y = plotEvent(data,'400M','Men','S')
ax.plot(x,y,label='Silver',c='#C0C0C0')
x,y = plotEvent(data,'400M','Men','B')
ax.plot(x,y,label='Bronze',c='#CD7F32')

ax.set(title='Men\'s 400m')
ax.legend()
plt.show()