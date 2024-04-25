##crontab -l                List
##crontab -e                Edit
##sudo cron                 käivitamiseks
##sudo service cron status  staatuse vaatamiseks(active)

from datetime import datetime

dt = datetime.now()

f = open("/home/martpors/ta23-alused/datetime.log", "a")

f.writelines(str(dt) + "\n")

f.close()