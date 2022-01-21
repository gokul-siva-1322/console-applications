import os
import datetime

new_adminid = "A0"
new_userid  = "U1"
new_bookid  = "B4"
new_borrow  = "5000"

users = [
{"userId":"U1","userName":"Karan","password":"1234","status":"Approved","balance":1500,"cart":[]}
]
books = [
{"bookId":"B1","bookName":"Python Programming","author":"Thareja","total":10,"awailable":5,"borrowed":5,"price":340,"onborrow":5},
{"bookId":"B2","bookName":"Python Programming","author":"Ashoke","total":10,"awailable":6,"borrowed":4,"price":390,"onborrow":4},
{"bookId":"B3","bookName":"C Programming","author":"Nelson","total":10,"awailable":8,"borrowed":2,"price":450,"onborrow":2},
{"bookId":"B4","bookName":"Java Programming","author":"Hari","total":10,"awailable":1,"borrowed":9,"price":640,"onborrow":9}
]
admins = [1
]
borrow =[
]
def borrowstatus():
    borrowid = input("\nEnter Borrow ID: ")
    flag = 0
    for i in borrow:
        if(i["borrowId"] == borrowid):
            currentborrow = borrow.index(i)
            flag = 1
            bookid = i["bookId"]
            for j in books:
                if(j["bookId"] == bookid):
                    currentbook = books.index(j)
                    break
            break
    if(flag == 1):
        print("\n{}\nStatus: {}".format(borrow[currentborrow]["bookName"],borrow[currentborrow]["status"]))
        a = borrow[currentborrow]["status"]
        if(a != "Received" and a != "Book Lost Amount Paid"):
            print("\nIf Received Press '1'\nIf Lost Press '2'\nIf Overdue Press '3'\nIf Continue Press '4'")
            ch = input("\nEnter Your Choice: ")
            userid = borrow[currentborrow]["userId"]
            for i in users:
                if(i["userId"] == userid):
                    currentuser = users.index(i)
                    break
            if(ch == "1"):
                borrow[currentborrow]["status"] = "Received"
                books[currentbook]["awailable"] += 1
                books[currentbook]["onborrow"] -= 1
                borrow[currentborrow]["returndate"] = datetime.date.today()
                print("\nBook Status Updated")
            elif(ch == "2"):
                print("\nFine Amount:",int(books[currentbook]["price"]/2))
                print("\n1.Cash\n2.Deduce Form Wallet")
                c = input("\nEnter Your Choice:")
                if(c == "1"):
                    users[currentuser]["balance"] -= int(books[currentbook]["price"]/2)
                    books[currentbook]["total"] -= 1
                    books[currentbook]["onborrow"] -= 1
                    borrow[currentborrow]["status"] = "Book Lost Amount Paid"
                    print("\\nBook Status Updated")
                elif(c == "2"):
                    if(users[currentuser]["balance"] >= int(books[currentbook]["price"]/2)):
                        users[currentuser]["balance"] -= int(books[currentbook]["price"]/2)
                        books[currentbook]["total"] -= 1
                        borrow[currentborrow]["status"] = "Book Lost Amount Paid"
                        print("\nAmount Debited from Wallet\nAwailable Balance: {}\nBook Status Updated".format(users[currentuser]["balance"]))
                    else:
                        print("\nInsufficient Balance In Account")
                        borrow[currentborrow]["status"] = "Book Lost Amount Not Paid"

            elif(ch == "3"):
                date = list(map(int,input("Enter Today Date [format-02/03/2001]:").split("/")))
                date = datetime.date(date[2],date[1],date[0])
                datediff = (date - borrow[currentborrow]["duedate"]).days
                print("Due Limit Upto:",int(books[currentbook]["price"]/2))
                if(datediff * 2 <= int(books[currentbook]["price"]/2)):
                    print("\nFine To be Paid:",datediff * 2)
                    print("\n1.Cash\n2.Use Wallet Balance")
                    c = input("\nEnter Your Choice: ")
                    if(c == "1"):
                        borrow[currentborrow]["status"] = "Received"
                        books[currentbook]["awailable"] += 1
                        books[currentbook]["onborrow"] -= 1
                        borrow[currentborrow]["returndate"] = datetime.date.today()
                        print("\nBook Status Updated")
                    elif(c == "2"):
                        if(users[currentuser]["balance"] >= datediff  * 2):
                            borrow[currentborrow]["status"] = "Received"
                            books[currentbook]["awailable"] += 1
                            books[currentbook]["onborrow"] -= 1
                            borrow[currentborrow]["returndate"] = datetime.date.today()
                            print("\nAmount Debited from Wallet\nAwailable Balance: {}\nBook Status Updated".format(users[currentuser]["balance"]))
                        else:
                            print("\nInsufficient Balance In Wallet")
                else:
                    print("\nVery Overdue Book is Considered Lost\nPay Due Limit")
                    print("\n1.Cash\n2.Use Wallet Balance")
                    c = input("\nEnter Your Choice: ")
                    if(c == "1"):
                        books[currentbook]["total"] -= 1
                        books[currentbook]["onborrow"] -= 1
                        borrow[currentborrow]["status"] = "Book Lost Amount Paid"
                        print("\nBook Status Updated")
                    elif(c == "2"):
                        if(users[currentuser]["balance"] >= int(books[currentbook]["price"]/2)):
                            users[currentuser]["balance"] -= int(books[currentbook]["price"]/2)
                            books[currentbook]["total"] -= 1
                            borrow[currentborrow]["status"] = "Book Lost Amount Paid"
                            print("\nAmount Debited from Wallet\nAwailable Balance: {}\nBook Status Updated".format(users[currentuser]["balance"]))
                        else:
                            print("\nInsufficient Balance In Account")
                            borrow[currentborrow]["status"] = "Book Lost Amount Not Paid"
            else:
                print("\nInvalid Choice")
    else:
        print("\nInvalid Borrow Id")
    input("\n\nPress Enter to Continue...")

