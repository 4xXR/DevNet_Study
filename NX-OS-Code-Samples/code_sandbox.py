import json
import requests

username = "admin"
password = "Admin_1234!"

ip_addr =  "10.10.20.95"
endpoints = "/api/mo/sys.json"
payload = {
  "topSystem": {
    "attributes": {
      "dn": "sys",
      "rn": "sys"
    },
    "children": [
      {
        "bdEntity": {
          "attributes": {
            "dn": "sys/bd",
            "rn": "bd"
          },
          "children": [
            {
              "l2BD": {
                "attributes": {
                  "dn": "sys/bd/bd-[vlan-103]",
                  "fabEncap": "vlan-103",
                  "name": "NXAPI_REST_VLAN_py",
                  "rn": "bd-[vlan-103]"
                }
              }
            }
          ]
        }
      }
    ]
  }
}


def aaa_login(username, password, ip_addr):
    payload = {
        'aaaUser' : {
            'attributes' : {
                'name' : username,
                'pwd' : password
                }
            }
        }
    url = "http://sandbox-nxos-1.cisco.com/api/aaaLogin.json"
    auth_cookie = {}

    response = requests.request("POST", url, data=json.dumps(payload),verify=False)
    if response.status_code == requests.codes.ok:
        data = json.loads(response.text)['imdata'][0]
        token = str(data['aaaLogin']['attributes']['token'])
        auth_cookie = {"APIC-cookie" : token}

    print ()
    print ("aaaLogin RESPONSE:")
    print (json.dumps(json.loads(response.text), indent=2))

    return response.status_code, auth_cookie


def aaa_logout(username, ip_addr, auth_cookie):
    payload = {
        'aaaUser' : {
            'attributes' : {
                'name' : username
                }
            }
        }
    url = "http://sandbox-nxos-1.cisco.com/api/aaaLogout.json"

    response = requests.request("POST", url, data=json.dumps(payload),
                                cookies=auth_cookie)

    print ()
    print ("aaaLogout RESPONSE:")
    print (json.dumps(json.loads(response.text), indent=2))
    print ()

def post(ip_addr, auth_cookie, url, payload):
    response = requests.request("POST", url, data=json.dumps(payload),
                                cookies=auth_cookie)

    print ()
    print ("POST RESPONSE:")
    print (json.dumps(json.loads(response.text), indent=2))


if __name__ == '__main__':
    status, auth_cookie = aaa_login(username, password, ip_addr)
    if status == requests.codes.ok:
        url = "http://" + ip_addr + endpoints 
        post(ip_addr, auth_cookie, url, payload)
        aaa_logout(username, ip_addr, auth_cookie)
        
