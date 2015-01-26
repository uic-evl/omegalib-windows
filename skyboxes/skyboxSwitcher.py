from omega import *
from cyclops import *
from omegaToolkit import *

skybox = None

def enableSkybox(value):
	global skybox
	if(value == False):
		getSceneManager().setSkyBox(None)
		getSceneManager().setBackgroundColor(Color('black'))
	else:
		getSceneManager().setSkyBox(skybox)

def setupSkyboxSwitcher(menu):
	# setup skybox
	global skybox
	skybox = Skybox()
	skybox.loadCubeMap("common/cubemaps/grid4", "png")
	getSceneManager().setSkyBox(skybox)
	
	miSkyboxes = menu.addItem(MenuItemType.SubMenu)
	miSkyboxes.setText("Background");
	menuSkyboxes = miSkyboxes.getSubMenu()

	misbe = menuSkyboxes.addItem(MenuItemType.Button)
	misbe.setText("Enable")
	misbe.getButton().setCheckable(True)
	misbe.getButton().setChecked(True)
	misbe.setCommand('skyboxSwitcher.enableSkybox(%value%)')

	misb1 = menuSkyboxes.addItem(MenuItemType.Button)
	misb1.setText("Gradient 1")
	misb1.setCommand('skyboxSwitcher.skybox.loadCubeMap("cubemaps/gradient1", "png")')
	misb1 = menuSkyboxes.addItem(MenuItemType.Button)
	misb1.setText("Gradient 2")
	misb1.setCommand('skyboxSwitcher.skybox.loadCubeMap("cubemaps/gradient2", "png")')
	misb1 = menuSkyboxes.addItem(MenuItemType.Button)
	misb1.setText("Grid 1")
	misb1.setCommand('skyboxSwitcher.skybox.loadCubeMap("common/cubemaps/grid3", "png")')
	misb1 = menuSkyboxes.addItem(MenuItemType.Button)
	misb1.setText("Grid 2")
	misb1.setCommand('skyboxSwitcher.skybox.loadCubeMap("common/cubemaps/grid4", "png")')
	misb1 = menuSkyboxes.addItem(MenuItemType.Button)
	misb1.setText("Stars")
	misb1.setCommand('skyboxSwitcher.skybox.loadCubeMap("common/cubemaps/stars", "png")')

