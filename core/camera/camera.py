#!/usr/bin/python

from panda3d.core import *
from direct.showbase.DirectObject import DirectObject
#----------------------------------------------------------------------#

## Camera ##

class Camera(DirectObject):
    
    def __init__(self, _game):
        
        self.game =_game


    def start(self):
        self.setCameraPos()
        self.setCameraHpr()
        self.attachCamOnPlayer()
        #taskMgr.add(self.update, "update-cam")


    def stop(self):
        pass

    # I dono why... but i want it this way...
    def setCameraPos(self):
        base.cam.setPos(-0.0874121, -21.9256, 38.6715)#-0.0874121, -21.9256, 38.6715)
        
    def setCameraHpr(self):
        base.cam.setHpr(-50.81908, -60.4154, -2.94735)

    def attachCamOnPlayer(self):
        base.cam.reparentTo(self.game.player.centerRotNode)
        base.cam.setCompass()

    ## EventMethod
    def getCameraPos(self):
        print "Pos:", base.cam.getPos()
        print "Hpr:", base.cam.getHpr()

    def update(self, task):
        self.getCameraPos()
        return task.cont

    