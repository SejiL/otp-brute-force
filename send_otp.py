import requests
import sys

# Send OTP
mobile_number = sys.argv[1]
send_otp_url = 'https://TARGET.com/api/v4/user/login'
data = {'mobile': mobile_number}
res_send_otp = requests.post(send_otp_url, data=data)

print("###########", "Send-OTP-Res:", res_send_otp.content)
print("###########", "Send-OTP-Res:", res_send_otp.status_code)

if res_send_otp.status_code == 200:
    print("###########", "Success Send-OTP")
    print("###########", "Start Test OTP Codes ...")
else:
    print("Problem in Runtime:", res_send_otp.status_code)
