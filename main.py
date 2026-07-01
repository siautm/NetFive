import os
import sys
import importlib.util

# Load netconf/main.py dynamically to avoid circular import namespace issues with "main"
netconf_main_path = os.path.join(os.path.dirname(__file__), 'netconf', 'main.py')
spec = importlib.util.spec_from_file_location("netconf_main", netconf_main_path)
netconf_main = importlib.util.module_from_spec(spec)
sys.modules["netconf_main"] = netconf_main
spec.loader.exec_module(netconf_main)

if __name__ == "__main__":
    netconf_main.main()