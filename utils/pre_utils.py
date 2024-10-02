#from headers.imports import *
import numpy as np
import matplotlib.pyplot as plt

class pre_utils:
    def __init__(self):
        pass

    @staticmethod
    def generate_analog_signal(frequency, amplitude, duration):
        """
        Generates an analog (continuous) sine wave signal.

        Args:
            frequency (float): Frequency of the sine wave.
            amplitude (float): Amplitude of the sine wave.
            duration (float): Duration in seconds.

        Returns:
            np.ndarray: Time values for the analog signal.
            np.ndarray: Analog sine wave signal values.
        """
        t_analog = np.linspace(0, duration, 1000)
        analog_signal = amplitude * np.sin(2 * np.pi * frequency * t_analog)
        return t_analog, analog_signal

    @staticmethod
    def generate_sampled_signal(frequency, amplitude, duration, sampling_rate):
        """
        Generates the sampled (discrete) signal based on Nyquist theorem.

        Args:
            frequency (float): Frequency of the sine wave.
            amplitude (float): Amplitude of the sine wave.
            duration (float): Duration in seconds.
            sampling_rate (float): Sampling rate in Hz.

        Returns:
            np.ndarray: Time points for the sampled signal.
            np.ndarray: Sampled signal values.
        """
        t_sampled = np.arange(0, duration, 1/sampling_rate)
        sampled_signal = amplitude * np.sin(2 * np.pi * frequency * t_sampled)
        return t_sampled, sampled_signal

    @staticmethod
    def plot_signals_test(t_analog, analog_signal, t_sampled, sampled_signal, frequency, sampling_rate):
        """
        Plots the analog (continuous) and sampled (discrete) signals.

        Args:
            t_analog (np.ndarray): Time values for the analog signal.
            analog_signal (np.ndarray): Analog signal values.
            t_sampled (np.ndarray): Time values for the sampled signal.
            sampled_signal (np.ndarray): Sampled signal values.
            frequency (float): Frequency of the analog signal.
            sampling_rate (float): Sampling rate used for the sampled signal.
        """
        plt.figure(figsize=(10, 6))
        plt.plot(t_analog, analog_signal, label='Analog Signal (Continuous)', color='blue', linewidth=2)
        plt.stem(t_sampled, sampled_signal, linefmt='r-', markerfmt='ro', basefmt='k', label='Sampled Signal (Discrete)')
        plt.xlabel('Time (seconds)')
        plt.ylabel('Amplitude')
        plt.title(f'Analog-to-Digital Conversion\nFrequency = {frequency} Hz, Sampling Rate = {sampling_rate} Hz')
        plt.legend()
        plt.grid(True)
        plt.show()

# frequency = 5
# sampling_rate = 40
# duration = 1
# amplitude = 1


# t_analog, analog_signal = pre_utils.generate_analog_signal(frequency, amplitude, duration)
# t_sampled, sampled_signal = pre_utils.generate_sampled_signal(frequency, amplitude, duration, sampling_rate)

# pre_utils.plot_signals(t_analog, analog_signal, t_sampled, sampled_signal, frequency, sampling_rate)

