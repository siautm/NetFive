# System Info Script Testing Report

---

# 1. Overview

The System Info Script is designed to collect real-time system information from a machine using Python automation.

The script provides the following system metrics:

- Hostname
- Date and Time
- CPU usage
- Memory usage
- Disk usage
- Logged-in users
- Top 5 processes by CPU usage

The purpose of this module is to demonstrate system monitoring automation using Python libraries such as `psutil`.

---

# 2. Current Implementation

As of the latest update, the script has been fully implemented and includes the following features:

### File: system_info.py

- System information collection using `psutil`
- Cross-platform basic support (Windows / Linux)
- Tabulated output display using `tabulate`
- File logging with timestamped reports

### Sample Output Structure:

- Hostname
- Date & Time
- CPU usage (%)
- Memory usage (GB / %)
- Disk usage (GB / %)
- Logged-in users
- Top 5 processes by CPU usage

---

# 3. Requirement Mapping

| Requirement | Description | Status |
|-------------|-------------|--------|
| Hostname | Display system hostname | PASS |
| Date/Time | Display current system time | PASS |
| CPU Usage | Display CPU usage percentage | PASS |
| Memory Usage | Display RAM usage | PASS |
| Disk Usage | Display disk usage | PASS |
| Logged-in Users | Display active users | PASS (OS dependent) |
| Top 5 Processes | Display top CPU processes | PASS |

---

# 4. Test Cases

| Test ID | Test Description | Expected Result | Status |
|---------|------------------|----------------|--------|
| TC-SYS-001 | Run system info script | Script executes successfully | PASS |
| TC-SYS-002 | Validate hostname output | Correct hostname displayed | PASS |
| TC-SYS-003 | Validate CPU usage output | CPU usage displayed | PASS |
| TC-SYS-004 | Validate memory usage output | Memory usage displayed correctly | PASS |
| TC-SYS-005 | Validate disk usage output | Disk usage displayed correctly | PASS |
| TC-SYS-006 | Check logged-in users | Users displayed or 0 users | PASS |
| TC-SYS-007 | Check top processes list | Top 5 processes displayed | PASS |

---


# 6. Pending Items

The following improvements are recommended for future development:

- Improve cross-platform compatibility for logged-in users detection
- Optimize CPU process sampling accuracy
- Add real-time monitoring mode (optional enhancement)
- Export results in JSON format for integration

---

# 7. Tester Remarks

The System Info Script is functioning correctly and meets all basic project requirements.

The script successfully collects system metrics and presents them in both terminal and file output formats.

Minor OS-level limitations exist, but they do not affect the overall functionality of the script.

Overall, the module is considered **PASS and ready for submission**.
