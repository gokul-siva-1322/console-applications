                                
                                        #AMAZON CONSOLE APPLICATION
import os

new_user_Id="5001"

new_product_Id="1003"

new_order_id = "7001"

products=[
{"merchantId":"1","productId":"1001","productName":"iPhone","price":50000,"discount":10,"stock":10,"sale":0,"profit":0},
{"merchantId":"2","productId":"1001","productName":"iPhone","price":15000,"discount":50,"stock":10,"sale":0,"profit":0},
{"merchantId":"3","productId":"1001","productName":"iPhone","price":25000,"discount":30,"stock":10,"sale":0,"profit":0},
{"merchantId":"1","productId":"1002","productName":"Mac Book Pro","price":30000,"discount":10,"stock":10,"sale":0,"profit":0},
{"merchantId":"2","productId":"1002","productName":"Mac Book Pro","price":17000,"discount":50,"stock":10,"sale":0,"profit":0},
{"merchantId":"3","productId":"1002","productName":"Mac Book Pro","price":5000,"discount":30,"stock":10,"sale":0,"profit":0},
{"merchantId":"1","productId":"1003","productName":"Apple Watch","price":10000,"discount":10,"stock":10,"sale":0,"profit":0},
{"merchantId":"2","productId":"1003","productName":"Apple Watch","price":95000,"discount":50,"stock":10,"sale":0,"profit":0},
{"merchantId":"3","productId":"1003","productName":"Apple Watch","price":55000,"discount":30,"stock":10,"sale":0,"profit":0}
]


merchants=[
{"merchantId":"1","merchantName":"aaditi","password":"1234","merchantStatus":"Approved","merchantprofit":1000},
{"merchantId":"2","merchantName":"vijay","password":"1234","merchantStatus":"Approved","merchantprofit":1000},
{"merchantId":"3","merchantName":"abarna","password":"1234","merchantStatus":"Approved","merchantprofit":1000},
]

users=[
{"userId":"5001","userName":"siva","password":"1234", "cart":[],"balance":24500}
]

orders=[
{"orderId":"7001","merchantId":"1","userId":"5001","productId":"1001","productName":"iPhone 5s","orderstatus":"Received","itemsneed":3,"paid":2400,"review":["* * * * ","Good Product"]}
] 

merchantsAproval=[]

def productfinder(merchid,productid):
    for i in products:
        if(i["merchantId"]==merchid and i["productId"]==productid):
            return products.index(i)
    return "-1"

def addproducts(merchid):
    global new_product_Id
    print("\nEnter New Product Details\n")
    productname=input("Enter Product Name    : ")
    productprice=int(input("Enter Product Price   : "))
    productstock=int(input("Enter Product Stock   : "))
    productdiscount=int(input("Enter Product Discount: "))
    for i in products:
        if(i["productName"]==productname):
            productid=i["productId"]
            break
    else:
        productid=str(int(new_product_Id)+1)
        new_product_Id=productid
    if(productfinder(merchid,productid)!="-1"):
        input("\n\nProduct Already Exists\n\nPress Enter to Continue...")
    else:
        products.append({"merchantId":merchid,"productId":productid,"productName":productname,"price":productprice,"discount":productdiscount,"stock":productstock,"sale":0,"profit":0})
        print("\nYour Product Id:",productid)
        input("\n\nProduct Added Sucessfully\n\nPress Enter to Continue...")

def removeproduct(merchid):
    global products
    temp = products
    productid=input("Enter the Product Id to remove Product: ")
    for i in products:
        if(i["merchantId"]==merchid and productid==i["productId"]):
            temp.remove(i)
    products=temp
    input("\n\nProduct Removed Sucessfully\n\nPress Enter to Continue...")
    
def showmyproducts(merchid):
    for i in products:
        if(i["merchantId"]==merchid):
            print("\nProduct Id   : {}\nProduct Name : {}\nProduct Price: {}\nProduct Stock: {}\nProduct offer: {}%".format(i["productId"],i["productName"],i["price"],i["stock"],i["discount"]))
    input("\n\nPress Enter to continue...")

