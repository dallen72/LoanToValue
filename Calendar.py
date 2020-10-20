
# class for representing the month number as shared state, using the Borg antipattern
class Calendar:
    __shared_state = {}
    month = 0
    def __init__(self):
        self.__dict__ = self.__shared_state

    # Acts as a clock
    def nextMonth(self):
        self.month += 1
