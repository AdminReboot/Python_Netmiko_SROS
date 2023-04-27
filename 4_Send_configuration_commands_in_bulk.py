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

# Create a dictionary
INT={
    "loopback10": "172.1.10.1/24",
    "loopback20": "172.1.20.1/24",
    "loopback30": "172.1.30.1/24", 
}

# Implement a for loop
for i in INT:
    SSH.send_config_set(["/configure router interface "+i,"address "+INT[i],"loopback"])

#Check the result:
OUTPUT=SSH.send_command("show router interface")
print(OUTPUT)

# Close SSH connection
SSH.disconnect()