from math import pi, sin, sqrt, cos


def harmonic_signal(big_n, phase=0):
    return lambda n: sin(2 * pi * n / big_n + phase)


def sample(signal, big_m):
    return tuple(map(signal, range(big_m)))


def rms_a(sampled_signal):
    big_m = len(sampled_signal)
    coeff = 1 / (big_m - 1)
    return sqrt(coeff * sum(signal_value ** 2 for signal_value in sampled_signal))


def rms_b(sampled_signal):
    big_m = len(sampled_signal)
    coeff = 1 / (big_m - 1)
    return sqrt(coeff * sum(signal_value ** 2 for signal_value in sampled_signal) - (coeff * sum(sampled_signal)) ** 2)


# An = √(an^2 + bn^2)
# an = 2 / M * Σ(an * cos(2 * 𝜋 * n / M))
# bn = 2 / M * Σ(an * sin(2 * 𝜋 * n / M))
def fourier_amplitude(sampled_signal):
    big_m = len(sampled_signal)
    an, bn = 0, 0
    for n, signal_value in enumerate(sampled_signal):
        angle = 2 * pi * n / big_m
        an += signal_value * cos(angle)
        bn += signal_value * sin(angle)
    an *= 2 / big_m
    bn *= 2 / big_m
    return sqrt(an ** 2 + bn ** 2)


def calculate_error(signal, characteristic, expected_value, big_m_range):
    return tuple(expected_value - characteristic(sample(signal, big_m)) for big_m in big_m_range)
