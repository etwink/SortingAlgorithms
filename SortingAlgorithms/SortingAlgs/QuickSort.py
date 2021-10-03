from SortingAlgs.AbstractSort import AbstractSort

import tkinter as tk
import random
from time import sleep

class QuickSort(AbstractSort):
    def __init__(self, gui, timeStep, l):
        super().__init__(gui, timeStep, l)
        # self.dummyList = l.copy()

    def partition(self, start, end, l):
        pivot_index = random.randrange(start,end)
        l[pivot_index], l[start] = l[start], l[pivot_index]

        pivot_index = start
        pivot = l[pivot_index]

        while start < end:
            if self.kill:
                return
            while start < len(l) and l[start] <= pivot:
                start += 1

            while l[end] > pivot:
                end -= 1

            if start < end:
                l[start], l[end] = l[end], l[start]
                self.updateGUI()

        l[end], l[pivot_index] = l[pivot_index], l[end]
        self.updateGUI()

        return end

    
    def quickSort(self, start, end, l):
        if self.kill:
            return
        if start < end:
            p = self.partition(start, end, l)
            self.quickSort(start, p-1, l)
            self.quickSort(p+1, end, l)