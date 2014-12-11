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


    # Don't know if this is the best way yet... The old way seemed stupid
    def registerEvent(self, _eventName=None, _eventMethod=None):

        if _eventName == None:
            print "Event Name can't be None"
            return

        # Add event name to the events list duh
        self.events.append(_eventName)
        # Build an event
        return self.accept(_eventName, _eventMethod)


