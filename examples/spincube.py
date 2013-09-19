# basic omegalib script: just display a textured spinning cube.
from omega import *
from cyclops import *

box = BoxShape.create(0.8, 0.8, 0.8)
box.setPosition(Vector3(0, 2, -3))

# Apply an emissive textured effect (no lighting)
box.setEffect("textured -v emissive -d cyclops/test/omega-transparent.png")

test = Text3D.create('fonts/arial.ttf', 1, "TEST")
test.setFacingCamera(getDefaultCamera())
test.setColor(Color("red"))
test.setPosition(Vector3(0,2,-3))
import time
def hey():
	while True:
		print "hey"
		time.sleep(1)
def ooh():
	while True:
		print "ooh"
		time.sleep(0.01)

# Spin the box!
def onUpdate(frame, t, dt):
	box.pitch(dt)
	box.yaw(dt / 3)
	print "AA"
setUpdateFunction(onUpdate)

import threading
t = threading.Thread(target = ooh)
t.start()



