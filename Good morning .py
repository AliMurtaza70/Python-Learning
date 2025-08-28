import time

# hour = int(time.strftime('%I'))
hour = int(input("Enter any hour: "))
am_pm = time.strftime('%p') 

if am_pm == "AM":
    print("Good Morning Sir jee")
elif am_pm == "PM" and hour < 5:
    print("Good Afternoon Sir jee")
elif am_pm == "PM" and hour < 9:
    print("Good Evening Sir jee")
else:
    print("Good Night Sir jee")
