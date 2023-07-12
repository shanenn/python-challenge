'''This script analyzes several metrics of budget_data.csv and prints and returns a txt file of the results'''
# import packages
import csv
import os

# read through csv
csv_path = os.path.join("Resources","budget_data.csv")
with open(csv_path,"r",) as file:
    csv_reader = csv.reader(file,delimiter=',')
    headers = next(csv_reader)
    num_month = 0                                       # initialize all variables
    total = 0
    profits = 0
    first = True
    large = 0
    small = 0
    for row in csv_reader:
        num_month += 1
        total += int(row[1])
        if first:                                       # check if first entry
            start = int(row[1])
            first = False
        else:
            prof = int(row[1])-start                    # if not first entry, subtract previous to find change
            start = int(row[1])
            if prof > large:                            # check for if greatest or smallest change
                large = prof
                largedate = row[0]
            if prof < small:
                small = prof
                smalldate = row[0]
            profits+=prof
ana = [num_month,total,profits/(num_month-1),[smalldate,small],[largedate,large]]   # list of results for easy reference

# write to txt and print results
txt_path = os.path.join("analysis","results.txt")
with open (txt_path, "w") as file:
    file.write("Financial Analysis\n")
    print("Financial Analysis\n")
    file.write("-"*28)
    print("-"*28)
    file.write(f"\nTotal Months: {ana[0]}")
    print(f"\nTotal Months: {ana[0]}")
    file.write(f"\nTotal: ${ana[1]}")
    print(f"\nTotal: ${ana[1]}")
    file.write(f"\nAverage Change: ${ana[2]:.2f}")
    print(f"\nAverage Change: ${ana[2]:.2f}")
    file.write(f"\nGreatest Increase in Profits: {ana[4][0]} (${ana[4][1]})")
    print(f"\nGreatest Increase in Profits: {ana[4][0]} (${ana[4][1]})")
    file.write(f"\nGreatest Decrease in Profits: {ana[3][0]} (${ana[3][1]})")
    print(f"\nGreatest Decrease in Profits: {ana[3][0]} (${ana[3][1]})")
    