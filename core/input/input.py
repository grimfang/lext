#!/usr/bin/python

# System imports

# Panda Engine imports
from direct.showbase.DirectObject import DirectObject
from direct.showbase.InputStateGlobal import inputState
from panda3d.core import Point3
# Game imports

#----------------------------------------------------------------------#

class Input(DirectObject):
    
    def __init__(self, _game):
        
        self.game = _game
        
        # Reset Player
        self.accept('r', self.msgPlayerReset)
        
        ## MOVEMENT INPUTS ## 
        inputState.watchWithModifiers('up', 'w')
        inputState.watchWithModifiers('down', 's')
        inputState.watchWithModifiers('left', 'a')
        inputState.watchWithModifiers('right', 'd')
        inputState.watchWithModifiers('space', 'space')
        inputState.watchWithModifiers('control', 'control')

        # Camera
        self.accept('c', self.evtGetCameraPos)

        # Mouse
        #self.accept("mouse1-up", self.setMouseHold, [False])
        self.accept("mouse1", self.evtLeftClick)
        #self.accept("mouse1", self.setMouseHold, [True])
        self.mouseBtnUp = False
        # Wheel
        self.accept("wheel_up", self.evtMouseWheel, [True])
        self.accept("wheel_down", self.evtMouseWheel, [False])
        

        ## Physic Objects list
        self.physicObjects = None
        self.physicSensors = None

        # should populate this automatically
        self.avoidObjects = []

    def start(self):
        taskMgr.add(self.update, "input-update")

    def setMouseHold(self, _bool):
        self.mouseBtnUp = _bool
        if _bool:
            base.messenger.send("mouseClick-down", [True])
        else:
            base.messenger.send("mouseClick-up", [False])

    def evtMouseWheel(self, _bool):
        if _bool:
            base.messenger.send("mouseWheel-up")

        else:
            base.messenger.send("mouseWheel-down")


    # Get the mouse clickPos
    ## Will have to make more than one to return the mouse pos for lookAt updates
    ## And one to handle the hold down for object handling
    def getMousePoint(self): 

        if base.mouseWatcherNode.hasMouse():
            pMouse = base.mouseWatcherNode.getMouse()
            pFrom = Point3()
            pTo = Point3()
            base.camLens.extrude(pMouse, pFrom, pTo)

            pFrom = render.getRelativePoint(base.cam, pFrom)
            pTo = render.getRelativePoint(base.cam, pTo)

            ## For the guns, maybe have it closest
            result = self.game.physicsMgr.physicsWorld.rayTestClosest(pFrom, pTo)

            # result.getNode().getName()
            if result.getNode() == None or result.getNode().getName() in self.avoidObjects:
                pass
            else:            
                messenger.send("check-mouse-lclick", [result])

        else:
            return [False, Point3(0, 0, 0)]


    def getMousePointAlways(self):

        if base.mouseWatcherNode.hasMouse():
            pMouse = base.mouseWatcherNode.getMouse()
            pFrom = Point3()
            pTo = Point3()
            base.camLens.extrude(pMouse, pFrom, pTo)

            pFrom = render.getRelativePoint(base.cam, pFrom)
            pTo = render.getRelativePoint(base.cam, pTo)

            ## For the guns, maybe have it closest
            result = self.game.physicsMgr.physicsWorld.rayTestAll(pFrom, pTo)
            
            for hit in result.getHits():
                if hit.getNode().getName() == "ground":
                    return hit.getHitPos()


    def update(self, task):
        self.getMousePoint()

        return task.cont
            
    def updatePhysicObjects(self, _listObjects):
        self.physicObjects = _listObjects

    def updatePhysicSensors(self, _listSensors):
        self.physicSensors = _listSensors
    
    ### EVENT MSGS ###
    def msgPlayerReset(self):
        base.messenger.send("player-reset")

    ## Rewrite other event type methods like this!
    def evtLeftClick(self):
        ## Move create device to ctrl+leftclick to place.
        #base.messenger.send("activate-gun", [True])
        self.getMousePoint()

    def evtRightClick(self):
        base.messenger.send("remove-antigravity-device")

    def evtGetCameraPos(self):
        self.game.camera.getCameraPos()

    def evtSetDebug(self):
        print "Set Debug"
        base.messenger.send("set-debug", [True])

    def evtButtonPressed(self, _btnName):
        base.messenger.send("switch-sensor", [_btnName])
