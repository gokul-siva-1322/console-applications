import os

new_user_id = "U3"
new_group_id = "G2"
memmeridarr =["U1","U2","U3"]

users =[
{"userId":"U1","userName":"Anu","password":"1234","balance":3000,"activity":[]},
{"userId":"U2","userName":"Ram","password":"1234","balance":3000,"activity":[]},
{"userId":"U3","userName":"Kit","password":"1234","balance":3000,"activity":[]},
]
expense = [
]
groups = [
{"groupId":"G1","groupName":"friends","members":["U1","U2"],"admin":"U1"}
]

def newuser():

    global new_user_id
    new_user_id = "U"+str(int(new_user_id[1:])+1)
    userid = new_user_id
    os.system('cls')
    print("\tSignup Page")
    print("\nYour User ID  :",userid)
    username = input("\nEnter Username: ").title()
    password = input("\nEnter Password: ")
    users.append({"userId":userid,"userName":username,"password":password,"balance":0,"activity":[]})
    memmeridarr.append(userid)
    input("\nUser Created Sucessfully\n\nPress Enter to Continue...")

def olduser():

    os.system('cls')
    print("\tLogin Page")
    userid   = input("\nEnter User ID : ").upper()
    password = input("\nEnter Password: ")
    flag = 0
    for i in users:
        if(i["userId"] == userid and i["password"] == password):
            currentuser = users.index(i)
            flag = 1
    if(flag == 1):
        userhome(currentuser)
    else:
        input("\nInvalid User ID or Password\n\nPress Enter to Continue...")

def userhome(currentuser):

    while(True):
        os.system('cls')
        username = users[currentuser]["userName"].title()
        print(f"\tWelcome {username}")
        ch = input("\n1.Add an Expense\n2.Update Wallet\n3.Create Group\n4.My Groups\n5.View & Pay\n6.Activities\n7.Logout\n\nEnter Your Choice: ")
        if(ch == "1"):
            selectexpense(currentuser)
        elif(ch == "2"):
            updatewallet(currentuser)
        elif(ch == "3"):
            creatgroup(currentuser)
        elif(ch == "4"):
            mygroups(currentuser)
        elif(ch == "5"):
            viewpay(currentuser)
        elif(ch == "6"):
            viewmyactivity(currentuser)
        elif(ch == "7"):
            break
        else:
            input("\nInvalid Choice\nPress Enter to Continue...")

def finduser(userid):
    for i in users:
        if(i["userId"] == userid):
            return users.index(i)
    return "0"

def selectexpense(currentuser):
    ch = input("\n1.Group Expense\n2.Non-Group Expense\n\nEnter Your Choice: ")
    if(ch == "1"):
        groupexpense(currentuser)
    elif(ch == "2"):
        addexpense(currentuser)
    else:
        input("Print Invalid Choice\n\nPress Enter to Continue...")
    
def groupexpense(currentuser):
    temp = []
    a = 1
    for i in groups:
        if(users[currentuser]["userId"] in  i["members"]):
            temp.append(i)
    if(len(temp)!=0):
        for i in temp:
            print("\n{}.{} - {}".format(a,i["groupId"],i["groupName"]))
            a+=1
        grpid = input("\nEnter Group ID: ").upper()
        currentgrp = findgroup(grpid)
        if(currentgrp != "0"):
            l = groups[currentgrp]["members"]
            expensename   = input("\nEnter Expense Name  : ")
            expenseamount = int(input("\nEnter Expense Amount: "))
            memberpaid = input("\nEnter Member ID Who Paid the Expense: ").upper()
            if(memberpaid in l):
                currentpaid   = memmeridarr.index(memberpaid)
                print("\n{} Paid {} expense\nExpense Amount: {}".format(users[currentpaid]["userName"],expensename.title(),expenseamount))
                equal = round(expenseamount/len(l),2)
                for i in l:
                    if(i != memberpaid):
                        expense.append({"expenseName":expensename,"userId":i,"topay":equal,"towhome":currentpaid,"paid":0,"creater":users[currentuser]["userName"],"status":"Not Paid","createrName":users[currentpaid]["userName"]})
                        x = memmeridarr.index(i)
                        print("\n{} owes {} {}".format(users[x]["userName"],users[currentpaid]["userName"],equal))

                    y = finduser(i)
                    if(y == currentuser):
                        users[y]["activity"].append("You created an Expense {}".format(expensename))
                    else:
                        users[y]["activity"].append("{} created an Expense {}".format(users[y]["userName"],expensename))
                print(f"\n{expensename} Expence created Sucessfully")
            else:
                print("\nMember Not In Group")
        else:
            print("\nGroup Not Found")
    else:
        print("\nYou are not in any groups")
    input("\nPress Enter to Continue...")