def updatemerchantproducts(merchid):
    while(True):
        os.system('cls')
        print("\tWelcome to Merchant product Updation")
        choice=input("\n1.Update Stock\n2.Update Discount\n3.Update Price\n4.Exit\n\nEnter Your Choice: ")
        if(choice=="4"):
                break
        os.system('cls')
        productid=input("Enter Product Id: ")
        current=productfinder(merchid,productid)
        if(current!="-1"):
            if(choice=="1"):
                print("Product Name: {}\nCurrent Stock: {}".format(products[current]["productName"],products[current]["stock"]))
                up_stock=int(input("Enter No of Stock to Added: "))
                products[current]["stock"]+=up_stock
                input("\nStock Updated Sucessfully\nPress Enter to continue")
            elif(choice=="2"):
                print("Product Name: {}\nCurrent Discount: {}".format(products[current]["productName"],products[current]["discount"]))
                up_diccount=int(input("Enter New discount percentage: "))
                products[current]["discount"]=up_diccount
                input("\nDiscount Updated Sucessfully\nPress Enter to continue")
            elif(choice=="3"):
                print("Product Name: {}\nCurrent price: {}".format(products[current]["productName"],products[current]["price"]))
                up_price=int(input("Enter New price: "))
                products[current]["price"]=up_price
                input("\nPrice Updated Sucessfully\nPress Enter to continue")
            else:
                input("\n\tInvalid Choice\nPress Enter to Continue....")
                continue
        else:
            input("\nNo Such Product Exists\nPress Enter to continue...")
            continue

def compareproducthome():
    while(True):
        os.system('cls')
        print("\nProduct Compare Portal")
        choice = input("\n1.Compare Product Price\n2.Compare Product Discounts\n3.Compare Best offers\n4.Exit\n\nEnter Your Choice: ")
        if(choice=="1"):
            productid=(input("\nEnter Your Product's Id to Compare: "))
            compareproducts(productid,"-1","price",False)
            input("\nPress Enter to Continue....")
        elif(choice=="2"):
            productid=(input("\nEnter Your Product's Id to Compare: "))
            compareproducts(productid,"-1","discount",True)
            input("\nPress Enter to Continue....")
        elif(choice=="3"):
            productid=(input("\nEnter Your Product's Id to Compare: "))
            compareproducts(productid,"0","0",False)
            input("\nPress Enter to Continue....")
        elif(choice=="4"):
            break                          
        else:
            input("\n\tInvalid Choice\nPress Enter to Continue....")
            continue

def compareproducts(productid,choice,tosort,condition):
    temp=[]
    for i in products:
        if(i["productId"]==productid):
            temp.append(i)
    if(len(temp)!=0):
        if(choice=="-1"):
            temp=sorted(temp,key = lambda X : X [tosort], reverse=condition)
            for i in temp:
                print("\nProduct Id\tProduct Name\tProduct Price\tProduct Discount\t")
                print(*[i["productId"],i["productName"],i["price"],i["discount"]],sep="\t\t")
        else:
            for i in range(len(temp)):
                bestoff=(temp[i]["price"]-((int(temp[i]["discount"]/100))*temp[i]["price"]))
                temp[i]["bestoff"]=bestoff
            temp=sorted(temp,key = lambda X : X ["bestoff"], reverse=False)
            for i in temp:
                print("\nProduct Id\tProduct Name\tProduct Price\tProduct Discount\t")
                print(*[i["productId"],i["productName"],i["price"],i["discount"]],sep="\t\t")
    else:
        input("\nNo Such Product Exists\nPress Enter to continue...")
  
def showallmerchants():
    if(len(merchants)>0):
        for i in merchants:
            print("\nMerchant Id    : {}\nMerchant Name  : {}\nMerchant Status: {}\n".format(i["merchantId"],i["merchantName"],i["merchantStatus"]))
    else:
        print("\nNo Merchants found")
    input("\nPress Enter to continue")

def check(id,arr):
    for i in arr:
        if(id == i["merchantId"]):
            return True
    return False

