import os 
import csv

Total_months = 0
Profit_losses = 0
Average_change = 0
g_increase = 0
y_increase = ""
g_decrease = 0
y_decrease = 0
cval = 0
pval = 0
count = 1
c_yer =1
# Path to collect data from the Resources folder
budget_dataCSV = os.path.join("..","PyBank","budget_data.csv") 
# Read in the CSV file
with open(budget_dataCSV, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    # Read the header row first (skip this part if there is no header)
    csv_header = next(csvreader)
    #print(f"Header: {csv_header}")
    #csv_first = next(csvreader)
    # Read through each row of data after the header
    for row in csvreader:

        if  count == 1:
            year = row[0]
            g_increase = int(row[1])
            g_decrease = int(row[1])
            count = 99

        if  year != row[0]:
            c_yer = c_yer + 1
            year = row[0]

        cval = int(row[1])

        if  g_increase < cval:
            g_increase = cval
            gc_inc = cval - pval
            y_increase = row[0]

        elif g_decrease > cval:
            g_decrease = cval
            gc_dec = cval - pval
            y_decrease = row[0] 

    #total months    
        Total_months = Total_months + int(1)

    # The net total amount of "Profit/Losses" over the entire period
        Profit_losses = Profit_losses + int(row[1])
    # Average Change analysis
        csv_last = int(row[1])
        if Total_months == 1:
            csv_first = csv_last

    Average_change = ((csv_last - csv_first)/(Total_months-1))

# Print he analysis in asked format
    print("Fiancial Analysis ")
    print("-----------------------------------------------------------------------")
    print (f"Total Months: {str(Total_months)}")
    print("Total: $"+str(Profit_losses))
    print("Average Change: $"+str(Average_change))
    print("Greatest Increase in Profits: "+ str(y_increase) + " $ " + str(g_increase))
    print("Greatest Decrease in Profits: "+ str(y_decrease) + " $ " + str(g_decrease))

    #Create .txt file and exports the code
    export_file = os.path.join("..","PyBank","Result_Output.txt")
    with   open (export_file,'w',newline="") as textfile:
            textfile.write("Financial Analysis" + os.linesep)
            textfile.write("----------------------------------------------------------" + os.linesep)
            textfile.write("Total Months: " + str(Total_months) + os.linesep)
            textfile.write("Total Revenue: $" + str(Profit_losses) + os.linesep)
            textfile.write("Average Change: $" + str(Average_change) + os.linesep)
            textfile.write("Greatest Increase in Profits: " +str(y_increase) + "(" + "$" + str(g_increase) +")" + os.linesep)
            textfile.write("Greatest Decrease in Profits: " +str(y_decrease) + "(" + "$" + str(g_decrease) +")" + os.linesep)