def addexpense(currentuser):

    os.system('cls')
    expensename   = input("\nEnter Expense Name  : ")
    expenseamount = int(input("\nEnter Expense Amount: "))
    memberscount  = int(input("\nExpense Member count: "))
    a = 1
    temp = []
    count = memberscount
    if(memberscount <= len(memmeridarr)):
        while(count > 0):
            memberid = input(f"\n{a}.Enter Member ID: ").upper()
            if(memberid in memmeridarr):
                temp.append(memberid)
                count -= 1
                a+=1
            else:
                input("\nInvalid Member ID\n\nPress Enter to Continue...")
                continue
        memberpaid = input("\nEnter Member ID Who Paid the Expense: ").upper()
        if(memberid not in temp):
            currentpaid   = memmeridarr.index(memberpaid)
            print("\n{} Paid {} expense\nExpense Amount: {}".format(users[currentpaid]["userName"],expensename.title(),expenseamount))
            print("\n1.Split Equally\n2.Split Unequally")
            ch = input("\n\nEnter Your Choice: ")

            if(ch == "1"):
                equal = round(expenseamount/memberscount,2)
                for i in temp:
                    if(i != memberpaid):
                        expense.append({"expenseName":expensename,"userId":i,"topay":equal,"towhome":currentpaid,"paid":0,"creater":users[currentuser]["userName"],"status":"Not Paid","createrName":users[currentpaid]["userName"]})
                        x = memmeridarr.index(i)
                        print("\n{} owes {} {}".format(users[x]["userName"],users[currentpaid]["userName"],equal))
                    y = finduser(i)
                    if(y == currentuser):
                        users[y]["activity"].append("You created an Expense {}".format(expensename))
                    else:
                        users[y]["activity"].append("{} created an Expense {}".format(users[y]["userName"],expensename))

            elif(ch == "2"):
                paidmembshare = int(input("\nEnter {} share in the Expense: ".format(users[currentpaid]["userName"])))
                amt = expenseamount - paidmembshare
                c = memberscount - 1
                i = 0
                while(c > 0):
                    x = memmeridarr.index(temp[i])
                    if(x != currentpaid):
                        users[x]["activity"].append("{} created an Expense {}".format(users[currentuser]["userName"],expensename))
                        splitamt = int(input("\nEnter Amount {} Owes to {}: ".format(users[x]["userName"],users[currentpaid]["userName"])))
                        if(splitamt <= amt):
                            expense.append({"expenseName":expensename,"userId":temp[i],"topay":splitamt,"towhome":currentpaid,"paid":0,"creater":users[currentuser]["userName"],"status":"Not Paid","createrName":users[currentpaid]["userName"]})
                            c -= 1
                            amt -= splitamt
                            i += 1
                    else:
                        users[x]["activity"].append("You created an Expense {}".format(expensename))
                        i+=1
                print(f"\n{expensename.title()} Expense Created Sucessfully")
        else:
            print("\nInvalid Member Id")
        input("\n\nPress Enter to Continue...")
    else:
        input("\nNot That much Users in Splitwise\n\nPress Enter to Continue...")
    
def updatewallet(currentuser):

    print("\nAwailable Wallet Balance: {}".format(users[currentuser]["balance"]))
    amount = int(input("\nEnter Amount to be Added:" ))
    users[currentuser]["balance"] += amount
    users[currentuser]["activity"].append("You Updated Your Wallet balance +{} total {}".format(amount,users[currentuser]["balance"]))
    print("\nWallet Balance Updated!")
    print("\nAwailable Wallet Balance: {}".format(users[currentuser]["balance"]))
    input("\n\nPress Enter to Continue...")
    
