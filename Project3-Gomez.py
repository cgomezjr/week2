print("This program will calculate the customers cost.")
newvid = int(input("How many new videos are being rented?: "))
oldies = int(input("How many oldies are being rented?: "))
nights = int(input("How many nights will these videos be rented for?: "))
cost = ((newvid * 3) + (oldies * 2)) * nights
print(" Customer's total is: " + str(cost))
