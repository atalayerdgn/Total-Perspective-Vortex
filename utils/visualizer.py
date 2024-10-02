# from headers.imports import *
import matplotlib.pyplot as plt
import numpy as np

class Visualizer:
    def __init__(self):
        pass
    @staticmethod
    def plot_signal(time_values, signal_values, label, color, title):
        """
        Plots a single signal.

        Args:
            time_values (np.ndarray): Time values for the signal.
            signal_values (np.ndarray): Signal values.
            label (str): Label for the signal.
            color (str): Color of the plot.
            title (str): Title of the plot.
        """
        plt.figure(figsize=(10, 6))
        plt.plot(time_values, signal_values, label=label, color=color, linewidth=2)
        plt.xlabel('Time (seconds)')
        plt.ylabel('Amplitude')
        plt.title(title)
        plt.legend()
        plt.grid(True)
        plt.show()

# frequency = 5
# amplitude = 1
# duration = 1
# sampling_rate = 40

# t_analog = np.linspace(0, duration, 1000)
# analog_signal = amplitude * np.sin(2 * np.pi * frequency * t_analog)

# Visualizer.plot_signal(
#     time_values=t_analog, 
#     signal_values=analog_signal, 
#     label='Analog Signal', 
#     color='blue', 
#     title='Analog Signal (Continuous)'
# )
