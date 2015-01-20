#!/usr/bin/python

# System imports

# Panda Engine imports
from direct.showbase.DirectObject import DirectObject
from panda3d.bullet import *
from panda3d.core import *

# Game imports

#----------------------------------------------------------------------#

class DevicePhysics():
    
    def __init__(self, _device):
        
        self.device = _device
        self.physicObjects = self.device.game.levelBuilder.physicObjects

    def createDeviceBody(self, _name, _placePos):

        ## This hack needs fixing...
    	shape = BulletBoxShape(Vec3(2, 2, 3.3))

    	ghost = BulletGhostNode('Ghost-'+_name)
    	ghost.addShape(shape)
    	ghostNP = self.device.game.physicsParentNode.attachNewNode(ghost)
    	# Make hack for adjusting the z axis...
    	fixedZ = _placePos[2] + 3.3
    	ghostNP.setPos(_placePos[0], _placePos[1], fixedZ)
    	ghostNP.setCollideMask(BitMask32(0x0f))

    	self.device.game.physicsMgr.physicsWorld.attachGhost(ghost)

    	return ghostNP

    ## Task method
    def deviceTask(self):
        device = self.device.dPhysicBody
        physicObjects = self.device.game.levelBuilder.physicObjects

        for obj in physicObjects:
            box = physicObjects[obj]

            result = self.device.game.physicsMgr.physicsWorld.contactTestPair(box.node(), device.node())


            if result.getContacts() == []:
                box.node().setGravity(Vec3(0, 0, -9))
                box.node().clearForces()

            else:
                box.node().setActive(True)
                box.node().setGravity(Vec3(0, 0, 0))
                box.node().applyCentralForce(Vec3(0, 0, 0.2))
                



