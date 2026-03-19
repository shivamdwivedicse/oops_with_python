import json
import random 
import string 
from pathlib import Path

class Bank:
    database = "data.json"
    data =[]
    try:
        if Path(database).exists():
            with open(database) as fs:
                data = json.load(fs)
        else:
            print("No such file exists.")
    except Exception as err:
        print(f"An exception occured as {err}")

    @staticmethod
    def __update():
        with open(Bank.database , 'w') as fs:
            fs.write(json.dumps(Bank.data, indent=4))

    @classmethod
    def __accountgenrete(cls):
        alpha = random.choices(string.ascii_letters,k=3)
        num = random.choices(string.digits , k=3)
        spchar = random.choices("!@#$%^&*" , k=1)
        id = alpha+num+spchar
        random.shuffle(id)
        return "".join(id)

    def Createaccount(self):
        info = {
            "Name" : input("Tell your name :-"),
            "Age" : int(input("Tell your age:-")), 
            "Email" : input("Tell your Email :-"), 
            "Pin" : int(input("Make a 4 pin number:-")),
            "Account Number" : Bank.__accountgenrete(),
            "Balance" : 0
        }

        if info['Age']<18 or len(str(info['Pin']))!=4:
            print("Sorry! You cannot make your account.")
        else:
            print("Account has been created succesfully.")
            for i in info:
                print(f"{i} :{info[i]}")
            print("Please Note down your ACCOUNT NUMBER.")

            Bank.data.append(info)
            Bank.__update()

    def depositemoney(self):
        accnumber = input("Please tell your account number :")
        pin = int(input("Tell your pin please :"))
        userdata = [i for i in Bank.data if i["Account Number"] == accnumber and i["Pin"] == pin]

        if not userdata:
            print("Sorry! No data found.")
        else:
            amount = int(input("Enter deposit amount :-"))
            if amount >10000 or amount<0:
                print("Sorry! The amount is too much deposite below 10k")
            else:
                userdata[0]['Balance'] += amount
                Bank.__update()
                print("Amount deposited succesfully.")

    def withdrawmoney(self):
        accnumber = input("Please tell your account number :")
        pin = int(input("Tell your pin please :"))
        userdata = [i for i in Bank.data if i["Account Number"] == accnumber and i["Pin"] == pin]

        if not userdata:
            print("Sorry! No data found.")
        else:
            amount = int(input("Enter withdraw amount :-"))
            if userdata[0]['Balance'] < amount:
                print("Sorry! You don't have that much money.")
            else:
                userdata[0]['Balance'] -= amount
                Bank.__update()
                print("Amount withdrawn succesfully.")

    def showdetails(self):
        accnumber = input("Please tell your account number :")
        pin = int(input("Tell your pin please :"))
        userdata = [i for i in Bank.data if i["Account Number"] == accnumber and i["Pin"] == pin]

        if not userdata:
            print("No user found!")
        else:
            print("Your information are \n\n")
            for i in userdata[0]:
                print(f"{i} : {userdata[0][i]}")
    
    def updatedetails(self):
        accnumber = input("Please tell your account number :")
        pin = int(input("Tell your pin please :"))
        userdata = [i for i in Bank.data if i["Account Number"] == accnumber and i["Pin"] == pin]

        if not userdata:
            print("No such user found!")
        else:
            print("You cannot change the AGE , ACCOUNT NUMBER , BALANCE")
            print("Fill the details for chnage or leave it empty if NO change.")
            newdata ={
                "Name": input("Enter new name OR press Enter:"),
                "Email": input("Enter your new Email OR press Enter to skip:"),
                "Pin": input("Enter new pin OR press Enter to skip")   
            }

            if newdata['Name']== "":
                newdata['Name'] = userdata[0]['Name']
            if newdata['Email']== "":
                newdata['Email'] = userdata[0]['Email']
            if newdata['Pin']== "":
                newdata['Pin'] = userdata[0]['Pin']
            else:
                newdata['Pin'] = int(newdata['Pin'])
            
            newdata['Age'] = userdata[0]['Age']
            newdata['Account Number'] = userdata[0]['Account Number']
            newdata['Balance'] = userdata[0]['Balance']

            for i in newdata:
                if newdata[i] == userdata[0][i]:
                    continue
                else:
                    userdata[0][i] = newdata[i]

            Bank.__update()
            print("Updated successfully.")

    def delete(self):
        accnumber = input("Please tell your account number :")
        pin = int(input("Tell your pin please :"))
        userdata = [i for i in Bank.data if i["Account Number"] == accnumber and i["Pin"] == pin]

        if not userdata:
            print("Sorry No data found!")
        else:
            check = input("Press y to delete or press n:")
            if check == "n" or check =="N":
                print("Bypassed")
            else:
                index = Bank.data.index(userdata[0])
                Bank.data.pop(index)
                print("Account Deleted Successfully.")
                Bank.__update()


user = Bank()
print("Press 1 for creating an account")
print("Press 2 for deposit money")
print("Press 3 for withdrawing money")
print("Press 4 for details")
print("Press 5 for updating details")
print("Press 6 for deleting your account")

a = int(input("Tell your response :-"))

if a==1:
    user.Createaccount()

if a ==2:
    user.depositemoney()

if a ==3:
    user.withdrawmoney()

if a ==4:
    user.showdetails()

if a==5:
    user.updatedetails()

if a ==6:
    user.delete()

