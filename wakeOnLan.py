import subprocess
import time

send_ping = "ping -c 4 192.168.1.120"
command = subprocess.getstatusoutput(send_ping)
result = command[1]
no_ping = "Destination Host Unreachable"
wake_up = "wakeonlan 10:E7:C6:14:E3:D5"
# wake_up = "wakeonlan 30:9C:23:A4:8D:07" Dvir PC



if no_ping in command[1]:
    print("The Server is Down")
    subprocess.run(wake_up , shell=True)
else:
    print("The Server is up and running")


# Main loop to send ping every 10 second
while True:
    send_ping()
    time.sleep(10)  # Wait for 10 seconds