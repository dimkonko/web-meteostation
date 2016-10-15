import date_service


class LastRecordStorage(object):
    def __init__(self):
        self.last_record = None

    def init_record(self, t, h, create_date):
        self.last_record = LastRecord(t, h, self.parse_date(create_date))
        return self.last_record

    def has_record(self):
        return self.last_record is not None

    def parse_date(self, date):
        return date if date_service.is_date_instance(date) else date_service.parse_date(create_date)
                
    def has_data_changed(self, t, h):
        data_changed = False

        record = self.last_record
        if not self.has_record() or (t !=record.temperature or h !=record.humidity):
            data_changed = True

        return data_changed

    def set_last_update_date(self, create_date):
        self.last_record.create_date = self.parse_date(create_date)

    def get_record(self):
        return self.last_record


class LastRecord(object):
    def __init__(self, t, h, create_date):
        self.temperature = int(t)
        self.humidity = int(h)
        self.create_date = create_date

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
