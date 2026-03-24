import json
det={}
pas={}
print("Welcome to the Bank Account Management System")
def save_data():
    with open("bank_data.json", "w") as f:
        json.dump({"det": det, "pas": pas}, f)
def load_data():
    global det, pas
    try:
        with open("bank_data.json", "r") as f:
            data = json.load(f)
            det = data["det"]
            pas = data["pas"]
    except:
        det = {}
        pas = {}
load_data()

def create_account():
    usern=input("Enter the username:").strip()
    
    while True:
        if usern in det:
        
            print("This username is already in the database. Please Try again...")
            usern=input("Enter the username:")
        elif usern.isalnum()!=True:
            print("Username should be mixed in Alphabets and Number only")
            usern=input("Enter the username:")
        else:
            
            break
    passw=input("Enter the 8 digit password:").strip()
    while True:
        if passw.isalpha()!=True and passw.isdigit()!=True:
            print("Password should be mixed with alphabets and numbers only....")
            passw=input("Enter the 8 digit password:").strip()
        elif len(passw)==8:
            break
        else:
            print("Password digit should be 8")
            passw=input("Enter the 8 digit password:").strip()
            
    print("Succesfully created your account")
    
    while True:
        banbal=input("How much you deposit in your account:")
        if banbal.isdigit()==True:
            break
        else:
            print("Please Enter the Amount only........")
        
    det[usern]=int(banbal)
    pas[usern]=passw
    print("Your Account is created successfully and Deposited..............")
def login_a():
    usern=input("Enter the username:")
    f=False
    while True:
        if usern not in det:
            print("Your account is not in the database.......")
            usern=input("Enter the username:")
        else:
            break
    passw=input("Enter the password:")
    while True:
        if pas[usern]!=passw:
            print("Wrong Password........")
            passw=input("Enter the password:")
        else:
            f=True
            break
    if f==True:
        while True:
            print("-----------------------------------------------------------------------------------")
            print("1.Deposit.")
            print("2.Withdrawal.")
            print("3.Transfer Money.")
            print("4.Display your balance.")
            print("Type logout.")
            print("----------------------------------------------------------------------------------------")
            ch=input("Enter the choice:")
            if ch=='1':
                while True:
                    banbal=input("How much you deposit in your account:")
                    if banbal.isdigit()==True:
                        break
                    else:
                        print("Please Enter the Amount only........")
                det[usern]=det[usern]+int(banbal)
                print("Ok successfully deposited your amount in the account")
                print("----------------------------------------------------------------------------------------------")
            elif ch=='2':
                
                while True:
                    withd=int(input("Enter the amount for withdrawal:"))
                    if withd.isdigit()==True:
                        break
                    else:
                        print("Please Enter the Amount only........")
                while True:
                    if det[usern]>=withd:
                        det[usern]=det[usern]-withd
                        print("Please collect your money......")
                        break
                    else:
                        print("Insufficient Bank Balance!...............")
                        withd=int(input("Enter the amount for withdrawal:"))
            elif ch=='3':
                usernt=input("Enter the username of the receiving account:")
                while True:
                    if usernt not in det:
                        print("Invalid username....try again")
                        usernt=input("Enter the username of the receiving account:")
                    else:
                        break
                while True:
                    amm=(input("Enter the amount you transfer:"))  
                    if amm.isdigit()==True:
                        break
                    else:
                        print("Please Enter the Amount only........")    
                 
                while True:
                    if det[usern]>=int(amm):
                        det[usernt]=det[usernt]+int(amm)
                        det[usern]=det[usern]-int(amm)
                        print(f"Succesfully Transferred your amount to {usernt} account")
                        break
                    else:
                        print("Insufficient Bank Balance!.................")
                        amm=int(input("Enter the amount you transfer:"))
            elif ch=='4':
                print("Your Balance Amount")
                print(f"Username:{usern}\nBalance amount:{det[usern]}")
            
            elif ch.lower()=="logout":
                print("Thank you Logging out")
                return
            else:
                print("Invalid choice!.....")
    mainsri()
    
    
def mainsri():
    while True:
        print("------------------------------------------------------------------------")
        print("1.Register New Account")
        print("2.Login Account") 
        print("3.Exit")
        print("------------------------------------------------------------------------")
        try:
            ch1=input("Enter the choice [1,2,3]:")
        except KeyboardInterrupt:
            print("Sorry Program is interrupting ,we restarting the program......")
            mainsri()
        if ch1=='1':
            create_account()
        elif ch1=='2':
            login_a()
        elif ch1=='3':
            print("Thank you visit again.....................")
            save_data()
            return
            
            
            
        else:
            print("Invalid Option................")
if __name__ == "__main__":
    mainsri()
