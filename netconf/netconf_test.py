import time

print("=== NETCONF AUTOMATION CONNECTIVITY TEST ===")
print("Connecting to network device target via SSH port 830...")
time.sleep(1)

# Simulating fetching capabilities
print("Status: Connected successfully!")
print("Device Capabilities Retrieved:")
print(" - urn:ietf:params:netconf:base:1.0")
print(" - urn:ietf:params:netconf:capability:xpath:1.0")
print(" - urn:ietf:params:netconf:capability:writable-running:1.0")
print("\n[SUCCESS] Mock device configuration retrieved successfully!")
print("============================================")