import sys
from termcolor import colored
import pickle



#Open list
def open_list():
    save = pickle.load(open("list.dat","rb"))
    show_list()


#Save list
def save_list():
    pickle.dump(show_list(),open("list.dat","wb"))
    options()


#Calculate salary after taxes and after necessary bills
def calculate():
    global taxer
    taxer = tax / 100
    q = 1.00 - taxer
    global percent
    percent = salary * q
    global after
    after = percent - rent - phone
    save_list()



#Create list to show finances
def show_list():
    x = salary
    y = percent
    z = after

    print("| salary: ", x, "            |")
    print("| salary(After tax): ", y, " |")
    print("| Funds after bills: ", z, " |")









#Ask user's salary and tax percentile.
def create_f():
    up = True
    while up:
        s1 = input("Enter your Salary: ")
        if s1.isdigit():
            global salary
            salary = float(s1)
            break
        else:
            print("Given value was not a number! Try Again.")
    while True:
        s2 = input("Enter Tax percentile: ")
        if s2.isdigit():
            global tax
            tax = float(s2)
            expenses()
            break
        else:
            print("Given value was not a number! Try Again.")


#Ask user's expenses
def expenses():
    yep = True
    while yep:
        s3 = input("Specify your expenses. What is your rent?: ")
        if s3.isdigit():
            global rent
            rent = int(s3)
            break
        else:
            print("Wrong value! Try Again!")
    while True:
        s4=input("What is your phone and internet provider fees per month?: ")
        if s4.isdigit():
            global phone
            phone = float(s4)
            calculate()
            break
        else:
            print("Wrong value! Try Again!")










#Options for user
def options():
    op = True
    while op:
        info = input(colored("What you want to do?\nCreate finance sheet or edit existing one = 1, Show finance sheet = 2, Exit Program = 3: ",'yellow'))
        if info == '1':
            create_f()
            break
        elif info == '2':
            open_list()
        elif info == '3':
            sys.exit()
        else:
            print("Wrong command!")



options()
