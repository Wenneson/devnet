from netmiko import ConnectHandler
from getpass import getpass

devUser = "admin"
devPass = getpass(prompt=f'Enter the password for {devUser}: ')

r01 = {
    'device_type': 'cisco_ios',
    'host': 'r01.miwenlabs.com',
    'username': devUser,
    'password': devPass,
    'secret': devPass,
}

r02 = {
    'device_type': 'cisco_ios',
    'host': 'r02.miwenlabs.com',
    'username': devUser,
    'password': devPass,
    'secret': devPass,
}

r03 = {
    'device_type': 'cisco_ios',
    'host': 'r03.miwenlabs.com',
    'username': devUser,
    'password': devPass,
    'secret': devPass,
}

all_routers = [r01, r02, r03]

configOSPF = ['router ospf 30',
              'network 10.0.0.0 0.255.255.255 area 0',
              'network 172.16.0.0 0.15.255.255 area 0',
              'network 192.168.0.0 0.0.255.255 area 0']

for router in all_routers:
    networkConnect = ConnectHandler(**router)
    networkConnect.enable()
    print("*****" * 20)
    print(router['host'])
    print("*****" * 20)
    networkConnect.send_command("show ip interface brief | ex unass")
    print("Configuring OSPF")
    networkConnect.send_config_set(configOSPF)
    networkConnect.send_config_from_file('ripConfig.txt')

