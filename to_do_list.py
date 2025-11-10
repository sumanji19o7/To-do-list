import pickle
import time 
import random
from tabulate import tabulate

# the data type is a list , a list will be a record for only one task which will be a string ,
# there are going to be multiple lists is the data file


def createfile():       #function to create a new data file or deleting all the data if already exists
    f=open("todo.dat","wb")
    sno=1
    
    number=int(input("enter number of records you wish to enter: "))        #number of enteries input from the user
    for i in range(number):
        time=int(input("enter the hour you want to do the task in(0-24)"))
        day=int(input("enter the date of the task: "))
        month=int(input("enter the month of task completing: "))
        year=int(input("enter year: "))
        completed=False
        task=input("enter task you want to achieve: ")

        if time <= 24 and time >= 1 and day <=31 and day >= 31 and month >=1 and month <=12 and year >= 0:
            if time > 24 or time < 1:
                print("time out of bound !".upper())
            if day > 31 or day < 1:
                print("date is out of bounds, please enter with 1-31".upper())
            if month > 12 or month < 1:
                print("please enter months 1-12".upper())
            if len(task) > 10000:
                print("TASK LENGTH TOO LONG PLEASE ENTER TASK WITHIN THOUSAND CHARACTERS")
            if task.strip() == "":
                raise ValueError("Input cannot be empty or just spaces!")
            
        else:
            rec=[sno,time,day,month,year,completed,task]
            sno+=1
            pickle.dump(rec,f)

def displaying():   #function to display all the user data
    records=[]
    f=open("todo.dat","rb")
    headers=['S.No','Hour','Day','Month','Year','completed','Task']
    try:
        while True:
            s=pickle.load(f)
            records.append(s)
            

            
    
    except EOFError:
        print(tabulate(records,headers=headers,tablefmt="fancy_grid"))
        print()
        print("all the tasks have been displayed".upper())
        print()
        f.close()


def searching():    #function to search for a paticular record
    headers=['S.No','Hour','Day','Month','Year','completed','Task']
    f=open("todo.dat","rb")
    records=[]
    searchwith=input("enter what you want to search with(sno) for serieal number,(date) for searching with date")
    if searchwith.lower() == 'sno':
        sno=int(input("enter serial number you want searched: "))
        found=False
        headers=['S.No','Hour','Day','Month','Year','completed','Task']
        records=[]
        try:
            while True:
                s=pickle.load(f)
                if s[0]== sno:
                    records.append(s)
                    print(tabulate(records,headers=headers,tablefmt="fancy_grid"))
                    found=True
                

                    
        except EOFError:
            if not found:
                print(f"no record with serial number {sno}")  
            f.close()
    
    elif searchwith.lower() == 'date':
        day=int(input('enter date(day 1-31): '))
        month=int(input('enter month(1-12): '))
        year=int(input('enter year (greater than 0000)'))

        try:
            while True:
                s=pickle.load(f)
                if s[2]==day and s[3]==month and s[4]==year:    
                    records.append(s)

        except EOFError:
            f.close()
            print(tabulate(records,headers=headers,tablefmt="fancy_grid"))



def updating():
    f=open("todo.dat","rb")
    sno=int(input("enter serial number of record you want to update: "))
    
    records=[]
    new_hour=input("enter new time(0-24): ")
    new_day=input("enter new day (1-31): ")
    new_month=input("enter new month(1-12): ")
    new_year=input("enter new year(greater than 0000): ")
    new_task_status=input("yes or no if completed or not: ")
    new_task=input("enter updated task statement less than 10000 chars: ")

    if new_task_status.lower()=="yes":
        new_task_status=True
    elif new_task_status.lower()=="no":
        new_task_status=False

    else:
        print("Error")
        updating()

    
    
    try:
        while True:
            s=pickle.load(f)
            old_hour=s[1]
            old_day=s[2]
            old_month=s[3]
            old_year=s[4]
            old_task_status=s[5]
            old_task=s[6]

            if s[0] != sno:
                records.append(s)
            elif s[0] == sno:
                if new_hour.strip()=="":
                    s[1]=old_hour
                else:
                    s[1]=int(new_hour)

                if new_day.strip()=="":
                    s[2]==old_day
                else:
                    s[2]=int(new_day)
                if new_month.strip=="":
                    s[3]=old_month
                else:
                    s[3]=int(new_month)
                if new_year.strip=="":
                    s[4]=old_year
                else:
                    s[5]=new_task_status
                if new_task.strip=="":
                    s[6]=old_task
                else:
                    s[6]=new_task

                records.append(s)
    except EOFError:
        f.close()

    f=open("todo.dat","wb")
    for i in records:
        pickle.dump(i,f)

    f.close()


