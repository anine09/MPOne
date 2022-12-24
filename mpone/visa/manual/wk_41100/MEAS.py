import pyvisa

rm = pyvisa.ResourceManager()
inst = rm.open_resource(f"GPIB0::6::INSTR")


# :MEAS:TRIGger
def TRIGger():
    return inst.query(":MEAS:TRIGger")


# :MEAS:RESult?
def RESult_():  # Deprecated
    return inst.query(":MEAS:RESult? ")


def NUMber_OF_TESTS():
    ...


def NUMber_OF_TESTS_():
    ...


def TEST():
    ...


# :MEAS:FREQuency <real>
def FREQuency(frequency):
    inst.write(f":MEAS:FREQ\x20{frequency}")


def FREQuency_():
    ...


# :MEAS:LEVel <real>
def LEVel(level):
    inst.write(f":MEAS:LEVel\x20{level}")


def LEVel_():
    ...


# :MEAS:SPEED <disc>
def SPEED(speed):
    inst.write(f":MEAS:SPEED\x20{speed}")


def SPEED_():
    ...


# :MEAS:RANGE <disc>
def RANGE(measurement_range):
    inst.write(f":MEAS:RANGE\x20{measurement_range}")


def RANGE_():
    ...


def EQU_CCT():
    ...


def EQU_CCT_():
    ...


# :MEAS:FUNC1 <disc>
def FUNC1(func_1):
    inst.write(f":MEAS:FUNC1\x20{func_1}")


def FUNC1_():
    ...


# :MEAS:FUNC2 <disc>
def FUNC2(func_2):
    inst.write(f":MEAS:FUNC2\x20{func_2}")


def FUNC2_():
    ...


# :MEAS:BIAS <disc>
def BIAS(bias):
    inst.write(f":MEAS:BIAS\x20{bias}")


def BIAS_STAT_():
    ...


def SCALE():
    ...


def SCALE_():
    ...


# :MEAS:LIMit1 <disc>
def LIMit1(limit_1):
    inst.write(f":MEAS:LIMit1\x20{limit_1}")


def LIMit1_():
    ...


# :MEAS:LIMit2 <disc>
def LIMit2(limit_2):
    inst.write(f":MEAS:LIMit2\x20{limit_2}")


def LIMit2_():
    ...


def NOMinal1():
    ...


def NOMinal1_():
    ...


def NOMinal2():
    ...


def NOMinal2_():
    ...


def HI_LIMit1():
    ...


def HI_LIMit1_():
    ...


def HI_LIMit2():
    ...


def HI_LIMit2_():
    ...


def LO_LIMit1():
    ...


def LO_LIMit1_():
    ...


def LO_LIMit2():
    ...


def LO_LIMit2_():
    ...


def OPER():
    ...


def OPER_():
    ...
