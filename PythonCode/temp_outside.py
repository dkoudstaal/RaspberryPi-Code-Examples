import os, fnmatch
from time import sleep

def find_dir(pattern, path):
    for root, dirs, files in os.walk(path):
        for name in dirs:
            if fnmatch.fnmatch(name, pattern):
                dir_name = os.path.join(root, name)
                return dir_name

#temp_sensor = "/sys/bus/w1/devices/28-0316201df4ff/w1_slave"

temp_sensor = find_dir("28-*", "/sys/bus/w1/devices/")+"/w1_slave"
temp_file = open(temp_sensor, "r")
temp_text = temp_file.read()
temp_file.close()
print(temp_text)

second_line = temp_text.split("\n")[1]
print(second_line)
print()

temp_data = second_line.split("=")[1]
print(temp_data)
print()

temperature = float(temp_data) / 1000
print("Ambient temperature is ", round(temperature, 1))
print()

temp_cpu_bash = "vcgencmd measure_temp"
temp_cpu = os.popen(temp_cpu_bash, "r")
temp_text_cpu = temp_cpu.read()
temp_cpu.close()

print(temp_text_cpu)

temp_cpu_data = temp_text_cpu[5 : 9]
print("CPU temperature is ", float(temp_cpu_data))

print()
print(find_dir("28-*", "/sys/bus/w1/devices/")+"/w1_slave")
