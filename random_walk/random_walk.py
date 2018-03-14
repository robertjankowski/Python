from random import choice
from random import random
from vpython import *
class Random_Walk():
	def __init__(self, n=10000):
		self.n = n
		self.x = [0]
		self.y = [0]
		self.z = [0]
	def fill_walk(self):
		while len(self.x)<self.n:
			direction_x,direction_y,direction_z = choice([1,-1]),choice([1,-1]),choice([1,-1])
			distance_x,distance_y,distance_z = choice([0,1]),choice([0,1]),choice([0,1])
			step_x,step_y,step_z = direction_x*distance_x,direction_y*distance_y,direction_z*distance_z
			next_x,next_y,next_z = self.x[-1]+step_x, self.y[-1]+step_y,self.z[-1]+step_z
			self.x.append(next_x)
			self.y.append(next_y)
			self.z.append(next_z)
	def colors(self):
	    r = random()
	    if (r < 1.0/8.0):
	        return [vector(1,0,0),vector(0,0,0)]
	    elif (r < 2.0/8.0):
	        return [vector(0,1,0),vector(0,0,0)]
	    elif (r < 3.0/8.0):
	        return [vector(-1,0,0),vector(0,0,0)]
	    elif (r < 4.0/8.0):
	        return [vector(0,-1,0),vector(0,0,0)]
	    elif (r < 5.0/8.0):
	        return [vector(0,0,1),vector(0,0,0)]
	    elif (r < 6.0/8.0):
	        return [vector(0,0,-1),vector(0,0,0)]
	    elif (r < 7.0/8.0):
	        return [vector(0,0,0),vector(1,0,-1)]
	    else:
	        return [vector(0,0,0),vector(-1,0,1)]
