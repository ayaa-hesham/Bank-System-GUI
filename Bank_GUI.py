from tkinter import *

########List Of Users(Nested dictionaries)##############
Users = {
    'user1' : { 'ID' : "215321701332",
                'Name' :"Ahmed Abdelrazek Mohamed",
                'Password' : "1783",
                'Balance' :  3500166},
    
    'user2' : { 'ID' : "203659302214",
                'Name' :"Salma Mohamed Foaad",
                'Password' : "1390",
                'Balance' :  520001},
    
    'user3' : { 'ID' : "126355700193",
                'Name' :"Adel Khaled Abdelrahman",
                'Password' : "1214",
                'Balance' :  111000},
    
    'user4' : { 'ID' : "123456789",
                'Name' : "Aya Hesham Ahmed",
                'Password' : "1234",
                'Balance' : 25000}
} 

##to count no of unscusseful times of pw entered
global WrongPwCount
WrongPwCount = 0

######### FUNCTIONS ###########

###Loged in menu###
def logedIn():
    ## to save id and pw
    ID = accNum.get()
    pw = pswrd.get()
    
    global WrongPwCount
    global logedInUser
    
    global MenuSc
    MenuSc= Toplevel(MainWindow)
    if ID == Users['user1']['ID'] or ID == Users['user2']['ID'] or ID == Users['user3']['ID'] or ID == Users['user4']['ID'] :
        if pw == Users['user1']['Password'] and ID == Users['user1']['ID']:
            ## to save user
            
            logedInUser = 'user1'
            
            MenuSc.geometry("300x170")
            
            Label(MenuSc,text="Welcome Back" , font = 12).pack(pady=20)
            
            b1 = Button(MenuSc,text="Cash Withdraw",command=CashWithdraw).place(x=50,y=60)
            b2 = Button(MenuSc,text="Balance Inquiry",command=BalanceInquiry).place(x=150,y=60)
            b3 = Button(MenuSc,text="Password Change",command=PasswordChange).place(x=50,y=90)
            b4 = Button(MenuSc,text="Fawry Service",command=FawryService).place(x=160,y=90)
            b5 = Button(MenuSc,text="Exit",command=Exit).place(x=130,y=120)
            
        elif pw == Users['user2']['Password'] and ID == Users['user2']['ID']:
            ## to save user
            logedInUser = 'user2'
            
            MenuSc.geometry("300x170")
            
            Label(MenuSc,text="Welcome Back" , font = 12).pack(pady=20)
            
            b1 = Button(MenuSc,text="Cash Withdraw",command=CashWithdraw).place(x=50,y=60)
            b2 = Button(MenuSc,text="Balance Inquiry",command=BalanceInquiry).place(x=150,y=60)
            b3 = Button(MenuSc,text="Password Change",command=PasswordChange).place(x=50,y=90)
            b4 = Button(MenuSc,text="Fawry Service",command=FawryService).place(x=160,y=90)
            b5 = Button(MenuSc,text="Exit",command=Exit).place(x=130,y=120)
            
        elif pw == Users['user3']['Password'] and ID == Users['user3']['ID']:
            ## to save user
            logedInUser = 'user3'
            
            MenuSc.geometry("300x170")
            
            Label(MenuSc,text="Welcome Back" , font = 12).pack(pady=20)
            
            b1 = Button(MenuSc,text="Cash Withdraw",command=CashWithdraw).place(x=50,y=60)
            b2 = Button(MenuSc,text="Balance Inquiry",command=BalanceInquiry).place(x=150,y=60)
            b3 = Button(MenuSc,text="Password Change",command=PasswordChange).place(x=50,y=90)
            b4 = Button(MenuSc,text="Fawry Service",command=FawryService).place(x=160,y=90)
            b5 = Button(MenuSc,text="Exit",command=Exit).place(x=130,y=120)
            
        elif pw == Users['user4']['Password'] and ID == Users['user4']['ID']:
            ## to save user
            logedInUser = 'user4'
            
            MenuSc.geometry("300x170")
            
            Label(MenuSc,text="Welcome Back" , font = 12).pack(pady=20)
            
            b1 = Button(MenuSc,text="Cash Withdraw",command=CashWithdraw).place(x=50,y=60)
            b2 = Button(MenuSc,text="Balance Inquiry",command=BalanceInquiry).place(x=150,y=60)
            b3 = Button(MenuSc,text="Password Change",command=PasswordChange).place(x=50,y=90)
            b4 = Button(MenuSc,text="Fawry Service",command=FawryService).place(x=160,y=90)
            b5 = Button(MenuSc,text="Exit",command=Exit).place(x=130,y=120)
            
        elif (WrongPwCount<3):
            MenuSc.geometry("200x200")
            Label(MenuSc,text="Wrong Password" , font = 12).pack(pady=20)
            Label(MenuSc,text="Reenter Password" , font = 12).pack(pady=20)
            Button(MenuSc,text="Ok",command=Close).pack(pady=20)
            
            del pw  #del command to delete var
            WrongPwCount += 1
            
        elif(WrongPwCount==3):
            MenuSc.geometry("250x150")
            Label(MenuSc,text="Account is Locked" , font = 12).pack(pady=20)
            Label(MenuSc,text="Please Go To The Branch" , font = 12).pack(pady=20)
            
    else:
        MenuSc.geometry("200x75")
        Label(MenuSc,text="User Doesn't Exist" , font = 12).pack(pady=20)
        Button(MenuSc,text="Ok",command=Close).pack(pady=20)

