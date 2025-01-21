import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
df=pd.read_csv("C:\\Users\\patel\\OneDrive\\Desktop\\PROJEECT\\IP-Project-main\\IP-Project-main\\read.csv")
print('Hello From Git!\n')
passw=input("Enter password : ")
print('''
   _____ _             _     __  __                                   _____             
  / ____| |           | |   |  \/  |                                 / ____|            
 | (___ | |_ _   _  __| |   | \  / | __ _ _ __   __ _  __ _  ___    | (___  _   _ ___   
  \___ \| __| | | |/ _` |   | |\/| |/ _` | '_ \ / _` |/ _` |/ _ \    \___ \| | | / __|  
  ____) | |_| |_| | (_| |_  | |  | | (_| | | | | (_| | (_| |  __/_   ____) | |_| \__ \_ 
 |_____/ \__|\__,_|\__,_(_) |_|  |_|\__,_|_| |_|\__,_|\__, |\___(_) |_____/ \__, |___(_)
                                                       __/ |                 __/ |      
                                                      |___/                 |___/       
''')

def mainMenu():
    print("------------------------------------------------")
    print("1. Read/Create CSV")
    print("2. Data Visualisation")
    print("3. Data Analysis")
    print("4. Data Manupulation")
    print("5. Exit Program")

