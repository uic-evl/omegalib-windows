#####################################################################################################################
# (C) 2013 - Jason Leigh, Electronic Visualization Laboratory, University of Illinois at Chicago
# Version 8/115/2013
#
# Demo application to show the use of the CAVEUTIL module
#
# This particular demo shows how to use the Flipbook class to flip through a bunch of objects
# that may be part of an animated sequence.
#
from math import *
from euclid import *
from omega import *
from cyclops import *
from omegaToolkit import *

# Import the CAVEUTIL module.
from caveutil import *

# Add the smart lights
caveutil.addSmartLights(getScene(), getDefaultCamera())
getScene().setBoundingBoxVisible(True)	

obj1 =caveutil.loadObject(getSceneManager(), "fractal", "fractal.fbx", False, False, False, True, False)
obj2 =caveutil.loadObject(getSceneManager(), "saber", "saber.fbx", False, False, False, True, False)
obj2.setScale(0.05,0.05,0.05)
obj3 =caveutil.loadObject(getSceneManager(), "ring", "ring.fbx", False, False, False, True, False)

rootScene = SceneNode.create("ROOT")
rootScene.addChild(obj1)
rootScene.addChild(obj2)
rootScene.addChild(obj3)

rootScene.setPosition(0,1.5,-2)

flipbook = FlipbookActor(rootScene)
flipbook.play(FlipbookActor.FORWARD)
flipbook.setFrameRate(1)

def onEvent():
	# Make sure to do this in your event loop- needed by Smart Lights.
	event = getEvent()
	caveutil.update(event, getScene())
	
	if event.isKeyDown(ord('n')) or event.isButtonDown(EventFlags.ButtonRight):
		print "NEXT FRAME"
		flipbook.nextFrame()
		
	if event.isKeyDown(ord('p')) or event.isButtonDown(EventFlags.ButtonLeft):
		print "PREV FRAME"
		flipbook.previousFrame()
		
	if event.isKeyDown(ord('f')) or event.isButtonDown(EventFlags.ButtonUp):
		print "PLAY FORWARD"
		flipbook.play(FlipbookActor.FORWARD)

	if event.isKeyDown(ord('b')) or event.isButtonDown(EventFlags.ButtonDown):
		print "PLAY BACKWARD"
		flipbook.play(FlipbookActor.BACKWARD)
		
setEventFunction(onEvent)
