import requests, urllib3

# Disable Self-Signed Cert warning for demo
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Assign requests.Session instance to session variable
session = requests.Session()

# Define URL and PAYLOAD variables
URL = "https://sandbox-nxos-1.cisco.com/api/aaaLogin.json"
PAYLOAD = {
          "aaaUser": {
            "attributes": {
              "name": "admin",
              "pwd": "Admin_1234!"
               }
            }
          }

# Obtain an authentication cookie
session.post(URL,json=PAYLOAD,verify=False)

# Define SYS_URL variable
SYS_URL = "https://sandbox-nxos-1.cisco.com/api/mo/sys.json"

# Obtain system information by making session.get call
# then convert it to JSON format then filter to system attributes
sys_info = session.get(SYS_URL,verify=False).json()["imdata"][0]["topSystem"]["attributes"]

# Print hostname, serial nmber, uptime and current state information
# obtained from the NXOSv9k
print("HOSTNAME:", sys_info["name"])
print("SERIAL NUMBER:", sys_info["serial"])
print("UPTIME:", sys_info["systemUpTime"])
print("DISTINGUISHED NAME:", sys_info["dn"])

