from utils.logger import logger
import datetime

APPOINTMENTS = []
BLIND_BOOK_KEEPER = []

'''
## Blind BookKeeper Algorithm

A bookshelf contains rows, and columns within rows, from now on called slots. # BOOKSHELF, ROW, SLOT

The number of rows is determined by the number of available agents for a given time period. # TIME_PERIOD, AGENT

The number of slots in a row is determined by the length of the time period evenly divided by the length of a base unit of time. # BASE_TIME_UNIT

A slot can either be booked or unbooked. #BOOKED

All config values are converted to integers to prevent indivisibility

+-----------------------------------------------+
|   |    |    |    |    |    |    | [] |    |   | Agent # 1
|---+----+----+----+----+----+----+----+----+---|
|   |    |    | [] |    |    |    | [] |    |   | ...
|---+----+----+----+----+----+----+----+----+---|
|   |    |    | [] |    | [] |    | [] |    |   |
|---+----+----+----+----+----+----+----+----+---|
|   |    |    |    |    |    |    | [] |    |   |
+---+----+----+----+----+----+----+----+----+---+

1. get available slots in row. (row_number)


I want to be able to generate a bookshelf on any day or any month quickly and with low cost.
A bookshelf needs to know start = datetime, end datetime, slot_size

'''

FAKE_DATA = [ [0,1,0,0], [0,1,0,1], [0,0,0,0], [0,1,1,0] ]

class BookShelf:
    def __init__(self, slot_length = 30, start = datetime.datetime.now(), end = None):
        st = start
        en = start + datetime.timedelta(0, (480 * 60)) if end is None else end
        p = en - st
        s = int(slot_length)
        n = int(p / s)


        print({
            s, p, n, st, en
        })


        self.config = {
            'num_slots': n,
            'row_length': p,
            'slot_length': s,
        }

        self.shelf = FAKE_DATA

    def is_row_empty(self, row):
        return self.shelf[row].index(1) == -1

    def get_free_slots__row(self, row_number):
        r = self.shelf[row_number]
        return [i for i in range(len(r)) if r[i] == 0]

    def get_free_slots__shelf(self):
        r = len(self.shelf)
        return [self.get_free_slots__row(i) for i in range(r)]

    def alter_book_state(self, row, slot, num):
        if not self.shelf[row][slot] == num:
            logger.warning('ERROR')
            raise Exception("you cannot do this")
        else:
            logger.info('successfully altered state of row: {} slot: {}'.format(row, slot))
            self.shelf[row][slot] = 1 if num == 0 else 0

    def put_book_on_shelf(self, row, slot):
        logger.info('attempting to add book to row: {} slot: {}'.format(row, slot))
        try:
            self.alter_book_state(row, slot, 0)
            return True
        except Exception as e:
            logger.warning('FAILURE ADDING BOOK: message: {} row: {} slot: {}'.format(e, row, slot))
            return False
    def delete_book_from_shelf(self, row, slot):
        logger.info('attempting to remove book from row: {} slot: {}'.format(row, slot))
        try:
            self.alter_book_state(row, slot, 1)
            return True
        except Exception as e:
            logger.warning('FAILURE REMOVING BOOK: message: {} row: {} slot: {}'.format(e, row, slot))
            return False