def aproveproductrequest(merchid):
    for i in orders:
        if(i["merchantId"] == merchid and (i["orderstatus"]!="Received" and i["orderstatus"]!="Canceled")):
            current = orders.index(i)
            print("\nOrder Id, Product Name: {}, {}\nNo.of Items Required: {}\nOrder Status: {}".format(i["orderId"],i["productName"],i["itemsneed"],i["orderstatus"]))
            choice = input("\nIf order in Packing Press '1'\nIf order is Dispatched Press '2'\nIf order is Received Press '3'\n\nEnter Your Choice: ")
            if(choice=="1"):
                i["orderstatus"] = "Packing"
                input("\nOrder Status Updated Sucessfully!\nPress Enter to continue")
            elif(choice=="2"):
                i["orderstatus"] = "Dispatched"
                input("\nOrder Status Updated Sucessfully!\nPress Enter to continue")
            elif(choice=="3"):
                i["orderstatus"] ="Received"
                input("\nOrder Status Updated Sucessfully!\nPress Enter to continue")
    input("\nNo Pending Aprovals")

def merchantproductprofits(merchid, current):
    print("\nOverall Merchat Profit:",merchants[current]["merchantprofit"])
    for i in products:
        if(i["merchantId"]==merchid):
            print("\nProduct Id    : {}\nProduct Name  : {}\nProduct Sales : {}\nProduct Profit: {}".format(i["productId"],i["productName"],i["sale"],i["profit"]))
    input("\nPress Enter to Continue...")

def showallproducts():
    for i in products:
        if(i["stock"]!=0):
            yousave = int((i["discount"] / 100) * i["price"])
            offerprice= i["price"] - yousave
            print("\n{}.Merchant Id & Product Id   : {} & {}\n  Product Name : {}\n  Product Price: {}\n  Product Stock: {}\n  Product offer: {}%\n  You save     : {}\n  You Pay      : {}".format(products.index(i)+1,i["merchantId"],i["productId"],i["productName"],i["price"],i["stock"],i["discount"],yousave,offerprice))

def viewmycart(current):
    print("\n\tMy Cart Items\n")
    temp = users[current]["cart"]
    if(len(temp)!=0):
        for i in temp:
            yousave = int((i["discount"] / 100) * i["price"])
            offerprice= i["price"] - yousave
            print("\n{}.Product Id   : {}\n  Product Name : {}\n  Product Price: {}\n  Product offer: {}%\n  You save     : {}\n  You Pay      : {}\n\n  No of Items : {}".format(temp.index(i)+1,i["productId"],i["productName"],i["price"],i["discount"],yousave,offerprice,i["noofitems"]))
    else:
        print("No Items in Cart Now...")

