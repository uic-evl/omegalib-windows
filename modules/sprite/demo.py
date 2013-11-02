from cyclops import *
from math import *
import random
import sprite


size = sprite.createSizeUniform()
window_size = sprite.createWindowSizeUniform()
window_size.setVector2f(Vector2(854, 480))

for i in range(0, 1000):
    x = random.random() * 10 - 5
    y = random.random() * 10 - 5
    z = -random.random() * 10
    star = sprite.createSprite('star.png', size, window_size, True)
    # disable culling for the sprite: since culling would be based on its center
    # the sprite would be culled before actually being out of screen.
    star.setCullingActive(False)
    # just for fun: color each star randomly.
    r = random.random()
    g = random.random()
    b = random.random()
    star.getMaterial().setColor(Color(r, g, b, 1), Color(0,0,0,1))
    star.setPosition(x, y, z)

# just for fun: animate star size
def onUpdate(frame, time, dt):
	sz = (sin(time) + 1) * 64
	size.setFloat(sz)
	
setUpdateFunction(onUpdate)