import os
import time


def reqActivity(req, timex):
    if req == 'Shutdown':
        # os.system("shutdown /s /t 1")
        print('your system is shutting down')
    else:
        print('your system is restarting')
        # os.system("shutdown /r /t 1")


