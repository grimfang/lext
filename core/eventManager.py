#!/usr/bin/python

# System imports

# Panda Engine imports
from direct.showbase.DirectObject import DirectObject

# Game imports

#----------------------------------------------------------------------#

## Rollin EventMgr ##

class EventMgr(DirectObject):

    def __init__(self, _game):
        self.game = _game
        self.events = []

    def start(self):
        self.accept("check-mouse-lclick", self.handleMouseLeft)
        self.accept("handle-lock", self.handleButtonLock)

    def stop(self):
        self.ignore("check-mouse-lclick")
        self.ignore("handle-lock")

    # Don't know if this is the best way yet... The old way seemed stupid
    def registerEvent(self, _eventName=None, _eventMethod=None):

        if _eventName == None:
            print "Event Name can't be None"
            return

        # Add event name to the events list duh
        self.events.append(_eventName)
        # Build an event
        return self.accept(_eventName, _eventMethod)

    def handleMouseLeft(self, _result):
        
        nodeName = _result.getNode().getName()

        if "button" in nodeName:
            if self.game.level.physicSensors[nodeName]:
                btn = self.game.level.physicSensors[nodeName]
                if btn.state == True:
                    cmd = btn.sendCommand
                    messenger.send(cmd)
                else:
                    print "The button is locked!"
                    # Show on screen msg!

    def handleButtonLock(self, _lock, _setUnlock):
        # _lock is the fuse
        # _setUnlock is the button to unlock, or to set needs for type fuse
        if _lock in self.game.level.physicSensors[_setUnlock].needs:
            self.game.level.physicSensors[_setUnlock].needs[_lock] = True
            self.checkButtonNeeds(_lock, _setUnlock)

    def checkButtonNeeds(self, _lock, _setUnlock):
        # Chec the button needs, if all true set the button to active, else leave dead
        tmp = []
        for lock in self.game.level.physicSensors[_setUnlock].needs:

            if self.game.level.physicSensors[_setUnlock].needs[lock] == True:
                tmp.append(True)
            else:
                tmp.append(False)

        if False in tmp:
            self.game.level.physicSensors[_setUnlock].state = False
            #print tmp
        else:
            self.game.level.physicSensors[_setUnlock].state = True
            #print tmp



