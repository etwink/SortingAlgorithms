import matplotlib.pyplot as plt

class myPlot():
    def __init__(self):
        self.fig = plt.figure(num=1)
        self.fm = plt.get_current_fig_manager()
        self.ax = self.fig.add_subplot(111)
        self.line1 = None
    
    
    def plot(self, l):
        yx = list()
        for i in range(min(l), max(l) + 1):
            yx.append(i)
        self.line1, = self.ax.plot(yx, l)
    
    def update(self, l):
        self.show()
        self.line1.set_ydata(l)
        self.fig.canvas.draw()

    def changeDimensions(self, l):
        yx = list()
        for i in range(min(l), max(l) + 1):
            yx.append(i)
        self.ax.set_xlim([min(l), max(l)+1])
        self.ax.set_ylim([min(l), max(l)+1])
        self.line1.set_xdata(yx)
        self.line1.set_ydata(l)
    
    def clear(self):
        self.fig.clf()

    def show(self):
        self.fig.show()

