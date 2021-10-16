import tkinter as tk
from time import sleep
import matplotlib.pyplot as plt

class AbstractSort:
    def __init__(self, gui, timeStep, l, myPlot):
        self.kill = False
        self.gui = gui
        self.timeStep = timeStep
        self.l = l
        self.myPlot = myPlot

    def killSort(self):
        self.kill = True

    def updateGUI(self):
        if not self.gui:
            return
        if len(self.l) <= 150:
            # self.gui.listText.set(self.l)
            sleep(self.timeStep)
        self.gui.root.update()
        
        