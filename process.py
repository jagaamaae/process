# create a file from um-server-1.txt to access it

log_file = open("um-server-01.txt")

#The function definition tells you to print sales info for Monday
def sales_reports(log_file):
# for loop tells you to get each line in log_file
    for line in log_file:
        #remove extra white space to the right
        line = line.rstrip()
        #ge the first three char s in line 
        day = line[0:3]
        #change Tue to Mon
        if day == "Mon":
            print(line)

sales_reports(log_file)
