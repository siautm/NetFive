
import os
import platform
import psutil
import datetime
from tabulate import tabulate

def get_system_info():
    """Collect all required Linux system information"""

    info = []
    
    # 1. Hostname
    info.append(["Hostname", platform.node()])
    
    # 2. Date & Time
    info.append(["Date & Time", datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")])
    
    # 3. CPU Information
    cpu_count = psutil.cpu_count()
    cpu_freq = psutil.cpu_freq()
    cpu_percent = psutil.cpu_percent(interval=1)  
    cpu_info = f"{cpu_count} cores, {cpu_freq.current:.0f} MHz, {cpu_percent}% usage"
    info.append(["CPU", f"{cpu_count} cores, {cpu_freq.current:.0f} MHz, {cpu_percent}% usage"])
    
    # 4. Memory Usage
    mem = psutil.virtual_memory()
    mem_info = f"{mem.used / (1024**3):.2f} GB / {mem.total / (1024**3):.2f} GB ({mem.percent}%)"
    info.append(["Memory", mem_info])
    
    # 5. Disk Usage
    disk = psutil.disk_usage('/')
    disk_info = f"{disk.used / (1024**3):.2f} GB / {disk.total / (1024**3):.2f} GB ({disk.percent}%)"
    info.append(["Disk Usage", disk_info])
    
    # 6. Logged-in Users - FIXED to handle empty output
    users_output = os.popen('who').read().strip()
    if users_output:
        users = users_output.split('\n')
        user_count = len(users)
        user_names = ", ".join([u.split()[0] for u in users])
        info.append(["Logged-in Users", f"{user_count} users ({user_names})"])
    else:
        info.append(["Logged-in Users", "0 users"])
    
    # 7. Top 5 Processes by CPU
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


def display_info(info):
    """Display system information in a formatted table"""
    print("\n" + "="*65)
    print("          LINUX SYSTEM INFORMATION REPORT")
    print("="*65)
    print(tabulate(info, headers=["METRIC", "VALUE"], tablefmt="grid"))
    print("="*65 + "\n")

def save_to_file(info):
    """Save system information to a log file with timestamp"""
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"system_info_{timestamp}.txt"
    
    try:
        with open(filename, 'w') as f:
            f.write("="*65 + "\n")
            f.write("          LINUX SYSTEM INFORMATION REPORT\n")
            f.write("="*65 + "\n")
            for metric, value in info:
                f.write(f"{metric:20} : {value}\n")
            f.write("="*65 + "\n")
        print(f"✅ Report saved to: {filename}")
        return filename
    except Exception as e:
        print(f"❌ Could not save report: {e}")
        return None

def main():
    """Main function with error handling"""
    try:
        print("📊 Collecting system information...")
        info = get_system_info()
        display_info(info)
        save_to_file(info)
        print("✅ Script completed successfully!")
    except Exception as e:
        print(f"❌ Error collecting system information: {e}")
        print("💡 Make sure you have psutil installed: pip install psutil tabulate")   

if __name__ == "__main__":
    main()