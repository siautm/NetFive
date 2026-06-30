# Use an official Python base image 
FROM python:3.10-slim

# Prevent Python from writing .pyc files and enable unbuffered logging
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install system dependencies (including ssh/ping utilities for network testing)
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    libffi-dev \
    libssl-dev \
    openssh-client \
    iputils-ping \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Install all Python packages required for the team (Members A, B, and C)
RUN pip install --no-cache-dir \
    ncclient \
    paramiko \
    psutil \
    tabulate \
    ansible \
    xmltodict

# Install Ansible Cisco networking collections (Member B)
RUN ansible-galaxy collection install cisco.ios ansible.netcommon

# Set up the working directory inside the container
WORKDIR /app

# Command to keep container running for development/execution
CMD ["tail", "-f", "/dev/null"]