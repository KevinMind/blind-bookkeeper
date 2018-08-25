from utils.logger import logger
from bookkeeper import BookShelf
import calendar
import datetime
from bookkeeper import BookShelf

CAL = calendar.Calendar(0)

config = {
    'slot_length': 30,
    'time_period_length': 480,
    'start_time': datetime.time(8,0),
    'end_time': datetime.time(18,9)
}

'''
Get a json of days in month given, (year: int, month: int)

[
    {
        date: datetime.date(year, month, day)
        booked: bool
    }
]

we store calendar events separately from the book ledger. Book ledger should know if appointment is valid.

Each calendar has a config 

{ slot_length: integer, row_length: }

I need to be able to convert an array of calendar events into a bookshelf.


'''
def get_days_in_month(year: int, month: int) -> list:
    return CAL.monthdays2calendar(year, month)

def is_open(row, slot):
    print('row: {} slot: {}'.format(row, slot))
    return True

def should_include_value(date: int, strict: bool = False) -> bool:
    return date > 0 or not strict

def format_date_tuple(year, month, day, weekday, i):
    return {
        'date': datetime.date(year, month, day),
        'row': i,
        'slot': weekday
    }

def build_shelf_row(year: int, month: int, day: int) -> list:
    print(config)
    Shelf = BookShelf(slot_length=30, start=config['start_time'], end=config['end_time'])

    # I have a list of calendar events with start_datetime, duration.
    return []


def build_book_shelf(year: int, month: int, strict: bool = False) -> list:
    m = get_days_in_month(year, month)
    return [
        [
            format_date_tuple(year, month, day, weekday, i)
            for (day, weekday) in m[i]
            if day > 0
        ]
        for i in range(len(m))
    ]


if __name__ == '__main__':
    # make a bookshelf with 4 slots per row and a row length of 53.
    y = int(input('year: '))
    m = int(input('month: '))
    d = int(input('day: '))
    values = build_shelf_row(y, m, d)
    print(values)



    # BOOKSHELF = BookShelf(4, 53)
    # print(BOOKSHELF.get_free_slots__shelf())
    #
    # times = [(0,2), (1,1)]
    # for row, slot in times:
    #     add_book = BOOKSHELF.put_book_on_shelf(row, slot)
    #     if add_book:
    #         logger.info('added the book!')
    #     else:
    #         logger.warning("Could not add the book, row: {} slot: {} ".format(row, slot))
    #
    # print(BOOKSHELF.get_free_slots__shelf())

