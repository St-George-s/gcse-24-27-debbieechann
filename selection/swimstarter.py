Swimtime = float(input("Enter your swim time: "))
if Swimtime < 60:
    print("you qualify for international swim competition")
if Swimtime <=55:
    print ("you qualify for the gold category")
if Swimtime >55 and Swimtime <= 59.99:
    print ("you qualify for the silver category")
if Swimtime >=60 and Swimtime <= 64.99:
    print ("you qualify for the bronze category")
if Swimtime >=65:
    print ("you do not qualify for any category")