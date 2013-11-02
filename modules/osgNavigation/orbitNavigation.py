###############################################################
#
# Orbital Navigation Code - 2013
# Thomas Marrinan
#
# This module provides simultaneous translational and 
# rotational motion for a camera. Code has been ported
# from Electro Vortex.
#
###############################################################

from math import *
from euclid import *
from omega import *
from cyclops import *


class orbitNavigation:
	def __init__(self, camera):
		self.cam = camera
		self.fly_enabled = False
		self.fly_p = Vector3(0.0, 0.0, 0.0)
		self.fly_x = Vector3(1.0, 0.0, 0.0)
		self.fly_y = Vector3(0.0, 1.0, 0.0)
		self.fly_z = Vector3(0.0, 0.0, 1.0)
		self.tspeed = 10.0
		self.rspeed = 50.0
	
	def getTranslationSpped(self):
		return self.tspeed
	
	def setTranslationSpeed(self, speed):
		self.tspeed = speed
	
	def getRotationSpeed(self):
		self.rspeed
		
	def setRotationSpeed(self, speed):
		self.rspeed = speed
	
	def startNavigation(self, pos, orient):
		self.fly_enabled = True
	
		self.fly_p = pos
	
		xVec = Vector3(1.0,0.0,0.0)
		yVec = Vector3(0.0,1.0,0.0)
		zVec = Vector3(0.0,0.0,1.0)
		self.fly_x = orient * xVec
		self.fly_y = orient * yVec
		self.fly_z = orient * zVec
		
	def stopNavigation(self):
		self.fly_enabled = False
	
	def updateNavigation(self, pos, orient, dt):
		if self.fly_enabled:	
			xVec = Vector3(1.0,0.0,0.0)
			yVec = Vector3(0.0,1.0,0.0)
			zVec = Vector3(0.0,0.0,1.0)
			cx = orient * xVec
			cy = orient * yVec
			cz = orient * zVec
	
			delta_p = (pos - self.fly_p) * dt*self.tspeed
			delta_y = self.fly_y - cy
			delta_z = self.fly_z - cz
	
			rX =  (delta_z[0]*self.fly_y[0] + delta_z[1]*self.fly_y[1] + delta_z[2]*self.fly_y[2]) * dt*self.rspeed
			rY = -(delta_z[0]*self.fly_x[0] + delta_z[1]*self.fly_x[1] + delta_z[2]*self.fly_x[2]) * dt*self.rspeed
			rZ =  (delta_y[0]*self.fly_x[0] + delta_y[1]*self.fly_x[1] + delta_y[2]*self.fly_x[2]) * dt*self.rspeed
	
			self.cam.translate(delta_p, Space.Local)
			self.cam.pitch(radians(rX))
			self.cam.yaw(radians(rY))
			self.cam.roll(radians(rZ))
