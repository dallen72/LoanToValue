import plotly
import plotly.graph_objs as go

from Investor import Investor
from Calendar import Calendar
from PropertyObj import PropertyObj

MONTHS_IN_PERIOD = 600
Y_RANGE = [0, 1000000]
DOWN_PAYMENT_PERCENTAGE = 20

calendar = Calendar()
investor = Investor(DOWN_PAYMENT_PERCENTAGE)
property_obj = PropertyObj()

# every month, money comes in and money goes out
for month in range(0, MONTHS_IN_PERIOD):
    calendar.nextMonth()
    property_obj.updateValue()
    investor.earnIncome()
    investor.payPropertyPayments(property_obj)
    investor.updateNetWorth(property_obj)
    if (investor.canAffordProperty( property_obj ) and len(investor.loans) < 1):
            investor.buyProperty( property_obj )

# function which takes the raw data and makes traces for the chart
# TODO: this function is too large. break it up, it smells
def mapTraces(investor):
    down_payment_percentage = investor.down_payment_percentage
    x_axis_months = [0]
    for month in range(0, MONTHS_IN_PERIOD):
        x_axis_months.append(month)

    property_value = property_obj.value_history
    color_variable = str(25*down_payment_percentage/10)
    name_variable = str(down_payment_percentage) + "% dp"
    color1 = 'rgb(' + color_variable + ', 200, ' + color_variable + ')'
    color2 = 'rgb(200, ' + color_variable + ', 240)'
    color3 = 'rgb(' + color_variable + ', 120, 240)'
    color4 = 'rgb(' + color_variable + ', 250, 100)'

    savings_history = investor.savings_history
    cash_trace = go.Scatter(x=x_axis_months, y=savings_history, name="Cash " + name_variable, line=dict(color = (color1)))

    property_value_trace = go.Scatter(x=x_axis_months, y=property_value, name="Property Value " + name_variable, line=dict(color = (color3)))
    net_worth_history = investor.net_worth_history
    net_worth_trace = go.Scatter(x=x_axis_months, y=net_worth_history, name="Net Worth " + name_variable, line=dict(color = (color4)))
    traces_list = [property_value_trace, cash_trace, net_worth_trace]
    loans = investor.loans
    loan_traces = []
    for loan in loans:
        loan_trace = go.Scatter(x=x_axis_months, y=loan.principle_history, name="Loan Principle " + name_variable, line=dict(color = (color2)))
        traces_list.append(loan_trace)
    
    return traces_list


traces = mapTraces(investor)


# plot the visualization
plotly.offline.plot({
    "data": traces,
    "layout": go.Layout(
        title="Dollars vs Months For Mortgage Related Values",
        yaxis=dict(range=Y_RANGE)
        )

}, auto_open=True)
