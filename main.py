#!/usr/bin/python

# System imports
import sys

# Panda Engine imports
from pandac.PandaModules import loadPrcFileData
loadPrcFileData("",
"""
    window-title Boxed-In 'Development build'
    fullscreen 0
    win-size 1260 876
    cursor-hidden 0
    sync-video 1
    show-frame-rate-meter 1

"""
)

from direct.showbase.ShowBase import ShowBase

# Game imports
from core.game import GameCore

#----------------------------------------------------------------------#

## BoxedIn ##

class Main(ShowBase):

    def __init__(self):
        ShowBase.__init__(self)
        # Set esc for force exit
        self.accept('escape', self.exitApp)

        # Load the game
        self.game = GameCore(self)
        self.game.startGame()

        print render.ls()
        self.game.physicsMgr.setPhysicsDebug(True)


    def exitApp(self):
        sys.exit()



main = Main()
run()
