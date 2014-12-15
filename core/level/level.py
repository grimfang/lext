#!/usr/bin/python

# System imports

# Panda Engine imports
from direct.showbase.DirectObject import DirectObject
from panda3d.core import *
from pandac.PandaModules import *
from panda3d.bullet import *
from direct.task.Task import Task
from direct.interval.LerpInterval import LerpPosInterval

# Game imports
from builder import LevelBuilder

#----------------------------------------------------------------------#

## Used for updating or keeping track of physic objects in the level
class Level(DirectObject):

    def __init__(self, _game):

    	self.game = _game
        self.levelBuilder = LevelBuilder(self)

        ## Level Details ##
        self.levelName = ""
        self.levelDesc = ""
        self.spawnPoint = (2, 2, 0)
        self.coinCount = 0

        ## Keep track of physic_box's so that we can reset the gravity setting upon leaving a device area.
        self.physicObjCount = 0
        self.physicObjects = {}
        self.physicSensors = {}
        self.physicLifts = {}
        self.physicDoors = {}
        self.avoidObjects = []

    def start(self):
    	self.updateAvoidObjects()

    def stop(self):
    	pass

    def buildLevel(self, _levelName):
    	self.levelBuilder.parseEggFile(_levelName)

    # Get physic objects: for guns
    def getPhysicObjects(self):
        xlist = []
    	for obj in self.physicObjects:
            xlist.append(obj)

        self.game.input.updatePhysicObjects(xlist)

    def getPhysicSensors(self):
        xlist = []
        for obj in self.physicSensors:
            xlist.append(obj)
            
        self.game.input.updatePhysicSensors(xlist)

    def getPhysicLifts(self):
        xlist = []
        for obj in self.physicLifts:
            xlist.append(obj)

    def updateAvoidObjects(self):
        # update the list found in input.
        self.game.input.avoidObjects = self.avoidObjects

    def liftHandler(self):
        pass
        # Move the lift with name whatever.

    def update(self, task):

    	print "Should be off"

    	return task.cont