import os
import csv
print("Financial Analysis")
print("---------------------------")
month = []
val = []
change_li = []
csvpath = os.path.join('Resources', 'budget_data.csv')
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvfile)

    for col in csvreader:
        val.append(int(col[1]))
        month.append(col[0])
        # print(val)
#    for row in csvreader:
#       print(row)

    numberofrows = len(val)
    print(f"Total months: {numberofrows}")

    totalvalue = sum(val)
    print(f"Total value: {totalvalue}")

    # print(val)

    y = 0
    while y < numberofrows - 1:
        change = val[y+1]-val[y]
        change_li.append(change)
        y += 1

    # print(change_li)

    avg_change = sum(change_li)/numberofrows
    decrease_month = month[change_li.index(min(change_li))+1]
    increase_month = month[change_li.index(max(change_li))+1]
    print(f"Average Change: {avg_change}")
    print(f"Greatest Increase in Profits: {increase_month} ({max(change_li)})")
    print(f"Greatest Decrease in Profits: {decrease_month} ({min(change_li)})")
