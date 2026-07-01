# Ansible Module Testing Report

---

# 1. Overview

The Ansible Automation module is designed to automate the configuration of Cisco network devices using Ansible.

The main objective of this module is to implement network automation tasks including:

- Creating Ansible playbooks
- Configuring user accounts on network devices
- Configuring banner messages
- Configuring interface descriptions

This module aims to improve efficiency and reduce manual configuration errors in network management.

---

# 2. Current Implementation

As of 19 June 2026, the current implementation only includes the Ansible inventory configuration file.

As of 26 June 2026, the Ansible Automation module has been fully implemented.

As of 30 June 2026, final validation was performed against a Cisco CSR1000v router (IOS-XE) deployed in GNS3, accessed from the labvm Linux environment.

### Description

The inventory file defines:

- Target device group (`routers`)
- Target device IP address
- Ansible connection type
- Network operating system type (Cisco IOS)
- Login credentials (username and password)

The implementation includes the following files:

- `inventory.ini` — defines the target device group, hostname, connection type, OS type, and credentials
- `playbook.yml` — main playbook that imports all configuration task files
- `user_config.yml` — automates user account creation using `cisco.ios.ios_user`
- `banner_config.yml` — automates login banner configuration using `cisco.ios.ios_banner`
- `interface_config.yml` — automates interface description configuration using `cisco.ios.ios_interfaces`

### Test Environment

| Item | Value |
|------|-------|
| Target Device | Cisco CSR1000v (GNS3) |
| Device IP | 192.168.56.102 |
| Interface | GigabitEthernet1 |
| Test Host | labvm (Linux) |
| Collection | `cisco.ios` |

---

# 3. Requirement Mapping

| Requirement | Description | Status |
| ------------------------------- | ---------------------------------------------------------- | ---------- |
| Create Ansible Playbook | Develop automation playbook for Cisco device configuration | ✅ Done |
| Configure User Account | Automate user account creation on router | ✅ Done |
| Configure Banner Message | Automate banner configuration | ✅ Done |
| Configure Interface Description | Automate interface description configuration | ✅ Done |

---

# 4. Test Cases

| Test ID | Test Description | Expected Result | Status |
| ---------- | ---------------------------- | --------------------------------------- | ---------- |
| TC-ANS-001 | Verify inventory file exists | Inventory file is present in repository | PASS |
| TC-ANS-002 | Validate inventory syntax | Inventory loads correctly in Ansible | PASS |
| TC-ANS-003 | Check playbook availability | Playbook files exist in repository | PASS |
| TC-ANS-004 | User account automation test | User is created on device | PASS |
| TC-ANS-005 | Banner configuration test | Banner message is applied | PASS |
| TC-ANS-006 | Interface description test | Interface description is configured | PASS |

### Test Command

```bash
ansible-galaxy collection install cisco.ios
ansible-playbook -i ansible/inventory.ini ansible/playbook.yml
```

### Verification (on Router)

```cisco
show run | include username
show run | include banner
show interfaces description
```

---

# 5. Pending Items

- Merge `feature/ansible` into `main` after final team review.
- Align `inventory.ini` device IP with the deployed lab router before submission.
- Optional: run playbook from inside the Docker `automation-runner` container for full integration demo.

---

# 6. Tester Remarks

The Ansible automation module has been successfully validated on a Cisco CSR1000v router in the GNS3 lab environment. All three configuration tasks — user account creation, login banner, and interface description — executed successfully via `ansible-playbook`.

The playbook structure is clear, modular, and meets all assignment requirements for Ansible-based network device automation. The module is considered **PASS and ready for merge**.
