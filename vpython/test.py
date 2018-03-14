import math 
from pobieranie_z_pliku import pobierz_dane
from vpython import *
import matplotlib.pyplot as plt
import numpy as np

ball = sphere(pos=vector(0,0,0),radius=1,color=color.blue)

test = pobierz_dane('sin.csv')

x = []
y = []

for i in range(len(test)):
	rate(20)
	ball.pos.x = i * 1
	ball.pos.z = float(test[i][0]) * 2
	x.append(i)
	y.append(float(test[i][0]))

plt.plot(x,y)
plt.show()
