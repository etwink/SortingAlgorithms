from SortingAlgs.AbstractSort import AbstractSort

import tkinter as tk
from time import sleep

class HeapSort(AbstractSort):
    def __init__(self, gui, timeStep, l, myPlot):
        super().__init__(gui, timeStep, l, myPlot)
        self.worstCase = 'O(n log(n))'
        self.avgCase = 'O(n log(n))'
        self.bestCase = 'O(n log(n))'
    
    def heapify(self, arr, n, i):
        if self.kill:
            return
        
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2

        if l < n and arr[largest] < arr[l]:
            largest = l
        
        if r < n and arr[largest] < arr[r]:
            largest = r

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            self.myPlot.update(arr)
            self.updateGUI()
            self.heapify(arr, n, largest)

    def heapSort(self, arr):
        n = len(arr)

        for i in range(n//2 - 1, -1, -1):
            if self.kill:
                return
            self.heapify(arr, n, i)

        for i in range(n-1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]
            self.myPlot.update(arr)
            self.updateGUI()
            if self.kill:
                return
            self.heapify(arr, i, 0)