def deleting():
    displaying()
    records=[]
    f=open("todo.dat","rb")
    sno=int(input("enter serial number of record you want to delelte"))
    try:
        while True:
            s=pickle.load(f)
            if s[0] != sno:
                records.append(s)
            else:
                pass

    except EOFError:
        f.close()
        print("deleting record...")
        time.sleep(0.4)
        print()

    f=open("todo.dat","wb")
    for i in records:
        pickle.dump(i,f)

    print("record deleted successfully")





import pickle

def adding():
    # Count existing records using direct file open/close
    f = open("todo.dat", "rb")
    num = 0
    try:
        while True:
            pickle.load(f)
            num += 1
    except (EOFError, FileNotFoundError):
        pass
    f.close()

    sno = num

    try:
        time = int(input("Enter the hour you want to do the task in (1-24): "))
        day = int(input("Enter the date of the task (1-31): "))
        month = int(input("Enter the month of task completing (1-12): "))
        year = int(input("Enter year (>= 0): "))
        completed = False
        task = input("Enter task you want to achieve: ").strip()

        errors = []
        if not (1 <= time <= 24):
            errors.append("Time out of bound! (1-24)")
        if not (1 <= day <= 31):
            errors.append("Date is out of bounds! (1-31)")
        if not (1 <= month <= 12):
            errors.append("Month out of bounds! (1-12)")
        if year < 0:
            errors.append("Year must be >= 0")
        if len(task) > 10000:
            errors.append("Task length too long (max 10000 chars)")
        if task == "":
            errors.append("Input cannot be empty or just spaces!")

        if errors:
            for e in errors:
                print(e.upper())
            return

        rec = [sno, time, day, month, year, completed, task]
        f = open("todo.dat", "ab")
        pickle.dump(rec, f)
        f.close()
        print(f"Record added successfully with serial number {sno}.")

    except ValueError:
        print("Invalid numeric input. Please enter valid numbers.")

def menu():   

    while True:
        print()
        time.sleep(0.5)

        print("Enter (new) to create a new file")
        print()

        time.sleep(0.5)

        print("Enter (read) to display all the tasks or records")
        print()

        time.sleep(0.5)

        print("Enter (search) to search for a record using serial number or date")
        print()

        time.sleep(0.5)

        print("Enter (update) to update a record")
        print()

        time.sleep(0.5)

        print("enter (delete) to delete a record")
        print()

        time.sleep(0.5)

        print("Enter (add) to append a record at the end")
        print()    

        time.sleep(0.5)

        print("Enter (quit) to exit the programme")
        print()

        print("_"*50)
        print()

        choice=input("PLEASE ENTER YOUR CHOICE OF FUNCTION TO PROCEED:")

        if choice.lower()=="new":
            createfile()
        elif choice.lower()=="read":
            displaying()
        elif choice.lower()=="search":
            searching()
        elif choice.lower()=="update":
            updating()
        elif choice.lower()=="delete":
            deleting()
        elif choice.lower()=="add":
            adding()
        elif choice.lower()=="quit":
            print("PROGRAMME ENDED")
            break
        else:
            print("ENTER VALID CHOICE!!")
            menu()

menu()






            

