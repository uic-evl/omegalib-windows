#####################################################################################################################
# (C) 2013 - Jason Leigh, Electronic Visualization Laboratory, University of Illinois at Chicago
# Version 8/115/2013
#
# Demo application to show the use of the CAVEUTIL module
#
# This particular demo shows how to use the InterpolActor to control the camera.
# Use the SHIFT key or DOWN DPAD to mark a waypoint location.
# Use the CTRL key or UP DPAD to play back the previously recorded waypoints.
# Use the d key to dump the waypoint data to a file.
# Use the r key to read the waypoint data from a file.
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

# Add the smart lights
caveutil.addSmartLights(getScene(), getDefaultCamera())

###############################################
# Set up the InterpolActor to control the camera
interp = InterpolActor(getDefaultCamera())
interp.setTransitionType(InterpolActor.SMOOTH)	# Use SMOOTH ease-in/ease-out interpolation rather than LINEAR
interp.setDuration(3)							# Set interpolation duration to 3 seconds
interp.setOperation(InterpolActor.POSITION | InterpolActor.ORIENT)	# Interpolate both position and orientation

# Load a scene into the CAVE.
g_platform =caveutil.loadObject(getSceneManager(), "platform", "walkplatform.fbx", False, False, False, True, False)

	
# These variables hold the position and orientation corresponding to the stored navigational waypoints.
g_positionArray = []
g_orientationArray = []
g_arrayTraversal = 0

# This function is used to iterate over the stored navigation waypoints.
def WaypointTraversalFunc(interpObj):
	global g_arrayTraversal
	global g_positionArray
	global g_orientationArray
	
	if g_arrayTraversal < len(g_positionArray):
		interpObj.setTargetPosition(g_positionArray[g_arrayTraversal])
		interpObj.setTargetOrientation(g_orientationArray[g_arrayTraversal])
		interpObj.startInterpolation()
		g_arrayTraversal=g_arrayTraversal+1

# Tell the camera's InterpolActor to call the WaypointTraversalFunc at the end of each interpolated waypoint so that it can cue up
# the next waypoint.
interp.setEndOfInterpolationFunction(WaypointTraversalFunc)

# Use Python's Pickle module to save and load previously recorded waypoints to file.
import pickle

def onEvent():
	global g_arrayTraversal
	global g_positionArray
	global g_orientationArray
	
	event = getEvent()
	
	# Make sure to do this in your event loop- needed by Smart Lights and wand tracking.
	caveutil.update(event, getScene())

	# Press CTRL or DPAD UP button to playback navigation through all the stored waypoints
	if event.isButtonDown(EventFlags.Ctrl) or event.isButtonDown(EventFlags.ButtonUp):
		g_arrayTraversal = 0
		WaypointTraversalFunc(interp)
		
	# Press SHIFT or DPAD DOWN to record a waypoint.
	if event.isButtonDown(EventFlags.Shift) or event.isButtonDown(EventFlags.ButtonDown):
		g_positionArray.append(getDefaultCamera().getPosition())
		g_orientationArray.append(getDefaultCamera().getOrientation())
		print "SAVE WAYPOINT"
	
	if event.isKeyDown(ord('d')):
		print "SAVE WAYPOINT FILE"
		pickle.dump(g_positionArray, open("POS.way","wb"))
		pickle.dump(g_orientationArray, open("ORI.way","wb"))
		
	if event.isKeyDown(ord('r')):
		print "LOAD WAYPOINT FILE"
		g_positionArray = pickle.load(open("POS.way","rb"))
		g_orientationArray = pickle.load(open("ORI.way","rb"))
		
setEventFunction(onEvent)
