import argparse
import sys
import xml.dom.minidom
from ncclient import manager
import xmltodict

# Default connection details
DEFAULT_HOST = "192.168.1.1"
DEFAULT_PORT = 830
DEFAULT_USER = "admin"
DEFAULT_PASS = "password"

def get_manager(host, port, username, password):
    """Establishes a connection to the NETCONF server."""
    print(f"Connecting to NETCONF device at {host}:{port} as user '{username}'...")
    return manager.connect(
        host=host,
        port=port,
        username=username,
        password=password,
        hostkey_verify=False
    )

def ip_to_cidr(ip_address, netmask):
    """Converts IP and Netmask to CIDR notation (e.g., 192.168.1.0/24)."""
    try:
        cidr = sum(bin(int(x)).count('1') for x in netmask.split('.'))
        return f"{ip_address}/{cidr}"
    except Exception:
        # Fallback if conversion fails
        return f"{ip_address}/24"

def get_device_info(host, port, username, password):
    """Retrieves system and interface information using NETCONF."""
    # Define filters for standard IETF system and interfaces schemas
    system_filter = """
    <filter>
        <system xmlns="urn:ietf:params:xml:ns:yang:ietf-system"/>
    </filter>
    """
    interfaces_filter = """
    <filter>
        <interfaces-state xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces"/>
    </filter>
    """
    
    try:
        with get_manager(host, port, username, password) as m:
            print("\n--- Fetching System Information ---")
            sys_reply = m.get(filter=system_filter)
            print("System Information XML:")
            # Pretty print XML
            dom = xml.dom.minidom.parseString(sys_reply.xml)
            print(dom.toprettyxml(indent="  "))
            
            print("\n--- Fetching Interfaces State ---")
            int_reply = m.get(filter=interfaces_filter)
            print("Interfaces State XML:")
            dom_int = xml.dom.minidom.parseString(int_reply.xml)
            print(dom_int.toprettyxml(indent="  "))
            
    except Exception as e:
        print(f"[-] Error retrieving device info: {e}", file=sys.stderr)

def configure_ip(host, port, username, password, interface, ip, mask):
    """Configures the IP address of a specified interface."""
    # Standard IETF interfaces configuration XML payload
    config_xml = f"""
    <config xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf:base:1.0">
      <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
        <interface>
          <name>{interface}</name>
          <type xmlns:ianaift="urn:ietf:params:xml:ns:yang:iana-if-type">ianaift:ethernetCsmacd</type>
          <enabled>true</enabled>
          <ipv4 xmlns="urn:ietf:params:xml:ns:yang:ietf-ip">
            <address>
              <ip>{ip}</ip>
              <netmask>{mask}</netmask>
            </address>
          </ipv4>
        </interface>
      </interfaces>
    </config>
    """
    
    try:
        with get_manager(host, port, username, password) as m:
            print(f"\nConfiguring IP {ip}/{mask} on interface {interface}...")
            reply = m.edit_config(target='running', config=config_xml)
            print("[+] Configuration successfully applied!")
            print(reply)
    except Exception as e:
        print(f"[-] Error configuring IP: {e}", file=sys.stderr)

def configure_static_route(host, port, username, password, destination, mask, next_hop):
    """Configures a static route on the device."""
    dest_prefix = ip_to_cidr(destination, mask)
    
    # Standard IETF routing configuration XML payload
    config_xml = f"""
    <config xmlns="urn:ietf:params:xml:ns:yang:ietf-netconf:base:1.0">
      <routing xmlns="urn:ietf:params:xml:ns:yang:ietf-routing">
        <routing-instance>
          <name>default</name>
          <routing-protocols>
            <routing-protocol>
              <type xmlns:rt="urn:ietf:params:xml:ns:yang:ietf-routing">rt:static</type>
              <name>static-routing</name>
              <static-routes>
                <ipv4 xmlns="urn:ietf:params:xml:ns:yang:ietf-ipv4-unicast-routing">
                  <route>
                    <destination-prefix>{dest_prefix}</destination-prefix>
                    <next-hop>
                      <next-hop-address>{next_hop}</next-hop-address>
                    </next-hop>
                  </route>
                </ipv4>
              </static-routes>
            </routing-protocol>
          </routing-protocols>
        </routing-instance>
      </routing>
    </config>
    """
    
    try:
        with get_manager(host, port, username, password) as m:
            print(f"\nConfiguring static route to {destination}/{mask} via {next_hop}...")
            reply = m.edit_config(target='running', config=config_xml)
            print("[+] Configuration successfully applied!")
            print(reply)
    except Exception as e:
        print(f"[-] Error configuring static route: {e}", file=sys.stderr)

def main():
    parser = argparse.ArgumentParser(description="NETCONF Automation CLI Tool")
    
    # Common connection options
    parser.add_argument("--host", default=DEFAULT_HOST, help=f"Device IP/Host (default: {DEFAULT_HOST})")
    parser.add_argument("--port", type=int, default=DEFAULT_PORT, help=f"NETCONF Port (default: {DEFAULT_PORT})")
    parser.add_argument("--username", default=DEFAULT_USER, help=f"NETCONF Username (default: {DEFAULT_USER})")
    parser.add_argument("--password", default=DEFAULT_PASS, help=f"NETCONF Password (default: {DEFAULT_PASS})")
    
    subparsers = parser.add_subparsers(dest="command", help="Available subcommands")
    
    # get-info subcommand
    subparsers.add_parser("get-info", help="Retrieve device information (system & interfaces)")
    
    # set-ip subcommand
    parser_ip = subparsers.add_parser("set-ip", help="Configure interface IP address")
    parser_ip.add_argument("--interface", required=True, help="Interface name (e.g. GigabitEthernet2)")
    parser_ip.add_argument("--ip", required=True, help="IPv4 address (e.g. 192.168.50.2)")
    parser_ip.add_argument("--mask", required=True, help="Subnet mask (e.g. 255.255.255.0)")
    
    # set-route subcommand
    parser_route = subparsers.add_parser("set-route", help="Configure static route")
    parser_route.add_argument("--destination", required=True, help="Destination IP network (e.g. 10.0.0.0)")
    parser_route.add_argument("--mask", required=True, help="Destination subnet mask (e.g. 255.255.255.0)")
    parser_route.add_argument("--next-hop", required=True, dest="next_hop", help="Next hop gateway IP (e.g. 192.168.1.254)")
    
    args = parser.parse_args()
    
    if not args.command:
        parser.print_help()
        sys.exit(1)
        
    if args.command == "get-info":
        get_device_info(args.host, args.port, args.username, args.password)
    elif args.command == "set-ip":
        configure_ip(args.host, args.port, args.username, args.password, args.interface, args.ip, args.mask)
    elif args.command == "set-route":
        configure_static_route(args.host, args.port, args.username, args.password, args.destination, args.mask, args.next_hop)

if __name__ == "__main__":
    main()