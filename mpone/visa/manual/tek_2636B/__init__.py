from . import smu


def measure(measure_func_="iv"):
    return smu.measure(measure_func_)


def set_Level(level):
    if "i" in level:
        smu.source_level("i", level["i"])

    if "v" in level:
        smu.source_level("v", level["v"])


def set_Range(range_list):
    if "src" in range_list:
        if "v" in range_list["src"]:
            range_value = range_list["src"]["v"]
            if range_value == "auto":  # auto range_list
                smu.source_autorange("v", "ON")
            elif range_value == "manual":
                smu.source_autorange("v", "OFF")
            else:
                smu.source_range("v", range_value)
    if "meas" in range_list:
        if "v" in range_list["meas"]:
            range_value = range_list["meas"]["v"]
            if range_value == "auto":  # auto range_list
                smu.source_autorange("v", "ON")
            elif range_value == "manual":
                smu.source_autorange("v", "OFF")
            else:
                smu.source_range("v", range_value)

# TODO: write Func for tk
def set_Func():
    pass

# TODO: write Limit(ONLY)
def set_Limit():
    pass

# TODO: write Output(ONLY)
def set_Output():
    pass