# Import library
from netmiko import ConnectHandler

device = {
    'device_type': 'nokia_sros',
    'ip': '10.18.8.158',
    'username': 'admin',
    'password': 'admin'
}

# Establish SSH connection to device
SSH = ConnectHandler(**device)

# Send Config
SSH.send_config_set(["/configure router interface loopback1","address 1.1.1.1/24","loopback",])

#Check the result:
OUTPUT=SSH.send_command("show router interface")
print(OUTPUT)

# Close SSH connection
SSH.disconnect()