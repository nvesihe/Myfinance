
import numpy as np
import pandas as pd
from datetime import date

EXPENSES = []
PRICES = []
DATES = []
EXPENSE_TYPES = []
    
def add_expense(good_or_service,price,date,expense_type):
    EXPENSES.append(good_or_service)
    PRICES.append(price)
    DATES.append(date)
    EXPENSE_TYPES.append(expense_type)

   
    
    

option = -1
while(option != 0):
    print('EXPENSE TRACKER')
    print('1. Add Food Expense')
    print('2. Add Household Expense')
    print('3. Add Transportation Expense')
    print('4. Show and Save the expanse report')
    print('0. Exit')

    option= int(input('Choose an option: '))
    if option == 0:
        break
    elif option == 1:
        print('Adding Food')
        expense_type="FOOD"
    elif option == 2:
        print('Adding Household')
        expense_type="HOUSEHOLD"
    elif option == 3:
        print('Adding Transportation')
        expense_type="TRANSPORTATION"
    elif option == 4:
        expense_report = pd.DataFrame()
        expense_report['EXPENSES'] = EXPENSES
        expense_report['PRICES']=PRICES
        expense_report['DATES']=DATES
        expense_report['EXPENSE_TYPE']=EXPENSE_TYPES  

        expense_report.to_csv('expenses.csv')
        print(expense_report)
                
    else:
        print('Warning! Choose 1,2,3,4 or 0!')

    if option == 1 or option == 2 or option == 3:
        good_or_service = input('Enter the good or service for the expense type' +expense_type+':\n' )
        price = float(input('Enter the price of the good or service:\n'))
        today = date.today()
        add_expense(good_or_service,price,today,expense_type)
    
    
    


