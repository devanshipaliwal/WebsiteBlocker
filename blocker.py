import time
from datetime import datetime as dt

host_file = "C:\Windows\System32\drivers\etc"
redirect = "127.0.0.1"

website_list = ["www.instagram.com"]

start_time = int(9)
end_time = int(18)

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, start_time) < dt.now() < dt(dt.now().year,dt.now().month, dt.now().day, end_time):
        print("Working Hours. Running...")
        # open hostfile
        with open(host_file, 'r+') as file:
            file.seek(0)
            content = file.read()
            # if website list not already in hostfile, add website in
            for website in website_list:
                if website in content:
                    pass
                else:
                    file.write(redirect + " " + website + "\n")
    else:
        with open(host_file, 'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
        print("Blocker is running")
    time.sleep(7)
