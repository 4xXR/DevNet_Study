import requests
import json

url = "https://devnetsandboxiosxe.cisco.com:443/restconf/data/Cisco-IOS-XE-interfaces-oper:interfaces/interface=GigabitEthernet1"

payload = {}
headers = {
  'Accept': 'application/yang-data+json',
  'Content-Type': 'application/yang-data+json',
  'Authorization': 'Basic YWRtaW46QzFzY28xMjM0NQ=='#.encode('utf-8')
}

response = requests.request("GET", url, headers=headers, data=payload, verify=False)

api_data = response.json()
interface_data = api_data["Cisco-IOS-XE-interfaces-oper:interface"][0]
print("/" * 50)
print(interface_data["description"])
print("/" * 50)
if interface_data["admin-status"] == 'if-state-up':
    print('Interface is up')