import pytz

from datetime import datetime


BASE_PATTERN = "%Y-%m-%d %H:%M:%S"


def is_date_instance(date):
    return isinstance(date, datetime)


def parse_date(date):
    return datetime.strptime(date, BASE_PATTERN)


def get_formated_date(date):
    return date.strftime(BASE_PATTERN)


def get_readable_date(date):
    """
    Return human readable date in string format:
    Fri 14, October 2016 at 08:22 AM
    """
    return date.strftime("%a %d, %B %Y at %I:%M %p")


def get_now():
    return datetime.now(pytz.utc)
