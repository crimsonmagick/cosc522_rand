import matplotlib.pyplot as plt
import numpy as np


def main():
    signal = np.array([0, 1, 1, 1, 0, 0, 1, 0])
    nrz_scenario(signal)


def nrz_scenario(binary_input):
    signal = pad(1 - binary_input)
    time = np.arange(len(signal))

    plt.step(time, signal, where='post', label='Binary Signal', color='red')

    plt.xlim(time.min(), time.max())
    plt.ylim(0, 1.5)

    plt.grid(True)
    plt.xlabel('Time')
    plt.ylabel('Binary Signal')
    plt.title('Non Return to Zero (Active Low)')
    plt.legend()
    plt.show()


def pad(signal):
    return np.append(signal, signal[-1])


if __name__ == '__main__':
    main()
