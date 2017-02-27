#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 24 15:11:35 2017

@author: Arti
"""

starting_annual_salary = float(input("Enter your starting annual salary: "))
portion_saved = 0 #calculate the best savings rate
total_cost = 1000000
portion_down_payment = 0.25 * total_cost
current_saving = 0.0
semi_annual_raise = 0.07
r = 0.04 #an annual return
monthly_return = r/12.0
print("portion_down_payment = $" + str(portion_down_payment))
i = 0 #no. of steps
low = 0
high = 10000
guess = (low + high)/2

while (abs(current_saving - portion_down_payment) > 100 and round(guess) > 0 and round(guess) < 10000):
    last_current_saving = current_saving
    last_portion_saved = portion_saved
    guess = (low + high)/2
    portion_saved = round((guess/10000), 4)
    i +=1
    print("*******************************************\nStep: {}\nLow: {}\nHigh: {}\nGuess: {}\nPercent saving: {}%\nSaving rate: {}".format(i, low, high, guess, round((guess/100), 4), portion_saved))
    current_saving = 0
    annual_salary = starting_annual_salary
    for j in range(36):
        if(j % 6 == 0):
            if(j > 0):
                annual_salary += annual_salary * semi_annual_raise
            #print("----------------------------\nAnnual_salary: {}".format(annual_salary))
            monthly_saving = portion_saved * (annual_salary/12)
            #print("Monthly_saving: {}".format(monthly_saving))
        total_monthly_return = current_saving * monthly_return
        current_saving += total_monthly_return + monthly_saving
        #print("Month:{}\nTotal_monthly_return: {}\nCurrent_saving: {}".format(i, total_monthly_return, current_saving))
    current_saving = round(current_saving)
    print("Total saving in 3 yrs: {}\nPortion_down_payment: {}".format(current_saving, portion_down_payment)) 
    
    if(current_saving < portion_down_payment):
        low = guess
    else:
        high = guess

if(abs(current_saving - portion_down_payment) <= 100):    
    print("Best saving rate: {}".format(portion_saved)) 
    print("Steps in bisection search:​ {}".format(i))
else:
    print("It is not possible to pay the down payment in three years.")
 