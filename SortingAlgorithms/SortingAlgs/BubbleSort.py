from HelperFunctions.plotterHelper import myPlot
from SortingAlgs.AbstractSort import AbstractSort

import tkinter as tk
from time import sleep

class BubbleSort(AbstractSort):
    def __init__(self, gui, timeStep, l, myPlot):
        super().__init__(gui, timeStep, l, myPlot)
        self.i = 0
        self.worstCase = 'O(n^2)'
        self.avgCase = 'O(n^2)'
        self.bestCase = 'O(n)'

    def bubbleSort(self):
        for i in range(0, len(self.l)):
            for j in range(len(self.l)-i-1):
                if self.l[j] > self.l[j+1]:
                    copy = self.l[j+1]
                    self.l[j+1] = self.l[j]
                    self.l[j] = copy
                    self.updateGUI()
                    self.myPlot.update(self.l)
                if self.kill:
                    self.i = i
                    return
        self.kill = True


