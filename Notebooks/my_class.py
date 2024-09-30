import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import medfilt, savgol_filter, wiener


class DataGenAndPlot():
    def __init__(self):
        self.data_X = None
        self.data_Y = None
        
    def generate_data(self,data_size = 200, noise_level = 1.0):
        self.data_X = np.linspace(0,1,data_size)
        self.data_Y = np.random.normal(size=data_size, scale = noise_level, loc = 1.0)
    
    def plot_data(self, data_X = None, data_Y = None):
        if data_Y is None:
            if self.data_Y is not None:
                data_Y = self.data_Y
                data_X = self.data_X
            else:
                raise ValueError("No data - You haven't run generate_data() yet, or provide some data")
        
        fig, axes = plt.subplots(figsize=(4,2))
        axes.plot(data_X, data_Y)
        return fig


#Now extend the class
# Subclass that extends the DataGenAndPlot class

class DataGenExtended(DataGenAndPlot):
    def __init__(self):
        # Initialize the base class (Person)
        super().__init__()
        
    def plot_data_smoothed(self, method = 'medfilt', window_size = 7):
        """
        Input: method (str): method of smoothing, can be 'medfilt' for median filter, 'savgol' or 'wiener'
        Returns: fig: matplotlib figure object
        """

        if self.data_Y is None:
            raise ValueError("You don't have any data! You need to generate some by running generate_data() !")
            
        if method=='medfilt':
            data_smoothed = medfilt(self.data_Y, kernel_size = window_size)
        elif method=='savgol':
            data_smoothed = savgol_filter(self.data_Y, window_length=window_size, polyorder=2)
        elif method == 'wiener':
            data_smoothed = wiener(self.data_Y, mysize = window_size)
        
        fig = self.plot_data(self.data_X, data_smoothed)

        return fig
        