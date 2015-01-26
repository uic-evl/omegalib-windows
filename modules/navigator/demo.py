########################################################################
# (C) 2013 - Jason Leigh, Electronic Visualization Laboratory, University of Illinois at Chicago
# Version 7/4/2013
#
# Demo application to show the use of Walkabout code
# This demo uses the Walkabout class to enable you to walk over geometry.
# The Walkabout class also does collision detection to prevent you from walking through objects.
# Look for comments below that say ADD THIS TO USE WALKABOUT
# to find out how to use it in your own programs.
#
from math import *
from euclid import *
from omega import *
from cyclops import *
from omegaToolkit import *

########################################################################
# ADD THIS TO USE WALKABOUT
from walkabout import walkabout

########################################################################
# Make a scene and load some walkable scene.

g_scene = getSceneManager()

# Create a light
g_light = Light.create()
g_light.setColor(Color("#FFFFFF"))
g_light.setAmbient(Color("#303030"))
g_light.setPosition(Vector3(-5,20,5))
g_light.setEnabled(True)

# Load a static model
g_sceneModel = ModelInfo()
g_sceneModel.name = "platform"
g_sceneModel.path = "demodata/walkplatform.fbx"
g_scene.loadModel(g_sceneModel)

# Create a scene object using the loaded model
g_platform = AnimatedObject.create("platform")
g_platform.setSelectable(True)
g_platform.setPosition(Vector3(0, 0,0))
g_platform.setEffect("colored")
g_platform.setEffect("textured")
#g_platform.playAnimation()
g_platform.loopAnimation(0)

########################################################################
# ADD THIS TO USE WALKABOUT
# Initialize the walkabout navigator by giving it the camera to use
walkabout.init(getDefaultCamera())

# Use options below to turn on and off floor and wall checking
#walkabout.setFloorCheck(False)
#walkabout.setWallCheck(False)

# Sets how high you can climb as a ratio of your body height.
# 0.4 is default and means you can climb things that are 40% of your height
#walkabout.setClimbRatio(0.5)

# Sets how smoothly you climb or fall (max is 1)
# 0.01 means it will take 100 steps to interpolate
#walkabout.setClimbInterpolationSpeed(0.01)

# You're going to need to have an onUpdate function in which you add the walkabout.update call.
def onUpdate(frame, time, dt):

	########################################################################
	# ADD THIS TO USE WALKABOUT
	walkabout.update(dt)

# Tell Omegalib about the onUpdate function
setUpdateFunction(onUpdate)