def carthome(current):
    global products
    while(True):
        os.system('cls')
        choice = input("\tCart options\n\n1.View my Cart\n2.Add to Cart\n3.Edit Cart Item\n4.Remove Item from Cart\n5.Exit\n\nEnter Your Choice: ")
        if(choice == "1"):
            viewmycart(current)
            input("\n\nPress Enter To Continue...")
            continue
        elif(choice == "2"):
            print("\n\tProduct Home")
            showallproducts()
            merchid, productid = map(str,input("\nEnter The Merchant Id and Product Id of the Product: ").split())
            for i in products:
                if(i["merchantId"] == merchid and i["productId"] == productid):
                    noofitems = int(input("Enter No of Items To Be added to Cart: "))
                    users[current]["cart"].append({"merchantId":merchid,"productId":productid,"productName":i["productName"],"price":i["price"],"discount":i["discount"],"noofitems":noofitems})
                    input("\n\nProduct Added to Cart\n\nPress Enter to Continue...")
                    break
            else:
                input("\n\nNo Product found\n\nPress Enter to Continue...")
                continue   

        elif(choice == "3"):

            viewmycart(current)
            indexno = int(input("\n\nEnter the Serial.No Item to edit: ")) -1
            if(indexno < indexno+1):
                d = users[current]["cart"][indexno]
                yousave = int((d["discount"] / 100) * d["price"])
                offerprice= d["price"] - yousave
                print("\nProduct Id   : {}\n  Product Name : {}\n  Product Price: {}\n  Product offer: {}%\n  You save     : {}\n  You Pay      : {}\n\n  No of Items : {}".format(d["productId"],d["productName"],d["price"],d["discount"],yousave,offerprice,d["noofitems"]))
                new_no = int(input("\nEnter New No of Items You Want: "))
                users[current]["cart"][indexno]["noofitems"] = new_no
            else:
                input("\n\nNo Product found\n\nPress Enter to Continue...")

        elif(choice == "4"):

            viewmycart(current)
            indexno = int(input("\n\nEnter the Serial.No of Item to delet: ")) -1
            if(indexno < indexno+1):
                d = users[current]["cart"][indexno]
                yousave = int((d["discount"] / 100) * d["price"])
                offerprice= d["price"] - yousave
                print("\nProduct Id   : {}\n  Product Name : {}\n  Product Price: {}\n  Product offer: {}%\n  You save     : {}\n  You Pay      : {}\n\n  No of Items : {}".format(d["productId"],d["productName"],d["price"],d["discount"],yousave,offerprice,d["noofitems"]))
                users[current]["cart"].pop(indexno)
                input("\n\nProduct Removed from Cart\n\nPress Enter to Continue...")
            else:
                input("\n\nNo Product found\n\nPress Enter to Continue...")

        elif(choice == "5"):
            break
        else:
            continue
    
def placeanorder(merchid,productid,itemsneed,userid,serial):
    global new_order_id
    flag=0
    for mer in merchants:
        if(mer["merchantId"]==merchid):
            currentmerch_index=merchants.index(mer)
    for i in products:
        if(i["merchantId"]==merchid and i["productId"]==productid):
            currentproduct_index = products.index(i)
            currentproduct=i
            flag=1
            if(itemsneed <= i["stock"]):
                flag =2
                yousave = int((i["discount"] / 100) * i["price"])
                offerprice = i["price"] - yousave
                for j in users:
                    if(j["userId"] == userid and j["balance"] >= offerprice * itemsneed):
                        currentuser_index=users.index(j)
                        currentuser = j
                        flag = 3
                        id=str(int(orders[-1]["orderId"])+1)
                        new_order_id +=str(int(new_order_id)+1)
    if(flag==3):
        orders.append({"orderId":id,"merchantId":merchid,"userId":userid,"productId":productid,"productName":currentproduct["productName"],"orderstatus":"Pending","itemsneed":itemsneed,"paid":offerprice * itemsneed,"review":[]})
        products[currentproduct_index]["stock"] -= itemsneed
        products[currentproduct_index]["sale"] += itemsneed
        users[currentuser_index]["balance"] -=  offerprice * itemsneed
        products[currentproduct_index]["profit"] = offerprice * itemsneed
        merchants[currentmerch_index]["merchantprofit"] += offerprice * itemsneed
        if(serial!='-1'):
            users[currentuser_index]["cart"].pop(serial)
        input("Order placed Sucessfully\nAwailable Wallet Balance: {}\n\nPress Enter To continue...".format(users[currentuser_index]["balance"]))
    elif(flag==2):
        input("Less Wallet Balance\n\nPress Enter to Continue...")
    elif(flag==1):
        print("Awailable Stock: ",currentproduct["stock"])
        input("Less stock Enter No. of Items below stock\n\nPress Enter to Continue...")
    else:
         input("\n\nNo Product or Merchant found\n\nPress Enter to Continue...")

