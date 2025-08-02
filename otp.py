import random 
a = random.randint(1000000,99999999)
print(a)
otp = int(input("enter otp"))
if(a==otp):
    print("werified successfully")
else:     
        print("invalid")
