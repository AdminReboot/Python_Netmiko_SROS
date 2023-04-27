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

# Execute batch command from text file 
SSH.send_config_from_file(config_file="5_Command_file.txt")

#Check the result:
OUTPUT=SSH.send_command("show router interface | match LB")
print(OUTPUT)

# Close SSH connection
SSH.disconnect()