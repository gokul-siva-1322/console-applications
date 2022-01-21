                              
                                                        #RAILWAY TICKET BOOKING
import os

new_user_id = "1"
new_train_id = "5002"
new_referance_id = "1"


trains = [
{"trainId":"5001","stops":6,"seats":10,"bookings":[[0 for i in range(6)] for j in range(10)],"wait":"Approved", "stopNames":["Coimbatore","Tirupur","Erode","Salem","Villupuram","Chennai"]},
{"trainId":"5002","stops":7,"seats":15,"bookings":[[0 for i in range(7)] for j in range(15)],"wait":"Approved", "stopNames":["Kanyakumari","Tirunelveli","Thuthukudi","KovilPatti","Sathur","Madurai","Kangeyam"]}
]

bookings = [
{"referenceId":"1", "userId":"1", "trainId":"5001","board":1, "desti":4, "ticketCount":2,"status":"Booked","allocated":[]}
]

users = [
{"userId":"1","password":"1234","userName":"Arun"}
]

def adminhome(): #Admin Home

    os.system('cls')
    print("\tWelcome To Admin Portal")
    adminname = input("\nEnter Username: ")
    adminpass = input("\nEnter Password: ")
    if(adminname == "admin" and adminpass == "1234"):
        while(True):
            os.system('cls')
            print("\tWelcome To Admin Portal")
            ch = input("\n1.Add Trains\n2.Edit Trains\n3.Exit\n\nEnter Your Choice: ")
            if(ch == "1"):
                addtrains()
            elif(ch == "2"):
                edittrain()
            elif(ch == "3"):
                break
            else:
                continue
    else:
        input("\nInvalid Username or Password\n\nPree Enter to Continue...")

def addtrains():# Add New Train

    global new_train_id
    print("\n\tNew Train Registeration")
    trainid = str(int(new_train_id)+1)
    new_train_id = trainid
    print("\nAuto Generated Train Id:",trainid)
    seats = int(input("\nEnter No of Seats In Train: "))
    stops = int(input("\nEnter No of Stops In Train: "))
    booking = [[0 for i in range(stops)] for j in range(seats)]
    stopnames = []
    for i in range(stops):
        ch = input("\n{}.Enter Stop Name: ".format(i+1))
        stopnames.append(ch)
    trains.append({"trainId":trainid,"stops":stops,"seats":seats,"bookings":booking,"wait":"Approved", "stopNames":stopnames})
    input("\nNew Train Added\n\nPress Enter to Continue...")
    
def edittrain(): #Edit Train
    print("\n\tEdit Train")
    
    trainid = input("\nEnter Train Id: ")
    for i in trains:
        if(i["trainId"] == trainid):
            currenttrain = findmytrain(trainid)
            flag = 1
            break
    else:
        flag = 0
    if(flag == 1):
        while(True):
            os.system('cls')
            print("\tEdit {} Train Details".format(trainid))
            ch = input("\n1.Edit Train Seats\n2.Edit Train Stops\n3.Edit Train Status\n4.Exit\n\nEnter Your Choice: ")
            if(ch == "1"):
                oldseatnum = trains[currenttrain]["seats"]
                oldstopnum = trains[currenttrain]["stops"]
                print(trains[currenttrain]["bookings"],sep="\n")
                print([[0 for i in range(oldstopnum)] for j in range(oldseatnum)],sep="\n")
                print("seat,stop",oldseatnum,oldstopnum)
                if(trains[currenttrain]["bookings"] == [[0 for i in range(oldstopnum)] for j in range(oldseatnum)]):
                    print("\nCurrent Seat Count:",oldseatnum)
                    newseatnum = int(input("\nEnter New Seat Count: "))
                    trains[currenttrain]["seats"] = newseatnum
                    booking = [[0 for i in range(oldstopnum)] for j in range(newseatnum)]
                    trains[currenttrain]["bookings"] = booking
                    print(trains[currenttrain])
                    input("\nTrain Seat Count Updated\n\nPress Enter to Continue...")

                else:
                    input("\nTrain is not Empty!\nYou Can Update When No Bookings Awailable\n\nPress Enter to Continue...")
            elif(ch == "2"):
                oldseatnum = trains[currenttrain]["seats"]
                oldstopnum = trains[currenttrain]["stops"]
                if(trains[currenttrain]["bookings"] == [[0 for i in range(oldstopnum)] for j in range(oldseatnum)]):
                    print("\nCurrent Stop Count:",oldseatnum)
                    newstopnum = int(input("\nEnter New Stop Count: "))
                    l = []
                    s = 1
                    for i in range(newstopnum):
                        ch = input("\n{}.Enter Stop Name: ".format(s))
                        l.append(ch)
                        s += 1
                    trains[currenttrain]["stops"] = newstopnum
                    booking = [[0 for i in range(newstopnum)] for j in range(oldseatnum)]
                    trains[currenttrain]["bookings"] = booking
                    trains[currenttrain]["stopNames"] = l
                    input("\nTrain Seat Count Updated\n\nPress Enter to Continue...")
                else:
                    input("\nTrain is not Empty!\nYou Can Update When No Bookings Awailable\n\nPress Enter to Continue...")
            elif(ch == "3"):
                print("\nTrain Current Status:",trains[currenttrain]["wait"])
                a = input("\n1.Approved\n2.Removed\n\nEnter Your Choice: ")
                if(a == "1"):
                    trains[currenttrain]["wait"] = "Approved"
                elif(a == "2"):
                    trains[currenttrain]["wait"] = "Removed"
                print("\nStatus Changed Sucessfully")
                input("\nPress Enter to Continue...")
            elif(ch == "4"):
                break
            else:
                continue
    else:
        print("\nNo Train Found")
        input("\nPress Enter to Continue...")

