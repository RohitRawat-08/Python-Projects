import createAdminUser
AdminJsonFilePath = 'Admin.json'
UserJsonFilePath = 'User.json'

def CreateAdmin():
    createAdminUser.Add_New_Admin(AdminJsonFilePath)
    

def CreateUser():
    createAdminUser.Add_New_User(UserJsonFilePath)


def AdminLogIn():
     ...


def UserLogIn():
    ...

