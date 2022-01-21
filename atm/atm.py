
                           #ATM CONSOLE APPLICATION
import os

max_with_count_native=3 #Max With Draw Count For Native Bank
max_with_count_other=2 #Max With Draw Count For Other Banks
max_with_amount=25000 #One day Max Withdraw Amount
atm_amount={100:1,200:1,500:1,2000:1} #100 200 500 2000

users=[
{"username":"g","password":"1234","Amount":125000,"passlimit":0},
{"username":"NATH","password":"1234","Amount":134000,"passlimit":0},
{"username":"SABA","password":"1234","Amount":125000,"passlimit":0}
]

users_bank=[
{"username":"g","password":"1234","Amount":125000,"Bank":"SBI","dailywithdrawlimit":0,"dailyamountlimit":0,"mini":[]},
{"username":"NATH","password":"1234","Amount":134000,"Bank":"SBI","dailywithdrawlimit":0,"dailyamountlimit":0,"mini":[]},
{"username":"SABA","password":"1234","Amount":125000,"Bank":"AXB","dailywithdrawlimit":0,"dailyamountlimit":0,"mini":[]}
]

def showmini(current): #transaction history
    l=users_bank[current]["mini"]
    if(len(l)<=5):
        print("\nLast {} transactions".format(len(l)))
        for i in l:
            print(i)
    else:
        c=0
        print("\nLast 5 transactions\n")
        for i in l[len(l)-1:len(l)-5-1:-1]:
            print(i)
    input("\nPress Enter to Continue")

def atmamount(): #calculate ATM amount
    amount=0
    for i in atm_amount:
        amount+=(i*atm_amount[i])
    return amount

def withdraw(w_at,current,flag): #user withdraw 
    users_bank[current]["dailywithdrawlimit"]+=1
    res_wt_at=w_at
    l=[0,0,0,0]
    if(w_at>=2000):
        l[-1]+=w_at//2000
        if(atm_amount[2000]==0):
            l[-1]=0
        elif(l[-1] >= atm_amount[2000]):
            l[-1]=atm_amount[2000]
            w_at=((w_at-(l[-1]*2000))%2000)*2000
        else:
            w_at=w_at-(l[-1]*2000)
        atm_amount[2000]-=l[-1]
    
    if(w_at>=500):
        l[-2]+=w_at//500
        if(atm_amount[500]==0):
            l[-2]=0
        elif(l[-2] >= atm_amount[500]):
            l[-2]=atm_amount[500]
            w_at=((w_at-(l[-2]*500))%500)*500
        else:
            w_at=w_at-(l[-2]*500)
        atm_amount[500]-=l[-2]
        
    if(w_at>=200):
        l[-3]+=w_at//200
        if(atm_amount[200]==0):
            l[-3]=0
        elif(l[-3] >= atm_amount[200]):
            l[-3]=atm_amount[200]
            w_at=((w_at-(l[-3]*200))%200)*200
        else:
            w_at=w_at-(l[-3]*200)
        atm_amount[200]-=l[-3]

    if(w_at>=100):
        l[-4]+=w_at//100
        if(atm_amount[100]==0):
            l[-4]=0
        elif(l[-4] >= atm_amount[100]):
            l[-4]=atm_amount[100]
            w_at=((w_at-(l[-4]*100))%100)*100
        else:
            w_at=w_at-(l[-4]*100)
        atm_amount[100]-=l[-4]

    temp=0
    d=0
    for i in atm_amount:
        temp+=i*l[d]
        d+=1

    k=0
    if(temp==res_wt_at):
        print("\nAmount Dispatched:",res_wt_at,"\n")
        for i in atm_amount:
            if(l[k]!=0):
                print("No. of "+str(i).rjust(4," ")+" Dispatched: ",l[k])
            k+=1
        users[current]["Amount"]-=res_wt_at
        users_bank[current]["dailyamountlimit"]+=res_wt_at
        users_bank[current]["mini"].append("\nWithdraw: -"+str(res_wt_at)+"\nOverall Balance  : "+str(users[current]["Amount"]))
        if(flag==1):
            users[current]["Amount"]-=30
    else:
        print("\nNo Cash in ATM\n")

def updateCash(current,awailable): #update cash in ATM and User Deposite
    d_amount = 0
    for i in atm_amount:
        ch=int(input("\nEnter No. of "+(str(i).rjust(4," "))+": "))
        atm_amount[i]+=ch
        d_amount += (i * ch)
    print("\nAmount Deposited:",d_amount)
    if(current!="0"):
        users[current]["Amount"]+=d_amount
        users_bank[current]["mini"].append("\nDeposited Balance: +"+str(d_amount)+"\nOverall Balance  : "+str(awailable))

def showBalance(): #show balance 
    amount=0
    for i in atm_amount:
        amount+=i*atm_amount[i]
        print("\nNo. of "+(str(i).rjust(4," ")),":",atm_amount[i])
    print("\nTotal: ",amount)