def userhome(): #User Home

    while(True):
        os.system('cls')
        print("\tWelcome To User Portal")
        ch = input("\n1.New User\n2.Existing User\n3.Exit\n\nEnter Your Choice: ")
        if(ch == "1"):
            newuser()
        elif(ch == "2"):
            olduser()
        elif(ch == "3"):
            break

def newuser(): #New User Home

    os.system('cls')
    global new_user_id
    new_user_id = str(int(new_user_id)+1)
    print("\tWelcome To User Sign Up\n\nYour Auto-Genetared User Id: {}".format(new_user_id))
    username = input("\nEnter Username: ")
    password = input("\nEnter Password: ")
    users.append({"userId":new_user_id,"password":password,"userName":username,"mybookings":[]})
    input("\nYour Registerations Was Sucessful\n\nPress Enter to Continue...")

def olduser(): #Olduser Home

    os.system('cls')
    print("\tWelcome To User Sign Up")
    userid = input("\nEnter User Id : ")
    userps = input("\nEnter Password: ")
    for i in users:
        if(i["userId"] == userid and i["password"] == userps):
            currentuser = users.index(i)
            while(True):
                os.system('cls')
                print("\tWelcome",i["userName"].title())
                ch = input("\n1.Book tickets\n2.Seat Awailability Check\n3.Cancelations\n4.Check Ticket satus\n5.Exit\n\nEnter Your Choice: ")
                if(ch == "1"):
                    bookticket(users[currentuser]["userId"])
                elif(ch == "2"):
                    checkseatawailability(0)
                elif(ch == "3"):
                    cancelticket(users[currentuser]["userId"])
                elif(ch == "4"):
                    checkstatus(users[currentuser]["userId"])
                elif(ch != "1" and ch != "2" and ch != "3" and ch != "4" and ch != "5"):
                    input("\nInvalid Choice\n\nPree Enter to Continue...")
                    continue
                elif(ch == "5"):
                    break
            break
    else: 
        input("\nUser Not Found\n\nPree Enter to Continue...")

def showalltrains(): #Show All Trains
    for i in trains:
        if(i["wait"] == "Approved"):
            print("\nTrain Id: {}\nFrom {} to {}".format(i["trainId"],i["stopNames"][0],i["stopNames"][-1]))

def findmytrain(trainid): #Find My Train
    for i in trains:
        if(i["trainId"] == trainid):
            current = trains.index(i)
    return current

def bookticket(userid):#Book Ticket

    global new_referance_id
    l = checkseatawailability(1)
    awailable_seates = l[0]
    board = l[1]
    desti = l[2]
    current = l[3]
    flag = l[4]
    if(flag == 1):
        reqseats = int(input("\nEnter Number of Tickets: "))    
        if(reqseats > len(awailable_seates)):
            print("\nInsufficient Seats")
        else:
            seats_allocated = []
            new_referance_id = str(int(new_referance_id)+1)
            for i in range(reqseats):
                seats_allocated.append(awailable_seates[i])
                for j in range(board,desti):
                    trains[current]["bookings"][awailable_seates[i]-1][j] = new_referance_id
            bookings.append({"referenceId":new_referance_id, "userId":userid, "trainId":trains[current]["trainId"],"board":board, "desti":desti, "ticketCount":reqseats,"status":"Booked","allocated":seats_allocated})
            print("\nSuccessfully Reserved with Reference No :", new_referance_id)
        input("\nPress Enter to Continue...")
    elif(flag == 0):
        count = 0
        for i in bookings:
            if(i["trainId"] == trains[current]["trainId"] and i["status"] == "Waiting"):
                count += 1
        if(count < 6):
            new_referance_id = str(int(new_referance_id)+1)
            reqseats = int(input("\n\nEnter Number of Tickets: "))
            print("\nBooking fulls\nYour added to Waiting list")
            bookings.append({"referenceId":new_referance_id, "userId":userid, "trainId":trains[current]["trainId"],"board":board, "desti":desti, "ticketCount":reqseats,"status":"Waiting","allocated":[]})
            print("\n\nIf any Cancelations You'll be Added To Booked List\nCheck You Ticket Status Regularlly")
        else:
            print("\nBoth Booking and Waiting list are fulls")
        input("\n\nPress Enter to Continue...")