def usercontrol():
    while(True):
        os.system('cls')
        print("\tAdmin's Borrower Portal")
        ch = input("\n1.Add Borrower\n2.Remove Borrower\n3.Update Borrower Wallet4.Exit\n\nEnter Your Choice: ")
        if(ch == "1"):
            adduser()
        elif(ch == "2"):
            removeuser()
        elif(ch == "3"):
            updatewallet()
        elif(ch == "4"):
            break
        else:
            input("Invalid Choice\n\nPress Enter to Continue...")
            continue

def mainadminhome():
    os.system('cls')
    print("\tWelcome to Admin Login")
    adminname = input("\nEnter Username: ")
    adminpass = input("\nEnter Password: ")
    if(adminname == "admin" and adminpass == "1234"):
        while(True):
            os.system('cls')
            print("\t\1 Welcome Admin \1")
            ch = input("\n1.Add Admin\n2.Remove Admin\n3.Borrower Control\n4.Add Book\n5.Edit Book\n6.Reports\n7.Borrow Status Edit\n8.Exit\n\nEnter Your Choice: ")
            if(ch == "1"):
                addadmin()
            elif(ch == "0"):
                viewbookdetails()
            elif(ch == "2"):
                removeadmin()
            elif(ch == "3"):
                usercontrol()
            elif(ch == "4"):
                addbook()
            elif(ch == "5"):
                editbook()
            elif(ch == "6"):
                report()
            elif(ch == "7"):
                borrowstatus()
            elif(ch == "8"):
                break
            else :
                input("\nInvalid Choice\n\nPress Enter to Continue...")
                continue
    else:
        input("\nInvalid Username or Password\n\nPress Enter to Continue...")

def addadmin():
    os.system('cls')
    global new_adminid
    new_adminid = "A"+str(int(new_adminid[1:])+1)
    print("\nYour Autogenerated Admin Id:",new_adminid)
    adminname = input("\nEnter Username: ")
    adminpass = input("\nEnter Password: ")
    admins.append({"adminId":new_adminid,"adminName":adminname,"password":adminpass,"status":"Approved"})
    input("\nNew Admin Added\n\nPress Enter to Continue...")

def adduser():
    os.system('cls')
    global new_userid
    new_userid = "U"+str(int(new_userid[1:])+1)
    print("\nYour Autogenerated Admin Id:",new_userid)
    username = input("\nEnter Username: ")
    userpass = input("\nEnter Password: ")
    users.append({"userId":new_userid,"userName":username,"password":userpass,"status":"Approved","balance":1500,"cart":[]})
    input("\nNew User Added\n\nPress Enter to Continue...")