def viewmyorders(userid,orderstatus):
    print("\n\tMy Ordered Items\n")
    temp=[]
    for i in orders:
        if(i["userId"]==userid and i["orderstatus"]==orderstatus):
            temp.append(i)
    if(len(temp)!=0):
        for i in temp:
            print("\nOrder Id   : {}\nProduct Id   : {}\nProduct Name : {}\nYou Payed    : {}\nItems count : {}\n\nOrder Status: {}".format(i["orderId"],i["productId"],i["productName"],i["paid"],i["itemsneed"],i["orderstatus"]))
        cancel = input("\nTo cancel an order An order press '1' or Press '0' ")
        if(cancel=="1"):
            orderid = input("Enter Order Id to cacel: ")
            for i in orders:
                if(i["orderId"]==orderid):
                    currentorder=orders.index(i)
                    break
            orders[currentorder]["orderstatus"] = "Canceled"
            merchid = orders[currentorder]["merchantId"]
            productid = orders[currentorder]["productId"]
            itemsneed = orders[currentorder]["itemsneed"]
            paid = orders[currentorder]["paid"]
            for i in merchants:
                if(i["merchantId"]==merchid):
                    currentmerch = merchants.index(i)
                    break
            for i in users:
                if(i["userId"]==userid):
                    currentuser = users.index(i)
                    break
            for i in products:
                if(i["productId"]==productid and i["merchantId"]==merchid):
                    currentproduct=products.index(i)
                    break
            products[currentproduct]["stock"] += itemsneed
            products[currentproduct]["sale"] -= itemsneed
            users[currentuser]["balance"] +=  paid
            products[currentproduct]["profit"] -= paid
            merchants[currentmerch]["merchantprofit"] -= paid
            input("fg")
            
    else:
        print("No Orders Till Now...")

def vieworderhistory(userid):
    print("\n\tMy Ordered Items\n")
    temp=[]
    for i in orders:
        if(i["userId"]==userid and (i["orderstatus"]=="Depatched" or i["orderstatus"]=="Received")):
            temp.append(i)
    if(len(temp)!=0):
        for i in temp:
            print("\nOrder Id   : {}\nProduct Id   : {}\nProduct Name : {}\nYou Payed    : {}\nItems count : {}\n\nOrder Status: {}".format(i["orderId"],i["productId"],i["productName"],i["paid"],i["itemsneed"],i["orderstatus"]))
    else:
        print("No Orders Till Now...")

def search():
    os.system('cls')
    choice=input("\nEnter the Product Name To search: ")
    temp=[]
    for i in products:
        if(i["productName"]==choice):
            temp.append(i)
    if(len(temp)!=0):
        for i in temp:
            yousave = int((i["discount"] / 100) * i["price"])
            offerprice= i["price"] - yousave
            print("\n{}.Merchant Id & Product Id   : {} & {}\n  Product Name : {}\n  Product Price: {}\n  Product Stock: {}\n  Product offer: {}%\n  You save     : {}\n  You Pay      : {}".format(products.index(i)+1,i["merchantId"],i["productId"],i["productName"],i["price"],i["stock"],i["discount"],yousave,offerprice))
    else:
        input("\nNo Such Product found\n\nPress Enter to Continue...")

def shophome(currentuser):
    while(True):
        os.system('cls')
        print("\n\tWelcome To Shoping Portal\n")
        choice = input("\n1.Search and place an Order\n2.Place an order from cart\n3.Check My Order Status\n4.Exit\n\nEnter Your Choice: ")
        if(choice=="1"):
            search()
            ch=input("\nTo place an Order Press '1'\n\nTo Add To Cart press '2'\n\nEnter Your Choice: ")
            
            if(ch=="1"):

                merchid = input("\nEnter the Merchant Id of the product: ")
                productid = input("\nEnter the Product Id of the Product:")
                itemsneed = int(input("\nEnter no of items needed: "))
                userid = users[currentuser]["userId"]
                placeanorder(merchid,productid,itemsneed,userid,'-1')
            
            elif(ch=="2"):
                merchid = input("\nEnter the Merchant Id of the product: ")
                productid = input("\nEnter the Product Id of the Product:")
                for i in products:
                    if(i["merchantId"] == merchid and i["productId"] == productid):
                        noofitems = int(input("Enter No of Items To Be added to Cart: "))
                        users[current]["cart"].append({"merchantId":merchid,"productId":productid,"productName":i["productName"],"price":i["price"],"discount":i["discount"],"noofitems":noofitems})
                        input("\n\nProduct Added to Cart\n\nPress Enter to Continue...")
                        break
                    else:
                        input("\n\nNo Product found\n\nPress Enter to Continue...")
                        continue 
        elif(choice=="2"):
            temp = users[currentuser]["cart"]
            if(len(temp)!=0):
                viewmycart(currentuser)
                serial = int(input("\nEnter Cart Serial No. : "))-1
                d = users[currentuser]["cart"][serial]
                merchid = d["merchantId"]
                productid = d["productId"]
                itemsneed = d["noofitems"]
                userid = users[currentuser]["userId"]
                placeanorder(merchid,productid,itemsneed,userid,serial)
                input()
            else:
                viewmycart(currentuser)
    

        elif(choice=="3"):
            ch = input("\nEnter Your Order Id: ")
            for i in orders:
                if(i["orderId"]==ch and i["userId"]==users[currentuser]["userId"]):
                    print("\nProduct Name : {}\nItems count : {}\n\nOrder Status: {}".format(i["productName"],i["itemsneed"],i["orderstatus"]))
                    input("\nPress Enter to Continue...")
                    break
            else:
                input("No Such Order Found")

        elif(choice=="4"):
            break

