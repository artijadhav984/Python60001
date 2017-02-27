#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 24 15:11:35 2017

@author: Arti
"""

annual_salary = float(input("Enter your starting annual salary: "))
portion_saved = float(input("Enter the portion of salary to be saved in decimal form (i.e. 0.1 for 10%): "))
total_cost = float(input("Enter the cost of your dream home: "))
portion_down_payment = 0.25 * total_cost
current_saving = 0
semi_annual_raise = float(input("Enter the semi­annual salary raise in decimal form (i.e. 0.08 for 8%): "))
r = 0.04 #an annual return
monthly_return = r/12.0

print("portion_down_payment = $" + str(portion_down_payment))
i = 0

while (current_saving < portion_down_payment):
    if(i % 6 == 0):
        if(i > 0):
            annual_salary += annual_salary * semi_annual_raise
        
        print("*****************************************************\nAnnual_salary: {}".format(annual_salary))
        monthly_saving = portion_saved * (annual_salary/12)
        print("Monthly_saving: {}".format(monthly_saving))
        
    i += 1
    total_monthly_return = current_saving * monthly_return
    current_saving += total_monthly_return + monthly_saving
    print("Month:{}\nTotal_monthly_return: {}\nCurrent_saving: {}".format(i, total_monthly_return, current_saving))
    
print("Months took to save up enough money for a down payment:", i)