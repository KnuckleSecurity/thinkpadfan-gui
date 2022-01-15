#!/usr/bin/python
import subprocess as sb
import shlex
import os
def get_temps():
    sensors_op=sb.check_output("sensors").decode("utf-8").split("\n")
    temps=[]
    device_index=0
    devices=["CPU","fan"]
    label_names=["CPU Temp: ","Fan Speed: "]
    ct=0
    for device in range(len(devices)):
        for sensors in sensors_op:
            if devices[device_index] in sensors:
                elements=label_names[device_index]+sensors.split(":")[-1].strip()
                temps.append(elements)
        device_index+=1
    return temps

def fan_speed(level=None):
    if (level == "e"):
        print("Exiting...")
        os._exit(0)
    try:
        print(f"Set level to {level}")
        set_speed=sb.check_output(f"echo level {level} | sudo tee '/proc/acpi/ibm/fan' 2>/dev/null",shell=True) 
        return set_speed.decode()
    except:
        print("Something went wrong, exiting...")
        os._exit(-1);

print(f"{get_temps()[0]} {get_temps()[1]}")
print("Choose level -> 1, 2, 3, 4 ,5, 6, 7, full-Speed, auto")
print("'e' to exit.")
a=input("> ")
fan_speed(a)
