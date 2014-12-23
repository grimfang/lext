#!/usr/bin/python

# System imports

# Panda Engine imports

# Game imports
from eventManager import EventMgr
from physicsManager import PhysicsMgr
from input.input import Input
from camera.camera import Camera
from level.level import Level
from player.player import Player


#----------------------------------------------------------------------#

## GameCore ##

class GameCore:

    def __init__(self, _main):
        
        self.main = _main

        ## Set parent nodes in the scenegraph
        self.physicsParentNode = render.attachNewNode("physicsParentNode")
        self.levelParentNode = render.attachNewNode("levelParentNode")
        self.objectsParentNode = render.attachNewNode("objectsParentNode")
        self.lightsParentNode = render.attachNewNode("lightsParentNode")
        self.aiParentNode = render.attachNewNode("aiParentNode")

        ## Start Event Manager
        self.eventMgr = EventMgr(self)

    def startGame(self, _playerName="DefaultPlayer"):
        self.autoShader()
        self.eventMgr.start()
        print "---> Started EventSystem"
        self.loadPhysicsSystem()
        print "---> Loaded Physics System"

        self.loadInputSystem()
        print "---> Loaded Input System"

        self.loadLevelSystem()
        print "---> Loaded Level System"

        self.loadPlayerSystem()
        print "---> Loaded Player System"

        self.loadCameraSystem()
        print "---> Loaded Camera System"

    def stopGame(self):
    	pass

##------- SUB SYSTEMS -------##
    def loadPhysicsSystem(self):
        self.physicsMgr = PhysicsMgr(self)
        self.physicsMgr.startPhysics()
        self.physicsMgr.setPhysicsDebug()

    def loadInputSystem(self):
        self.input = Input(self)
        #self.input.start()

    def loadLevelSystem(self):
        self.level = Level(self)
        self.level.buildLevel("assets/level/intro")
        self.level.start()

    def loadPlayerSystem(self):
        self.player = Player(self, "Main Man")
        self.player.start()

    def loadCameraSystem(self):
        self.camera = Camera(self)
        self.camera.start()

    def autoShader(self):
        render.setShaderAuto()


