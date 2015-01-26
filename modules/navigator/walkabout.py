## @package walkabout
# Walking navigation and wall collision class
# Contains only static members and member functions so you do not need to create any objects of this class to use it.
# To import the module into your own program:
#
#	from walkabout import walkabout
#
# To initialize call:
#
#	walkabout.init(getDefaultCamera())
#
# Then use it in your onUpdate function as follows:
#
#	walkabout.update(dt) -- where dt is the dt given to you by Omegalib on each frame update.
#
# A number of accessor functions can be used to change the behavior of the code. See documentation for details.
#
# (C) 2013 - Jason Leigh, Electronic Visualization Laboratory, University of Illinois at Chicago
# Original Version 7/3/2013
# Current Version 7/9/2013
from math import *
from euclid import *
from omega import *
from cyclops import *
from omegaToolkit import *


## walkabout class
# This class is used to enable walking over geometry in Omegalib. Collision detection is also provided
# so that you can't walk through walls or over high tables or fences, for example.
# It works by firing a ray downward in the scene to determine how high to raise you, and it also
# fires a second ray forward and downward to look for barriers in the direction you are walking.
class walkabout:

	# Constants
	__FAR = 999999
	__DEFAULT_RAY_ANGLE = 20
	__DEFAULT_CLIMB_RATIO = 0.4
	__DEFAULT_INTERP_STEP_SIZE = 0.05
	__DEFAULT_WALKCHECK_LENGTH = 0.05
	
	__minDistance = __FAR
	__theCamera = None
	__wallCollision = True
	__floorCollision = True
	
	# To what extent of your body length do you consider something climbable
	__climbableRatio = __DEFAULT_CLIMB_RATIO
	
	# Angle (from vertical) at which to cast a ray forward to determine what you can/cannot walk through
	__rayAngle = __DEFAULT_RAY_ANGLE
	
	# Old Camera is used to restore your location should you walk into an object that you should not
	# be able to.
	__oldCamera = Vector3(0,0,0)
	__old__headPositionWorld = Vector3(0,0,0)
	__camPosition = Vector3(0,0,0)
	__headPositionWorld = Vector3(0,0,0)
	__headOffset = Vector3(0,0,0)
	__interpSpeed = __DEFAULT_INTERP_STEP_SIZE

	@staticmethod
	## Initialize by setting the desired camera to use. 
	# @param camera camera to use for navigation (usually from getDefaultCamera())
	def init(camera):
		walkabout.__theCamera=camera


	@staticmethod
	## Set climb ratio
	# The proportion of the body height that constitutes something you can climb.
	# @param ratio Default is 0.3. e.g. if climbRation is 0.3 that means you can climb things that are 30% of your body height Valid ratios are > 0 and <= 1
	def setClimbRatio(ratio):
		if (ratio > 1): walkabout.__climbableRatio = walkabout.__DEFAULT_CLIMB_RATIO
		elif (ratio <= 0): walkabout.__climbableRatio = walkabout.__DEFAULT_CLIMB_RATIO
		else: walkabout.__climbableRatio = ratio

	@staticmethod
	## Set the angle at which a sloped ray is fired to check for obstacles in your way as you navigate.
	# @param angle Default is 20 degrees. e.g. 20 degrees means the ray is 20 degrees from the vertical aimed downwards from the head.
	# Valid angles are > 0 and <= 90
	def setRayAngle(angle):
		if (angle >= 90): walkabout.__rayAngle =  walkabout.__DEFAULT_RAY_ANGLE
		elif (angle <=0): walkabout.__rayAngle = walkabout.__DEFAULT_RAY_ANGLE
		else: walkabout.__rayAngle = angle

	@staticmethod
	## Set the speed at which climbing and falling is interpolated.
	# @param speed Valid ranges are > 0 and <= 1
	def setClimbInterpolationSpeed(speed):
		if (speed > 1): walkabout.__interpSpeed = 1
		elif (speed <= 0): walkabout.__interpSpeed = __DEFAULT_INTERP_STEP_SIZE
		else: walkabout.__interpSpeed = speed

	@staticmethod		
	## Enable or disable wall collision checking. By default it is enabled.
	# @param val Set to True to enable wall collision checks or False otherwise.
	def setWallCheck(val):
		walkabout.__wallCollision = val

	@staticmethod
	## Enable or disable floor collision checking. By default it is enabled.
	# @param val Set to True to enable wall floor checks or False otherwise.
	def setFloorCheck(val):
		walkabout.__floorCollision = val
	
	# PRIVATE METHOD
	@staticmethod
	def __getCameraInfo():
		walkabout.__camPosition = walkabout.__theCamera.getPosition()
		walkabout.__headOffset = walkabout.__theCamera.getHeadOffset()
		walkabout.__headPositionWorld = walkabout.__theCamera.localToWorldPosition(walkabout.__headOffset)
	
	# PRIVATE METHOD
	@staticmethod
	def __saveState():
		walkabout.__oldCamera = walkabout.__camPosition
		walkabout.__old__headPositionWorld = walkabout.__headPositionWorld
	
	# PRIVATE METHOD
	# Callback for querySceneRay
	@staticmethod
	def __walkaboutCallback(node, distance):
		# save away the closest object you have intersected with
		if (node != None):
			if (distance < walkabout.__minDistance):
				walkabout.__minDistance = distance
				#print(">>" + str(walkabout.__minDistance)+"\n")

	# PRIVATE METHOD
	# Code to do floor collisions
	@staticmethod
	def __climb(dt):
		
		climbablePositionWorld = Vector3(walkabout.__headPositionWorld.x, walkabout.__headPositionWorld.y, walkabout.__headPositionWorld.z)
		#print(__headOffset)
			
		climbablePositionWorld.y = walkabout.__headPositionWorld.y-(walkabout.__headOffset.y*(1-walkabout.__climbableRatio))
		#print(__headPositionWorld.y, climbablePositionWorld.y, headOffset.y, walkabout.__climbableRatio)

		walkabout.__minDistance = walkabout.__FAR
			
		# fire a ray downward from head to climbable height. And figure out what you hit.
		# i.e. you can only climb objects that are climbable height
		# whenever something is hit call the callback (note: there is no guarantee of order of objects hit so you
		# need to go thru all hit objects and figure out which has the minimum distance from your head
		querySceneRay(climbablePositionWorld, Vector3(0,-1,0), walkabout.__walkaboutCallback)

		# Try to control how fast you step based on dt - THIS IS CURRENTLY DISABLED UNTIL FURTHER TESTING
		# Generally if framework is more than 1 then it's pretty bad so make the stepSize 1 so that
		# you immediately land on the next step, no interpolation.
		# If your dt is small (frame rate is good) then base stepsize on dt * 10
		# Still needs more experimentation. An alternative strategy is to just make the stepSize constant
		# like 0.1 which forces all steps no matter how big to take 10 iterations to interpolate
		# if (dt >=1): stepSize = 1
		# else: stepSize = dt*10
		# if (stepSize >=1): stepSize=1
			
		if (walkabout.__minDistance != walkabout.__FAR):
			walkabout.__camPosition.y = walkabout.__camPosition.y + ((climbablePositionWorld.y - walkabout.__camPosition.y - walkabout.__minDistance)* walkabout.__interpSpeed)
			walkabout.__theCamera.setPosition(walkabout.__camPosition)
	
	# PRIVATE METHOD
	# Code to do wall collisions
	@staticmethod
	def __collide(dt):

		climbablePositionWorld = Vector3(walkabout.__headPositionWorld.x, walkabout.__headPositionWorld.y, walkabout.__headPositionWorld.z)
		#print(headOffset)
			
		climbablePositionWorld.y = walkabout.__headPositionWorld.y-(walkabout.__headOffset.y*(1-walkabout.__climbableRatio))
		#print(__headPositionWorld.y, climbablePositionWorld.y, headOffset.y, walkabout.__climbableRatio)
		
		####################
		# Now check for objects in the direction you are walking.
		# This works by computing an angled ray forward and downward.
		# So first compute that vector.
		
		# It only does collision checks for movements greater than DEFAULT_WALKCHECK_LENGTH meters.
		# Anything smaller may be overkill
		# So we ignore it but we return False so to tell walkabout not to save the current position info
		# so that we can accumulate a larger movement step
		difference = walkabout.__headPositionWorld - walkabout.__old__headPositionWorld
		length = difference.magnitude()
		if (length < walkabout.__DEFAULT_WALKCHECK_LENGTH):
			return False
	
		# Compute the direction you are walking in (not facing). Remember you can walk backwards into a wall.
		# Filter for situations where atan2 is undefined i.e. atan2(y,x) where y=0 and x=0
		if (not((walkabout.__headPositionWorld.x == walkabout.__old__headPositionWorld.x) and (walkabout.__headPositionWorld.z == walkabout.__old__headPositionWorld.z))):
			angle = math.atan2(walkabout.__headPositionWorld.z-walkabout.__old__headPositionWorld.z,walkabout.__headPositionWorld.x-walkabout.__old__headPositionWorld.x)
			angle = degrees(angle)+90
		else:
			angle = 0
		
		# THIS SECOND CALL MAY NOT BE NECESSARY
		#headOffset = walkabout.__theCamera.getHeadOffset()
		#__headPositionWorld = walkabout.__theCamera.localToWorldPosition(headOffset)
	
		collisionRayAdjacent = walkabout.__headPositionWorld.y-climbablePositionWorld.y
		collisionRayOpposite = tan(radians(walkabout.__rayAngle)) * collisionRayAdjacent

		# This is the head of the vector
		collisionRay = Vector3(0,-collisionRayAdjacent,-collisionRayOpposite).normalize()
		
		# Rotate the ray in the direction you are walking in about the y axis
		verticalAxis = Vector3(0,1,0)
		collisionRay = collisionRay.rotate_around(verticalAxis, radians(-angle))
		
		# This is the tail of the vector
		#collisionRayBase = Vector3(0,0,0)
		
		# Need to transform these into world coordinates before we can use it to fire the ray
		collisionRayWorld = walkabout.__theCamera.localToWorldPosition(collisionRay)
		#collisionRayBaseWorld = walkabout.__theCamera.localToWorldPosition(collisionRayBase)
		
		#g_sphere.setPosition(Vector3(0,2,0)+collisionRay)
		#g_sphere2.setPosition(Vector3(0,2,0))

		walkabout.__minDistance = walkabout.__FAR
		#querySceneRay(__headPositionWorld, collisionRayWorld-collisionRayBaseWorld, walkabout.walkaboutCallback)
		querySceneRay(walkabout.__headPositionWorld, collisionRay, walkabout.__walkaboutCallback)

		if (walkabout.__minDistance != walkabout.__FAR):
			# If something is obstructing you then restore to previous camera position.
			hypoteneuse = collisionRayOpposite/sin(radians(walkabout.__rayAngle))
			if (walkabout.__minDistance < hypoteneuse):
				walkabout.__camPosition=walkabout.__oldCamera - (walkabout.__headPositionWorld-walkabout.__old__headPositionWorld)
				walkabout.__theCamera.setPosition(walkabout.__camPosition)	
				
		return True


	@staticmethod
	## Call this function each time in your OmegaLib update function and give it the dt
	# @param dt Give it dt from Omegalib's update function.
	def update(dt):
		walkabout.__getCameraInfo()
		if (walkabout.__floorCollision == True):
			walkabout.__climb(dt)
		
		if (walkabout.__wallCollision == True):
			if (walkabout.__collide(dt)):
				walkabout.__saveState()
		else:
			walkabout.__saveState()
		
			
