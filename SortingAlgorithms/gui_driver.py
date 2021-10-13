from SortingAlgs.AbstractSort import AbstractSort
from SortingAlgs.BubbleSort import BubbleSort
from SortingAlgs.SelectionSort import SelectionSort
from SortingAlgs.InsertionSort import InsertionSort
from SortingAlgs.MergeSort import MergeSort
from SortingAlgs.QuickSort import QuickSort
from SortingAlgs.RadixSort import RadixSort
from SortingAlgs.HeapSort import HeapSort

from HelperFunctions.CreateList import createList
from HelperFunctions.ListShuffle import ListShuffle
from HelperFunctions.reverseList import reverseList
from HelperFunctions.correctnessCheck import correctnessCheck
from HelperFunctions.plotterHelper import myPlot

import tkinter as tk
from tkinter.constants import HORIZONTAL
import matplotlib.pyplot as plt


class GUI_Driver:
    def __init__(self) -> None:
        self.root = tk.Tk()
        self.root.title("Sorting Algorithms")
        self.root.geometry("1800x450")
        self.list = createList(100) #create a list --SHOULD UPDATE SO USER CAN SPECIFY HOW MANY LIST ITEMS WITH AN INPUT FIELD OR SLIDER--
        self.myPlot = myPlot()
        self.listText = tk.StringVar() #create a list text variable to show user the current list. --SHOULD UPDATE WHERE IF LIST LENGTH > ABOUT 200 THEN DISPLAY START AND STOP TIMES INSTEAD AND MAYBE USE A MATPLOT TO SHOW LIST INSTEAD--
        self.currentSort = AbstractSort 
        self.currentSort.kill = True 

    def gui_setUp(self):

        #logic for each of the buttons
        def shuffleClick(): #button that is used to shuffle the list
            stopClick()
            actionText.set("Shuffling...") 
            ListShuffle(self.list) #shuffling the list
            self.listText.set(self.list) 
            self.myPlot.update(self.list)
            correctText.set("Not Sorted Correctly :(") 
            actionText.set("Idle...") 

        def stopClick(): #button that is used to stop the current action --POTENTIALLY NEED TO UPDATE FOR MERGESORT-- as well as issues with concurrency control
            if not self.currentSort.kill: 
                actionText.set("Stopping...") 
                self.currentSort.killSort() #run the killSort definition for the current sorting operation
                self.listText.set(self.list) 

        def changeListClick():
            stopClick()
            actionText.set("Creating a new list...")
            s = int(listSizeEntry.get())
            self.list = createList(s)
            self.listText.set(self.list) 
            self.myPlot.changeDimensions(self.list)
            self.myPlot.update(self.list)
            del self.currentSort
            self.currentSort = AbstractSort
            checkClick()
            actionText.set("Idle...")

        def reversedListClick():
            stopClick()
            actionText.set("Creating a new list...")
            self.list = reverseList(int(listSizeEntry.get()))
            self.listText.set(self.list)
            self.myPlot.changeDimensions(self.list) 
            self.myPlot.update(self.list)
            del self.currentSort
            self.currentSort = AbstractSort
            checkClick()
            actionText.set("Idle...")
        
        def checkClick(): #button that is used to check if the current list is sorted correctly
            actionText.set("Checking Correctness...") 
            if correctnessCheck(self.list): #if the correctnessCheck definition returns true set the correct text variable to sorted correctly
                correctText.set("Sorted Correctly!")
            else: #else if the correctnessCheck definition returns false, set the correct text variable to not sorted correctly
                correctText.set("Not Sorted Correctly :(")
            actionText.set("Idle...") 

        def bubbleClick(): #button that is used to start a bubblesort
            stopClick()
            actionText.set("Bubble Sorting...") 
            if not isinstance(self.currentSort, BubbleSort): #if the current sort is not a bubble sort then create a new bubblesort object
                self.currentSort = BubbleSort(self, speedSlider.get() / float(1000), self.list, self.myPlot)
            self.currentSort.timeStep = speedSlider.get() / float(1000) #set the current sort timestep. Semi-redundant but is useful if the user wants to change the speed of the current sort.
            if not correctnessCheck(self.list): #if it fails the correctnessCheck... (is useful so the user won't try sorting a sorted list. Could be removed if it is something that I would like the user to be able to do i.e. best case scenario sorts)
                self.currentSort.kill=False 
                self.currentSort.bubbleSort() 
            checkClick() 
            actionText.set("Idle...") 

        def selectionClick(): #button that is used to start a selection sort
            stopClick()
            actionText.set("Selection Sorting...") 
            if not isinstance(self.currentSort, SelectionSort):
                self.currentSort = SelectionSort(self, speedSlider.get() / float(1000), self.list, self.myPlot)
            self.currentSort.timeStep = speedSlider.get() / float(1000)
            if not correctnessCheck(self.list):
                self.currentSort.kill=False
                self.currentSort.selectionSort()
            checkClick() 
            actionText.set("Idle...") 

        def insertionClick(): #button that is used to start an insertion sort
            stopClick()
            actionText.set("Insertion Sorting...")
            if not isinstance(self.currentSort, InsertionSort): 
                self.currentSort = InsertionSort(self, speedSlider.get() / float(1000), self.list, self.myPlot)
            self.currentSort.timeStep = speedSlider.get() / float(1000) 
            if not correctnessCheck(self.list):
                self.currentSort.kill=False
                self.currentSort.insertionSort()
            checkClick() 
            actionText.set("Idle...") 


        def mergeClick(): #button that is used to start a merge sort
            stopClick()
            actionText.set("Merge Sorting...") 
            if not isinstance(self.currentSort, MergeSort): 
                self.currentSort = MergeSort(self, speedSlider.get() / float(1000), self.list, self.myPlot)
            else:
                self.currentSort.dummyList = self.list
            self.currentSort.timeStep = speedSlider.get() / float(1000)
            if not correctnessCheck(self.list): 
                self.currentSort.kill=False
                self.currentSort.mergeSort(self.list, 0, len(self.list))
                self.myPlot.update(self.list)
            checkClick() 
            actionText.set("Idle...") 

        def quickClick(): #button that is used to start a merge sort
            stopClick()
            actionText.set("Quick Sorting...") 
            if not isinstance(self.currentSort, QuickSort):
                self.currentSort = QuickSort(self, speedSlider.get() / float(1000), self.list, self.myPlot)
            self.currentSort.timeStep = speedSlider.get() / float(1000) 
            if not correctnessCheck(self.list):
                self.currentSort.kill=False
                self.currentSort.quickSort(0, len(self.list) - 1, self.list)
            checkClick() 
            actionText.set("Idle...")

        def radixClick(): #button that is used to start a radix sort
            stopClick()
            actionText.set("Radix Sorting...") 
            if not isinstance(self.currentSort, RadixSort): 
                self.currentSort = RadixSort(self, speedSlider.get() / float(1000), self.list, self.myPlot)
            self.currentSort.timeStep = speedSlider.get() / float(1000) 
            if not correctnessCheck(self.list): 
                self.currentSort.kill=False
                self.currentSort.radixSort(self.list)
            checkClick() 
            actionText.set("Idle...") 

        def heapClick(): #button that is used to start a radix sort
            stopClick()
            actionText.set("Heap Sorting...") 
            if not isinstance(self.currentSort, HeapSort): 
                self.currentSort = HeapSort(self, speedSlider.get() / float(1000), self.list, self.myPlot)
            self.currentSort.timeStep = speedSlider.get() / float(1000) 
            if not correctnessCheck(self.list): 
                self.currentSort.kill=False
                self.currentSort.heapSort(self.list)
            checkClick() 
            actionText.set("Idle...") 

        self.myPlot.plot(self.list)
        self.myPlot.show()

        actionText = tk.StringVar() 
        actionText.set("Idle...")

        correctText = tk.StringVar() 
        correctText.set("")

        self.listText.set(self.list) 
        
        shuffleButton = tk.Button(self.root, text="Shuffle", command=shuffleClick)
        stopButton = tk.Button(self.root, text="Stop", command=stopClick)
        checkButton = tk.Button(self.root, text="Check Correctness", command=checkClick)
        listSizeEntry = tk.Entry(self.root)
        listSizeEntry.insert(0, '100')
        changeSizeButton = tk.Button(self.root, text="Change Size of List", command=changeListClick)
        reversedListButton = tk.Button(self.root, text="Create a Backwards List", command=reversedListClick)
        speedSlider = tk.Scale(self.root, from_=0, to=100, length=500, orient=HORIZONTAL)

        bubbleButton = tk.Button(self.root, text="Bubble", command=bubbleClick)
        selectionButton = tk.Button(self.root, text="Selection", command=selectionClick)
        insertionButton = tk.Button(self.root, text="Insertion", command=insertionClick)
        mergeButton = tk.Button(self.root, text="Merge", command=mergeClick)
        quickButton = tk.Button(self.root, text="Quick", command=quickClick)
        radixButton = tk.Button(self.root, text="Radix", command=radixClick)
        heapButton = tk.Button(self.root, text="Heap", command=heapClick)

        listLabel = tk.Label(self.root, textvariable=self.listText)
        actionLabel = tk.Label(self.root, textvariable=actionText)
        correctLabel = tk.Label(self.root, textvariable=correctText)

        shuffleButton.pack()
        stopButton.pack()
        checkButton.pack()
        listSizeEntry.pack()
        changeSizeButton.pack()
        reversedListButton.pack()
        speedSlider.pack()

        bubbleButton.pack()
        selectionButton.pack()
        insertionButton.pack()
        mergeButton.pack()
        quickButton.pack()
        radixButton.pack()
        heapButton.pack()

        correctLabel.pack()
        actionLabel.pack()
        listLabel.pack()

        # canvas = FigureCanvasTkAgg(self.myPlot.fig, master=self.root)
        # canvas.draw()
        # canvas.get_tk_widget().pack()

    def currentAction(self, action):
        pass

    def gui_run(self):
        self.root.mainloop()


