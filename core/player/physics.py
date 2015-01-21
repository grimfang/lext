#!/usr/bin/python

# System imports

# Panda Engine imports
from direct.showbase.DirectObject import DirectObject
from panda3d.bullet import *
from panda3d.core import *
from direct.showbase.InputStateGlobal import inputState

# Game imports

#----------------------------------------------------------------------#

class PlayerPhysics():
    
    def __init__(self, _player):
        
        self.player = _player

        ## Player States
        self.isFloating = False

    def createPlayerBody(self, _name):
    	radius = 0.4
        shape = BulletSphereShape(radius)
        
        node = BulletRigidBodyNode("physicsBody-"+_name)
        node.setMass(1)
        node.addShape(shape)
        
        body = self.player.game.physicsParentNode.attachNewNode(node)
        body.setPos(self.player.game.level.spawnPoint)
        body.setCollideMask(BitMask32.allOn())
        body.setCompass()

        self.player.game.physicsMgr.physicsWorld.attachRigidBody(node)

        return body

    def createRopeNode(self):

    	node = BulletRigidBodyNode("RopeHolder")
    	node.setMass(1)
    	bodyNP = self.player.pPhysicsBody.attachNewNode(node)
    	#bodyNP.setZ(1)
    	bodyNP.setCompass()

    	self.player.game.physicsMgr.physicsWorld.attachRigidBody(node)

    	return bodyNP

    def doMovement(self, _mousePos):
        playerBody = self.player.pPhysicsBody
        speed = Vec3(0, 0, 0)
        jump = Vec3(0, 0, 0)
        force = 4.0
        jumpForce = 1.5
        
        speed = _mousePos
        '''
        if inputState.isSet('left'):
            speed.setX(-force)
        
        if inputState.isSet('right'):
            speed.setX(force)
        
        if inputState.isSet('up'):
             #setY(force)
            print speed
            
        if inputState.isSet('down'):
            speed =- _mousePos #setY(-force)
        '''
        if inputState.isSet('space'):
        
            self.checkFloorCollide()
            if self.isFloating != True:
                jump.setZ(jumpForce)
                self.isFloating = True
            elif self.isFloating == True:
                jump.setZ(0.0)
                #self.game.isFloating = False

        playerBody.node().setActive(True)
        playerBody.node().applyCentralForce(speed)
        playerBody.node().applyCentralImpulse(jump)


    def checkFloorCollide(self):
        # Get player pos
        pos = Point3(self.player.pRayNode.getPos(render))
        
        pFrom = Point3(pos)
        pTo = Point3(float(pos.getX()), float(pos.getY()),float(pos.getZ()-0.7))
        
        result = self.player.game.physicsMgr.physicsWorld.rayTestClosest(pFrom, pTo)
        contactNode = result.getNode()
        
        if contactNode == None or contactNode.getName() == "Ghost-telekinesis":
            self.isFloating = True
            
        else:
            self.isFloating = False

