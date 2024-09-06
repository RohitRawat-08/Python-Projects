import os
import xlsxwriter

def CreateAdminLogIn():
        
    workbook = xlsxwriter.Workbook("AdminData.xlsx")
    worksheet = workbook.add_worksheet('adminData')

    Admin_name = input("\nEnter Admin Name :")
    Admin_password = input("Enter Admin Password :")

    worksheet.write(0,0,'Name')
    worksheet.write(0,1,'Password')


    worksheet.write(1,0,Admin_name)
    worksheet.write(1,1,Admin_password)



    workbook.close()

def CreateUserLogIn():
    
    workbook = xlsxwriter.Workbook("UserData.xlsx")
    worksheet = workbook.add_worksheet('UserData')

    User_name = input("\nEnter User Name :")
    User_password = input("Enter User Password :")

    worksheet.write(0,0,'Name')
    worksheet.write(0,1,'Password')


    worksheet.write(1,0,User_name)
    worksheet.write(1,1,User_password)



    workbook.close()

def AdminLogIn():
    ...

def UserLogIn():
    ...

