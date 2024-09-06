import requests
import json

client_cert_auth=False
switchuser='admin'
switchpassword='Admin_1234!'
#client_cert='PATH_TO_CLIENT_CERT_FILE'
#client_private_key='PATH_TO_CLIENT_PRIVATE_KEY_FILE'
#ca_cert='PATH_TO_CA_CERT_THAT_SIGNED_NXAPI_SERVER_CERT'

url='https://sandbox-nxos-1.cisco.com/ins'
myheaders={'content-type':'application/json'}
payload={
  "ins_api": {
    "version": "1.0",
    "type": "cli_show",
    "chunk": "0",
    "sid": "sid",
    "input": "show version",
    "output_format": "json"
  }
}

#if client_cert_auth is False:
response = requests.post(url,data=json.dumps(payload), headers=myheaders,auth=(switchuser,switchpassword), verify=False).json()
#else:
#url='https://10.10.20.95/ins'
#response = requests.post(url,data=json.dumps(payload), headers=myheaders,auth=(switchuser,switchpassword),cert=(client_cert,client_private_key),verify=ca_cert).json()
print(response)