def userreview(userid):
    
    temp = []
    for i in orders:
        print(i)
        if(i["userId"]==userid and i["orderstatus"] == "Received" and len(i["review"]) == 0):
            temp.append(i) 
    if(len(temp)==0):
        print("\nNo Orders To Review")
    else:
        num = 1
        for i in temp:
            print("\n{}. Order Id   : {}\n Product Name : {}\n You Payed    : {}\n Items count : {}\n\n Order Status: {}".format(num,i["orderId"],i["productName"],i["paid"],i["itemsneed"],i["orderstatus"]))
            num += 1
        orderid  = input("Enter Order Id to review Product: ")
        for i in orders:
            if(i["userId"]==userid and i["orderstatus"] == "Received" and i["orderId"]==orderid):
                currentorder = orders.index(i)
        rate = int(input("Enter Your Rating: "))
        desc = input("Enter Description: ")
        orders[currentorder]["review"] += ["* "*rate, desc]
    input("Press Enter To Continue...")

def viewuserreview(merchid,productid):
    count = 0 
    for i in orders:
        if(i["merchantId"] == merchid and i["productId"] == productid):
            l = i["review"]
            for j in users:
                if(i["userId"] == j["userId"]):
                    username = j["userName"]
                    break
            count+=1
            print("\nUser Name   : {}\nProduct Name: {}\nUser Rating : {}\n\"{}\"".format(username,i["productName"],l[0],l[1]))
    if(count == 0):
        input("\nNo Reviews Yet\n\nPress Enter To Continue...")
    else:
        input("\npress Enter to Continue...")
    
