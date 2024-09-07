import json

AdminJsonFilePath = 'Admin.json'
UserJsonFilePath = 'User.json'

# Adding Admin Data 

def LoadAdminData(Filepath):
    try:
        with open(Filepath,'r') as Json_file:
            return json.load(Json_file)
    except FileNotFoundError:
        return f"file not found creating new file "

def Add_New_Admin(Filepath):

    data = LoadAdminData(Filepath)
    print(data)

    admin_name = input("Enter Admin Name: ")
    admin_password = input("Enter Admin Password: ")

    new_admin = {
        "AdminName": admin_name,
        "Password": admin_password
    }

    data.append(new_admin)

    # print(data)

    with open(Filepath,'w') as json_file:
        json.dump(data, json_file,indent=4)

    print("Successfull Added New Admin!!!")

Add_New_Admin(AdminJsonFilePath)

# Adding User Data 

def LoadUserData(Filepath):
    try:
        with open(Filepath,'r') as Json_file:
            return json.load(Json_file)
    except FileNotFoundError:
        return f"file not found creating new file"

def Add_New_User(Filepath):
    
    data = LoadUserData(Filepath)
    print(data)

    user_name = input("Enter User Name: ")
    user_password = input("Enter User Password: ")

    new_User = {
        "UserName": user_name,
        "Password": user_password
    }

    data.append(new_User)

    # print(data)

    with open(Filepath,'w') as json_file:
        json.dump(data, json_file,indent=4)

    print("Successfull Added New User!!!")

# Add_New_User(UserJsonFilePath)




