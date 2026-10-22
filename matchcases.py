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

        
    











# questions on match case are given in the file matchcases.py.
# upload and mail to github.

