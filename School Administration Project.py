import csv

def add_into_file(info_list):
    with open("student_info.csv", "a", newline='') as csv_file:
        writer= csv.writer(csv_file)
        
        if csv_file.tell()==0:
            writer.writerow(["Name", "Age", "Contact", "Email"])
        
        writer.writerow(info_list)

while(1):
    entry= input("Please enter th edetails int he format of Name age contact_no. email_id")
    mylist=[]
    mylist= entry.split()
    add_into_file(mylist)
    ask= input("Do you want to add another entry , Press 1 for yes and 0 for no")
    if(ask=='0'):
        break
