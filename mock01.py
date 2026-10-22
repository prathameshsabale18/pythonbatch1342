#check wheter the string contains vowels using string class methods


name = input("Enter name: ").lower()

if ("a" in name) or ("e" in name) or ("i" in name) or ("o" in name) or ("u" in name):
    print("Vowels present")
else:
    print("No vowels present")


# text = input("Enter text: ").lower()

# if text.find("a") != -1 and text.find("e") != -1 and text.find("i") != -1 and text.find("o") != -1 and text.find("u") != -1:
#     print("Vowels present")
# else:
#     print("No vowels present")