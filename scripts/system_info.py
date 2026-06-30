import psutil
import platform
from datetime import datetime

print("=== CONTAINER SYSTEM INFO TEST ===")
print(f"Hostname: {platform.node()}")
print(f"Current Time: {datetime.now()}")
print(f"CPU Count: {psutil.cpu_count()} cores")
print("==================================")