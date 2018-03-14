from vpython import *
from math import pi,sin,e,exp

#freq
f1 = 5
f2 = 3
f3 = 1.002
f4 = 0
f5 = 0
f6 = 0
#przesuniecia
p1 = pi/16
p2 = 3*pi/2
p3 = 13*pi/16
p4 = pi
p5 = 0
p6 = 0
#stale
d1 = 0.02
d2 = 0.0315
d3 = 0.02
d4 = 0.02
d5 = 0
d6 = 0

t = 0
dt = 0.01

scene2 = canvas(title='Examples of Tetrahedrons',
     width=800, height=800,
     center=vector(5,0,0), background=color.cyan)

ball = sphere(pos = vector(0,0,0),radius=0.01, make_trail=True)
attach_trail(ball)
for i in range(500000):
	rate(200)
	ball.pos.x = 10*sin(f1*t+p1)*exp(-t*d1)+10*sin(f2*t+p2)*exp(-t*d2)
	ball.pos.y = 10*sin(f3*t+p3)*exp(-t*d3)+10*sin(f4*t+p4)*exp(-t*d4)
	#ball.pos.z = 10*sin(f5*t+p5)*exp(-t*d5)+10*sin(f6*t+p6)*exp(-t*d6)
	t += dt


