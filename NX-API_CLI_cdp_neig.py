import requests
import json

url = 'https://sbx-nxos-mgmt.cisco.com/ins'
switchuser = 'admin'
switchpassword = 'Admin_1234!'
myheader = {'content-type' : 'application/json'}

payload = {
  "ins_api": {
    "version": "1.0",
    "type": "cli_show",
    "chunk": "0",
    "sid": "sid",
    "input": "sh cdp nei",
    "output_format": "json"
  }
}

response = requests.request (
    url,
    data=json.dumps(payload),
    headers=myheader,
    auth=(switchuser,switchpassword),
    verify=False 
    ).json()

print(json.dumps(response, indent=2, sort_keys=True))