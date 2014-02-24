from omega import *
from cyclops import *

scene = getSceneManager()

# Load a static model
torusModel = ModelInfo()
torusModel.name = "torus"
torusModel.path = "chicago_flat.earth"
scene.loadModel(torusModel)

# Create a scene object using the loaded model
torus = StaticObject.create("torus")
torus.setEffect("colored")
setNearFarZ(1, 2 * torus.getBoundRadius())

# Load a kmz file
#kmzModel = ModelInfo()
#kmzModel.name = "UnionStation"
#kmzModel.path = "tribunetower.kmz"
#kmzModel.mapName = "torus"
#scene.loadModel(kmzModel)

#kmz = StaticObject.create("UnionStation")
#all = SceneNode.create("everything")
#all.addChild(kmz)

cam = getDefaultCamera()

# Setting the camera by hand. Should find a better way
cam.setPosition(torus.getBoundCenter() + Vector3(7768.82, 2281.18, 7034.08))
cam.getController().setSpeed(300)
