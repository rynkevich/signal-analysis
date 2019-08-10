from math import pi


# Inefficient and unsecure, not to be used in real-life apps

def k_to_number(string, n_big):
    return round(eval(string.replace('N', str(n_big))))


def phi_to_number(string):
    return eval(string.replace('pi', str(pi)))
