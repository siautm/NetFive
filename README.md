# NetFive
# Network Automation Project

## Overview

This project is developed for the SECR3253 Network Programming Group Assignment. The objective is to build a simple network automation solution using Docker, Ansible, and NETCONF technologies. The project also includes Linux system information collection and reporting.

The automation solution is designed to perform common network configuration tasks and retrieve system information automatically, reducing the need for manual configuration.

---

## Project Objectives

### Network Device Automation

The project will automate the following tasks:

* Configure IP address
* Configure static route
* Create user account
* Configure banner message
* Configure interface description
* Retrieve device information

### Linux System Information Collection

The project will automatically collect and display:

* Hostname
* Current date and time
* CPU information
* Memory usage
* Disk usage
* Logged-in users
* Top 5 running processes by CPU usage

---

## Proposed Architecture

Docker Container
│
├── Ansible Module
│   ├── User Account Configuration
│   ├── Banner Configuration
│   └── Interface Description Configuration
│
├── NETCONF Module
│   ├── IP Address Configuration
│   ├── Static Route Configuration
│   └── Device Information Retrieval
│
└── Linux Monitoring Module
└── System Information Collection

---

## Team Responsibilities

### Member A(Aaron Tan Yoong Thzen) – NETCONF Configuration

Responsibilities:

* Configure IP address
* Configure static route
* Retrieve device information
* Develop NETCONF automation scripts

### Member B(Leo Min Xue) – Ansible Automation

Responsibilities:

* Configure user account
* Configure banner message
* Configure interface description
* Develop Ansible playbooks

### Member C(Melody Lui Ruo Ning) – Linux Monitoring

Responsibilities:

* Collect Linux system information
* Display system status
* Develop monitoring scripts

### Member D(Yeo Wern Min) – Docker Integration

Responsibilities:

* Create Docker environment
* Configure Docker Compose
* Integrate all project modules
* Manage project deployment environment

### Member E(Sia Jun Yi) – Testing & Documentation

Responsibilities:

* Prepare project documentation
* Maintain README and project records
* Perform testing and validation
* Record results and screenshots

---

## Repository Structure

project/

├── ansible/

├── netconf/

├── docs/

├── docker/

├── system-script/

└── README.md

---

## Project Status

Current Phase:

* Project planning and task allocation

Next Steps:

* Set up development environment
* Develop individual modules
* Perform integration testing
* Complete final documentation
