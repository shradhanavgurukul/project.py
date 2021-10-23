print("WELCOME TO TRAVELS")
current_location=input("enter the location")
droping_point=input("enter the droping point")
nearby_riders=[["Arjun","cab=auto","he is ready to go for prise=200","min=15min"],
               ["Name=Yash","cab=mini","he is ready to go for prise=300","min=1/2hour"],
               ["Name=Raju","cab=prime","he is ready to go for prise=100","min=1hour"]]
riders_details=[["HR28DQ55","Red","1234567890"],
                ["KL2158924","Blue","9876543210"],
                ["MH240DS","White","8762465623"]]
for i in range(len(nearby_riders)):
    print(nearby_riders[i])
if current_location=="pune":
    print("karam is avaliable")
elif current_location=="kataraj":
    print("Arjun and Yash avaliable for this ride")
if droping_point=="pune station":
    print("your joury start now")
elif droping_point=="tulsibag":
    print("found your location")
else:
    print("no one is avaliable for this ride")

riders=input("ENTER  DRIVER YOU WOULD LIKE TO CHOOSE")

rider1="Arjun"
rider2="Yash"
rider3="Raju"
rider4="Shubham"

if riders==rider1:
    print((riders_details[0][::]),"cab will be coming in 15 min")
elif riders==rider2:
    print((riders_details[1][::]),"cab will be coming in 1/2 hour")   
elif riders==rider3:
    print((riders_details[2][::]),"cab will be coming in 1 hour") 
elif riders==rider4:
    print((riders_details[3][::]),"cab will be coming in 1 hour") 

else:
    print("NO SERVICES AVAILIABLE TO YOUR DESTINATION LOCATION")

# OTP
print("****please wait for the OTP verification****")
OTP=input("enter your OTP")
if OTP=="1107":
    print("done")
else:
    print("invalid")

# PAYMENT
payment=input("which was you want to pay")
if payment=="cash on hand":
    print("you have to pay in cash amount")
if payment=="UPI payment":
    print("you have swipe the card")
if payment=="google pay":
    print("scan the QR code") 

# PRISE
prise=input("enter the prise")
if prise=="cash on hand":
    print("you have pay in prise")
else:
    print("your payment sucessful")    


#FEEDBACK
feedback=input("how many stars you have to give this ride")
if feedback=="****":
    print("excellent")
if feedback=="***":
    print("good")
if feedback=="*":
    print("not good")

print("****************Thanks for visit*******************")
print("****************have a good bye********************")












