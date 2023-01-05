import os
import csv

file = os.path.join('budget_data.csv')
with open('budget_data.csv','r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    header = next(csvreader)
   

    months = []
    profit = []
    profit_change = []
    
                      
   
    for row in csvreader:
        months.append(row[0])
        profit.append(int(row[1]))
    for i in range(len(profit)-1):
        profit_change.append(profit[i+1]-profit[i])
                      

increase = max(profit_change)
decrease = min(profit_change)


month_increase = profit_change.index(max(profit_change))+1
month_decrease = profit_change.index(min(profit_change))+1


print("Financial Analysis")
print("------------------------")
print(f"Total Months:{len(months)}")
print(f"Total: ${sum(profit)}")
print(f"Average Change: {round(sum(profit_change)/len(profit_change),2)}")
print(f"Greatest Increase in Profits: {months[month_increase]} (${(str(increase))})")
print(f"Greatest Decrease in Profits: {months[month_decrease]} (${(str(decrease))})")      
