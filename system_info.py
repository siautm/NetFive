
import os
import platform
import psutil
import datetime
from tabulate import tabulate

def get_system_info():
    info = []
    
    # 1. Hostname
    info.append(["Hostname", platform.node()])
    
    # 2. Date & Time
    info.append(["Date & Time", datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")])
    
    # 3. CPU Information
    cpu_count = psutil.cpu_count()
    cpu_percent = psutil.cpu_percent(interval=1)  # interval=1 gives accurate reading
    info.append(["CPU", f"{cpu_count} cores, {cpu_percent}% usage"])
    
    # 4. Memory Usage
    mem = psutil.virtual_memory()
    info.append(["Memory", f"{mem.used / 1e9:.2f} GB / {mem.total / 1e9:.2f} GB ({mem.percent}%)"])
    
    # 5. Disk Usage
    disk = psutil.disk_usage('/')
    info.append(["Disk", f"{disk.used / 1e9:.2f} GB / {disk.total / 1e9:.2f} GB ({disk.percent}%)"])
    
    # 6. Logged-in Users - FIXED to handle empty output
    users_output = os.popen('who').read().strip()
    if users_output:
        users = users_output.split('\n')
        user_count = len(users)
        user_names = ", ".join([u.split()[0] for u in users])
        info.append(["Logged-in Users", f"{user_count} users ({user_names})"])
    else:
        info.append(["Logged-in Users", "0 users"])
    
    # 7. Top 5 Processes by CPU - FIXED error handling
    processes = []
    for proc in psutil.process_iter(['name', 'cpu_percent']):
        try:
            p = proc.info
            if p['name'] and p['cpu_percent'] is not None:
                processes.append((p['name'], p['cpu_percent']))
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass
    
    processes.sort(key=lambda x: x[1], reverse=True)
    top_5 = processes[:5]
    proc_text = "\n".join([f"{i+1}. {name}: {cpu:.1f}%" for i, (name, cpu) in enumerate(top_5)])
    info.append(["Top 5 Processes", proc_text])
    
    return info

if __name__ == "__main__":
    info = get_system_info()
    print("\n" + "="*55)
    print("     LINUX SYSTEM INFORMATION REPORT")
    print("="*55)
    print(tabulate(info, headers=["METRIC", "VALUE"], tablefmt="grid"))
    print("="*55)
    