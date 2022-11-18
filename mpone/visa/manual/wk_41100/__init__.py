from . import MEAS


def measure():
    return MEAS.TRIGger()


def set_Freq(frequency):
    MEAS.FREQuency(frequency)


def set_Level(level):
    MEAS.LEVel(level)


def set_Speed(speed):
    MEAS.SPEED(speed)


def set_Range(measurement_range):
    MEAS.RANGE(measurement_range)


def set_Func_1(func_1):
    MEAS.FUNC1(func_1)


def set_Func_2(func_2):
    MEAS.FUNC2(func_2)


def set_Bias(bias):
    MEAS.BIAS(bias)
