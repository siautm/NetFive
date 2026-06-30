# System Info Script Testing Report

---

# 1. Overview

The System Info Script is designed to collect real-time system information from a machine using Python automation.

The script provides the following system metrics:

- Hostname
- Date and Time
- CPU information (cores + usage)
- Memory usage
- Disk usage
- Logged-in users
- Top 5 processes by CPU usage

The purpose of this module is to demonstrate system monitoring automation using Python libraries such as `psutil`.

---

# 2. Current Implementation

As of the latest update, the script has been fully implemented in `system_info.py`.

As of 30 June 2026, final validation was performed on labvm (Linux) and inside the project Docker `automation-runner` container.

### Description

### File: `system_info.py`

- System information collection using `psutil`
- Cross-platform basic support (Linux)
- Tabulated output display using `tabulate`
- File logging with timestamped reports

### Sample Output Structure:

- Hostname
- Date & Time
- CPU usage (cores, frequency, %)
- Memory usage (GB / %)
- Disk usage (GB / %)
- Logged-in users
- Top 5 processes by CPU usage

### Test Environment

| Item | Value |
|------|-------|
| Platform | labvm (Linux) |
| Docker | `automation-runner` container |
| Dependencies | `psutil`, `tabulate` |

---

# 3. Requirement Mapping

| Requirement | Description | Status |
|-------------|-------------|--------|
| Hostname | Display system hostname | PASS |
| Date/Time | Display current system time | PASS |
| CPU Usage | Display CPU usage percentage | PASS |
| Memory Usage | Display RAM usage | PASS |
| Disk Usage | Display disk usage | PASS |
| Logged-in Users | Display active users | PASS |
| Top 5 Processes | Display top CPU processes | PASS |

---

# 4. Test Cases

| Test ID | Test Description | Expected Result | Status |
|---------|------------------|----------------|--------|
| TC-SYS-001 | Run system info script on labvm | Script executes successfully | PASS |
| TC-SYS-002 | Run system info script in Docker | Script executes successfully | PASS |
| TC-SYS-003 | Validate hostname output | Correct hostname displayed | PASS |
| TC-SYS-004 | Validate CPU usage output | CPU usage displayed | PASS |
| TC-SYS-005 | Validate memory usage output | Memory usage displayed correctly | PASS |
| TC-SYS-006 | Validate disk usage output | Disk usage displayed correctly | PASS |
| TC-SYS-007 | Check logged-in users | Users displayed or 0 users | PASS |
| TC-SYS-008 | Check top processes list | Top 5 processes displayed | PASS |

### Sample Output (Docker Container)

```
Hostname             : labvm
Date & Time          : 2026-06-30 06:15:45
CPU                  : 8 cores, 2918 MHz, 4.7% usage
Memory               : 2.19 GB / 3.84 GB (57.0%)
Disk Usage           : 13.03 GB / 30.14 GB (45.6%)
Logged-in Users      : 0 users
Top 5 Processes      : (displayed)
```

---

# 5. Pending Items

- Merge `feature/system-script` into `main` after final team review.
- Optional: add JSON export format for integration with other modules.

---

# 6. Tester Remarks

The System Info Script is functioning correctly and meets all basic project requirements. The script successfully collects all seven required system metrics and presents them in both terminal and file output formats.

Testing was completed on labvm and inside the Docker container environment. The module is considered **PASS and ready for merge**.
