#######################################################################################################################################################
# 
# Name:
# SID:
# Exam Date:
# Module:
# Github link for this assignment:  
#
#######################################################################################################################################################
# Instruction 1. Read each question carefully and complete the scripts as instructed.

# Instruction 2. Only ethical and minimal use of AI is allowed. You may use AI to get advice on tool usage or language syntax, 
#                but not to generate code. Clearly indicate how and where you used AI.

# Instruction 3. Include comments explaining the logic of your code and the output as a comment below the code.

# Instruction 4. Commit to Git and upload to ELE once you finish.

#######################################################################################################################################################

# Question 1 - Loops and Lists
# You are given a list of numbers representing weekly sales in units.
weekly_sales = [120, 85, 100, 90, 110, 95, 130]

# Write a for loop that iterates through the list and prints whether each week's sales were above or below the average sales for the period.
# Calculate and print the average sales.
average_sales = sum(weekly_sales)/ len(weekly_sales)
for item in weekly_sales:
    if item > average_sales:
        print(f'{item} is higher than average')
    else:
        print(f'{item} is lower than average')
print(average_sales)
#######################################################################################################################################################

# Question 2 - String Manipulation
# A customer feedback string is provided:
customer_feedback = """The product was good but could be improved. I especially appreciated the customer support and fast response times."""

# Find the first and last occurrence of the words 'good' and 'improved' in the feedback using string methods.
# Store each position in a list as a tuple (start, end) for both words and print the list.
location1 = (customer_feedback.find('good'),customer_feedback.find('good')+len('good'))
location1 = (customer_feedback.find('improved'),customer_feedback.find('improved')+len('improved'))
location = [location1,location2]
print(location)
#######################################################################################################################################################

# Question 3 - Functions for Business Metrics
# Define functions to calculate the following metrics, and call each function with sample values (use your student ID digits for customization).

# 1. Net Profit Margin: Calculate as (Net Profit / Revenue) * 100.
# 2. Customer Acquisition Cost (CAC): Calculate as (Total Marketing Cost / New Customers Acquired).
# 3. Net Promoter Score (NPS): Calculate as (Promoters - Detractors) / Total Respondents * 100.
# 4. Return on Investment (ROI): Calculate as (Net Gain from Investment / Investment Cost) * 100.
def Net_profit_margin (net_profit,revenue):
    return (net_profit/revenue)*100

def Net_promoter_score (promoters,detractors,total_respondents):
    return (promoters- detractors)/total_respondents
print(Net_profit_margin(1,2))
print(Net_profit_margin(1,2,3))
#######################################################################################################################################################

# Question 4 - Data Analysis with Pandas
# Using a dictionary sales_data, create a DataFrame from this dictionary, and display the DataFrame.
# Write code to calculate and print the cumulative monthly sales up to each month.
import pandas as pd

sales_data = {'Month': ['Jan', 'Feb', 'Mar', 'Apr', 'May'], 'Sales': [200, 220, 210, 240, 250]}
df = pd.DataFrame(sales_data)
df['cumulative_sales']= df['Sales'].cumsum()
print(df)
#######################################################################################################################################################

# Question 5 - Linear Regression for Forecasting
# Using the dataset below, create a linear regression model to predict the demand for given prices.
# Predict the demand if the company sets the price at £26. Show a scatter plot of the data points and plot the regression line.

# Price (£): 15, 18, 20, 22, 25, 27, 30
# Demand (Units): 200, 180, 170, 160, 150, 140, 130
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression    #总是犯错
price = np.array([15, 18, 20, 22, 25, 27, 30]).reshape(-1,1)
demand = np.array ([200, 180, 170, 160, 150, 140, 130])

model = LinearRegression()
model.fit(price,demand)

predict_demand = model.predict(np.array([[26]]))
print(f'predicted demand is {predict_demand}')
plt.scatter(price,demand,color='red')
plt.plot(price,model.predict(price),color='blue')  #不理解model.predict(price)
plt.xlabel('Price')
plt.ylabel('Demand')
plt.title('price and demand')
plt.show()
#######################################################################################################################################################

# Question 6 - Error Handling
# You are given a dictionary of prices for different products.
prices = {'A': 50, 'B': 75, 'C': 'unknown', 'D': 30}

# Write a function to calculate the total price of all items, handling any non-numeric values by skipping them.
# Include error handling in your function and explain where and why it’s needed.
def calculate_price (prices):
    total_price = 0
    for name,number in prices.items(): #items不知道是做什么的，总忘记
        try:
            total_price = float(number)+ total_price
        except ValueError:
            print(f'{name} is unknown')
    return total_price
print(calculate_price(prices))



#######################################################################################################################################################

# Question 7 - Plotting and Visualization
# Generate 50 random numbers between 1 and 500, then:
# Plot a histogram to visualize the distribution of these numbers.
# Add appropriate labels for the x-axis and y-axis, and include a title for the histogram.

import matplotlib.pyplot as plt
import random

random_number = [random.randint(1,500) for item in range(50)]

plt.hist(random_number,bins= 10, edgecolor= 'black')
plt.xlabel('value')
plt.ylabel('number')
plt.title('histogram')
plt.show()

#######################################################################################################################################################

# Question 8 - List Comprehensions
# Given a list of integers representing order quantities.
quantities = [5, 12, 9, 15, 7, 10]

# Use a list comprehension to create a new list that doubles each quantity that is 10 or more.
# Print the original and the new lists.
new_quantities = [a*2 for a in quantities if a >= 10]
print(new_quantities)
#######################################################################################################################################################

# Question 9 - Dictionary Manipulation
# Using the dictionary below, filter out the products with a rating of less than 4 and create a new dictionary with the remaining products.
ratings = {'product_A': 4, 'product_B': 5, 'product_C': 3, 'product_D': 2, 'product_E': 5}
new_ratings = {name:number for name,number in ratings.items() if number >=4 }
print(new_ratings)
#######################################################################################################################################################

# Question 10 - Debugging and Correcting Code
# The following code intends to calculate the average of a list of numbers, but it contains errors:
values = [10, 20, 30, 40, 50]
total = 0
for i in values:
    total = total + i
average = total / len(values)
print(f'The average is  {average}')

# Identify and correct the errors in the code.
# Comment on each error and explain your fixes.

################################################