def viewpay(currentuser):
    temp1 = []
    temp2 = []
    for i in expense:
        if(i["userId"] == users[currentuser]["userId"] and i["status"] == "Not Paid"):
            temp1.append(i)
        if(i["towhome"] == currentuser and i["status"] == "Not Paid"):
            temp2.append(i)
    a = 1
    
    if(len(temp1) !=0 ):
        print("\n\tExpense You Owe Someone\n")
        for i in temp1:
            print("\nExpense Number : {}\nExpense Name   : {}\nExpense Creator: {}\nYou Owes {} {}\nExpense Status : {}".format(expense.index(i)+1,i["expenseName"],i["creater"],i["createrName"],round(i["topay"]-i["paid"],2),i["status"]))
            a+=1
        print("\nEnter '1' to Settle up...\nEnter '0' to Continue...")
        ch = input("\nEnter Your Choice: ")
        if(ch == "1"):
            currentexp = int(input("\nEnter Expense Number    : "))-1
            amount    = float(input("\nEnter Amount You Want Pay: "))
            if(amount <= users[currentuser]["balance"]):
                currentpaid = expense[currentexp]["towhome"]
                if(amount <= expense[currentexp]["topay"]):
                    users[currentuser]["balance"] -= amount
                    users[currentpaid]["balance"] += amount
                    expense[currentexp]["paid"] += round(amount,2)
                    if(expense[currentexp]["topay"] == expense[currentexp]["paid"]):
                        expense[currentexp]["status"] = "Paid"
                        users[currentuser]["activity"].append("You paid {} and settled Up ({} of {}) to {}".format(amount,expense[currentexp]["paid"],expense[currentexp]["topay"],expense[currentexp]["createrName"]))
                        users[currentpaid]["activity"].append("{} paid {} settled up ({} of {})".format(users[currentuser]["userName"],amount,expense[currentexp]["paid"],expense[currentexp]["topay"]))
                    else:
                        users[currentuser]["activity"].append("You Paid {} ({} of {}) to {}".format(amount,expense[currentexp]["paid"],expense[currentexp]["topay"],expense[currentexp]["createrName"]))
                        users[currentpaid]["activity"].append("{} paid You {} ({} of {})".format(users[currentuser]["userName"],amount,expense[currentexp]["paid"],expense[currentexp]["topay"]))
                else:
                    print("\nYou Entered Wrong Amount")
            else:
                print("\nLess Wallet Balance")
    else:
        print("\n\tExpense You Owe Someone: 0")

    if(len(temp2)!=0):
        print("\n\tExpense someone owes You\n")
        for i in temp2:
            current = users[memmeridarr.index(i["userId"])]["userName"]
            print("\n{} owes you {}".format(current,round(i["topay"]-i["paid"],2)))
    else:
        print("\n\tNo One Owes You any Expense")
    input("\n\nPress Enter to Continue...")

def viewmyactivity(currentuser):
    if(len(users[currentuser]["activity"]) != 0):
        for i in users[currentuser]["activity"]:
            print("\n"+i)
    else:
        print("\nNo Activity till Now")
    input("\nPress Enter to Continue...")

def creatgroup(currentuser):
    print("\nCreat New Group")
    global new_group_id
    new_group_id = "G"+str(int(new_group_id[1:])+1)
    print("\nYour Autogenerated Group ID is",new_group_id)
    grpname =   input("\nEnter Group Name   : ").title()
    count = int(input("\nEnter Members Count: "))
    groups.append({"groupId":new_group_id,"groupName":grpname,"members":[],"admin":users[currentuser]["userId"]})
    temp = []
    while(count > 0):
        membid = input("\nEnter User ID to Add:")
        if(membid in memmeridarr):
            groups[-1]["members"].append(membid)
            temp.append(membid)
            count -= 1
        else:
            input("User Not Found\n\nPress Enter to continue...")
            continue

    l = [[i,users[finduser(i)]["userName"]] for i in temp]
    print(l)
    print("\nGroup name : {}\nGroup Admin: {}\nGroup Members:".format(grpname,users[currentuser]["userName"]))
    print(*l,sep=" - ")
    input("\nGroup Created Sucessfully\n\nPress Enter to Continue...")

