import cpuinfo
from colorama import Fore
import platform
import psutil
import os
import distro
#info about system
class Variables():
    try:
        shell = os.environ['SHELL'].replace("/usr/bin/", "")
    except:
        shell = "Unknown"
        pass
    try:
        proc = cpuinfo.get_cpu_info()
        CPU = proc["brand_raw"]
    except:
        CPU = "Unknown"
        pass
    try:
        proc = cpuinfo.get_cpu_info()
        Bit = proc["arch_string_raw"]
    except:
        Bit = "Unknown"
        pass
    try:
        ram = str(round(psutil.virtual_memory().total / (1024.0 **3)))+" GB"
    except:
        ram = "Unknown"
        pass
    try:
        User = os.environ['USER']
    except:
        pass
        User = "Unknown"
    try:
        distr = distro.linux_distribution()[0]
    except:
        distr = "Unknown"
        pass
    try:
        if os.environ['XDG_CURRENT_DESKTOP'] and os.environ['DESKTOP_SESSION']:
            GUI = os.environ['XDG_CURRENT_DESKTOP'] +  ", " + os.environ['DESKTOP_SESSION']
    except:
        GUI = "Unknown"
        pass
    try:
        term = os.environ["TERM"]
    except:
        term = "Unknown"
        pass
