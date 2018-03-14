from random_walk import Random_Walk
from vpython import *
from random import random

scene = canvas(title='Random_Walk',width=800, height=800,center=vector(0,0,0), background=color.gray(0.5))
ball = sphere(pos=vector(0,0,0),raduis=0.0005,color=color.blue,make_trail=True)

col_dir = vector(0,0,0)
rw = Random_Walk()
for i in range(10000):
	rate(20)
	rw.fill_walk()
	col_dir = rw.colors()
	ball.pos.x = rw.x[i]
	ball.pos.z = rw.y[i]
	ball.pos.y = rw.z[i]
	ball.color += col_dir[0]
	ball.trail_color = ball.color
	print (col_dir[0])