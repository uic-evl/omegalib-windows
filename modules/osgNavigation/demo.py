###############################################################
#
# Orbital Navigation Demo - 2013
# Thomas Marrinan
#
# This demonstrates how to use the orbitNavigation module.
# The orbitNavigation module allows the user to translate 
# and rotate the camera simultaneously in a natural and
# comfortable manner using a Wand input device
#
###############################################################

from math import *
from euclid import *
from omega import *
from cyclops import *

from orbitNavigation import *


scene = getSceneManager()
scene.setBackgroundColor(Color(0.2, 0.2, 0.2, 1.0))

cam = getDefaultCamera()
cam.setControllerEnabled(False)
orbit_cam = orbitNavigation(cam)
orbit_cam.setTranslationSpeed(10.0)
orbit_cam.setRotationSpeed(35.0)

light1 = Light.create()
light1.setLightType(LightType.Directional)
light1.setLightDirection(Vector3(-0.5, -1.0, 0.5))
light1.setColor(Color(1.0, 1.0, 1.0, 1.0))
light1.setAmbient(Color(0.2, 0.2, 0.2, 1.0))
light1.setEnabled(True)

box = BoxShape.create(0.8, 0.8, 0.8)
box.setPosition(Vector3(0.0, 2.0, -3.0))
box.setEffect("textured -d omega-transparent.png")

wand_pos = None
wand_orient = None

###################################################################################
###################################################################################

def onUpdate(frame, t, dt):
	global orbit_cam
	global wand_pos
	global wand_orient
	
	orbit_cam.updateNavigation(wand_pos, wand_orient, dt)

###################################################################################
###################################################################################

def handleEvent():
	global orbit_cam
	global wand_pos
	global wand_orient
	
	e = getEvent()
	
	if e.getServiceType() == ServiceType.Wand:		
		if e.isButtonDown(EventFlags.Button7):
			orbit_cam.startNavigation(wand_pos, wand_orient)
		if e.isButtonUp(EventFlags.Button7):
			orbit_cam.stopNavigation()
	
	if e.getServiceType() == ServiceType.Mocap:
		if e.getSourceId() == 1:
			wand_pos = e.getPosition()
			wand_orient = e.getOrientation()

###################################################################################
###################################################################################

setUpdateFunction(onUpdate)
setEventFunction(handleEvent)
