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
    except Exception as shell:
        shell = ""
        pass
    try:
        proc = cpuinfo.get_cpu_info()
        CPU = proc["brand_raw"]
    except Exception as CPU:
        CPU = ""
        pass
    try:
        proc = cpuinfo.get_cpu_info()
        Bit = proc["arch_string_raw"]
    except Exception as Bit:
        Bit = ""
        pass
    try:
        ram = str(round(psutil.virtual_memory().total / (1024.0 **3)))+" GB"
    except Exception as ram:
        ram = ""
        pass
    try:
        User = os.environ['USER']
    except Exception as User:
        pass
        User = ""
    try:
        distr = distro.linux_distribution()[0]
    except Exception as distr:
        distr = ""
        pass
    try:
        if os.environ['XDG_CURRENT_DESKTOP'] and os.environ['DESKTOP_SESSION']:
            GUI = os.environ['XDG_CURRENT_DESKTOP'] +  ", " + os.environ['DESKTOP_SESSION']
    except Exception as GUI:
        GUI = ""
        pass
    try:
        term = os.environ["TERM"]
    except Exception as term:
        term = ""
        pass
