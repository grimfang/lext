#!/usr/bin/python

# System imports

# Panda Engine imports
# NEEDS CLEANING !
from panda3d.bullet import BulletWorld, BulletDebugNode
from pandac.PandaModules import Vec3
from direct.task.Task import Task

# Game imports

#----------------------------------------------------------------------#

class PhysicsMgr():

    def __init__(self, _game, _gravity=(0, 0, -9)):

    	self.game = _game
    	self.physicsWorld = BulletWorld()
    	self.physicsWorld.setGravity(Vec3(_gravity))

    def startPhysics(self):
    	taskMgr.add(self.updatePhysics, "update-physics")

    def stopPhysics(self):
    	taskMgr.remove("update-physics")

    def setPhysicsDebug(self, _bool=False):
        debugNode = BulletDebugNode('Debug')
        self.debugNP = render.attachNewNode(debugNode)

        if _bool:
            debugNode = BulletDebugNode('Debug')
            debugNode.showWireframe(True)
            debugNode.showConstraints(True)
            debugNode.showBoundingBoxes(False)
            debugNode.showNormals(False)
            self.debugNP = render.attachNewNode(debugNode)
            self.physicsWorld.setDebugNode(self.debugNP.node())
            self.debugNP.show()
        else:
            self.debugNP.hide()
            #debugNode = None

    def updatePhysics(self, task):
    	dt = globalClock.getDt()
        self.physicsWorld.doPhysics(dt, 5, 1.0/240.0)

        return task.cont

