num = int(input("Enter a month as a number between 1-12: "))
if(1 <= num <= 3):
    print("The month is in first quarter")
elif(4 <= num <= 6):
    print("The month is in second quarter")
elif(7 <= num <=9):
    print("The month is in third quarter")
elif(10 <= num <=12):
    print("The month is in fourth quarter")
else:
    print("Error! Enter a number between 1-12")
