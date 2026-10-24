###1 Quarter year

# month = str(input("Enter the month : "))

# match month:
#     case "January" | "February" | "March" :
#         print("First quarter")
#     case "April" | "May" | "June" :
#         print("Second quarter")
#     case "July" | "August" | "September" :
#         print("Third quarter")
#     case "October" | "November" | "December" :
#         print("Fourth quarter")

#     case _:
#         print("Out of range")


###2 Grade


# grade= (input("Enter your grade:"))

# match grade:
#     case "A" :  
#         print("marks = 90-100")
#     case "B" :
#         print("marks = 80-89")
#     case "C" :
#         print("marks = 70-79")
#     case "D":
#         print("marks = 60-69")
#     case "E" :
#         print("marks = 50-59")
#     case "F" :
#         print("marks = 0-49")  
#     case _:
#         print("Invalid marks")


###3 Arithmetic operations between two numbers using match case

# a = int(input("Enter any number:"))
# b = int(input("Enter any number:"))

# op = input("Enter the operation (+, -, *, /): ")

# match op :
#     case "+":
#         print(a+b)
#     case "-":
#         print(a-b)
#     case "*":
#         print(a*b)
#     case "/":
#         # if b!= 0:
       
#         if a==0:
#             print("not allowed")
#         elif b==0:
#             print("infinity.")
#         else:
#             print(a/b)
#     case _:
#         print("Invalid operation")



###4 vowel or consonant

# a = input("Enter any character:").lower()

# match a: 
#     case "a" | "e" | "i" | "o" | "u":
#         print("vowel")
#     case _:
#         print("consonant")





###5 ATM Menu

# Display:
# 1. Check Balance
# 2. Deposit
# 3. Withdraw
# 4. Exit

# balance = 5000


# print("ATM Menu:")
# print("1. Check Balance")
# print("2. Deposit")
# print("3. Withdraw")
# print("4. Exit")

# choose = int(input("Enter your choice (1-4): "))

# match choose :
#     case 1:
#         print("your balanceis.:", balance)
#     case 2:
#         deposit = int(input("Enter the mount to deposit: "))
#         balance+= deposit
#         print("Depoasited successfully. New balance is:", balance)
#     case 3:
#         withdraw= int(input("Enter withdrawal amount: "))
#         if withdraw> balance:
#             print("Insufficient balance.")
#         else:
#             balance-= withdraw
#             print("Withdrawal successful. New balance is:", balance)

#     case 4:
#         print("Exiting the ATM menu.")

#     case _:
#         print("Invalid choice. Please select options from(1,2,3,4 ).")


###6 Days in a month
        
month = input("Enter month: ").capitalize()

match month:
    case "January" | "March" | "May" | "July" | "August" | "October" | "December":
        print("31 days")
    case "April" | "June" | "September" | "November":
        print("30 days")
    case "February":
        print("28 or 29 days")
    case _:
        print("Invalid month")


###7 Traffic light color

color = input("Enter traffic light color: ").lower()

match color:
    case "red":
        print("Stop")
    case "yellow":
        print("Get Ready")
    case "green":
        print("Go")
    case _:
        print("Invalid color")


###8 food ordering system

print("1. Pizza - Rs.200")
print("2. Burger - Rs.100")
print("3. Sandwich - Rs.80")
print("4. Coffee - Rs.50")

choice = int(input("Choose item: "))
quantity = int(input("Enter quantity: "))

match choice:
    case 1:
        print("Total bill:", 200 * quantity)
    case 2:
        print("Total bill:", 100 * quantity)
    case 3:
        print("Total bill:", 80 * quantity)
    case 4:
        print("Total bill:", 50 * quantity)
    case _:
        print("Invalid item")


### 9 calculator for discount

customer = input("Enter customer type: ").lower()
amount = float(input("Enter purchase amount: "))

match customer:
    case "student":
        print("Final amount:", amount - amount * 0.10)
    case "senior":
        print("Final amount:", amount - amount * 0.20)
    case "regular":
        print("Final amount:", amount)
    case _:
        print("Invalid customer type")


### 10 mobilerecharge

plan = int(input("Choose plan (1-3): "))

match plan:
    case 1:
        print("Price: Rs.199, Validity: 28 days")
    case 2:
        print("Price: Rs.299, Validity: 56 days")
    case 3:
        print("Price: Rs.399, Validity: 84 days")
    case _:
        print("Invalid plan")




# questions on match case are given in the file matchcases.py.
# upload and mail to github.

