# import time
import pyvisa
# import lupa
# from lupa import LuaRuntime
# lua = LuaRuntime(unpack_returned_tuples=True)  # that not an error

rm = pyvisa.ResourceManager()
rm.list_resources()
inst = rm.open_resource('GPIB0::14::INSTR')
print(inst.query('*IDN?'))

input_text = "Test Success"
