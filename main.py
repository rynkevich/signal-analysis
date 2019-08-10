import json
import sys
import matplotlib.pyplot as plt

from analysis import harmonic_signal, rms_a, rms_b, calculate_error, fourier_amplitude
from helpers import k_to_number, phi_to_number

N = 64
EXPECTED_RMS = 0.707
EXPECTED_AMPLITUDE = 1

SIGNAL_LABEL = r"$\mathrm{sin}(\frac{2\pi n}{N})$"
SHIFTED_SIGNAL_LABEL = r"$\mathrm{sin}(\frac{2\pi n}{N} + \phi)$"


def main():
    data_path = sys.argv[1]
    variant = int(sys.argv[2])
    with open(data_path, encoding='utf-8') as data_file:
        data = json.loads(data_file.read())

    data = data[variant - 1]
    k = k_to_number(data['K'], N)
    phi = phi_to_number(data['phi'])

    fig, axes = plt.subplots(3, sharex=True)
    fig.canvas.set_window_title('Signal Analysis')
    fig.suptitle('Signal Analysis')
    plt.xlabel('M')

    big_m_range = range(k, 2 * N)

    signal = harmonic_signal(N)
    shifted_signal = harmonic_signal(N, phi)

    show_errors(axes, signal, big_m_range, SIGNAL_LABEL)
    show_errors(axes, shifted_signal, big_m_range, SHIFTED_SIGNAL_LABEL)

    plt.show()


def show_errors(axes, signal, big_m_range, legend_label):
    show_error(axes[0], signal, rms_a, EXPECTED_RMS, big_m_range, legend_label)
    show_error(axes[1], signal, rms_b, EXPECTED_RMS, big_m_range, legend_label)
    show_error(axes[2], signal, fourier_amplitude, EXPECTED_AMPLITUDE, big_m_range, legend_label)


def show_error(ax, signal, characteristic, expected_value, big_m_range, legend_label):
    signal_errors = calculate_error(signal, characteristic, expected_value, big_m_range)
    ax.margins(0.01)
    ax.plot(big_m_range, signal_errors, label=legend_label)
    ax.legend(loc=7, prop={'size': 9})


if __name__ == '__main__':
    main()
