import platform
import os
import subprocess
import psutil
import socket
import speedtest
from win32api import GetSystemMetrics
import wmi

def get_installed_software():
    installed_software = []
    process = subprocess.Popen(['wmic', 'product', 'get', 'name'], stdout=subprocess.PIPE, universal_newlines=True)
    output, _ = process.communicate()
    installed_software = [line.strip() for line in output.split('\n') if line.strip()]
    return installed_software

def get_internet_speed():
    st = speedtest.Speedtest()
    download_speed = st.download() / 1_000_000  # in Mbps
    upload_speed = st.upload() / 1_000_000  # in Mbps
    return download_speed, upload_speed

def get_screen_resolution():
    return GetSystemMetrics(0), GetSystemMetrics(1)

def get_cpu_info():
    cpu_info = platform.processor()
    cpu_count = psutil.cpu_count(logical=False)
    thread_count = psutil.cpu_count(logical=True)
    return cpu_info, cpu_count, thread_count

def get_gpu_info():
    try:
        w = wmi.WMI()
        gpu_info = w.Win32_VideoController()[0].Caption
        return gpu_info
    except Exception as e:
        return None

def get_ram_size():
    ram_info = psutil.virtual_memory()
    ram_size_gb = round(ram_info.total / (1024 ** 3), 2)
    return ram_size_gb

def get_screen_size():
    screen_size = input("Enter your screen size (e.g., 15 inch, 21 inch): ")
    return screen_size

def get_mac_address(interface='Wi-Fi'):
    try:
        mac_address = ':'.join(['{:02x}'.format((uuid.getnode() >> elements) & 0xff) for elements in range(5, -1, -1)])
        return mac_address
    except Exception as e:
        return None

def get_public_ip():
    try:
        public_ip = socket.gethostbyname(socket.gethostname())
        return public_ip
    except Exception as e:
        return None

def get_windows_version():
    return platform.system() + ' ' + platform.version()

if __name__ == "__main__":
    installed_software = get_installed_software()
    download_speed, upload_speed = get_internet_speed()
    screen_resolution = get_screen_resolution()
    cpu_info, cpu_count, thread_count = get_cpu_info()
    gpu_info = get_gpu_info()
    ram_size_gb = get_ram_size()
    screen_size = get_screen_size()
    mac_address = get_mac_address()
    public_ip = get_public_ip()
    windows_version = get_windows_version()

    print("Installed Software: ", installed_software)
    print("Internet Speed (Download/Upload): {:.2f} Mbps / {:.2f} Mbps".format(download_speed, upload_speed))
    print("Screen Resolution: {} x {}".format(screen_resolution[0], screen_resolution[1]))
    print("CPU Model: ", cpu_info)
    print("Number of Cores: ", cpu_count)
    print("Number of Threads: ", thread_count)
    print("GPU Model: ", gpu_info)
    print("RAM Size: {:.2f} GB".format(ram_size_gb))
    print("Screen Size: ", screen_size)
    print("Mac Address: ", mac_address)
    print("Public IP Address: ", public_ip)
    print("Windows Version: ", windows_version)
