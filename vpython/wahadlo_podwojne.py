from vpython import *

scene = canvas(title='Wahadlo',witdh=800,height=800,center=vector(0,12,0),background=color.black)

g = 9.8 
ball = sphere(pos=vector(5,2,0),radius=0.5,color=color.blue,make_trail=True)
pivot = vector(0,20,0)
roof = box(pos=pivot,size=vector(10,0.5,10),color=color.green)

rod = cylinder(pos=pivot,axis=ball.pos-pivot,radius=0.1,color=color.red)

# drugie wahadlo


ball2 = sphere(pos=ball.pos+vector(0,-10,0),radius=0.5,color=color.green)


rod2 = cylinder(pos=ball.pos,axis=ball2.pos-ball.pos,radius=0.1,color=color.red)


t = 0
dt = 0.01
l = mag(ball.pos-pivot) # dlugosc wahadla (modul)
cs = (l-ball.pos.y)/l # cos(theta)
theta = acos(cs)
vel = 1.0

while(t<100):
	rate(100)
	acc = -g/l*sin(theta)
	theta += vel*dt
	vel += acc*dt
	ball.pos = vector(l*sin(theta),l*(1-cos(theta)),0)
	rod.axis = ball.pos - rod.pos
	t+=dt