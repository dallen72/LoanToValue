
# Purpose: As the value of a property increadses and the amount for minimum payment changes on a 20% loan, it makes sense to have a Loan object to store the minimum payment, Interest rate and principle history.

import pdb

class Loan:
    APR = 5
    PAYMENTS_PER_YEAR = 12
    term_years = 30
    minimum_payment = 450
    principle_history = []
    initial_value = 0

    def __init__(self, loan_value, current_month):
        while (len(self.principle_history)-1 < current_month):
                self.principle_history.append(0)
        self.term_years = 30
        self.principle_history.append( loan_value )
        self.initial_value = loan_value
        self.determineMinPayment()
        # TODO: using month, update the minimum payment and APR
        pass

    # calculate the new principle based on one payment, for the new month
    def addPrinciple(self, current_month):
        last_principle = self.principle_history[current_month]
        new_principle = last_principle*(1 + self.APR/100/12.0) - self.minimum_payment
        self.principle_history.append(new_principle)
        # TODO: this is the formula for the actual payment        new_principle = self.payment + self.hoa + (self.value_history[month])*self.tax/100 

    # determines the payment of the loan, given the loan value. the term and APR are constant.
    def determineMinPayment(self):
        num_payments = self.PAYMENTS_PER_YEAR * self.term_years
        interest_rate = float(self.APR) / float(self.PAYMENTS_PER_YEAR)/100.0
        discount_factor = (((1 + interest_rate)**num_payments) - 1) / (interest_rate*((1+interest_rate)**num_payments))

        loan_value = self.initial_value
        self.minimum_payment = loan_value / discount_factor
        
# needs to be able to recalc principle like in Investor.payPropertyPayments
# needs to have a minimum payment, like given in PropertyObj.py
# PropertyObj.calcprinciple is where the new principle is calculated
