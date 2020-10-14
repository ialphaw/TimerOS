# Python Program - Shutdown and Restart Computer

import os
import time

print("1. Shutdown Computer")
print("2. Restart Computer")
print("3. Exit")
choice = int(input("\nEnter your choice: "))
if 1 <= choice <= 2:
    sleepTime = int(input('Enter remaining time(seconds): '))
    if choice == 1:
        time.sleep(sleepTime)
        os.system("shutdown /s /t 1")
    else:
        time.sleep(sleepTime)
        os.system("shutdown /r /t 1")
else:
    exit()
