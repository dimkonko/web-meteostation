import date_service


def create_from_last_update(record):
    """
    :param (LastUpdate) record
    """
    return None if record is None else {
        "temperature": record.temperature,
        "humidity": record.humidity,
        "create_date":  date_service.get_readable_date(record.create_date)
    }


def get_records(records):
    return (create_record(record) for record in records)


def create_record(record):
    record['create_date'] = date_service.get_readable_date(record['create_date'])
    return record
