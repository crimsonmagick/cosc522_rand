import matplotlib.pyplot as plt
import numpy as np


def main():
    signal = np.array([0, 1, 1, 1, 0, 0, 1, 0])
    nrz_scenario(signal)
    nrzi_scenario(signal)
    manchester_scenario(signal)
    differential_manchester_scenario(signal)
    alternate_mark_inversion(signal)


def nrz_scenario(binary_input):
    signal = pad(1 - binary_input)
    time = np.arange(len(signal))

    plt.figure()
    plt.step(time, signal, where='post', label='Binary Signal Voltage', color='red')

    plt.xlim(time.min(), time.max())
    plt.ylim(0, 1.5)
    plt.grid(True)

    boundaries = np.arange(len(binary_input) + 1)
    centers = np.arange(len(binary_input)) + 0.5
    ticks = np.concatenate([boundaries, centers])
    ticks.sort()
    labels = [''] * len(boundaries) + list(map(str, binary_input))
    labels = [lbl for _, lbl in sorted(zip(np.concatenate([boundaries, centers]), labels))]

    plt.xticks(ticks, labels)

    plt.xlabel('Bit Stream')
    plt.ylabel('Binary Signal Voltage')
    plt.title('Non Return to Zero (Active Low)')
    plt.legend()
    plt.show()


def nrzi_scenario(binary_input):
    level = 1
    signal = []
    for b in binary_input:
        if b == 1:
            level = 1 - level
            signal.append(level)
        else:
            signal.append(level)
    signal = pad(signal)

    time = np.arange(len(signal))

    plt.figure()
    plt.step(time, signal, where='post', label='Binary Signal Voltage', color='red')

    plt.xlim(time.min(), time.max())
    plt.ylim(0, 1.5)
    plt.grid(True)

    boundaries = np.arange(len(binary_input) + 1)
    centers = np.arange(len(binary_input)) + 0.5
    ticks = np.concatenate([boundaries, centers])
    ticks.sort()
    labels = [''] * len(boundaries) + list(map(str, binary_input))
    labels = [lbl for _, lbl in sorted(zip(np.concatenate([boundaries, centers]), labels))]

    plt.xticks(ticks, labels)

    plt.xlabel('Bit Stream')
    plt.ylabel('Binary Signal Voltage')
    plt.title('NRZI Encoding (Assume We Start High)')
    plt.legend()
    plt.show()


def manchester_scenario(binary_input):
    signal = [y for x in binary_input for y in manchester_tuple(x)]
    signal = pad(signal)

    time = np.arange(0, len(signal) / 2, 0.5)

    plt.figure()
    plt.step(time, signal, where='post', label='Binary Signal Voltage', color='red')

    plt.xlim(time.min(), time.max())
    plt.ylim(0, 1.5)
    plt.grid(True)

    boundaries = np.arange(len(binary_input) + 1)
    centers = np.arange(len(binary_input)) + 0.5
    ticks = np.concatenate([boundaries, centers])
    ticks.sort()
    labels = [''] * len(boundaries) + list(map(str, binary_input))
    labels = [lbl for _, lbl in sorted(zip(np.concatenate([boundaries, centers]), labels))]

    plt.xticks(ticks, labels)

    plt.xlabel('Bit Stream')
    plt.ylabel('Binary Signal Voltage')
    plt.title('Manchester encoding')
    plt.legend()
    plt.show()


def differential_manchester_scenario(binary_input):
    level = 1
    signal = []
    for b in binary_input:
        if b == 1:
            signal.append(level)
            level = 1 - level
            signal.append(level)
        else:
            level = 1 - level
            signal.append(level)
            level = 1 - level
            signal.append(level)

    signal = pad(signal)

    time = np.arange(0, len(signal) / 2, 0.5)

    plt.figure()
    plt.step(time, signal, where='post', label='Binary Signal Voltage', color='red')

    plt.xlim(time.min(), time.max())
    plt.ylim(0, 1.5)
    plt.grid(True)

    boundaries = np.arange(len(binary_input) + 1)
    centers = np.arange(len(binary_input)) + 0.5
    ticks = np.concatenate([boundaries, centers])
    ticks.sort()
    labels = [''] * len(boundaries) + list(map(str, binary_input))
    labels = [lbl for _, lbl in sorted(zip(np.concatenate([boundaries, centers]), labels))]

    plt.xticks(ticks, labels)

    plt.xlabel('Bit Stream')
    plt.ylabel('Binary Signal Voltage')
    plt.title('Differential Manchester Encoding (Previous Signal High)')
    plt.legend()
    plt.show()


def alternate_mark_inversion(binary_input):
    level = 1
    signal = []
    for b in binary_input:
        if b == 1:
            level = -1 * level
            signal.append(level)
        else:
            signal.append(0)

    signal = pad(signal)

    time = np.arange(len(signal))

    plt.figure()
    plt.step(time, signal, where='post', label='Binary Signal Voltage', color='red')

    plt.xlim(time.min(), time.max())
    plt.ylim(-1.5, 1.5)
    plt.grid(True)

    boundaries = np.arange(len(binary_input) + 1)
    centers = np.arange(len(binary_input)) + 0.5
    ticks = np.concatenate([boundaries, centers])
    ticks.sort()
    labels = [''] * len(boundaries) + list(map(str, binary_input))
    labels = [lbl for _, lbl in sorted(zip(np.concatenate([boundaries, centers]), labels))]

    plt.xticks(ticks, labels)

    plt.xlabel('Bit Stream')
    plt.ylabel('Binary Signal Voltage')
    plt.title('Alternate Mark Inversion (Previous "1" Was High)')
    plt.legend()
    plt.show()


def manchester_tuple(num):
    if num == 0:
        return 1, 0
    else:
        return 0, 1


def pad(signal):
    return np.append(signal, signal[-1])


if __name__ == '__main__':
    main()
