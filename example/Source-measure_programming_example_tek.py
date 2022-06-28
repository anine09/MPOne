import pyvisa

# Argument List
"""
Source function and range: Voltage, autorange 
Source output level: 5 V 
Current compliance limit: 10 mA 
Measure function and range: Current, 10 mA 
"""

# Tek Code Example
"""
-- Restore 2600B defaults. 
smua.reset() 
-- Select voltage source function. 
smua.source.func = smua.OUTPUT_DCVOLTS 
-- Set source range to autorange. 
smua.source.autorangev = smua.AUTORANGE_ON 
-- Set voltage source to 5 V. 
smua.source.levelv = 5  
-- Set current limit to 10 mA. 
smua.source.limiti = 10e-3 
-- Set current range to 10 mA. 
smua.measure.rangei = 10e-3 
-- Turn on output. 
smua.source.output = smua.OUTPUT_ON 
-- Print and place the current reading in the reading buffer. 
print(smua.measure.i(smua.nvbuffer1)) 
-- Turn off output. 
smua.source.output = smua.OUTPUT_OFF 
"""


def source_measure(device_name, channel, source_function, source_range, source_output_level, current_compliance_limit,
                   measure_function,
                   measure_range, debug=False):
    if debug:
        channel = "suma"
        source_function = "Voltage"
        source_range = "autorange"
        source_output_level = "5"  # 5 V
        current_compliance_limit = "10e-3"  # 10 mA
        measure_function = "Current"
        measure_range = "10e-3"  # 10 mA

    device_name.write(f"{channel}.reset()")  # Restore 2600B defaults.
    if source_function == "Voltage":
        device_name.write(f"{channel}.source.func = {channel}.OUTPUT_DCVOLTS")  # Select voltage source function.
    if source_range == "autorange":
        device_name.write(f"{channel}.source.autorangev = {channel}.AUTORANGE_ON")  # Set source range to autorange.
    device_name.write(f"{channel}.source.levelv = {source_output_level}")  # Set voltage source to 5 V.
    device_name.write(f"{channel}.source.limiti = {current_compliance_limit}")  # Set current range to 10 mA.
    if measure_function == "Current":
        device_name.write(f"{channel}.measure.rangei = {measure_range}")  # Set current range to 10 mA.
    device_name.write(f"{channel}.source.output = {channel}.OUTPUT_ON")  # Turn on output.
    device_name.write(
        f"{channel}.measure.i({channel}.nvbuffer1)")  # Print and place the current reading in the reading buffer.
    device_name.write(f"{channel}.source.output = {channel}.OUTPUT_OFF ")  # Turn off output.
