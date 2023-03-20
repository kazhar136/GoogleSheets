print("Please Wait....")

#import modules
import gspread #pip install gspread
import pandas as pd

# googlesheet link
# https://docs.google.com/spreadsheets/d/19GoEWlb-wgTI8GRiMSRxcSlQpYiap6lU_V4ouZw16QM/edit#gid=0

# read Google Sheets
def read_csv():
    global data_frame1,data_frame2
    
    cred_file = 'sheet_auth.json'
    gc = gspread.service_account(cred_file)
    # Establish the connection
    database = gc.open("python csv file")
    # Selecting a Worksheets
    worksheet1 = database.worksheet("test1")
    worksheet2 = database.worksheet("test2")
    # Acess all the records
    data_frame1 = pd.DataFrame(worksheet1.get_all_records())
    data_frame2 = pd.DataFrame(worksheet2.get_all_records())
    
    return data_frame1 , data_frame2

# merge two Sheets
def merge_csv():
    read_csv()
    global data_frame3
    data_frame3=pd.merge(data_frame1,data_frame2,on="name",how='outer')
    return data_frame3

# create merge sheets    
def save_csv():
    merge_csv()
    data_frame3.to_csv("sheet.csv",index=False)
    print("Create Successfully")


while True:
    print("press 1 for read csv file")
    print("press 2 for merge csv file")
    print("press 3 for save csv file")
    print("press 4 for exit")
    ch=int(input("Please Enter Your Choices: "))
    if ch==1:
        a,b=read_csv()
        print(a)
        print(b)
    elif ch==2:
        print(merge_csv())
    elif ch==3:
        save_csv()
    elif ch==4:
        break
    else:
        print("Wrong key try again")