while(True):
    os.system('cls')
    ch=int(input("\n\tWelcome to ATM\n1.Admin login\n2.User login\n3.Exit\n\nEnter your choice: "))
   
    
    if(ch==1):
        os.system('cls')
        print("\n\tWelcome to Admin Login")

        id=input("\nEnter Admin Username: ")
        ps=input("Enter Admin Password: ")

        if(id=="Admin" and ps=="1234"):
            
            while(True):
                os.system('cls')
                ch=int(input("\n\tWelcome Admin\n\n1.Update Cash\n2.Show Available Balance & Denominations3\n3.Logout\n\nEnter Your choice: "))
                
                if(ch==1):
                    updateCash("0","0")
                    input("\n\tAmount Added Sucessfully\n\nPress Enter to continue...")
               
                elif(ch==2):
                    showBalance()
                    input("\nPress Enter to continue...")
                
                elif(ch==3):
                    break
        else:
            print("\nInvalid Username or Password\nPress Enter to continue...")
            input()

    
    elif(ch==2): #USER LOGIN
        os.system('cls')
        print("\n\tWelcome to User Login")
        id=input("\nEnter User Username: ")
        ps=input("Enter User Password: ")
        flag=0
        for i in users:
            if(i["username"] == id):
                user=str(i["username"])
                amnt=i["Amount"]
                current=users.index(i)
                bank=users_bank[current]["Bank"]
                flag = 1
                break
        if(flag==1):
            if(users[current]["password"]==ps and users[current]["passlimit"] < 3 ):
                if(bank=="SBI"):
                    max_withdraw_limit=max_with_count_native
                
                else:
                    max_withdraw_limit=max_with_count_other
                
                while(True):
                    os.system('cls')
                    ch=int(input("\n\tWelcome\n1.Withdrawl\n2.View Balance\n3.Deposite\n4.Pin Change\n5.Mini Statement\n6.Logout\n\nEnter Your Choice: "))
                    
                    if(ch==1):
                        w_at=int(input("\nEnter the Withdraw Amount: "))
                        
                        if(w_at>15000):
                            print("\nATM Limit Exceeded\nEnter Amount less than 15,000\nPress Enter to Continue...")
                            input()
                        
                        elif(w_at%100!=0):
                            print("\nEnter Valid Amount\n\n(Multiples of 100 200 500 2000)\n")
                            input("\nPress Enter to Continue!")
                        
                        elif(w_at > users[current]["Amount"]):
                            print("\nInsufficient Balance In Your Account\n")
                            input("\nPress Enter to Continue...")
                        
                        elif(atmamount()<w_at):
                            print("\nInsufficient Balance In ATM\nAvailable balance in ATM:",atmamount())
                            input("\nPress Enter to Continue...")
                        
                        else:
                            
                            if(users_bank[current]["dailyamountlimit"]+w_at <= max_with_amount):
                                flag=0
                                
                                if(users_bank[current]["dailywithdrawlimit"] < max_withdraw_limit):
                                    withdraw(w_at,current,flag)
                                    input("\nPress Enter to Continue...")
                                
                                else:
                                    flag=1
                                    print("\nDaily Free Withdrawal limit Exceeded!\nAmount 30 Rs. will be debited from your Account\n")
                                    withdraw(w_at,current,flag)
                                    input("\nPress Enter to Continue...")
                            
                            else:
                                print("\nDaily Withdrawal Amount limit Exceeded!\n Try entering amount below:",max_with_amount - users_bank[current]["dailyamountlimit"])
                                input("\nPress Enter to Continue...")

                    elif(ch==2):
                        print("\nAvailable Balance: ",users[current]["Amount"])
                        input("\nPress Enter to Continue...")
                    
                    elif(ch==3):
                        print("\nCurrent Balance:",users[current]["Amount"],"\n")
                        updateCash(current,users[current]["Amount"])
                        print("\nUpdated Balance: ",users[current]["Amount"])
                        input("\nPress Enter to Continue...")
                    
                    elif(ch==4):
                        new_pin=input("\nEnter New Pin: ")
                        users[current]["password"]=new_pin
                        input("\nPin Updated sucessfully!\n\nPress Enter to Continue...")
                    
                    elif(ch==5):
                        showmini(current)
                    
                    elif(ch>6):
                        continue
                    
                    elif(ch==6):
                        break

            elif(users[current]["password"]!=ps and users[current]["passlimit"] < 4):
                users[current]["passlimit"]+=1
                print("\nInvalid Password\nPress Enter to Continue...")
                input()
                continue

            elif(users[current]["password"]!=ps and users[current]["passlimit"] >= 3):
                print("\nUser Password Limit Exceded")
                input("\nPress Enter To Continue...")
            else:
                print("\nUser Password Limit Exceded\nWait For 24 hr To")
                input("\nPress Enter To Continue...")
        else:
            input("\nUser Not Found\n\nPress Enter to Continue...")
    
    elif(ch==3):
        os.system('cls')
        print("\n\n\1 \2 \3 Thanks for Using ATM \3 \2 \1")
        break