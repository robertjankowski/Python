from vpython import *
import math

class Ball:
	def __init__(self,mass,fi,r,v=0,x0=0,y0=0):
		self.mass = mass
		self.fi = fi
		self.body = sphere(pos=vector(x0+r*math.sin(fi),y0+r*math.sin(fi),0),radius=1,color=color.blue,make_trail=True)
		self.r = r
		self.v = v
		self.x0 = x0
		self.y0 = y0
		self.e0 = mass/2*v**2 
		#self.line = 


scene = canvas(title='Random_Walk',width=800, height=800,center=vector(0,0,0), background=color.gray(0.5))

b1 = Ball(20,0,100,10,0,0)


dt = 0.05
g = 9.81
# mv^2/2 = e0 - mg(dy)

ujemne = False
for _ in range(200):
	rate(50)
	defi = b1.v*dt/b1.r
	y2 = b1.y0 + b1.r*math.cos(b1.fi+defi)
	dy = b1.y0 +b1.r - y2
	ksi = 2/b1.mass*(b1.e0-b1.mass*g*dy) 
	if ksi < 0 :
		ksi = -ksi
		if ujemne: 
			ujemne = False
		else : 
			ujemne = True
	b1.v = math.sqrt(ksi)
	if ujemne:
		b1.v *= -1
	b1.fi += defi
	print(b1.body.pos.y)
	b1.body.pos.x = b1.v*dt*math.sin(b1.fi)
	b1.body.pos.y = b1.y0 - dy

