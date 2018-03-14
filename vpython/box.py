from vpython import *


scene1 = canvas(title='Examples of Tetrahedrons',
     width=600, height=200,
     center=vector(5,0,0), background=color.cyan)

rod = cylinder(pos=vector(0,2,1),axis=vector(5,0,0),radius=1)

ball = sphere()