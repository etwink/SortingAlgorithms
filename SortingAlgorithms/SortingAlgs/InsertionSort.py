from SortingAlgs.AbstractSort import AbstractSort

import tkinter as tk
from time import sleep

class InsertionSort(AbstractSort):
    def __init__(self, gui, timeStep, l):
        super().__init__(gui, timeStep, l)
        self.i = 1

    def insertionSort(self):
        for i  in range(1, len(self.l)):
            key = self.l[i]
            j = i-1
            while j >= 0 and key < self.l[j]:
                self.l[j+1] = self.l[j]
                j -= 1
                self.updateGUI()
            self.l[j+1]=key
            if self.kill:
                    self.i = i
                    return
        self.kill = True