while passw == 'admin':
    # print("------------------------------------------------")
    mainMenu()
    choice=int(input("Enter your choice : "))
    if choice==1:
        print("------------------------------------------------")
        print("-->1. Read CSV")
        print("-->2. Create CSV")
        print("-->3. Go Back")
        opt1=int(input("Enter your internal choice : "))
        if opt1==1:
            print("------------------------------------------------")
            print(df.to_string(index=False))
            print("------------------------------------------------")
        elif opt1==2:
            print("------------------------------------------------")
            d=eval(input("Enter data (Using Dictionary): "))
            newdf=pd.DataFrame(d)
            newdf.to_csv("C:\\Users\\patel\\OneDrive\\Desktop\\PROJEECT\\IP-Project-main\\IP-Project-main\\created.csv")
            print("File created at : E:\IP-Project")
            print("------------------------------------------------")
        elif opt1==3:
            False
        else:
            print("------------------------------------------------")
            print("Enter Valid Choice !!!")
            print("------------------------------------------------")
    elif choice==2:
        print("------------------------------------------------")
        print("-->1. Line Graph")
        print("-->2. Bar Graph")
        print("-->3. Histogram")
        print("-->4. Pie Chart")
        print("-->5. Go Back")
        opt2=int(input("--> Ener your internal choice : "))
        if opt2==1:
            df.plot.line()
            plt.title("Data Visualization")
            plt.show()
        elif opt2==2:
            df.plot.bar(x="Name")
            plt.show()
        elif opt2==3:
            df.plot.hist()
            plt.show()
        elif opt2==4:
            df.plot.pie(y='Percentage',autopct='%1.0f%%')
            plt.show()
        elif opt2==5:
            False
        else:
            print("------------------------------------------------")
            print("Enter Valid Choice !!!")
            print("------------------------------------------------")
    elif choice==3:
        while True:
            print("------------------------------------------------")
            print("-->1. Show all records")
            print("-->2. Show first and last 5 records")
            print("-->3. Show records in a selected range")
            print("-->4. show other attributes")
            print("-->5. Go Back")
            opt3=int(input("--> Enter your internal choice : "))
            if opt3==1:
                print("------------------------------------------------")
                print(df)
            elif opt3==2:
                print("------------------------------------------------")
                print(df.head())
                print("------------------------------------------------")
                print(df.tail())
            elif opt3==3:
                print("------------------------------------------------")
                startVal,stopVal=input("Enter start and stop value : ").split(",")
                print(df[int(startVal):int(stopVal):])
            elif opt3==4:
                print("------------------------------------------------")
                print("---->1. Check dataframe is empty or not")
                print("---->2. Show names of columns")
                print("---->3. Check datatype of columns")
                print("---->4. Count number of rows and columns")
                print("---->5. Transpose the Dataframe")
                print("---->6. Go Back")
                print("---->7. Go to main menu")
                attCh=int(input("----> Enter internal choice : "))
                if attCh==1:
                    print("------------------------------------------------")
                    print("Dataframe is Empty" if df.empty == True else "Datafame is not empty")
                elif attCh==2:
                    print("------------------------------------------------")
                    print("Column names are : ")
                    for colName in df.columns:
                        print("------------------------------------------------")
                        print(colName,end=' | ')
                    print()
                elif attCh==3:
                    print("------------------------------------------------")
                    print("Datatype : ",df.dtypes)
                elif attCh==4:
                    print("------------------------------------------------")
                    print("Co-ordinates : \n",df.shape)
                elif attCh==5:
                    print("------------------------------------------------")
                    print(df)
                    print("------------------------------------------------")
                    print("Transpose : ",df.T)
                elif attCh==6:
                    False
                elif attCh==7:
                    break
                else:
                    print("------------------------------------------------")
                    print("Enter Valid Choice !!!")
                    print("------------------------------------------------")
            elif opt3==5:
                break
    elif choice==4:
        print("------------------------------------------------")
        print("-->1. Insert new data")
        print("-->2. Delete data")
        print("-->3. Go Back")
        opt4=int(input("Enter your internal choice : "))
        if opt4==1:
            print("------------------------------------------------")
            print("---->1. Add new Row")
            print("---->2. Add new Column")
            interCh=int(input("----> Enter internal choice : "))
            if interCh==1:
                print("------------------------------------------------")
                print(df)
                l1=[]
                entry1=int(input("Enter total number of entries : "))
                for i in range(entry1):
                    value1=input("Enter data : ")
                    l1.append(value1)
                index=int(input("Enter new row index : "))
                df.loc[index]=l1
                df.to_csv('E:\\IP-Project\\read.csv')
                print("------------------------------------------------")
                print(df)
            elif interCh==2:
                print("------------------------------------------------")
                print(df)
                l2=[]
                entry2=int(input("Enter total number of entries : "))
                for j in range(entry2):
                    value2=input("Enter data : ")
                    l2.append(value2)
                colName=input("Enter column name : ")
                df[colName]=l2
                df.to_csv('E:\\IP-Project\\read.csv')
                print("------------------------------------------------")
                print(df)
        elif opt4==2:
            print("------------------------------------------------")
            print("---->1. Delete Row")
            print("---->2. Delte Column")
            interCh1=int(input("----> Enter your internal choice : "))
            if interCh1==1:
                print("------------------------------------------------")
                print(df)
                delrow=int(input("Enter row index to delete : "))
                df.drop(delrow,inplace=True)
                print(df)
                df.to_csv('E:\\IP-Project\\read.csv')
            elif interCh1==2:
                print("------------------------------------------------")
                print(df)
                delcol=input("Enter cloumn index to delete : ")
                df.pop(delcol)
                print(df)
                df.to_csv('E:\\IP-Project\\read.csv')
            else:
                print("------------------------------------------------")
                print("Enter valid Choice !!!")
                print("------------------------------------------------")
        elif opt4==3:
            False
    elif choice==5:
        print("------------------------------------------------")
        print("-->1. Shutdown")
        print("-->2. Log Off")
        print("-->3. Restart")
        print("-->4. Sleep")
        print("-->5. Go Back")
        opt5=int(input("Enter your internal choice : "))
        if opt5==1:
            confirm=input("Are you sure ? (y/n)")
            if confirm=='y' or confirm=='Y':
                os.system("shutdown /s")
            else:
                print("Choice Declined")
        elif opt5==2:
            confirm=input("Are you sure ? (y/n)")
            if confirm=='y' or confirm=='Y':
                os.system("shutdown /l")
            else:
                print("Choice Declined")
        elif opt5==3:
            confirm=input("Are you sure ? (y/n)")
            if confirm=='y' or confirm=='Y':
                os.system("shutdown /r")
            else:
                print("Choice Declined")
        elif opt5==4:
            confirm=input("Are you sure ? (y/n)")
            if confirm=='y' or confirm=='Y':
                os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
            else:
                print("------------------------------------------------")
                print("Choice Declined")
        elif opt5==5:
            False
    else:
        print("------------------------------------------------")
        print("Enter Valid Choice !!!")
        print("------------------------------------------------")


