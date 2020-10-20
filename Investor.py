
from Calendar import Calendar
from Loan import Loan


class Investor:
    INITIAL_SAVINGS = 10000
    SAFETY_NET = 10000 # savings to keep on reserve
    savings_history = []
    salary = 1000
    properties = []
    loans = [] # contains lists for each principle containing the history of the principle
    net_worth_history = []
    down_payment_percentage = 0
    calendar = None

    def __init__(self, down_payment_percentage):
        self.savings_history.append( self.INITIAL_SAVINGS )
        self.down_payment_percentage = down_payment_percentage 
        self.calendar = Calendar()
        self.net_worth_history.append(self.INITIAL_SAVINGS)

    # update cash according to cashflow: salary and rental income
    def earnIncome(self):
        last_month = self.calendar.month - 1
        rental_income = 0
        for property_obj in self.properties:
            rental_income += 300 # TODO get from property object, not hardcode 300
        new_savings = self.savings_history[last_month] + self.salary + rental_income
        self.savings_history.append(new_savings)
 
    # update the remaining loans on loans and update cash according to property payments
    def payPropertyPayments(self, property_obj):
        current_month = self.calendar.month
        for loan in self.loans:
            loan.addPrinciple( current_month )

            mortgage_payment = loan.minimum_payment
            self.savings_history[current_month] -= mortgage_payment
        for properties_owned in self.properties:
            monthly_fees = property_obj.hoa # TODO: better calculation of payment
            #self.savings_history[current_month] -= monthly_fees

    # check if can afford the down payment on a loan using the cash in hand
    def canAffordProperty(self, property_obj):
        current_month = self.calendar.month
        current_savings = self.savings_history[current_month]
        property_value = property_obj.value_history[ current_month ]
        down_payment = self.down_payment_percentage*property_value/100.0 # TODO: function for calcing down payment
        can_afford = (current_savings >= (self.SAFETY_NET + down_payment))

        return can_afford

    # add property to list of properties owned, add new loan to list of loans, pay down payment
    def buyProperty(self, property_obj):
        current_month = self.calendar.month

        # buy property
        property_value = property_obj.value_history[current_month]
        down_payment = self.down_payment_percentage*property_value/100.0 # TODO: function for calcing down payment
        self.savings_history[current_month] -= down_payment
        self.properties.append( property_obj )

        # take on loan
        new_loan = Loan( property_value - down_payment, current_month )  
        self.loans.append( new_loan)

    # return the net worth based on cash, property values, and remaining loans
    def updateNetWorth(self, property_obj):
        current_month = self.calendar.month
        current_savings = self.savings_history[current_month]
        total_equity = 0
        property_value = property_obj.value_history[current_month]
        for loan in self.loans:
            principle = loan.principle_history[current_month] # TODO: replace month with current_month everywhere
            equity = property_value - principle
            total_equity += equity
        net_worth = current_savings + total_equity
        self.net_worth_history.append( net_worth )





