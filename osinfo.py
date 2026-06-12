# osinfo.py – system information gathering with optional dependencies

import os
import platform
import subprocess
from importlib.util import find_spec
from datetime import datetime, timedelta

class SystemInfo:
    def __init__(self):
        self.shell = self._get_shell()
        self.cpu = self._get_cpu()
        self.bit = self._get_bit()
        self.ram = self._get_ram()
        self.user = self._get_user()
        self.distro = self._get_distro()
        self.kernel = platform.release()
        self.uptime = self._get_uptime()
        self.disk = self._get_disk()
        self.packages = self._get_packages()
        self.gui = self._get_gui()
        self.term = self._get_term()
        self.gpu = self._get_gpu()
        self.resolution = self._get_resolution()

    def _get_shell(self):
        return os.path.basename(os.environ.get('SHELL', os.environ.get('COMSPEC', 'Unknown')))

    def _get_cpu(self):
        if find_spec("cpuinfo"):
            import cpuinfo
            return cpuinfo.get_cpu_info().get('brand_raw', platform.processor() or 'Unknown')
        return platform.processor() or 'Unknown'

    def _get_bit(self):
        return platform.machine() or 'Unknown'

    def _get_ram(self):
        if find_spec("psutil"):
            import psutil
            return f"{round(psutil.virtual_memory().total / (1024.0 ** 3))} GB"
        try:
            with open('/proc/meminfo', 'r') as f:
                for line in f:
                    if line.startswith('MemTotal:'):
                        mem_kb = int(line.split()[1])
                        return f"{round(mem_kb / (1024 ** 2))} GB"
        except:
            pass
        return 'Unknown'

    def _get_user(self):
        return os.environ.get('USER', os.environ.get('USERNAME', 'Unknown'))

    def _get_distro(self):
        if find_spec("distro"):
            import distro
            return distro.name()
        system = platform.system()
        if system == 'Linux':
            try:
                with open('/etc/os-release', 'r') as f:
                    for line in f:
                        if line.startswith('PRETTY_NAME='):
                            return line.split('=')[1].strip().strip('"')
            except:
                pass
            return 'Linux'
        elif system == 'Darwin':
            return 'macOS'
        elif system == 'Windows':
            return 'Windows'
        return system

    def _get_uptime(self):
        if find_spec("psutil"):
            import psutil
            uptime_seconds = int(datetime.now().timestamp() - psutil.boot_time())
            return str(timedelta(seconds=uptime_seconds)).split('.')[0]
        if platform.system() == 'Linux':
            try:
                with open('/proc/uptime', 'r') as f:
                    uptime_seconds = float(f.read().split()[0])
                    return str(timedelta(seconds=int(uptime_seconds))).split('.')[0]
            except:
                pass
        return 'Unknown'

    def _get_disk(self):
        if find_spec("psutil"):
            import psutil
            disk = psutil.disk_usage('/')
            return f"{disk.used // (2**30)} GB / {disk.total // (2**30)} GB ({disk.percent}%)"
        if platform.system() == 'Linux':
            try:
                df = subprocess.check_output(['df', '-h', '/'], text=True).splitlines()[1]
                parts = df.split()
                return f"{parts[2]} / {parts[1]} ({parts[4]})"
            except:
                pass
        return 'Unknown'

    def _get_packages(self):
        if platform.system() != 'Linux':
            return 'Unknown'
        try:
            if os.path.exists('/usr/bin/dpkg'):
                count = subprocess.check_output(['dpkg', '-l'], text=True).count('\n') - 5
                return f"{count} (dpkg)"
            elif os.path.exists('/usr/bin/rpm'):
                count = subprocess.check_output(['rpm', '-qa'], text=True).count('\n')
                return f"{count} (rpm)"
            elif os.path.exists('/usr/bin/pacman'):
                count = subprocess.check_output(['pacman', '-Q'], text=True).count('\n')
                return f"{count} (pacman)"
        except:
            pass
        return 'Unknown'

    def _get_gui(self):
        gui_parts = []
        if os.environ.get('XDG_CURRENT_DESKTOP'):
            gui_parts.append(os.environ['XDG_CURRENT_DESKTOP'])
        if os.environ.get('DESKTOP_SESSION'):
            gui_parts.append(os.environ['DESKTOP_SESSION'])
        return ', '.join(gui_parts) if gui_parts else 'Unknown'

    def _get_term(self):
        term = os.environ.get('TERM', 'Unknown')
        if term == 'Unknown' and platform.system() == 'Windows':
            term = os.environ.get('COMSPEC', 'cmd.exe')
        return term

    def _get_gpu(self):
        system = platform.system()
        if system == 'Linux':
            try:
                lspci = subprocess.check_output(['lspci'], text=True)
                for line in lspci.splitlines():
                    if 'VGA' in line or '3D' in line:
                        return line.split(':')[-1].strip()
            except:
                pass
        elif system == 'Windows':
            try:
                import wmi
                c = wmi.WMI()
                for gpu in c.Win32_VideoController():
                    return gpu.Name
            except ImportError:
                pass
        elif system == 'Darwin':
            try:
                output = subprocess.check_output(['system_profiler', 'SPDisplaysDataType'], text=True)
                for line in output.splitlines():
                    if 'Chipset Model' in line:
                        return line.split(':')[-1].strip()
            except:
                pass
        return 'Unknown'

    def _get_resolution(self):
        if platform.system() == 'Linux' and os.environ.get('DISPLAY'):
            try:
                xrandr = subprocess.check_output(['xrandr'], text=True)
                for line in xrandr.splitlines():
                    if '*' in line and ' connected' not in line:
                        res = line.split()[0]
                        if 'x' in res:
                            return res
            except:
                pass
        return 'Unknown'
