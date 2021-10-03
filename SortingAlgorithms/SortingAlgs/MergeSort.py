from SortingAlgs.AbstractSort import AbstractSort

import tkinter as tk
from time import sleep

class MergeSort(AbstractSort):
    def __init__(self, gui, timeStep, l):
        super().__init__(gui, timeStep, l)
        self.dummyList = l.copy()

    def updateGUI(self, l, low, high):
        if not self.gui:
            return
        dummyText = list()
        dummyText.append(self.dummyList[:low])
        dummyText.append(self.dummyList[low:high])
        dummyText.append(self.dummyList[high:])
        self.gui.listText.set(dummyText)
        self.gui.root.update()
        sleep(self.timeStep)

    #def mergeSort(self, l):
    def mergeSort(self, l, low, high):
        if len(l) > 1:
            mid = len(l)//2
            L = l[:mid]
            R = l[mid:]
            #self.mergeSort(L)
            #self.mergeSort(R)
            self.mergeSort(L, low, mid)
            self.mergeSort(R, mid, high)
            if self.kill:
                return
            i = j = k = 0
            while i < len(L) and j < len(R):
                if L[i] < R[j]:
                    l[k] = L[i]
                    i += 1
                else:
                    l[k] = R[j]
                    j += 1
                self.dummyList[low+k] = l[k]
                k += 1
                if len(l) == len(self.l):
                    super().updateGUI()
                else:
                    self.updateGUI(l, low, high)
                if self.kill:
                    return
            while i < len(L):
                l[k] = L[i]
                self.dummyList[low+k] = l[k]
                i += 1
                k += 1
                if len(l) == len(self.l):
                    super().updateGUI()
                else:
                    self.updateGUI(l, low, high)
                if self.kill:
                    return
            while j < len(R):
                l[k]=R[j]
                self.dummyList[low+k] = l[k]
                j += 1
                k += 1
                if len(l) == len(self.l):
                    super().updateGUI()
                else:
                    self.updateGUI(l, low, high)
                if self.kill:
                    return