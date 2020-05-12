import matplotlib.pyplot as plt
import pandas as pd
import sys 

unrate = pd.read_csv('unrate.csv')

#pick first twelve rows
first_twelve = unrate[0:12]
#graph date on x and value on y
figure = plt.plot(first_twelve['DATE'], first_twelve['VALUE'])
figure.savefig('plot.png')
plt.close(figure)