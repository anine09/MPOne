import pyvisa

from .manual import tek_2636B
from .manual import wk_41100

class Instrument:

    def __init__(self, Instrument_MAC: int):
        self.MAC = Instrument_MAC
        rm = pyvisa.ResourceManager()
        self.inst = rm.open_resource(f"GPIB0::{self.MAC}::INSTR")
        self.query_inst_type()

    def query_inst_type(self):
        inst_IDN = self.inst.query("*IDN?\x20")
        if inst_IDN == "Keithley Instruments Inc., Model 2636B, 4308079, 3.2.2\n":
            # Tektronix Keithley 2636B
            self.inst_type = "tek_2636B"
            self.man = tek_2636B
        elif inst_IDN == "WAYNE KERR, 41100, 17411029, 4.143Z3\n":
            self.inst_type = "wk_41100"
            self.man = wk_41100
        else:
            # Not Support
            raise NotImplementedError("Temporary does not support this instrument.")

    def set(self, **set_dict):
        if "Level" in set_dict:
            Level = set_dict["Level"]
            self.man.set_Level(Level)

        if "Range" in set_dict:
            Range = set_dict["Range"]
            self.man.set_Range(Range)

        if "Func" in set_dict:
            Func = set_dict["Func"]
            self.man.set_Func(Func)

        if "Limit" in set_dict:
            Limit = set_dict["Limit"]
            self.man.set_Limit(Limit)

        if "Freq" in set_dict:
            Freq = set_dict["Freq"]
            self.man.set_Freq(Freq)
 
        if self.inst_type == "tek_2636B":
            if "Output" in set_dict:
                Output_STATE = set_dict["Output"].upper()
                self.man.set_Output(Output_STATE)

    def measure(self, measure_func_=None):
        if self.inst_type == "tek_2636B" and measure_func_ is not None:
            return self.man.measure(measure_func_)
        return self.man.measure()

    def raw_command(self, command, communication_mode="w"):
        if communication_mode == "w":
            self.inst.write(f"{command}")
        elif communication_mode == "q":
            return self.inst.query(f"{command}")
        elif communication_mode == "r":
            return self.inst.read()