def removeadmin():
    os.system('cls')
    print("\n\tAdmin Removal Page")
    adminid = input("\nEnter Admin Id: ").upper()
    for i in admins:
        if(i["adminId"] == adminid and i["status"] == "Approved"):
            ch = input("\nConfirm Removal (Y/N): ")
            if(ch in "Yy"):
                i["status"] = "Removed"
                input("\nAdmin Removed Sucessfully\n\nPress Enter to Continue...")
                break
            else:
                input("\nRequest Canceled Sucessfully\n\nPress Enter to Continue...")
                break
        elif(i["adminId"] == adminid and i["status"] == "Removed"):
            input("\nAdmin Alread Removed\n\nPress Enter to Continue...")
            break
    else:
        input("\nAdmin Not Found\n\nPress Enter to Continue...")

def removeuser():
    os.system('cls')
    print("\n\tUser Removal Page")
    userid = input("\nEnter Borrower Id: ").upper()
    for i in users:
        if(i["userId"] == userid and i["status"] == "Approved"):
            ch = input("\nConfirm Removal (Y/N): ")
            if(ch in "Yy"):
                i["status"] = "Removed"
                input("\nBorrower Removed Sucessfully\n\nPress Enter to Continue...")
                break
            else:
                input("\nRequest Canceled Sucessfully\n\nPress Enter to Continue...")
                break
        elif(i["userId"] == userid and i["status"] == "Removed"):
            input("\nBorrower Alread Removed\n\nPress Enter to Continue...")
            break
    else:
        input("\nBorrower Not Found\n\nPress Enter to Continue...")

def updatewallet():
    userid = input("\nEnter User ID: ").upper()
    currentuser = "0"
    for i in users:
        if(i["userId"] == userid):
            currentuser = users.index(i)
            if(currentuser != "0"):
                print("\nAwailable Balance:",users[currentuser]["balance"])
                amount = int(input("\nEnter Amount to be Added: "))
                users[currentuser]["balance"] += amount
                print("\nUpdated Balance  :",users[currentuser]["balance"])
        else:
            print("\nUser Not Found")
        input("\n\nPress Enter to Continue...")

def addbook():
    os.system('cls')
    global new_bookid
    new_bookid = "B"+str(int(new_bookid[1:])+1)
    print("\n\tAdd Book Page")
    print(f"\nAutogenerated Book Id is {new_bookid}.")
    bookname = input("\nEnter Book Name  : ")
    author = input("\nEnter Author Name: ")
    price = int(input("\nEnter Book Price : "))
    quantity = int(input("\nEnter Quantity   :"))
    books.append({"bookId":new_bookid,"bookName":bookname,"author":author,"total":quantity,"awailable":quantity,"borrowed":0,"price":price})
    input("\nBook Added Sucessfully\n\nPress Enter to Continue....")

def editbook():
    os.system('cls')
    while(True):
        os.system('cls')
        print("\n\tBook Edit Page")
        ch = input("\n1.Update Stocks\n2.Remove Book\n3.Exit\n\nEnter Your Choice: ")
        os.system('cls')
        if(ch == "3"):
            break
        elif(ch != "1" and ch !="2"):
            input("\nInvalid Choice\n\nPress Enter to Continue...")
            continue
        bookid = input("\nEnter Book Id: ").upper()
        flag = 0
        for i in books:
            if(i["bookId"] == bookid):
                flag = 1
                currentbook = books.index(i)
                break
        if(flag == 1):
            if(ch == "1"):
                bookname = books[currentbook]["bookName"]
                author = books[currentbook]["author"]
                total = books[currentbook]["total"]
                awailable = books[currentbook]["awailable"]
                print(f"\n{bookname.title()}\nAuthor: {author.title()}\n\nTotal Quantity    : {total}\nBorrowed Quantity : {total-awailable}\nAwailable Quantity: {awailable}")
                quantity = int(input("\nEnter No. of Books Added: "))
                books[currentbook]["total"] += quantity
                books[currentbook]["awailable"] += quantity
                total = books[currentbook]["total"]
                awailable = books[currentbook]["awailable"]
                print("\nStock Updated Sucessfully\n")
                print(f"\n{bookname.title()}\nAuthor: {author.title()}\n\nTotal Quantity    : {total}\nBorrowed Quantity : {total-awailable}\nAwailable Quantity: {awailable}")
                input("\n\nPress Enter to Continue...")
            elif(ch == "2"):
                confirm = input("\nConfirm Removal(Y/N): ")
                if( confirm in "Yy"):
                    books.pop(currentbook)
                    input("\nBook Removed Sucessfully\n\nPress Enter to Continue...")
                else:
                    input("\nBook Removal Canceled\n\nPress Enter to Continue...")
        else:
            input("\nBook Not Found\n\nPress Enter to Continue...")