### Func To Close MenuSc Loged in menu ###
def Close():
    MenuSc.destroy()

### Cash WithDraw Menu ###
def CashWithdraw():
    global cash 
    cash = IntVar()
    
    MenuSc.destroy()
    
    global WithdrawSc
    WithdrawSc=Toplevel(MainWindow)
    WithdrawSc.geometry("450x150")
    Label(WithdrawSc ,text="Please Enter The Desired Amount To Withdraw" , font = 12).pack(pady=20)
    Entry(WithdrawSc ,textvariable=cash).pack()
    Button(WithdrawSc,text="Press To Confirm",command=ATM_Actuator_Out).pack(pady=20)


#### Balance Inquiry Menu ###
def BalanceInquiry():
    MenuSc.destroy()
    global BalanceSc
    BalanceSc=Toplevel(MainWindow)
    Label(BalanceSc , text= Users[logedInUser]['Name'] , font = 12).pack(pady=20)
    Label(BalanceSc , text= "Your Balance is :" , font = 12).pack(pady=20)
    Label(BalanceSc , text= Users[logedInUser]['Balance'] , font = 12).pack(pady=20)
    Button(BalanceSc,text="Okay",command=BalanceinqQuit).pack(pady=20)

def BalanceinqQuit():
    logedIn()
    BalanceSc.destroy()

def PasswordChange():
    
    MenuSc.destroy()
    
    global Passw1 
    global Passw2 
    Passw1= StringVar()
    Passw2= StringVar()
    
    global PasswordSc
    PasswordSc=Toplevel(MainWindow)
    Label(PasswordSc , text= "Enter Password Twice" , font = 12).pack(pady=20)
    Entry(PasswordSc ,textvariable=Passw1).pack()
    Entry(PasswordSc ,textvariable=Passw2).pack()
    Button(PasswordSc,text="Confirm",command=ConfPWChange).pack(pady=20)


