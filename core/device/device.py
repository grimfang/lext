#!/usr/bin/python

# System imports

# Panda Engine imports
from direct.showbase.DirectObject import DirectObject
from panda3d.bullet import *
from panda3d.core import *

# Game imports
from physics import DevicePhysics

#----------------------------------------------------------------------#
# Anti gravity panels.
# Devices will have to be come more static... like a chamber of force either up/down/left/right, with only one length for now...

class Device():
    
    def __init__(self, _game):
        
        self.game = _game

        self.physics = DevicePhysics(self)

        self.activeDevice = None

    def start(self):
    	taskMgr.add(self.update, "device-task")

    def stop(self):
    	taskMgr.remove("device-task")

    def loadDeviceModel(self, _modelName, _dPhysicBody):
    	self.deviceModel = loader.loadModel("assets/models/"+_modelName)
    	self.deviceModel.reparentTo(_dPhysicBody)

    ## Event Metods
    def evtCreateAntiGravityDev(self, _placePos, _type="up_forwards"):

        if self.activeDevice == None:
    	   self.dPhysicBody = self.physics.createDeviceBody("AntiGravity", _placePos)
    	   self.loadDeviceModel("device_antigravity", self.dPhysicBody)

    	   # Start the task for the device.
    	   # Should add a limit on the devices being created... or delete one if active then create new one.
    	   self.start()
    	   self.activeDevice = self.dPhysicBody

    def evtRemoveAntiGravityDev(self):
        if self.activeDevice != None:
            self.game.physicsMgr.physicsWorld.remove(self.dPhysicBody.node())
            self.deviceModel.removeNode()
            self.dPhysicBody = None
            self.stop()
            self.activeDevice = None
        else:
            pass


    def update(self, task):

    	self.physics.deviceTask()

    	return task.cont