def viewbookdetails():
    if(len(books) != 0):
        for i in books:
            bookname = i["bookName"]
            author = i["author"]
            total = i["total"]
            awailable = i["awailable"]
            print(f"\n{bookname.title()}\nAuthor: {author.title()}\n\nTotal Quantity    : {total}\nBorrowed Quantity : {total-awailable}\nAwailable Quantity: {awailable}")
    else:
        print("\nNo Books Found")
    input("\n\nPress Enter to Continue...")

def reportsort(arr,dictkey,condition):
    temp = sorted(arr,key = lambda x : x [dictkey],reverse = condition)
    return temp
    
def report():
    while(True):
        os.system('cls')
        ch = input("\n1.Quantity Report\n2.Not Borrow Report\n3.Heavy Borrow Report\n4.Outstanding Report\n5.Status of current Book\n6.Exit\n\nEnter Your Choice: ")
        if(ch == "1"):
            temp = reportsort(books,"awailable",False)
            print("\nBook ID\t\tBookName\t\t\tAwailable Quantity\n")
            for i in temp:
                print("{}\t{}\t\t{}".format(i["bookId"].ljust(10," "),i["bookName"].ljust(25," "),i["awailable"]))

        elif(ch == "2"):
            temp = []
            for i in books:
                if(i["borrowed"] == 0):
                    temp.append(i)
            if(len(temp) !=0 ):
                print("\nBook ID\t\tBookName\t\t\tAwailable Quantity\n")
                for i in temp:
                    print("{}\t{}\t\t{}".format(i["bookId"].ljust(10," "),i["bookName"].ljust(25," "),i["awailable"]))
            else:
                print("\nAll Books Are Borrowed At Least One Time")

        elif(ch == "3"):
            temp = []
            for i in books:
                if(i["borrowed"] != 0):
                    temp.append(i)
            if(len(temp) !=0 ):
                print("\nBook ID\t\tBookName\t\t\tBorrows Till Now\n")
                temp = reportsort(temp,"borrowed",True)
                for i in temp:
                    print("{}\t{}\t\t{}".format(i["bookId"].ljust(10," "),i["bookName"].ljust(25," "),i["borrowed"]))
            else:
                print("\nNo Book Borrowals Yet")
        elif(ch == "4"):
            temp = []
            for i in borrow:
                if(i["status"] == "Pending"):
                    temp.append(i)
            if(len(temp)!=0):
                for i in temp:
                    print("\nBorrow Id    : {}\nBorrower Name: {}\nBook Name    : {}\nAuthor Name  : {}\nBorrow date  : {}\nReturned Date: {}\nBook Status  : {}".format(i["borrowId"],i["borrowName"],i["bookName"],i["author"],i["takedate"].strftime("%d/%m/%Y"),i["duedate"].strftime("%d/%m/%Y"),i["status"]))
            else:
                print("\nNo Outstanding Borrowals")
        elif(ch == "5"):

            bp = []
            blp=[]
            blnp =[]
            bookid = input("\nEnter Book ID: ").upper()
            flag =0
            for i in books:
                if(i["bookId"]==bookid):
                    flag = 1
            if(flag == 1):
                for i in borrow:
                    if(i["bookId"] == bookid and i["status"]!="Returned"):
                        if(i["status"] == "Book Lost Amount Paid"):
                            blp.append(i)
                        if(i["status"] == "Pending"):
                            bp.append(i)
                        if(i["status"] == "Book Lost Amount Not Paid"):
                            blnp.append(i)
                if(len(bp)!=0):
                    print("\nPending Borrowals:",len(bp))
                    for i in bp:
                        print("\nBorrow ID   : {}\nBorrower Name: {}\nBorrowed Date: {}\nDue Date     : {}".format(i["borrowId"],i["borrowName"],i["takedate"].strftime("%d/%m/%Y"),i["duedate"].strftime("%d/%m/%Y")))
                else:
                    print("\nNo Pending Borrwals")
                if(len(blp)!=0):
                    print("\nBook Lost And Amount Paid:",len(blp))
                    for i in blp:
                        print("\nBorrow ID    : {}\nBorrower Name: {}\nBorrowed Date: {}".format(i["borrowId"],i["borrowName"],i["takedate"].strftime("%d/%m/%Y")))

                else:
                    print("\nNo Book Lost till Now")
                if(len(blnp)!=0):
                    print("\nBook Lost And Amount Not Paid:",len(blnp))
                    for i in blnp:
                        print("\nBorrow ID    : {}\nBorrower Name: {}\nBorrowed Date: {}".format(i["borrowId"],i["borrowName"],i["takedate"].strftime("%d/%m/%Y")))
            else:
                print("\nInvalid Book ID")
            
        elif(ch == "6"):
            break
        else:
            continue
        input("\nPress Enter to Continue....")