def checkseatawailability(a): #Check Seat Awailability

    os.system('cls')
    print("\tAll Trains")
    showalltrains()
    trainid = input("\nEnter Train Id to Start Booking: ")
    current = findmytrain(trainid)
    stopnumb = 1
    for i in trains[current]["stopNames"]:
        print("{}.{}".format(stopnumb,i))
        stopnumb += 1
    board = int(input("\nEnter Bording Point    : ")) - 1
    desti = int(input("\nEnter Destination Point: ")) - 1
    awailable_seates = []
    if(desti < board):
        print("\nInvalid Data")
    else:
        for i in range(trains[current]["seats"]):
            if(trains[current]["bookings"][i][board : desti] == [0 for i in range(desti-board)]):
                awailable_seates.append(i+1)
    if(len(awailable_seates) == 0):
        print("\nNo Seats Awailable")
        flag = 0
    else:
        flag = 1
        print("\nAwailable Seats:",*awailable_seates)
    if(a == 0):
        input("\nPress Enter to Continue...")
    else:
        return [awailable_seates,board, desti, current, flag]

def cancelticket(userid): #Cancel Ticket
    os.system('cls')
    print("\tTicket Cancelation Portal")
    refid = input("Enter Reference Id: ")
    flag = 0
    for i in bookings:
        if(i["referenceId"] == refid and i["userId"] == userid):
            currentbook = bookings.index(i)
            flag = 1
            break
    else:
        input("Reference Id Not Found\n\nPress Enter to Continue...")
    if(flag == 1):
        trainid = bookings[currentbook]["trainId"]
        for i in trains:
            if(i["trainId"] == trainid):
                currenttrain = trains.index(i)
        board = bookings[currentbook]["board"]
        board1 = trains[currenttrain]["stopNames"][board]
        desti = bookings[currentbook]["desti"]
        desti1 = trains[currenttrain]["stopNames"][desti]
        reserved_seats = bookings[currentbook]["allocated"]
        print("\nTrain Id: {}\nFrom {} to {}\nNo.of Tickets : {}".format(trainid,board1,desti1,bookings[currentbook]["ticketCount"]))
        ch = input("\nIs these Details are Correct (Y/N):")
        if(ch in ["y","Y"]):
            for i in range(bookings[currentbook]["ticketCount"]):
                for j in range(board,desti):
                    trains[currenttrain]["bookings"][reserved_seats[i]-1][j] = 0
            bookings[currentbook]["status"] = "Canceled"
            input("\nTickets Canceled Sucessfully\nPress Enter To Continue...")
        else:
            input("\nTickets Cancelation Canceled\nPress Enter To Continue...")

        #Waiting Auto Booking
        
        for i in bookings:
            if(i["status"] == "Waiting"):
                awailable_seats = []
                board = i["board"]
                desti = i["desti"]
                for j in range(trains[currenttrain]["seats"]):
                    if(trains[currenttrain]["bookings"][j][board : desti] == [0 for j in range(desti-board)]):
                        awailable_seats.append(j+1)
                if(len(awailable_seats) >= i["ticketCount"]):
                    seats_allocated = []
                    for k in range(i["ticketCount"]):  
                        seats_allocated.append(awailable_seats[k])
                        for l in range(board,desti):
                            trains[currenttrain]["bookings"][awailable_seats[k]-1][l] = i["referenceId"]
                    i["status"] = "Booked"
                    i["allocated"] += seats_allocated

def checkstatus(userid): #Check Ticket Status
    referenceid = input("\nEnter Your Reference Id: ")
    for i in bookings:
        if(i["referenceId"] == referenceid and i["userId"] == userid):
            currentbook = bookings.index(i)
            trainid = bookings[currentbook]["trainId"]
            for train in trains:
                if(train["trainId"] == trainid):
                    currenttrain = trains.index(train)
                    board = trains[currenttrain]["stopNames"][bookings[currentbook]["board"]]
                    desti = trains[currenttrain]["stopNames"][bookings[currentbook]["desti"]]
                    print("\nTrain Id: {}\nFrom {} to {}\nNo.of Tickets : {}\nTicket Status : {}".format(trainid,board,desti,bookings[currentbook]["ticketCount"],bookings[currentbook]["status"]))
                    print("Seat Allocated:",*bookings[currentbook]["allocated"])
                    input("\n\nPress Enter to Continue...")
                    break
            break
    else:
        input("No such Reference Id found\n\nPress Enter to Continue...")

while(True): #Main While Loop
    os.system('cls')
    print("\tWelcome To Railway Ticket Booking")
    ch = input("\n1.Admin\n2.User\n3.Exit\n\nEnter Your Choice: ")
    if(ch == "1"):
        adminhome()
    elif(ch == "2"):
        userhome()
    elif(ch == "3"):
        os.system('cls')
        print("\n\1Thanks For Using App\1")
        break
    else:
        input("Invalid Choice\n\nPress Enter to Continue...")
        continue
