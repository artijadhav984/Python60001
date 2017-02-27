#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 24 14:20:18 2017

@author: Arti
"""

annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the portion of salary to be saved in decimal form (i.e. 0.1 for 10%): "))
total_cost = float(input("Enter the cost of your dream home: "))
portion_down_payment = 0.25 * total_cost
current_saving = 0
r = 0.04 #an annual return
monthly_return = r/12.0
monthly_saving = portion_saved * (annual_salary/12)
#print("portion_down_payment = $" + str(portion_down_payment))
#print("Monthly_saving:", monthly_saving)
i = 0

while (current_saving < portion_down_payment):
    i += 1
    total_monthly_return = current_saving * monthly_return
    current_saving += total_monthly_return + monthly_saving
    #print("Month:{}\nTotal_monthly_return: {}\nCurrent_saving: {}".format(i, total_monthly_return, current_saving))
    
print("Months took to save up enough money for a down payment:", i)