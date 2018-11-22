# -*- coding: utf-8 -*-
"""
Created on Thu Nov  1 10:00:58 2018

@author: heyon
"""

# pset1
# part A

total_cost = float(input("Enter the cost of your dream house: "))
annual_salary = float(input("Enter your annual salary in numbers: "))
portion_saved = float(input("Enter the portion of salary to be saved in decimal points: "))

portion_down_payment = 0.25
current_savings = 0
r = 0.04
monthly_salary = annual_salary/12
monthly_savings = monthly_salary*portion_saved
i = 0

while current_savings < portion_down_payment*total_cost:
    monthly_savings = monthly_salary*portion_saved + current_savings*r/12 
    current_savings += monthly_savings
    i+=1


num_months = i
print("You need",num_months, "months to save up for down payment.")

# part B
total_cost = float(input("Enter the cost of your dream house: "))
annual_salary = float(input("Enter your annual salary in numbers: "))
portion_saved = float(input("Enter the portion of salary to be saved in decimal points: "))
semi_annual_raise = float(input("Enter your semi-annual raise in decimal points: "))

portion_down_payment = 0.25
current_savings = 0
r = 0.04
i = 0

while current_savings < portion_down_payment*total_cost:
    if i!=0 and i%6==0:
        annual_salary = annual_salary*(1+semi_annual_raise)    
    monthly_savings = (annual_salary/12)*portion_saved + current_savings*r/12
    current_savings += monthly_savings
    i+=1

num_months = i
print("You need",num_months, "months to save up for down payment.")

# part C

# given
total_cost = 1000000
semi_annual_raise = 0.07
portion_down_payment = 0.25
r = 0.04
down_payment = portion_down_payment*total_cost
#user input
starting_annual_salary = int(input("Enter your starting annual salary in numbers: "))


steps = 0
possible_to_pay_in_three_years = True
low_int = 0
high_int = 10000
best_int = (low_int+high_int)/2

i =0
current_savings = 0
annual_salary = starting_annual_salary

while i <=36:
       
    best_int = (low_int+high_int)/2.0
    monthly_savings = (annual_salary/12)*(best_int/10000)
    current_savings += monthly_savings + current_savings*r/12
        
    if i!=0 and i%6==0:
        annual_salary += annual_salary*semi_annual_raise
        monthly_savings = (annual_salary/12)*(best_int/10000)
        
    if abs(down_payment - current_savings) <=100:
        break
    
    elif abs(down_payment - current_savings) >100 and current_savings < down_payment:
        low_int = best_int
        
    elif abs(down_payment - current_savings) >100 and current_savings < down_payment:
        high_int = best_int
       
    if low_int >= high_int:
        possible_to_pay_in_three_years = False
        break
    
    steps +=1
    i+=1

if possible_to_pay_in_three_years:
    #print('current_savings: {}'.format(current_savings))
    print('Best savings rate: {}'.format(best_int/10000))
    print('Steps in bisection search: {}'.format(steps))
else:
    print('It is not possible to pay the down payment in three years.')
    

# part c code by sturrion
# https://github.com/sturrion/MIT_OCW_6-0001-introduction-to-computer-science-and-programming-in-python-fall-2016/blob/master/ps1/ps1c.py

starting_salary = int(input("Enter the starting salary: "))
semi_annual_rise = 0.07
annual_return = 0.04
total_cost = 1000000
portion_down_payment = total_cost * 0.25
months = 36

min_rate = 0        # 0%
max_rate = 10000    # 100%

portion_saved = int((max_rate + min_rate) / 2)
steps = 0
found = False

while abs(min_rate - max_rate) > 1:
    steps += 1
    annual_salary = starting_salary
    monthly_saved = (annual_salary / 12.0) * (portion_saved / 10000)
    current_savings = 0.0

    for i in range(1, months + 1):
        monthly_return = current_savings * (annual_return / 12)
        current_savings += monthly_return + monthly_saved

        if abs(current_savings - portion_down_payment) < 100:
            min_rate = max_rate
            found = True
            break
        elif current_savings > portion_down_payment + 100:
            break
        
        if i % 6 == 0:
            annual_salary += annual_salary * semi_annual_rise
            monthly_saved = (annual_salary / 12.0) * (portion_saved / 10000)

    if current_savings < portion_down_payment - 100:
        min_rate = portion_saved
    elif current_savings > portion_down_payment + 100:
        max_rate = portion_saved
    
    portion_saved = int((max_rate + min_rate) / 2)
    
if found:
    print("Best savings rate:", portion_saved / 10000)
    print("Steps in bisection search", steps)
else:
    print("Is is not possible to pay the down payment in three years")