while(True):
    os.system('cls')
    choice=input("\tWelcome To Amazon\n1.Admin Login\n2.Merchant Login\n3.User Login\n4.Exit\n\nEnter Your choice to Continue: ")
    
    
    if(choice=="1"): #__ADMIN__


        os.system('cls')
        id=input("\nWelcome to Admin Login\n\nEnter Admin Username: ")
        ps=input("Enter Admin Password: ")
        if(id=="admin" and ps=="1234"):
            while(True):
                os.system('cls')
                print("\tWelcome Admin")
                choice=input("\n1.Approve Merchant\n2.Remove Merchant\n3.Show All Merchants\n4.Add Merchant\n5.Logout\n\nEnter Your Choice: ")
                
                if(choice=="1"): #1.Approve Merchant
                    for i in merchants:
                        if(i["merchantStatus"]=="Pending"):
                            print("Merchant Id and Name {}, {}".format(i["merchantId"],i["merchantName"]))
                            admin_aproval_choice = input("Enter '1' to Aprove merchant and '0' for not: ")
                            if(admin_aproval_choice == "1"):
                                i["merchantStatus"] = "Approved"
                                input("\nMerchant Added Sucessfully!\nPress Enter to continue")
                            else:
                                i["merchantStatus"] = "Rejected"
                                input("\nMerchant Rejected Sucessfully!\nPress Enter to continue")
                    input("\nNo Pending Aprovals")

                elif(choice=="2"): #2.Remove Merchant

                    os.system('cls')
                    merchant_to_remove=input("\nEnter Merchant Id to remove: ")
                    if(check(merchant_to_remove,merchants)):
                        confirm=input("!!!!Confirm removal!!\nEnter Admin Password: ")
                        if(confirm!="1234"):
                            input("\nInvalid Password!\nPress Enter to continue")
                            continue
                        else:
                            for i in merchants:
                                if(merchant_to_remove)==i["merchantId"]:
                                    i["merchantStatus"]="Removed"
                                    input("Merchant Removed\nPress Enter to Continue...")
                                    continue
                    else:
                        input("Merchant Not Found\nPress Enter to Continue...")
                        continue
                
                elif(choice=="3"): #3.Show all merchants

                    showallmerchants()

                elif(choice=="4"): #4.Add Merchants

                    os.system('cls')
                    id=str(int(merchants[-1]["merchantId"])+1)
                    print("Your Auto Generated Merchant Id:",id)
                    name=input("\nEnter Merchant Name    : ")
                    ps=input("Enter Merchant Password: ")
                    merchants.append({"merchantId":id,"merchantName":name,"password":ps,"merchantStatus":"Approved","merchantprofit":0})
                    input("\nMerchant Added Sucessfully\nPress Enter to Continue...")

                elif(choice=="5"): #3.Logout

                    break

                else:

                    input("\n\tInvalid Choice\nPress Enter to Continue....")
                    continue
        else:
            input("\n\tInvalid Choice\nPress Enter to Continue....")
            continue

    
    elif(choice=="2"): #___MERCHANT___


        while(True):
            os.system('cls')
            choice=input("\tWelcome Merchant\n1.New Merchant\n2.Existing Merchant\n3.Exit\n\nEnter Your Choice: ")
            
            if(choice=="1"): #1.New Merchant
                print("\n\tWelcome to New Merchant Registeration")
                id=str(int(merchants[-1]["merchantId"])+1)
                print("\nYour Auto Generated Merchant Id:",id)
                name=input("\n\nEnter Username: ")
                ps=input("Enter Password: ")
                merchants.append({"merchantId":id,"merchantName":name,"password":ps,"merchantStatus":"Pending","merchantprofit":0})
                input("Your Request for New Merchant is Recorded!\n\nYou'll be Allowed to Acess your Account Once Admin Verify you\n\nThank you!\n\nPress Enter to continue!")
            
            elif(choice=="2"): #2.Existing Merchant

                id=input("\nEnter Merchant Id   : ")
                ps=input("\nEnter Your Password : ")
                flag=0
                for i in merchants:
                    if(id==i["merchantId"]):
                        if(i["merchantStatus"]=="Approved" and i["password"]==ps):
                            current = merchants.index(i)
                            while(True):
                                os.system('cls')
                                choice=input("\tWelcome to Merchant Portal\n\n1.Add Products\n2.Remove Product\n3.Show My products\n4.Update My Product\n5.Compare Products\n6.Aprove Product request\n7.Merchant Product profits\n8.Check User Reviews\n9.Logout\n\nEnter Your Choice: ")
                                if(choice=="1"):
                                    addproducts(i["merchantId"])
                                elif(choice=="2"):
                                    removeproduct(i["merchantId"])
                                elif(choice=="3"):
                                    showmyproducts(i["merchantId"])
                                elif(choice=="4"):
                                    updatemerchantproducts(i["merchantId"])
                                elif(choice=="5"):
                                    compareproducthome()
                                elif(choice=="6"):
                                    aproveproductrequest(i["merchantId"])
                                elif(choice=="7"):
                                    merchantproductprofits(i["merchantId"], current)
                                elif(choice=="8"):
                                    productid = input("\nEnter Product Id: ")
                                    viewuserreview(i["merchantId"],productid)
                                elif(choice!="1" and choice!="2" and choice!="3" and choice!="4" and choice!="5" and choice!="6" and choice!="7" and choice!="8" and choice!="9"):
                                    input("\n\tInvalid Choice\nPress Enter to Continue....")
                                    continue
                                elif(choice=="9"):
                                    break
                            break
                        elif(i["merchantStatus"]=="Pending"):
                            input("\nYour Request for Merchant is Still bending\nTry Again Later\nPress Enter to Continue....")
                            break
                        elif(i["merchantStatus"]=="Rejected"):
                            input("\nYour Request for Merchant is Rejected\nPlease Contact Admin\nPress Enter to Continue....")
                            break
                        elif(i["merchantStatus"]=="Removed"):
                            input("\nYou are removed from Merchant List\nPlease Contact Admin\nPress Enter to Continue....")
                            break
                else:
                    input("\nMercahnt Not Found\nPress Enter to continue...")
                            
                   
            elif(choice=="3"): #3.Exit
                break

    elif(choice=="3"): #___USER___

        while(True):
            os.system('cls')
            choice=input("\nWelcome to User Portal\n1.New User\n2.Existing User\n3.Exit\n\nEnter Your Choice: ")
            if(choice=="1"):
                userid=str(int(new_user_Id)+1)
                new_user_Id=str(int(new_user_Id)+1)
                print("\nWelcome to New User Login\n\nYour Autogenerated User Id:",userid)
                username=input("\nEnter Username: ")
                password=input("\nEnter Password: ")
                users.append({"userId":userid,"userName":username,"password":password,"cart":[],"balance":0})
                input("\nUser Registeration Sucessful\nPress Enter to Continue...")
                continue

            elif(choice=="2"):
                userid=input("\nEnter User Id : ")
                password=input("\nEnter Password: ")
                for i in users:
                    if(i["userId"]==userid and i["password"]==password):
                        current=users.index(i)
                        while(True):
                            os.system('cls')
                            choice = input("\nWelcome "+users[current]["userName"]+"\n\n01.Shoping\n02.View All Products\n03.Compare Products\n04.My Cart\n5.Cancel an Orders\n06.Show My Wallet balance\n07.Update my wallet balance\n08.Show Order History\n09.Review Products\n10.Exit\n\nEnter Your Choice: ")
                            if(choice == "1"):
                                shophome(current)
                            elif(choice == "2"):
                                showallproducts()
                                input("\n\nPress Enter to continue...")
                            elif(choice == "3"):
                                compareproducthome()
                            elif(choice == "4"):
                                carthome(current)
                            elif(choice == "5"):
                                viewmyorders(users[current]["userId"],"Pending")
                            elif(choice=="6"):
                                print("\nAwailable Balance:",users[current]["balance"])
                                input("\nPress Enter to Continue...")
                            elif(choice=="7"):
                                print("\nAwailable Balance:",users[current]["balance"])
                                ch = int(input("\nEnter The Amount To Added: "))
                                users[current]["balance"]+=ch
                                print("\nUpdate Balance:",users[current]["balance"])
                                input("\nPress Enter to Continue...")
                            elif(choice=="8"):
                                vieworderhistory(users[current]["userId"])
                            elif(choice=="9"):
                                userreview(users[current]["userId"])
                            elif(choice!="1" and choice!="2" and choice!="3" and choice!="4" and choice!="5" and choice!="6" and choice!="7" and choice!="8" and choice!="9" and choice!="10"):
                                input("\n\tInvalid Choice\nPress Enter to Continue....")
                                continue
                            elif(choice == "10"):
                                break
                        break
                            
                else:
                    input("User Not Found\n\n Press Enter to Continue...")
                    continue

                

            elif(choice=="3"):
                break
            else:
                input("\n\tInvalid Choice\nPress Enter to Continue....")
                continue
        pass
    
    
    elif(choice=="4"):
        os.system('cls')
        print("\n\3 \2 \1 Thanks for Shopping \1 \2 \3")
        break
    
    
    else:
        input("\n\tInvalid Choice\nPress Enter to Continue....")
        continue