import subprocess as sb
from tkinter import *
import shlex
import os
from threading import Thread
from time import sleep
def get_temps():
    sensors_op=sb.check_output("sensors").decode("utf-8").split("\n")
    temps=[]
    device_index=0
    devices=["CPU","GPU","fan"]
    label_names=["CPU Temp: ","GPU Temp: ","Fan Speed: "]
    ct=0
    for device in range(len(devices)):
        for sensors in sensors_op:
            if devices[device_index] in sensors:
                elements=label_names[device_index]+sensors.split(":")[-1].strip()
                temps.append(elements)
        device_index+=1
    return temps
def fan_speed(level=None):
    print(f"Set level to {level}")
    set_speed=sb.check_output(f"echo level {level} | sudo tee '/proc/acpi/ibm/fan'",shell=True) 
    return set_speed.decode()

def display_loop():
    while True:
        sleep(0.5)
        display_label["text"]=" // ".join(get_temps())
Thread(target=display_loop).start()
root=Tk()
root.geometry("405x90")
display_label=Label(root,text="")
display_label.place(x=0,y=0)
root.title("ThinkPad Fan Controller")
icon=PhotoImage(file="./Images/fan-icon-vector-15.png")
root.iconphoto(False,icon)
cmd_one='sudo dmidecode'
dmidecode_info=sb.Popen(shlex.split(cmd_one),stdout=sb.PIPE)
out, err=dmidecode_info.communicate()

for version in out.decode().split("\n"):
    if "Version: T" in version:
        laptop_version="Model: "+version.split(": ")[-1]
label_model=Label(root,text=laptop_version,fg="red",font=(25)).place(x=10,y=58)
for i in range(8):
    Button(root,text=f"L{i}",command=lambda x=i :fan_speed(x)).place(x=5+(i*50),y=20)
Button(root,text=f"Auto",command=lambda :fan_speed("auto")).place(x=343,y=55)
Button(root,text=f"Full-Speed",command=lambda :fan_speed("full-speed")).place(x=245,y=55)
root.mainloop()
