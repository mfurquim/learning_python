import os

from dotenv import load_dotenv

load_dotenv()


def get_env(option):
    def list_alert_time():
        return [int(num) for num in (os.getenv("LIST_ALERT_TIME", "-")).split(",")]

    options = {
        "LIST_ALERT_TIME": list_alert_time,
    }

    return options[option]()
