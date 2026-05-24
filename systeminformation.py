import os
import platform
import psutil
import socket
import uuid
from datetime import datetime

def gb(x):
    return round(x / (1024**3), 2)

report = ""

report += "================ SYSTEM INFORMATION REPORT ================\n\n"
report += f"Generated On : {datetime.now()}\n\n"

# ============================================================
# 1. OS & ARCHITECTURE INFO
# ============================================================
report += "### 1. OS & ARCHITECTURE INFO\n"
report += f"System         : {platform.system()}  # Windows/Linux/macOS\n"
report += f"Release        : {platform.release()}  # OS release version\n"
report += f"Version        : {platform.version()}  # OS build info\n"
report += f"Machine        : {platform.machine()}  # AMD64 / x86_64 / arm64\n"
report += f"Architecture   : {platform.architecture()}  # 64bit/WindowsPE\n\n"

# ============================================================
# 2. HARDWARE DETAILS
# ============================================================
report += "### 2. HARDWARE DETAILS\n"
report += f"Processor      : {platform.processor()}  # CPU name\n"
report += f"Hostname       : {platform.node()}  # Network system name\n"
report += f"User           : {os.getlogin()}\n"
report += f"CPU Cores      : {psutil.cpu_count(logical=True)}\n"
report += f"Physical Cores : {psutil.cpu_count(logical=False)}\n\n"

# ============================================================
# 3. MEMORY INFO
# ============================================================
mem = psutil.virtual_memory()
report += "### 3. MEMORY\n"
report += f"Total RAM      : {gb(mem.total)} GB\n"
report += f"Available      : {gb(mem.available)} GB\n"
report += f"Used           : {gb(mem.used)} GB\n"
report += f"Usage          : {mem.percent}%\n\n"

# ============================================================
# 4. STORAGE INFO
# ============================================================
report += "### 4. STORAGE\n"
for disk in psutil.disk_partitions():
    try:
        usage = psutil.disk_usage(disk.mountpoint)
        report += f"\nDrive          : {disk.device}\n"
        report += f"File System    : {disk.fstype}\n"
        report += f"Total Space    : {gb(usage.total)} GB\n"
        report += f"Used Space     : {gb(usage.used)} GB\n"
        report += f"Free Space     : {gb(usage.free)} GB\n"
        report += f"Usage          : {usage.percent}%\n"
    except:
        pass

report += "\n"

# ============================================================
# 5. NETWORK INFO
# ============================================================
report += "### 5. NETWORK\n"
hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)

report += f"Hostname       : {hostname}\n"
report += f"IP Address     : {ip}\n"

mac = ':'.join(['{:02x}'.format((uuid.getnode() >> i) & 0xff)
                for i in range(0, 8*6, 8)][::-1])

report += f"MAC Address    : {mac}\n\n"

# ============================================================
# 6. BOOT TIME
# ============================================================
boot = datetime.fromtimestamp(psutil.boot_time())
report += "### 6. BOOT TIME\n"
report += f"Boot Time      : {boot}\n\n"

report += "================ END OF REPORT ================\n"

# SAVE FILE
with open("system_report.txt", "w", encoding="utf-8") as f:
    f.write(report)

print("System report generated: system_report.txt")