def mygroups(currentuser):
    while(True):
        os.system('cls')
        print("\tMy Groups")
        ch = input("\n1.View my groups\n2.Delet a Group\n3.Add Member\n4.Remove Member\nExit\n\nEnter Your Choice: ")
        if(ch == "1"):
            viewmygroups(currentuser)
        elif(ch == "2"):
            deletgroup(currentuser)
        elif(ch == "3"):
            addmember(currentuser)
        elif(ch == "4"):
            removemember(currentuser)
        elif(ch == "5"):
            break
        else:
            input("\nInvalid Choice\n\nPress Enter to Continue....")

def viewmygroups(currentuser):
    admintemp = []
    usertemp = []
    userid = users[currentuser]["userId"]
    for i in groups:
        if(userid == i["admin"]):
            admintemp.append(i)
        if(userid in i["members"] and i not in admintemp):
            usertemp.append(i)
    if(len(admintemp) != 0):
        print("\nGroups You are Admin")
        l = [[k,users[finduser(k)]["userName"]] for k in i["members"]]
        for i in admintemp:
            print("\nGroup name : {}\nGroup Admin: {}\nGroup Members:".format(i["groupName"],"You"))
            for i in l:
                print(*i,sep = " - ")
    if(len(usertemp) != 0):
        print("\nGroups You are Member")
        l = [[k,users[finduser(k)]["userName"]] for k in i["members"]]
        for i in usertemp:
            print("\nGroup name : {}\nGroup Admin: {}\nGroup Members:".format(i["groupName"],users[finduser(i["admin"])]["userName"]))
            for i in l:
                print(*i,sep = " - ")
    if(len(admintemp) == 0 and len(usertemp) == 0):
        print("\nNo Groups to Show")
    input("\nPress Enter to Continue...")

def findgroup(grpid):
    for i in groups:
        if(i["groupId"] == grpid):
            return groups.index(i)
    return "0"

def deletgroup(currentuser):

    grpid = input("\nEnter Group ID to delet: ")
    currentgrp = findgroup(grpid)
    if(currentgrp != "0"):
        if(groups[currentgrp]["admin"] == users[currentuser]["userId"]):
            confirm = input("\nCofirm removal(Y/N): ").upper()
            if(confirm == "Y"):
                groups.pop(currentgrp)
                print("\nGroup Deleted Sucessfully")
            else:
                print("\nGroup Deletion Canceled")
        else:
            print("\nOnly Admin Can Delet the Group")
    else:
        print("\nGroup Not Found")
    input("\nPress Enter to Continue...")

def addmember(currentuser):
    grpid = input("\nEnter Group ID: ").upper()
    currentgrp = findgroup(grpid)
    
    if(currentgrp != "0"):
        temp = groups[currentgrp]["members"]
        if(groups[currentgrp]["admin"] == users[currentuser]["userId"]):
            membid = input("\nEnter Member ID to Add: ").upper()
            if(membid not in temp):
                groups[currentgrp]["members"].append(membid)
                print("\nUser added to Group")
            else:
                print("\nMember Already In Group")
        else:
            print("\nOnly Addmins Can Add members to Group")
    else:
        print("\nGroup Not Found")
    input("\nPress Enter to Continue...")

def removemember(currentuser):
    grpid = input("\nEnter Group ID: ").upper()
    currentgrp = findgroup(grpid)
    
    if(currentgrp != "0"):
        temp = groups[currentgrp]["members"]
        if(groups[currentgrp]["admin"] == users[currentuser]["userId"]):
            membid = input("\nEnter Member ID to Delet: ").upper()
            if(membid in temp):
                groups[currentgrp]["members"].remove(membid)
                print("\nUser Removed From the Group")
            else:
                print("\nMember Not In Group")
        else:
            print("\nOnly Addmins Can Delet members in Group")
    else:
        print("\nGroup Not Found")
    input("\nPress Enter to Continue...")

while(True):
    os.system('cls')
    print("\tWelcome")
    ch = input("\n1.New User\n2.Existing User\n3.Exit\n\nEnter Your Choice: ")
    if(ch == "1"):
        newuser()
    elif(ch == "2"):
        olduser()
    elif(ch == "3"):
        os.system('cls')
        print("Thank You...\3")
        break
    else:
        input("Invalid Input\nPress Enter to Continue...")