def adminhome():
    os.system('cls')
    print("\tWelcome to Admin Login")
    adminid   = input("\nEnter User ID : ").upper()
    adminpass = input("\nEnter Password: ")
    flag = 0
    for i in admins:
        if(i["adminId"] == adminid and adminpass == i["password"]):
            if(i["status"] == "Approved"):
                flag = 1
                currentadmin = admins.index(i)
            else:
                flag = 2
    if(flag == 1):
         while(True):
            os.system('cls')
            print("\t\1 Welcome Admin {} \1".format(admins[currentadmin]["adminName"].title()))
            ch = input("\n1.Add Borrower\n2.Remove Borrower\n3.Borrower Wallet\n4.Add Book\n5.Edit Book\n6.Reports\n7.Borrow Status Edit\n8.Exit\n\nEnter Your Choice: ")
            if(ch == "1"):
                adduser()
            elif(ch == "2"):
                removeuser()
            elif(ch == "3"):
                updatewallet()
            elif(ch == "4"):
                addbook()
            elif(ch == "5"):
                editbook()
            elif(ch == "6"):
                report()
            elif(ch == "7"):
                borrowstatus()
            elif(ch == "8"):
                break
            else:
                input("\nInvalid Choice\n\nPress Enter to Continue...")
                continue
    elif(flag == 2):
        input("\nYour Account is Blocked\nPlease Contact Admin\n\nPress Enter to Continue...")
    else:
        input("\nInvalid Username or Password\n\nPress Enter to Continue...")

def olduserhome():
    os.system('cls')
    print("\tWelcome to User Login")
    userid   =  input("\nEnter User ID : ").upper()
    userpass = input("\nEnter Password: ")
    flag = 0
    for i in users:
        if(i["userId"] == userid and userpass == i["password"]):
            if(i["status"] == "Approved"):
                flag = 1
                currentuser = users.index(i)
            else:
                flag = 2
    if(flag == 1):
         while(True):
            os.system('cls')
            print("\t\1 Welcome {} \1".format(users[currentuser]["userName"].title()))
            ch = input("\n1.View all Books\n2.Search A Book\n3.Add to Cart\n4.View my Cart\n5.Check Out from Cart\n6.Borrow History\n7.Show Wallet Balance\n8.Exit\n\nEnter Your Choice: ")
            if(ch == "1"):
                viewallbooks(currentuser)
            elif(ch == "2"):
                searchabook(currentuser)
            elif(ch == "3"):
                addtocart(currentuser)
            elif(ch == "4"):
                viewcart(currentuser)
            elif(ch == "5"):
                checkout(currentuser)
            elif(ch == "6"):
                borrowhistory(currentuser)
            elif(ch == "7"):
                print("\nAwailable Wallet Balance:",users[currentuser]["balance"])
                input("\n\nPress Enter to Continue...")
                continue
            elif(ch == "8"):
                break
            else:
                input("\nInvalid Choice\n\nPress Enter to Continue...")
                continue
    elif(flag == 2):
        input("\nYour Account is Blocked\nPlease Contact Admin\n\nPress Enter to Continue...")
    else:
        input("\nInvalid Username or Password\n\nPress Enter to Continue...")

