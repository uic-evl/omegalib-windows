from cyclops import *
from math import *
import random
import sprite

light = SphereShape.create(0.3, 2)
light.setPosition(-2, 2, -4)
light.setEffect('colored -e yellow')

window_size = sprite.createWindowSizeUniform()
window_size.setVector2f(Vector2(854, 480))

getSceneManager().setBackgroundColor(Color('black'))

lf = []

for i in range(0, 15):
	size = sprite.createSizeUniform()
	size.setFloat(150 - i * 32)
	star = sprite.createSprite('monochromatic/img%i.png'%i, size, window_size, False)
	star.setCullingActive(False)
	star.getMaterial().setTransparent(True)
	star.getMaterial().setAdditive(True)
	lf.append(star)

def onUpdate(frame, time, dt):
	screenDistance = 2
	opticsWidth = 0.5
	
	localHeadPos = getDefaultCamera().getHeadOffset()
	worldHeadPos = getDefaultCamera().localToWorldPosition(localHeadPos)
	screenCenter = getDefaultCamera().localToWorldPosition(localHeadPos - Vector3(0,0,screenDistance))
	
	lightDir = (light.getPosition() - worldHeadPos).normalize()
	
	lensFlareStart = worldHeadPos + lightDir * (screenDistance + opticsWidth)
	lensFlareDir = (screenCenter - lensFlareStart).normalize()
	#print(lensFlareDir)
	
	# start 1 meter behind 'lens' 
	cur = 0
	incr = (screenCenter - lensFlareStart).magnitude() / 7
	
	for lensFlare in lf:
		lensFlare.setPosition(lensFlareStart + lensFlareDir * cur)
		cur = cur + incr
	
#sz = (sin(time) + 1) * 64
#size.setFloat(sz)
	
setUpdateFunction(onUpdate)