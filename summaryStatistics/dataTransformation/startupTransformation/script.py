import codecademylib3
from sklearn import preprocessing
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np

# load in financial data
financial_data = pd.read_csv('financial_data.csv')

# code goes here
print(financial_data.head())

month = financial_data['Month']
revenue = financial_data['Revenue']
expenses = financial_data['Expenses']
#plot graph of revenue by month
plt.plot(month,revenue)
plt.xlabel('Month')
plt.ylabel('Amount ($)')
plt.title('Revenue')
plt.show()
#plot grid of expenses by month
plt.clf()
plt.plot(month,expenses)
plt.xlabel('Month')
plt.ylabel('Amount ($)')
plt.title('Expenses')
plt.show()

# build expenses data frame
expense_overview = pd.read_csv('expenses.csv')
print(expense_overview.head(7))
expense_categories = expense_overview['Expense']
proportions = expense_overview['Proportion']
# create pie chart for expenses
plt.clf()
plt.pie(proportions, labels = expense_categories)
plt.title('Expenses')
plt.axis('Equal')
plt.tight_layout()
plt.show()

#new pie chart to make all proportions under 0.05 in other category
expense_categories = ['Salaries', 'Advertising','Office Rent','Other']
proportions = [0.62,0.15,0.15,0.08]
plt.clf()
plt.pie(proportions, labels = expense_categories)
plt.title('Expenses')
plt.axis('Equal')
plt.tight_layout()
plt.show()

expense_cut = 'Salaries'

#Employee Productivity

#import employee data

employees = pd.read_csv('employees.csv')
print(employees.head())
#find the 100 least productive employees to cut
sorted_productivity = employees.sort_values(by=['Productivity'])
print(sorted_productivity)
employees_cut = sorted_productivity.head(100)
transformation ='standardization'

commute_times = employees['Commute Time']
commute_times_log = np.log(commute_times)
print(commute_times.describe())

#commute time histogram
plt.clf()
plt.hist(commute_times)
plt.title('Commute Times')
plt.show()

#log of commute times histogram
plt.clf()
plt.hist(commute_times_log)
plt.title('log of Commute Times')
plt.show()

