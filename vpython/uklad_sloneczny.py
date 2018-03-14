from vpython import *
import random

def r(a,b):
	return random.uniform(a,b);

class Point:
	def __init__(self):
		super(Point, self).__init__()
		self.position = vector(r(0,400),r(0,400),0)
		self.speed = vector(r(-1,1),r(-1,1),0)
		self.acce = vector(r(-0.1,0.1),r(-0.1,0.1),0)
		self.lifespan = 1
		self.mass = random.uniform(3,9)
	def update(self,dt=0.01):
		speed += acce * dt;
		position += speed * dt;
	def display(self):
		ball = sphere(pos=position,radius=mass,color=color.red)
	def run(self):
		update() 
		display()

class Center:
	def __init__(self, arg):
		super(Center, self).__init__()
		self.position = vector(200,0,200)
		self.mass = mass
	def show():
		ball = sphere(pos=position,radius=mass,color=color.black)
	def force(p,count):
		for i in range(count):
			pass


		

def test():
	scene = canvas(title='Uklad sloneczny',width=800, height=800,center=vector(0,0,0), background=color.cyan)



if __name__ == '__main__':
	#test()
	scene = canvas(title='Uklad sloneczny',width=800, height=800,center=vector(0,0,0), background=color.cyan)
	point = Point()
	point.run()
	print("Hello")

