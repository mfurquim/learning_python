import os

from dotenv import load_dotenv

load_dotenv()


def get_env(option):
    def string_example():
        return os.getenv("STRING_EXAMPLE", "-")

    def int_example():
        return int(os.getenv("INT_EXAMPLE", "0"))

    def bool_example():
        return os.getenv("BOOL_EXAMPLE", "FALSE").upper() == "TRUE"

    def list_string_example():
        return [s for s in (os.getenv("LIST_STRING_EXAMPLE", "a,b,c")).split(",")]

    def list_alert_time():
        return [int(n) for n in (os.getenv("LIST_INT_EXAMPLE", "1,2,3")).split(",")]

    options = {
        "STRING_EXAMPLE": string_example,
        "INT_EXAMPLE": int_example,
        "BOOL_EXAMPLE": bool_example,
        "LIST_STRING_EXAMPLE": list_string_example,
        "LIST_INT_EXAMPLE": list_alert_time,
    }

    return options[option]()
