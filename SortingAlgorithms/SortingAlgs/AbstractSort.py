import tkinter as tk
from time import sleep

class AbstractSort:
    def __init__(self, gui, timeStep, l):
        self.kill = False
        self.gui = gui
        self.timeStep = timeStep
        self.l = l
    def killSort(self):
        self.kill = True
    def updateGUI(self):
        if not self.gui:
            return
        self.gui.listText.set(self.l)
        self.gui.root.update()
        sleep(self.timeStep)