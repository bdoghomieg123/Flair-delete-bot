import praw
from common import clear
import os
import time
from datetime import datetime
from threading import Timer
from main import *

x=datetime.today()
y=x.replace(day=x.day+1, hour=16, minute=8, second=0, microsecond=0)
delta_t=y-x

secs = delta_t.seconds+1


def start():
    try:
        os.remove("username_log.txt")
        os.remove("posts_replied_to.txt")
        main()
    except Exception as e:
        t = Timer(secs, main)
        t.start()
        main()

def delete_files_restart():
    try:
        os.remove("username_log.txt")
        os.remove("posts_replied_to.txt")
        print("Reset was completed successfully")
        print("Sleeping for 5 seconds...")
        time.sleep(5)
        clear()
        main()
    except Exception as e:
        print(e)
        main()




start()
