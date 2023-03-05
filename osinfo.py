import cpuinfo
import platform
import psutil
import os
import distro
from colorama import Fore

class Variables():
    shell = os.path.basename(os.environ.get('SHELL', 'Unknown'))
    proc = cpuinfo.get_cpu_info()
    CPU = proc.get('brand_raw', 'Unknown')
    Bit = proc.get('arch_string_raw', 'Unknown')
    ram = f"{round(psutil.virtual_memory().total / (1024.0 ** 3))} GB"
    User = os.environ.get('USER', 'Unknown')
    distr = distro.linux_distribution()[0]
    GUI = f"{os.environ.get('XDG_CURRENT_DESKTOP', 'Unknown')}, {os.environ.get('DESKTOP_SESSION', 'Unknown')}"
    term = os.environ.get('TERM', 'Unknown')
