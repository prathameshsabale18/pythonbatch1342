#check wheter the string contains vowels using string class methods


name = input("Enter name: ").lower()

if ("a" in name) or ("e" in name) or ("i" in name) or ("o" in name) or ("u" in name):
    print("Vowels present")
else:
    print("No vowels present")

