import login

def main():
    print("\n\n================== Welcome to the Demo Marketplace ==================\n")

    while(True):
        print("\n\t\t---------- Press Key ----------\n")
        print("\t\t1 : Create Admin")
        print("\t\t2 : Create User")
        print("\t\t3 : Admin Log in")
        print("\t\t4 : User Log in")
        print("\t\t5 : Exit\n")
        
        user_input = int(input("\nEnter value :"))

       
        match user_input:

            case 1: 
                # print("Create Admin Log in")
                login.CreateAdmin()
                # ...

            case 2:
                # print("Create User Log in")
                login.CreateUser()
                # ...

            case 3:
                print("Admin Log In")

            case 4:
                print("User Log In")

            case 5:
                exit()



if __name__ == "__main__":
    main()