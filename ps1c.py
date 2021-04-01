"""
In Part B, you had a chance to explore how both the percentage of your salary that you save each month 
and your annual raise affect how long it takes you to save for a down payment.  This is nice, but
suppose you want to set a particular goal, e.g. to be able to afford the down payment in three years.
How much should you save each month to achieve this?  In this problem, you are going to write a 
program to answer that question.  To simplify things, assume:
3
1. Your semi­annual raise is .07 (7%)
2. Your investments have an annual return of 0.04 (4%)  
3. The down payment is 0.25 (25%) of the cost of the house 
4. The cost of the house that you are saving for is $1M.
You are now going to try to find the best rate of savings to achieve a down payment on a $1M house in 
36 months. Since hitting this exactly is a challenge, we simply want your savings to be within $100 of 
the required down payment. 
In ps1c.py, write a program to calculate the best savings rate, as a function of your starting salary.
You should use bisection search to help you do this efficiently. You should keep track of the number of 
steps it takes your bisections search to finish. You should be able to reuse some of the code you wrote
for part B in this problem.  
Because we are searching for a value that is in principle a float, we are going to limit ourselves to two
decimals of accuracy (i.e., we may want to save at 7.04% ­­ or 0.0704 in decimal – but we are not 
going to worry about the difference between 7.041% and 7.039%).  This means we can search for an
integer between 0 and 10000 (using integer division), and then convert it to a decimal percentage
(using float division) to use when we are calculating the current_savings after 36 months. By using
this range, there are only a finite number of numbers that we are searching over, as opposed to the
infinite number of decimals between 0 and 1. This range will help prevent infinite loops. The reason we
use 0 to 10000 is to account for two additional decimal places in the range 0% to 100%. Your code
should print out a decimal (e.g. 0.0704 for 7.04%).
"""

import numpy as np

#Initializing all variables
portion_down_payment = 0.25
current_savings = 0
r = 0.04
monthly_salary = 0
months = 36
semi_annual_raise = 0.07
total_cost = 1000000
portion_saved = 5000
num_steps = 0
lower_bound = 0
upper_bound = 10000
steps = 0

#Getting User data
annual_salary = float(input("Please enter your annual salary: "))


#Performing conversions from annual values to month values: 
monthly_salary = annual_salary/12

#Bisection Search
while (not((current_savings > (total_cost*portion_down_payment - 100))&((current_savings < (total_cost*portion_down_payment + 100))))):

    current_savings = 0
    monthly_salary = annual_salary/12

    for x in range(36):
        current_savings += current_savings*r/12
        current_savings += portion_saved*monthly_salary/10000
        if x%5 == 0:
            monthly_salary = monthly_salary*(1 + semi_annual_raise)

    if(current_savings > (total_cost*portion_down_payment + 100)):
        upper_bound = portion_saved
        portion_saved = round((lower_bound + upper_bound)/2)
    if(current_savings < (total_cost*portion_down_payment - 100)):
        lower_bound = portion_saved
        portion_saved = round((lower_bound + upper_bound)/2)

    #print("Upper Bound: ", upper_bound, "Lower Bound: ", lower_bound, "   Portion Saved: ", portion_saved, "Savings: ", current_savings)
    steps += 1 


#Prints out the number of months: 
portion_saved = round(portion_saved/10000, 4)

print("Best Rate: ", portion_saved)
print("Steps in Bisection Search: ", steps)