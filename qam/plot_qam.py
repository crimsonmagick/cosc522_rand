import matplotlib.pyplot as plt
import numpy as np

constellation = {
    (0, 0, 0): (1, 0),
    (0, 0, 1): (2, 0),
    (0, 1, 0): (1, np.pi / 2),
    (0, 1, 1): (2, np.pi / 2),
    (1, 0, 0): (1, np.pi),
    (1, 0, 1): (2, np.pi),
    (1, 1, 0): (1, 3 * np.pi / 2),
    (1, 1, 1): (2, 3 * np.pi / 2)
}

def normalize_angle(angle):
    return (angle + 2 * np.pi) % (2 * np.pi)

def plot_constellation():
    pts = []
    labels = []
    for bits, (A, theta) in constellation.items():
        I = A * np.cos(theta)
        Q = A * np.sin(theta)
        pts.append((I, Q))
        labels.append("".join(map(str, bits)))

    I_vals = np.array([p[0] for p in pts]) # apparently called in-phase
    Q_vals = np.array([p[1] for p in pts]) # apparently called quadarature

    plt.figure(figsize=(5, 5))
    plt.scatter(I_vals, Q_vals, s=60)
    for (x, y), lab in zip(pts, labels):
        plt.text(x, y, " "+lab, va="center", ha="left", fontsize=10)

    # Axes through origin
    lim = max(2.2, 1.2 * max(np.abs(I_vals).max(), np.abs(Q_vals).max()))
    plt.axhline(0, color="0.7", linewidth=1)
    plt.axvline(0, color="0.7", linewidth=1)
    plt.xlim(-lim, lim)
    plt.ylim(-lim, lim)
    plt.gca().set_aspect("equal", adjustable="box")
    plt.grid(True, linestyle=":")
    plt.title("Constellation")

def plot_qam():

    signal = [
        (1, 0, 1),
        (1, 1, 0),
        (1, 0, 1),
        (1, 0, 0),
        (0, 1, 1),
        (0, 0, 1),
        (0, 0, 0),
        (1, 1, 1)
    ]
    signal_str = "".join("".join(str(b) for b in triplet) for triplet in signal)

    theta_p = np.pi / 2

    # rectangular coordinates for matplotlib
    signal_b = []  # let's use b for baud
    signal_y = []

    baud_offset = -1
    period = 1.0  # period is 1 baud

    # assume theta = pi / 2 to start
    b_arr, y_arr = sinusoid_segment(1, theta_p)
    signal_b.append(b_arr + baud_offset)
    signal_y.append(y_arr)
    baud_offset += period

    for triplet in signal:
        amp, theta_delta = constellation[triplet]
        theta_c = normalize_angle(theta_delta + theta_p)
        b_arr, y_arr = sinusoid_segment(amp, theta_c)  # get rectangular coordinates
        signal_b.append(b_arr + baud_offset)
        signal_y.append(y_arr)
        baud_offset += period
        theta_p = theta_c

    signal_b = np.concatenate(signal_b)
    signal_y = np.concatenate(signal_y)
    plt.figure(figsize=(12, 5))
    plt.plot(signal_b, signal_y)
    plt.title(f"QAM {signal_str}")
    plt.xlabel("Baud")
    plt.ylabel("A")
    plt.grid(True)

    # draw baud boundaries
    n = len(signal)
    for k in range(n + 1):
        plt.axvline(k * period, color='0.8', linewidth=0.8)

    # leave some room above and place tuple labels centered in each baud
    y_min, y_max = float(signal_y.min()), float(signal_y.max())
    y_range = y_max - y_min
    y_label = y_max + 0.12 * y_range  # push labels above the waveform
    plt.ylim(y_min - 0.05 * y_range, y_label + 0.15 * y_range)

    for k, triplet in enumerate(signal):
        x = k * period + 0.5 * period
        txt = "".join(map(str, triplet))  # e.g., '101'
        plt.text(x, y_label, txt, ha='center', va='bottom', fontsize=11)

    plt.text(-0.25, y_label + 1, "Welby Seely COSC 522 9/11/25 - Corrected", ha='center', va='bottom', fontsize=14)

    plt.show()


def sinusoid_segment(amp, phase, f_c=1, T=1, samples=100):
    """
    Create a sinusoidal segment representing one baud.

    amp: amplitude of the symbol
    phase: phase of the symbol (radians)
    f_c: carrier frequency (Hz)
    T: symbol duration
    samples: number of points per symbol
    """
    t = np.linspace(0, T, samples, endpoint=False)
    y = amp * np.sin(2 * np.pi * f_c * t + phase)
    return t, y


if __name__ == '__main__':
    plot_constellation()
    plot_qam()