def viewallbooks(currentuser):
    for i in books:
        if(i["awailable"] > 0):
            bookid = i["bookId"]
            bookname = i["bookName"]
            author = i["author"]
            print(f"\nBook Id: {bookid}\n{bookname.title()}\nAuthor : {author.title()}")
    input("\nPress Enter to Continue...")

def searchabook(currentuser):
    while(True):
        os.system('cls')
        print("\tBook Search Page")
        ch = input("\n1.Search Book By Name\n2.Search Book By ID\n3.Exit\n\nEnter Your Choice: ")
        if(ch == "1"):
            os.system('cls')
            print("\tSearch Book By Name")
            bookname = input("\nEnter Book Name: ").lower()
            temp = []
            for i in books:
                if( bookname in i["bookName"].lower()):
                    temp.append(i)
            if(len(temp) != 0):
                for i in temp:
                    bookid = i["bookId"]
                    bookname = i["bookName"]
                    author = i["author"]
                    print(f"\nBook Id: {bookid}\n{bookname.title()}\nAuthor : {author.title()}")
                ch = input("\nPress '1' to Add to Cart\nPress'0' to Continue\n\nEnter Your Choice: ")
                if(ch == "1"):
                    addtocart(currentuser)
                else:
                    continue   
            else:
                input("\nNo Such Book Found\n\nPress Enter to Continue...")
            
        elif(ch == "2"):
            os.system('cls')
            print("\tSearch Book By Book ID")
            bookid = input("\nEnter Book ID: ").upper()
            for i in books:
                if(i["bookId"] == bookid):
                    bookid = i["bookId"]
                    bookname = i["bookName"]
                    author = i["author"]
                    print(f"\nBook Id :{bookid}\n{bookname.title()}\nAuthor: {author.title()}")
                    break
            else:
                input("\nNo Such Book ID Found\n\nPress Enter to Continue...")
            ch = input("\nPress '1' to Add to Cart\nPress'0' to Continue\n\nEnter Your Choice: ")
            if(ch == "1"):
                addtocart(currentuser)
            else:
                continue

        elif(ch == "3"):
            break
        
        else:
            input("\nInvalid Choice\n\nPress Enter to Continue...")
            continue

def addtocart(currentuser):

    bookid = input("\nEnter Book Id to ADD to Cart: ").upper()
    flag = 0
    for i in books:
        if(i["bookId"] == bookid):
            flag = 1
            currentbook = books.index(i)
    if(flag == 1):
        flag1 = 0  
        for i in users[currentuser]["cart"]:
            if(i["bookId"] == bookid):
                flag1 = 1
        flag2 = 0
        for i in borrow:
            if(i["bookId"] == bookid and i["status"] == "Pending"):
                flag2 = 1
        if(len(users[currentuser]["cart"]) < 3):
            if(flag1 == 0 and flag2 == 0):
                users[currentuser]["cart"].append(books[currentbook])
                input("\nBook Added To Cart\n\nPress Enter to Continue...")
            elif(flag1 == 1 and flag2 == 0 ):
                input("\nThis Book Already Present In Cart\nYou Can't Add this Book to Cart\n\nPress Enter to Continue...")
            elif(flag1 == 0 and flag2 == 1):
                input("\nYou Still Not Returned This Book\nYou Can't Add this Book to Cart\n\nPress Enter to Continue...")
            elif(flag1 == 1 and flag2 == 1):
                input("\nYou Still Not Returned This Book\nAnd This Book is Already In Your Cart\nYou Can't Add this Book to Cart\n\nPress Enter to Continue...")
        else:
            input("\nMaximun Cart Limit Reached\nYou Can't Add Books\n\nPress Enter to Continue...")
    else:
        input("\nBook Not Found\n\nPress Enter to Continue...")

