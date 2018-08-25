import calendar

def calendar_factory(start_day): calendar.Calendar(start_day)

class calendar(calendar):
    def __init__(self):
        self.banana = 'foo'
