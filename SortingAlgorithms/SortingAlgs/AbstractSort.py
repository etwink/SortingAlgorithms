import time
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
        self.worstCase = 'O()'
        self.avgCase = 'O()'
        self.bestCase = 'O()'
        self.specialCaseInfo = ''

    def killSort(self):
        self.kill = True

    def updateGUI(self):
        if not self.gui:
            return
        if len(self.l) <= 150:
            # self.gui.listText.set(self.l)
            sleep(self.timeStep)
        # if not isinstance(self.gui.currentSort, self):
        timeComplexity = self.getTimeComplexity()
        timeComplexityString = 'Worst Case: {} Average Case: {} Best Case: {}'.format(timeComplexity[0], timeComplexity[1], timeComplexity[2])
        if self.specialCaseInfo:
            timeComplexityString += '\nAdditional Info: {}'.format(timeComplexity[3])
        self.gui.timeComplexity.set(timeComplexityString)
        self.gui.root.update()

    def getTimeComplexity(self):
        return [self.worstCase, self.avgCase, self.bestCase, self.specialCaseInfo]
        
        