from netmiko import ConnectHandler

# Define the command as a variable
command_to_run = "show clock"

from netmiko import ConnectHandler

command_to_run = "show clock"

switches = [
    {"device_type": "cisco_ios", "ip": "192.168.1.3", "username": "cisco", "pas>
    {"device_type": "cisco_ios", "ip": "192.168.1.4", "username": "cisco", "pas>
    {"device_type": "cisco_ios", "ip": "192.168.1.5", "username": "cisco", "pas>
    {"device_type": "cisco_ios", "ip": "192.168.1.6", "username": "cisco", "pas>
]


with open("result.txt", "w") as f:
    for switch in switches:
        f.write(f"\nConnecting to {switch['ip']}...\n")
        try:
            net_connect = ConnectHandler(**switch)
            output = net_connect.send_command(command_to_run)
            f.write(f"Output from {switch['ip']} ({command_to_run}):\n{output}\>
            net_connect.disconnect()
        except Exception as e:
            f.write(f"Failed to connect to {switch['ip']}: {e}\n")
