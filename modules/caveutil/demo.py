#####################################################################################################################
# (C) 2013 - Jason Leigh, Electronic Visualization Laboratory, University of Illinois at Chicago
# Version 8/1/2013
#
# Demo application to show the use of the CAVEUTIL module
#
# This particular demo loads some objects into a scene, creates Smart Lights, lets you aim your head and wand at objects and watch their bounding boxes turn on/off.
# A fractal and a sphere are  tied to InterpolActors so you can watch them smoothly move and transform around the space. The the objects are also bound to interactors
# which allow you to click and drag them around the world with your wand.
# The UP DPAD button (or CTRL key) will set a random scale for the sphere to interpolate to.
# The fractal will continue to randomly interpolate on its own and demonstrates how to use the InterpolActor's callback function to tell you when an interpolation is done.
#
from math import *
from euclid import *
from omega import *
from cyclops import *
from omegaToolkit import *
#from random import *
import random 

# Import the CAVEUTIL module.
from caveutil import *

# Important to seed a random number in the CAVE or else each compute node's random number will be different.
random.seed(1)

# Add the smart lights
caveutil.addSmartLights(getScene(), getDefaultCamera())
# Turn on bounding box of the entire scene as a debugging tool to show you how large your current scene is.
#getScene().setBoundingBoxVisible(True)	

# Add a headlight (if desired)
g_camera = getDefaultCamera()
#caveutil.addHeadLight(g_camera)
#caveutil.enableHeadLight(True)

def MakeSphere(size):
	sphere = SphereShape.create(size/2,8)
	sphere.setEffect('colored')
	sphere.getMaterial().setColor(Color(1,0.3,0.3,1),Color(0,0,0,1))
	sphere.setSelectable(True)
	return sphere

# Load a fractal and an InterpolActor to perform position interpolation on the object
sp1=caveutil.loadObject(getSceneManager(), "fractal", "fractal.fbx", False, False, True, True, False)
sp1.setPosition(0,2,-3)
interp = InterpolActor(sp1)
interp.setTransitionType(InterpolActor.SMOOTH)
interp.setDuration(2)
interp.setOperation( InterpolActor.POSITION)
interactor1 = ToolkitUtils.setupInteractor("config/interactor")
if (interactor1 != None):
	interactor1.setSceneNode(sp1)

interp.setTargetPosition(Vector3(-2+random.random()*4,random.random()*2, -random.random()*4))
interp.startInterpolation()

# Make a second object and an InterpolActor with different properties
sp2 = MakeSphere(0.5)
sp2.setPosition(2,2,-3)
interp2 = InterpolActor(sp2)
interp2.setTransitionType(InterpolActor.LINEAR)
interp2.setDuration(4)
interp2.setOperation(InterpolActor.SCALE)
interactor2 = ToolkitUtils.setupInteractor("config/interactor")
if (interactor2 != None):
	interactor2.setSceneNode(sp2)


# Load a light saber. We're going to eventually attach this to the wand.
g_saber=caveutil.loadObject(getSceneManager(), "saber", "saber.fbx", False, False, False, True, False)
g_saber.setScale(0.05,0.05,0.05)

# Load a targeting cursor. We're going to eventually attach this to your head.
g_ring=caveutil.loadObject(getSceneManager(), "ring", "ring.fbx", False, False, False, True, False)

# Load a giant scene into the CAVE.
g_platform =caveutil.loadObject(getSceneManager(), "platform", "walkplatform.fbx", False, False, False, True, False)

# If you want you can scale the scene to all fit within the CAVE.
#caveutil.fitInCAVE(g_platform)

g_currentObj = None
g_prevObj = None
g_distance = 0


def onUpdate(frame, time, dt):
	global g_currentObj
	global g_prevObj
	global g_distance
	
	# Position a targeting cursor at the user's head and orient it in accordance with the user's head.
	caveutil.positionAtHead(g_camera, g_ring, 0.5)
	caveutil.orientWithHead(g_camera, g_ring)
	
	# Position a light saber in the user's wand.
	caveutil.positionAtWand(g_camera, g_saber, caveutil.WAND1, 0)
	caveutil.orientWithWand(g_camera, g_saber, caveutil.WAND1)

	# Compute what a ray fired from the head is intersecting, and draw its bounding box.
	g_currentObj, g_distance = caveutil.getNearestIntersectingObject(caveutil.getHeadWorldPosition(g_camera), caveutil.getHeadRay(g_camera))

	if g_currentObj != None:
		if g_prevObj != None:
			g_prevObj.setBoundingBoxVisible(False)
		g_currentObj.setBoundingBoxVisible(True)			
		g_prevObj = g_currentObj
	
	#Compute what a ray fired from the wand is intersecting, and draw its bounding box.
	g_currentObj, distance = caveutil.getNearestIntersectingObject(caveutil.getWandWorldPosition(g_camera, caveutil.WAND1), caveutil.getWandRay(g_camera, caveutil.WAND1))
	if g_currentObj != None:
		if g_prevObj != None:
			g_prevObj.setBoundingBoxVisible(False)
		g_currentObj.setBoundingBoxVisible(True)			
		g_prevObj = g_currentObj
	
setUpdateFunction(onUpdate)
	
# This is my own callback for when an interpolation ends.
# I use it initiate a new interpolation
def MyFunc(interpObj):
	interpObj.setTargetPosition(Vector3(-2+random.random()*4,random.random()*2, -random.random()*4))
	interpObj.startInterpolation()

# When interpolation ends for interp (i.e. object sp1) call my function
interp.setEndOfInterpolationFunction(MyFunc)

def onEvent():
	event = getEvent()
	
	# Make sure to do this in your event loop
	caveutil.update(event, getScene())

	# If you press the button it will randomly move the sphere to a new position using smooth interpolation.
	if event.isButtonDown(EventFlags.Ctrl) or event.isButtonDown(EventFlags.ButtonUp):
		
		# Scale the other sphere randomly
		interp2.setTargetScale(Vector3(random.random(),random.random(), random.random()))
		interp2.startInterpolation()
		
setEventFunction(onEvent)