def viewcart(currentuser):
    temp = []
    for i in users[currentuser]["cart"]:
        temp.append(i)
    if(len(temp) != 0):
        a = 1
        for i in temp:
            bookid = i["bookId"]
            bookname = i["bookName"]
            author = i["author"]
            print(f"\n{a}.Book Id :{bookid}\n  {bookname.title()}\n  Author: {author.title()}")
            a += 1
        ch = input("\nPress '1' to Remove a Book from Cart\nPress '0' to Continue\n\nEnter Your Choice: ")
        if(ch == "1"):
            serial = int(input("\nEnter Serial No. to Remove: "))
            if(serial - 1 < len(users[currentuser]["cart"])):
                users[currentuser]["cart"].pop(serial-1)
                input("\nBook Removed From Cart\n\nPress Enter to Continue...")
            else:
                input("\nInvalid Serial Number\n\nPress Enter to Continue...")
    else:
        input("\nCart is Empty\n\nPress Enter to Continue...")

def checkout(currentuser):
    global new_borrow
    temp = []
    for i in users[currentuser]["cart"]:
        temp.append(i)
    if(len(temp) != 0):
        a = 1
        for i in temp:
            bookid = i["bookId"]
            bookname = i["bookName"]
            author = i["author"]
            print(f"\n{a}.Book Id :{bookid}\n  {bookname.title()}\n  Author: {author.title()}")
            a += 1
    else:
        input("\nCart is Empty\n\nPress Enter to Continue...")

    userid = users[currentuser]["userId"]
    if len(users[currentuser]["cart"])!=0:
        ch = input("\nPress '1' to Checkout\nPress '0' to Exit\n\nEnter Your Choice: ")
        if(ch == "1"):
            if(users[currentuser]["balance"] >= 500):
                for i in users[currentuser]["cart"]:
                    username = users[currentuser]["userName"]
                    currentbook = books.index(i)
                    bookid = i["bookId"]
                    bookname = i["bookName"]
                    author = i["author"]
                    new_borrow = str(int(new_borrow)+1)
                    takedate = datetime.date.today()
                    duedate = takedate+datetime.timedelta(days=3)
                    borrow.append({"borrowId":new_borrow,"bookId":bookid,"userId":userid,"bookName":bookname,"author":author,"status":"Pending","takedate":takedate,"duedate":duedate,"returndate":0,"fine":0,"borrowName":username})
                    books[currentbook]["awailable"] -= 1
                    books[currentbook]["borrowed"] += 1
                    print("\nBorrow Id: {}\nBook Name: {}".format(new_borrow,bookname))
                users[currentuser]["cart"] = []
                input("\nBook Borrowed\n\nPress Enter to Continue...")
            else:
                input("Not Enough Amount In You Library Account\n\nPress Enter to Continue...")
    
def borrowhistory(currentuser):
    userid = users[currentuser]["userId"]
    temp = []
    for i in borrow:
        if(i["userId"] == userid):
            temp.append(i)
    if(len(temp)!=0):
        for i in temp:
            if(i["status"] == "Received"):       
                print("\nBorrow Id    : {}\nBook Name    : {}\nAuthor Name  : {}\nBorrow date  : {}\nReturned Date: {}\nBook Status  : {}".format(i["borrowId"],i["bookName"],i["author"],i["takedate"].strftime("%d/%m/%Y"),i["returndate"].strftime("%d/%m/%Y"),i["status"]))
            elif(i["status"] == "Pending"):
                print("\nBorrow Id  : {}\nBook Name  : {}\nAuthor Name: {}\nBorrow date: {}\nDue Date   : {}\nBook Status: {}".format(i["borrowId"],i["bookName"],i["author"],i["takedate"].strftime("%d/%m/%Y"),i["duedate"].strftime("%d/%m/%Y"),i["status"]))
            else:
                print("\nBorrow Id  : {}\nBook Name  : {}\nAuthor Name: {}\nBorrow date: {}\nBook Status: {}".format(i["borrowId"],i["bookName"],i["author"],i["takedate"].strftime("%d/%m/%Y"),i["status"]))
    else:
        print("\nNo Borrow Till Now")
    input("\n\nPress Enter to Continue...")


while(True):
    os.system('cls')
    print("\n\t\3 Welcome \3")
    ch = input("\n1.Main Admin\n2.Admins\n3.Users\n4.Exit\n\nEnter Your Choice: ")
    if(ch == "1"):
        mainadminhome()
    elif(ch == "2"):
        adminhome()
    elif(ch == "3"):
        olduserhome()
    elif(ch == "4"):
        os.system('cls')
        print("\nThank You...\3")
        break
    else:
        input("\nInvalid Choice\n\nPress Enter to Continue...")
