import re
def Sample():
    password=input("enter password : ")
    if len(password)<8:
        print("password must have atleast 8 characters ! ")
        Sample()
    elif not re.search("[A-Z]",password) :
               print("password must have atleast one upper case letter")
               Sample()
    elif not re.search("[a-z]",password):
        print("password must have atleast one lower case letter")
        Sample()
    elif not re.search("[0-9]",password):
        print("password must have atleast one digit")
        Sample()
    elif not re.search("[@_]",password):
        print("password must have atleast one special character")
        Sample()
    else:
        print("password is correct")
Sample()
    
