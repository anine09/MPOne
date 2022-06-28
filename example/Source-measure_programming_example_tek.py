from VISA import Automatic_Instrument_Detection as autoDetect
from VISA.Source_Measure.simple_source_measure import simple_source_measure as sm
from test import Live_Data_Plot as plot

# 自动检测与连接设备
tek2600B = autoDetect.detection()

# 根据 Tek 手册示例写的简单的电流测量函数
data = sm(tek2600B, "smua", "voltage", "autorange", 5, 10e-3, "current", 10e-3)

# 启动图形界面，实时画图
plot(data)

"""
sm电流测量函数各参数:
tek2600B --> 这个名字代表着连接上的设备，后期我们会把它给简化掉
smua --> 在 1 号通道进行检测，在手册里叫做通道 A，用 smua 与 smub 表示，后期应该也可以简化
voltage --> 设置源为电压源
autorange --> 自动进行范围设置，当然也支持手动输入最大值，但是手册上说如果规格不对会导致超出范围的错误
5 --> 设定源电压为 5V
第一个 10e-3 --> 设定测量电流的上限为 10mA
current --> 要测量的对象是电流
第二个 10e-3 --> 测量范围是 10mA，这个就是手动设置范围，会比自动设置要快
测量的对象是可以改的，只要 voltage 和  current 调换位置，然后适当调整其他参数就行，总体来说，前5个属于源参数，后3个属于测量参数
"""