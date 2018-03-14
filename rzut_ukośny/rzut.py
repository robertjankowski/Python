from vpython import *
from math import * 


b = 1.6*10**-3
c = 0.25
x0,y0,z0 = -20,0,0
g = 9.81
yz0 = 0
m = 1
pi = 3.14
fi = pi/4
teta = pi/4
v0 = 30
dt = 0.01
x,y,z = x0,y0,z0
vx = v0 * cos(fi) * sin(teta)
vz = v0 * sin(fi) * sin(teta)
vy = v0 * cos(teta)
vz2 = v0 * sin(fi) * sin(teta)
vx2 = v0 * cos(fi) * sin(teta)
vy2 = v0 * cos(teta)
wind = vector(0,0,0)

scene =  canvas(title='Rzut ukosny',
     width=800, height=800,
     center=vector(0,0,0), background=color.cyan)

ziemia = box(pos=vector(0,0,0),
       length=100, height=0.1, width=100,color=color.blue)

pilka = sphere(pos=vector(x0,y0,z0),radius=0.5,color=color.red)
pilka2 = sphere(pos=vector(x0,y0,z0),radius=0.5,color=color.black)

wector = arrow(pos=vector(10,10,10),axis=vector(wind.x,wind.y,wind.z),color=color.yellow,shaftwidth=0.3)

pilka.trail = curve(color=pilka.color)
pilka2.trail = curve(color=pilka2.color)

while 1:
	rate(100)
	if (pilka.pos.y >= ziemia.pos.y):
		vx += (-c*(vx-wind.x) - b*(vx-wind.x)**2)/m * dt
		vz += (-c*(vz-wind.z) - b*(vz-wind.z)**2)/m * dt
		vy += (-c*(vy-wind.y) - b*(vy-wind.y)**2 -m*g)/m * dt
		pilka.pos.x += vx*dt
		pilka.pos.y += vy*dt
		pilka.pos.z += vz*dt
	if (pilka2.pos.y >= ziemia.pos.y):
		vy2 += -g*dt 
		pilka2.pos.y += vy2*dt
		pilka2.pos.x += vx2*dt
		pilka2.pos.z += vz2*dt
	if (pilka2.pos.y < ziemia.pos.y and pilka.pos.y < ziemia.pos.y ):
		break
	pilka.trail.append(pos=pilka.pos)
	pilka2.trail.append(pos=pilka2.pos)
	 