def FawryService():
    MenuSc.destroy()
    global FawrySc
    FawrySc=Toplevel(MainWindow)
    FawrySc.geometry("325x170")
    
    global FSc
    
    Label(FawrySc,text="Please Pick Which Fawry Service" , font = 12).pack(pady=20)
    
    b1 = Button(FawrySc,text="Orange Recharge",command=OrangeWithDraw).place(x=50,y=60)
    b2 = Button(FawrySc,text="Etisalat Recharge",command=EtisalatWithDraw).place(x=160,y=60)
    b3 = Button(FawrySc,text="Vodafone Recharge",command=VodaWithDraw).place(x=50,y=100)
    b4 = Button(FawrySc,text="We Recharge",command=WeWithDraw).place(x=170,y=100)
    Button(FawrySc,text="Okay",command=FawryQuit).place(x=130,y=140)

def FawryQuit():
    FawrySc.destroy()
    logedIn()

def Exit():
    MenuSc.destroy()



### Fun For ATM Withdrawel ###
def ATM_Actuator_Out():
    global NoteSc
    NoteSc=Toplevel()
    WithdrawSc.destroy()
    
    CashAmount = int(cash.get())
    if CashAmount <= Users[logedInUser]['Balance']  and Users[logedInUser]['Balance'] > 0 and CashAmount <= 5000 and (CashAmount % 100 ) == 0 :

        Users[logedInUser]['Balance'] = Users[logedInUser]['Balance'] - CashAmount
        
        Label(NoteSc,text="Thank You!" , font = 12).pack(pady=20)
        Button(NoteSc,text="Back",command=ATMQuit, font= 12).pack(pady=20)
        
    elif Users[logedInUser]['Balance'] < 0 or CashAmount > Users[logedInUser]['Balance'] :
        Label(NoteSc,text="Unsufficant Amont Of Money" , font = 12).pack(pady=20)
        Button(NoteSc,text="Okay",command=ATMQuit).pack(pady=20)
        
    elif (CashAmount % 100 ) != 0 :
        Label(NoteSc,text="Only Allowed Multible of 100" , font = 12).pack(pady=20)
        Label(NoteSc,text="Please Reenter The Value" , font = 12).pack(pady=20)
        Button(NoteSc,text="Okay",command=ATMError).pack(pady=20)
        
    elif CashAmount > 5000:
        Label(NoteSc,text="Only Allowed 5000 Or Less Per Time" , font = 12).pack(pady=20)
        Label(NoteSc,text="Please Reenter The Value" , font = 12).pack(pady=20)
        Button(NoteSc,text="Okay",command=ATMError).pack(pady=20)


def ATMQuit():
    logedIn()
    NoteSc.destroy()

def ATMError():
    CashWithdraw()
    NoteSc.destroy()

### Funcs For Fawry ###
def OrangeWithDraw():
    global cash2
    cash2 = IntVar()
    phonenum = StringVar()
    
    FawrySc.destroy()
    
    global FSc
    FSc=Toplevel()
    Label(FSc,text="Please Enter The Phone Number" , font = 12).pack(pady=20)
    Entry(FSc,textvariable=phonenum).pack()
    Label(FSc,text="Please Enter The Amount To Send" , font = 12).pack(pady=20)
    Entry(FSc,textvariable=cash2).pack()
    Button(FSc,text="Confirm",command=FawryWithDraw).pack(pady=20)


def VodaWithDraw():
    global cash2
    cash2 = IntVar()
    phonenum = StringVar()
    
    FawrySc.destroy()
    
    global FSc
    FSc=Toplevel()
    Label(FSc,text="Please Enter The Phone Number" , font = 12).pack(pady=20)
    Entry(FSc,textvariable=phonenum).pack()
    Label(FSc,text="Please Enter The Amount To Send" , font = 12).pack(pady=20)
    Entry(FSc,textvariable=cash2).pack()
    Button(FSc,text="Confirm",command=FawryWithDraw).pack(pady=20)


def WeWithDraw():
    global cash2
    cash2 = IntVar()
    phonenum = StringVar()
    
    FawrySc.destroy()
    
    global FSc
    FSc=Toplevel()
    Label(FSc,text="Please Enter The Phone Number" , font = 12).pack(pady=20)
    Entry(FSc,textvariable=phonenum).pack()
    Label(FSc,text="Please Enter The Amount To Send" , font = 12).pack(pady=20)
    Entry(FSc,textvariable=cash2).pack()
    Button(FSc,text="Confirm",command=FawryWithDraw).pack(pady=20)


