from dbconfig import *




    
un = input("Enter your Username:")
pwd = input("Enter your password:")

mycursor.execute("select*from admin where Username='{}'and Pswd='{}'".format(un,pwd))
adata= mycursor.fetchone()

if adata:
    print("========WELCOME {} =========".format(adata[3]))
else:
    print("invalid")
    

def callAdmin():
    while True:
        print("1.Add company")
        print("2.Add policy and policy details")
        print("3.Enter clients details")
        print("4.View Policy and Policy Details")
        print("5.Client Policy Report")
        print("6.Logout")
        ch = int(input("Enter your choice:"))

        if ch==1:
            cpid = int(input("Enter company Id:"))
            cpname = input("Enter Company Name:")

            mycursor.execute("insert into company(Cid,Cname)values('{}','{}')".format(cpid,cpname))
            mydb.commit()
            print("~~~~~~~~~~~~~~Company Added~~~~~~~~~~~~~~`~")
          
        elif ch == 2:
            pcode=int(input("Enter Policy Code:"))
            pcpid = int(input("Enter Company Id:"))
            pname=input("Enter Policy Name:")
            pdetails=input("Enter Policy Details:")
            ppremium=input("Enter Policy Premium:")
            pduration= input("Enter Policy Duration:")
            cage=input("Enter Clients age period:")
            wpc=input("Waiting Period After Policy Taken:")
            icovered= input("Enter Issues Covered:")
            ncovered= input("Enter Issues Not Covered:")

            mycursor.execute("insert into Policy(Policycode,Pcid,Policyname,Policydetails,Policypremium,Policyduration,Clientage,waiting_priod_covered,covered,Not_covered)values('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(pcode,pcpid,pname,pdetails,ppremium,pduration,cage,wpc,icovered,ncovered))
            mydb.commit()
          
            print("~~~~~~~~~~~~~~~~~~Policy Details Added Successfully~~~~~~~~~~~~~~~~~~~~")


        elif ch==3:
      
            cname = input("Client's Name:")
            cid = int(input("Enter Client's Id:"))
            cmobileno=int(input("Enter Your Mobile Number:"))
            cemail  = input("Enter Your Email Address:")
            clientAddress = input("Enter your Address:")
            c_age = int(input("Client's Age:"))
            cgender = input("Enter Clients Gender:")
            occlient = input("Enter Occupation Of The Client:")
            crequirement= input("Plan Required:")

            mycursor.execute("insert into Client_(clientname,clientid,clientmobile_number,clientemail,clientaddress,clientge_,clientgender,clientoccupation,clientrequirement)values('{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(cname,cid,cmobileno,cemail,clientAddress,c_age,cgender,occlient,crequirement))
            mydb.commit()

            print("*************CLIENT DETAILS ADDED SUCCESSFULLY************")
            
        elif ch==4:
            print("Policy Details Are As Follows:")
            mycursor.execute("select* from policy")
            data = mycursor.fetchall()
            print(data)
            
        elif ch==5:
            Cid = int(input("Enter Client's Id:"))
            Cname = input("Enter Clients Name:")
            Cpid = int(input("Client Policy Code:"))
            Pname = input("Enter Policy Name:")
            Ctpremium = input("Enter Client Total Premium:")
            Cpduration = input("Enter Client Policy Duration:")
            creview = input("Enter clients review:")

            mycursor.execute("insert into  ClientpolicyReport(client_id,clientname,clientpolicyid,policy_name,clienttotalpremium,CLIENTpolicyduration,clientreview)values('{}','{}','{}','{}','{}','{}','{}')".format(Cid,Cname,Cpid,Pname,Ctpremium,Cpduration,creview))
            mydb.commit()

            print("******************Report Added Successfully******************")

        elif ch==6:
            break
        
callAdmin()


print("================Welcome to client portal please enter your name to see your policy report!===================")  
clientsname = input("Enter your name:")
mycursor.execute("select*from Client_ where clientname='{}'".format(clientsname))
adata= mycursor.fetchone()
if adata:
    print("========WELCOME {} Your Details Regarding Policy Is AS Follows:".format(adata[1]))

def callClient():
    mycursor.execute("select * from  ClientpolicyReport")
    Pdata = mycursor.fetchall()
    print(Pdata)

callClient()











