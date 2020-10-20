# LoanToValue

## Use Cases
1. Enter data related to loans, salary, property prices and generate a chart from that, showing the predicted cash on hand, property value, and net worth over a period of several months.

Visualizer for finding the optimal down payment amount on a rental property, given certain parameters

## Files:

### runScenario.py
Main program file. Algorithm shown below.

### Calendar.py
File for shared state. Uses the Borg antipattern.

### PropertyObj.py
Class for the Property Object. Holds associated info such as HOA Dues. instantiated only once. TODO: change to interface? or is this a Singleton?

### Investor.py
The File for the Investor Class. Holds data such as salary and initial savings.

###
