from SortingAlgs.AbstractSort import AbstractSort

import tkinter as tk
from time import sleep

class SelectionSort(AbstractSort):
    def __init__(self, gui, timeStep, l, myPlot):
        super().__init__(gui, timeStep, l, myPlot)
        self.worstCase = 'O(n^2)'
        self.avgCase = 'O(n^2)'
        self.bestCase = 'O(n^2)'
        self.i = 0

    def selectionSort(self):
        for i in range(len(self.l)):
            min = i
            for j in range(i + 1, len(self.l)):
                if self.l[min] > self.l[j]:
                    min = j
            copy = self.l[min]
            self.l[min] = self.l[i]
            self.l[i] = copy
            self.updateGUI()
            self.myPlot.update(self.l)
            if self.kill:
                    self.i = i
                    return
        self.kill = True


