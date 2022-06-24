# import pyvisa
# import re
#
# Resource_Manager = pyvisa.ResourceManager()
# Instrument_List = Resource_Manager.list_resources()
#
# print(Instrument_List)
#
# # Finde_Instrument = reInstrument_List

# coding=utf8
# the above tag defines encoding for this document and is for Python 2.x compatibility

import re

regex_ASRL = r"('ASRL[0-9]::INSTR')(, ){1,}"

test_str = "('ASRL3::INSTR', 'ASRL4::INSTR', 'GPIB0::14::INSTR')"

matches = re.sub(regex_ASRL, "", test_str)

regeex_left = r"(\(){1,}"

matches = re.sub(regeex_left, "", matches)

regeex_right = r"(\)){1,}"

matches = re.sub(regeex_right, "", matches)

print(matches)
