# Use lines and spheres to create a disc.
from math import *
from euclid import *
from omega import *
from cyclops import *

circle = LineSet.create()

segments = 32
radius = 1
thickness = 0.1

a = 0.0
while a <= 360:
	x = cos(radians(a)) * radius
	y = sin(radians(a)) * radius
	a += 360.0 / segments 
	nx = cos(radians(a)) * radius
	ny = sin(radians(a)) * radius
	
	l = circle.addLine()
	l.setStart(Vector3(x, y, 0))
	l.setEnd(Vector3(nx, ny, 0))
	l.setThickness(thickness)
	
	s = SphereShape.create(thickness / 2, 2)
	circle.addChild(s)
	# Use a full emissive color. Using transparent colors does not work very well due
	# to overlapping polygons.
	s.setEffect('colored -e red')
	s.setPosition(Vector3(nx, ny, 0))
	
circle.setPosition(Vector3(0,2,-4))
circle.setEffect('colored -e red')

# Squish z to turn the torus into a disc-like shape.
circle.setScale(Vector3(1.0,1.0,0.1))
	