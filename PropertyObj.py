
from Calendar import Calendar

class PropertyObj:
    initial_value = 100000
    value_history = []
    rent = 300
    hoa = 150
    tax_rate = 0.1 # percent
    inflation_rate = 4 # annual inflation rate
    calendar = None

    def __init__(self):
        calendar = Calendar()
        self.calendar = calendar
        self.value_history.append( self.initial_value )

    # update the value of the property based on inflation
    def updateValue(self):
        last_month = self.calendar.month - 1
        old_value = self.value_history[last_month]
        new_value = old_value*(1 + self.inflation_rate/100.0/12)
        self.value_history.append( new_value )