def EtisalatWithDraw():
    global cash2
    cash2 = IntVar()
    phonenum = StringVar()
    
    FawrySc.destroy()
    
    global FSc
    FSc=Toplevel()
    Label(FSc,text="Please Enter The Phone Number" , font = 12).pack(pady=20)
    Entry(FSc,textvariable=phonenum).pack()
    Label(FSc,text="Please Enter The Amount To Send" , font = 12).pack(pady=20)
    Entry(FSc,textvariable=cash2).pack()
    Button(FSc,text="Confirm",command=FawryWithDraw).pack(pady=20)


def FawryWithDraw():
    FawrySc.destroy()
    
    CashAmount2 = int(cash2.get())
    
    global psSc
    psSc=Toplevel()
    
    if CashAmount2 <= Users[logedInUser]['Balance']  and Users[logedInUser]['Balance'] > 0 :
        Users[logedInUser]['Balance'] = Users[logedInUser]['Balance'] - CashAmount2
        Label(psSc,text="Thank You!" , font = 12).pack(pady=20)
        Button(psSc,text="Okay",command=FawryBack).pack(pady=20)
        
    elif Users[logedInUser]['Balance'] < 0 or CashAmount2 > Users[logedInUser]['Balance'] :
        Label(psSc,text="Unsufficant Amont Of Money" , font = 12).pack(pady=20)
        Button(psSc,text="Okay",command=FawryBack).pack(pady=20)

def FawryBack():
    FSc.destroy()
    psSc.destroy()
    FawryService()


### Fun For Pw Change ###
def ConfPWChange ():
    global TopSc
    TopSc = Toplevel()
    Pass1 = Passw1.get()
    Pass2 = Passw2.get()

    if (Pass1 == Pass2):
        if (len(Pass1) <= 4 and len(Pass1) > 0 ):
            Users[logedInUser]['Password'] = Pass1
            pw = Pass1
            Label(TopSc , text= "Password Succsufully Changed" , font = 12).pack(pady=20)
            Label(TopSc , text= "Please LogIn again" , font = 12).pack(pady=20)
            Button(TopSc,text="Okay",command=PassQuit).pack(pady=20)
            
        elif(len(Pass1)>4):
            Label(TopSc , text= "Password Must Be Less Than 4 Characters" , font = 12).pack(pady=20)
            Button(TopSc,text="Okay",command=PassBack).pack(pady=20)
    elif(Pass1 != Pass2):
        Label(TopSc , text= "Password Isn't Matched" , font = 12).pack(pady=20)
        if(len(Pass1)>4):
            Label(TopSc , text= "Password Must Be Less Than 4 Characters" , font = 12).pack(pady=20)
        Button(TopSc,text="Okay",command=PassBack).pack(pady=20)

def PassQuit():
    PasswordSc.destroy()
    TopSc.destroy()
    # logedIn()


def PassBack():
    PasswordSc.destroy()
    TopSc.destroy()
    PasswordChange()


######### main window ###########
global MainWindow
MainWindow=Tk()
#vars to get user an pw
accNum = StringVar()
pswrd =StringVar()

MainWindow.title("Log-In")
#label to get user and pw 
Label(MainWindow ,text="Please Enter Your Account Number Below" , font = 12).pack(pady=20)
Entry(MainWindow ,textvariable=accNum).pack()

Label(MainWindow ,text="Please Enter Your Password Below" , font = 12).pack(pady=20)
Entry(MainWindow ,textvariable=pswrd,show="*").pack()    

Button(MainWindow ,text="Log In",command=logedIn).pack(pady=20)

# window size and title
MainWindow.geometry("400x250")
MainWindow.title("Bank Manager")

MainWindow.mainloop()
