from SortingAlgs.AbstractSort import AbstractSort

import tkinter as tk
from time import sleep

class MergeSort(AbstractSort):
    def __init__(self, gui, timeStep, l, myPlot):
        super().__init__(gui, timeStep, l, myPlot)
        self.worstCase = 'O(n log(n))'
        self.avgCase = 'O(n log(n))'
        self.bestCase = 'O(n log(n))'
        self.dummyList = l.copy()

    def updateGUI(self, l, low, high):
        if not self.gui:
            return
        dummyText = list()
        dummyText.append(self.dummyList[:low])
        dummyText.append(self.dummyList[low:high])
        dummyText.append(self.dummyList[high:])
        if len(self.l) <= 150:
            self.gui.listText.set(dummyText)
            sleep(self.timeStep)
        self.gui.root.update()
        self.myPlot.update(self.dummyList)
        

    #def mergeSort(self, l):
    def mergeSort(self, l, low, high):
        if len(l) > 1:
            mid = len(l)//2
            L = l[:mid]
            R = l[mid:]
            #self.mergeSort(L)
            #self.mergeSort(R)
            self.mergeSort(L, low, low+mid)
            self.mergeSort(R, low+mid, high)
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
                    self.myPlot.update(self.dummyList)
                else:
                    self.updateGUI(l, low, high)
                if self.kill:
                    return
            while i < len(L):
                l[k] = L[i]
                self.dummyList[low+k] = L[i]
                i += 1
                k += 1
                if len(l) == len(self.l):
                    super().updateGUI()
                    self.myPlot.update(self.dummyList)
                else:
                    self.updateGUI(l, low, high)
                if self.kill:
                    return
            while j < len(R):
                l[k]=R[j]
                self.dummyList[low+k] = R[j]
                j += 1
                k += 1
                if len(l) == len(self.l):
                    super().updateGUI()
                    self.myPlot.update(self.dummyList)
                else:
                    self.updateGUI(l, low, high)
                if self.kill:
                    return
                    