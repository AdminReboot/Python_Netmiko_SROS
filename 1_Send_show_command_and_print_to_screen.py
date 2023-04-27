# Import library
from netmiko import ConnectHandler

device = {
    'device_type': 'nokia_sros', #device type is fixed, you shouldn't change this
    'ip': '10.18.8.158', #ip connect to your device via SSH
    'username': 'admin', #default username
    'password': 'admin' #default password
}

# Establish SSH connection to device
SSH = ConnectHandler(**device)

# Send a command and print output
OUTPUT = SSH.send_command('admin display-config')
print(OUTPUT)

# Close SSH connection
SSH.disconnect()