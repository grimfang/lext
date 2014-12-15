#!/usr/bin/python

# System imports

# Panda Engine imports
from direct.showbase.DirectObject import DirectObject
from panda3d.core import *

# Game imports
from physics import PlayerPhysics

#----------------------------------------------------------------------#

class Player():
    
    def __init__(self, _game, _name):
        
        self.game = _game
        self.name = _name

        # Player physics body
        self.pPhysicsBody = None
        self.pRayNode = None

        ## Physics
        self.physics = PlayerPhysics(self)

    def start(self):
    	self.buildPlayerPhysicsBody()
    	self.setPlayerModel("ralph")
        taskMgr.add(self.update, "player-update")

    def stop(self):
        taskMgr.remove("player-update")

    def buildPlayerPhysicsBody(self):
    	self.pPhysicsBody = self.physics.createPlayerBody(self.name)
    	#self.playerRopeNode = self.physics.createRopeNode()
        

    def setPlayerModel(self, _modelName):
        self.playerModel = loader.loadModel("assets/models/"+_modelName)
        self.playerModel.setScale(.40)
        self.playerModel.setHpr(180, 0, 0)
        #self.playerModel.setPos(0, 0, 0)

        if self.pPhysicsBody != None:
            self.playerModel.reparentTo(self.pPhysicsBody)
            self.playerModel.setPos(0, 0, -1.15)
        else:
            print "No Player Physics Body found!"

        ## Attach a raynode used for jumping.
        playerRayNode = self.pPhysicsBody.attachNewNode("ray-dummy")
        playerRayNode.setCompass()
        self.pRayNode = playerRayNode

        ## Attach a dummy node for the camera
        self.camDummy = self.pPhysicsBody.attachNewNode("cam-dummy")
        self.camDummy.setCompass()

        ## Telekinesis np to hack pivot
        self.centerRotNode = self.camDummy.attachNewNode("tele-dummy")
        self.centerRotNode.setCompass()

    def update(self, task):

        ## Get the direction to the mouse and set it so that it directs the player to it.
        # Make a change depending on gear
        mpos = self.game.input.getMousePointAlways()
        if mpos != None:
            vector = mpos - self.playerModel.getPos(render)
            #print vector

            self.pPhysicsBody.lookAt(mpos)
        #self.physics.telekinesisTask()
        self.physics.doMovement()

        return task.cont

    ## Event Methods
    def evtPlaceDevice(self, _mouseFromTo):
    	pass

    def playRunAnim(self):
        pass
