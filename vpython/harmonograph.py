from turtle import *
from math import pi,sin,e

#freq
f1 = 5
f2 = 3
f3 = 1.002
f4 = 2

#przesuniecia
p1 = pi/16
p2 = 3*pi/2
p3 = 13*pi/16
p4 = pi

#stale
d1 = 0.02
d2 = 0.0315
d3 = 0.02
d4 = 0.02

t = 0
dt = 0.05

clear()

for i in range(5000):
	speed(1000)
	x1 = 100*sin(f1*t+p1)*e**(-t*d1)+100*sin(f2*t+p2)*e**(-t*d2)
	y1 = 100*sin(f3*t+p3)*e**(-t*d3)+100*sin(f4*t+p4)*e**(-t*d4)
	setpos(x1,y1)
	t += dt