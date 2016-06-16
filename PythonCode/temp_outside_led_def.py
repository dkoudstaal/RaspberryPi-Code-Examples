import os, fnmatch
import RPi.GPIO as IO
from time import sleep

IO.setmode(IO.BOARD)
IO.setwarnings(False)

warning_ambient = 16
warning_cpu = 18
IO.setup(warning_ambient, IO.OUT)
IO.setup(warning_cpu, IO.OUT)
IO.output(warning_ambient, False)
IO.output(warning_cpu, False)

def find_dir(pattern, path):
    '''
    Function finds the directory name for the temperature
    sensor
    '''
    for root, dirs, files in os.walk(path):
        for name in dirs:
            if fnmatch.fnmatch(name, pattern):
                dir_name = os.path.join(root, name)
                return dir_name

def temperature(dir):
    temp_file = open(dir, "r")
    temp_text = temp_file.read()
    temp_file.close()
    second_line = temp_text.split("\n")[1]
    temp_data = second_line.split("=")[1]
    temp = float(temp_data) / 1000
    return round(temp, 1)

def cpu_temperature():
    temp_cpu_bash = "vcgencmd measure_temp"
    temp_cpu = os.popen(temp_cpu_bash, "r")
    temp_text_cpu = temp_cpu.read()
    temp_cpu.close()
    temp_cpu_data = temp_text_cpu[5 : 9]
    return float(temp_cpu_data)

temp_sensor = find_dir("28-*", "/sys/bus/w1/devices/")+"/w1_slave"
ambient_temp = temperature(temp_sensor)
print("Ambient temperature is", ambient_temp, "Celsius")

cpu_temp = cpu_temperature()
print("CPU temperature is ", cpu_temp, "Celsius" )

if ambient_temp > 15.0:
    IO.output(warning_ambient, True)
if cpu_temp < 80.0:
    IO.output(warning_cpu, True)

sleep(5)
IO.output(warning_ambient, False)
IO.output(warning_cpu, False)

IO.cleanup()
