from vpython import *
import random

class Ball(object):
	"""docstring for Ball"""
	def __init__(self):
		super(Ball, self).__init__()
	def generateBall():
		x = random.uniform(-10,10)
		y = random.uniform(-10,10)
		z = random.uniform(-10,10)
		ball = sphere(pos=vector(x,y,z),radius=1)
		return ball
	def velocity(dt):
		speed = random()
		generateBall()


scene = canvas(title='Gravity',width=800,height=800,center=vector(0,0,0),background=color.cyan)
tab =  []
n = 10
for i in range(n):
	tab = Ball.generateBall()

t = 0
dt = 0.01

for i in range(5000):
	rate(10)
	for i in tab:
		i.velocity(dt)
	t += dt

