import pyvisa

rm = pyvisa.ResourceManager()
inst = rm.open_resource(f"GPIB0::9::INSTR")

__channel__ = "a"


def abort():
    ...


def buffer_getstats():
    ...


def buffer_recalculatestats():
    ...


def cal_adjustdate():
    ...


def cal_date():
    ...


def cal_due():
    ...


def cal_lock():
    ...


def cal_...word():
    ...


def cal_polarity():
    ...


def cal_restore():
    ...


def cal_save():
    ...


def cal_state():
    ...


def cal_unlock():
    ...


def contact_calibratehi():
    ...


def contact_calibratelo():
    ...


def contact_check():
    ...


def contact_r():
    ...


def contact_speed():
    ...


def contact_threshold():
    ...


def makebuffer():
    ...


def measure_analogfilter():
    ...


def measure_autorange(measure_func_, STATE, channel=__channel__):
    inst.write(f"smu{channel}.measure.autorange{measure_func_} = smu{channel}.AUTORANGE_{STATE}")


def measure_autozero():
    ...


def measure_calibrate():
    ...


def measure_count():
    ...


def measure_delay():
    ...


def measure_delayfactor():
    ...


def measure_filter_count():
    ...


def measure_filter_enable():
    ...


def measure_filter_type():
    ...


def measure_highcrangedelayfactor():
    ...


def measure_interval():
    ...


def measure_lowrange():
    ...


def measure_nplc():
    ...


def measure_overlapped():
    ...


def measure_range(measure_func_, max_value, channel=__channel__):
    inst.write(f"smu{channel}.measure.range{measure_func_} = {max_value}")


def measure_rel_enable():
    ...


def measure_rel_level():
    ...


def measure(measure_func_, channel=__channel__):
    result = inst.query(f"print(smu{channel}.measure.{measure_func_}())")
    if measure_func_ == "iv":
        return float(result[:11]), float(result[12:-1])
    return float(result)


def measure_andstep():
    ...


def nvbuffer():
    ...


def reset(channel=__channel__):
    inst.write(f"smu{channel}.reset()")


def savebuffer():
    ...


def sense():
    ...


def source_autorange(source_func_, STATE, channel=__channel__):
    inst.write(f"smu{channel}.source.autorange{source_func_} = smu{channel}.AUTORANGE_{STATE}")


def source_calibrate():
    ...


def source_compliance():
    ...


def source_delay():
    ...


def source_func(source_function, channel=__channel__):
    inst.write(f"smu{channel}.source.func = smu{channel}.OUTPUT_{source_function}")


def source_highc():
    ...


def source_level(source_func_, level_value, channel=__channel__):
    inst.write(f"smu{channel}.source.level{source_func_} = {level_value}")


def source_limit(source_func_, limit_value, channel=__channel__):
    inst.write(f"smu{channel}.source.limit{source_func_} = {limit_value}")


def source_lowrange():
    ...


def source_offfunc():
    ...


def source_offlimit():
    ...


def source_offmode():
    ...


def source_output(STATE, channel=__channel__):
    inst.write(f"smu{channel}.source.output = smu{channel}.OUTPUT_{STATE}")


def source_outputenableaction():
    ...


def source_range(source_func_, range_value, channel=__channel__):
    inst.write(f"smu{channel}.source.range{source_func_} = {range_value}")


def source_settling():
    ...


def source_sink():
    ...


def trigger_arm_count():
    ...


def trigger_arm_set():
    ...


def trigger_stimulus():
    ...


def trigger_ARMED_EVENT_ID():
    ...


def trigger_autoclear():
    ...


def trigger_count():
    ...


def trigger_endpulse_action():
    ...


def trigger_endpulse_set():
    ...


def trigger_endpulse_stimulus():
    ...


def trigger_endsweep_action():
    ...


def trigger_IDLE_EVENT_ID():
    ...


def trigger_initiate():
    ...


def trigger_measure_action():
    ...


def trigger_measure_set():
    ...


def trigger_measure_stimulus():
    ...


def trigger_measure():
    ...


def trigger_MEASURE_COMPLETE_EVENT_ID():
    ...


def trigger_PULES_COMPLETE_EVENT_ID():
    ...


def trigger_source_action():
    ...


def trigger_source_limit():
    ...


def trigger_source_linear():
    ...


def trigger_source_list():
    ...


def trigger_source_log():
    ...


def trigger_source_set():
    ...


def trigger_source_stimulus():
    ...


def trigger_SOURCE_COMPLETE_EVENT_ID():
    ...


def trigger_SWEEP_COMPLETE_EVENT_ID():
    ...


def trigger_SWEEPING_EVENT_ID():
    ...
