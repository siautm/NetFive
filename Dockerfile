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

# Install Python packages required for NETCONF (Member A) and system utilities
RUN pip install --no-cache-dir \
    ncclient \
    paramiko \
    psutil

# Install Ansible (Member B)
RUN pip install --no-cache-dir ansible

# Set up the working directory inside the container
WORKDIR /app

# (Optional placeholder) Command to keep container running for development
CMD ["tail", "-f", "/dev/null"]