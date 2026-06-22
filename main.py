from ncclient import manager


device_config = {
    "host": "192.168.1.1",
    "port": 830,
    "username": "admin",
    "password": "password",
    "hostkey_verify": False
}

def get_device_info():
    """Retrieves device configuration using NETCONF."""
    try:
        with manager.connect(**device_config) as m:

            netconf_filter = """
            <filter>
                <system xmlns="urn:ietf:params:xml:ns:yang:ietf-system">
                </system>
            </filter>
            """
            response = m.get_config(source='running', filter=netconf_filter)
            print("Device Configuration retrieved successfully:")
            print(response.xml)
            
    except Exception as e:
        print(f"Error connecting to device: {e}")

if __name__ == "__main__":
    get_device_info()