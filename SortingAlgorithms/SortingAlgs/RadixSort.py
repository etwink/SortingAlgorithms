from SortingAlgs.AbstractSort import AbstractSort

import tkinter as tk
from time import sleep

class RadixSort(AbstractSort):
    def __init__(self, gui, timeStep, l, myPlot):
        super().__init__(gui, timeStep, l, myPlot)
        self.worstCase = 'O(nk)'
        self.avgCase = 'O(nk)'
        self.bestCase = 'O(nk)'
        self.specialCaseInfo = 'Where n is the size of the list and k is the maximum number of digits (in this case, 10)'

    def countingSort(self, l, exp1):
        n = len(l)
        output = [0]*(n)
        count = [0]*(10)

        for i in range(0,n):
            if self.kill:
                return
            index = l[i] // exp1
            count[index % 10] += 1

        for i in range(1,10):
            if self.kill:
                return
            count[i] += count[i-1]
        
        i = n - 1

        while i >= 0:
            if self.kill:
                return
            index = l[i]//exp1
            output[count[index%10] - 1] = l[i]
            count[index%10] -= 1
            i -= 1
            self.updateGUI()
            self.myPlot.update(self.l)

        i = 0
        for i in range(0, len(l)):
            if self.kill:
                return
            l[i] = output[i]
            self.updateGUI()
            self.myPlot.update(self.l)
        
    def radixSort(self, l):
        max1 = max(l)
        exp = 1
        while max1 / exp >= min(l):
            if self.kill:
                return
            self.countingSort(l, exp)
            exp *= 10

