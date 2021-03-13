from crontab import CronTab
import yaml
from app.init import *

CRON_COMMENT = 'ta_notification'
PYTHON_PATH = ROOT_PATH + '/venv/bin/python'
NOTIFICATION_SCRIPT_PATH = ROOT_PATH + '/app/notification.py'


def remove_old_cron_jobs(local_cron):
    for job in local_cron:
        if job.comment == CRON_COMMENT:
            local_cron.remove(job)
            local_cron.write()


def create_cron_jobs(local_cron):
    with open(SCHEDULE_PATH, 'r') as yml_file:
        try:
            notifications = yaml.safe_load(yml_file)['notifications']
        except yaml.YAMLError as e:
            logging.error(e)
            return False
    for index, msg in enumerate(notifications):
        job = local_cron.new(command=cron_command(index), comment=CRON_COMMENT)
        job.setall(msg['time'])
        local_cron.write()
    return True


def cron_command(index):
    return " /bin/bash -c \"" + PYTHON_PATH + ' ' + NOTIFICATION_SCRIPT_PATH + ' ' + str(index) + "\""


if __name__ == '__main__':
    cron = CronTab(user='shpmax')
    remove_old_cron_jobs(cron)
    create_cron_jobs(cron)
    cron.write()
    pass
