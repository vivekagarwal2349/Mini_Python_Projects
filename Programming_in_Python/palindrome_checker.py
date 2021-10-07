
text=input("Enter the string to be checked: ")
palindrom_text= text[::-1]

if text==palindrom_text:
    print("Palindrome")
else:
    print("Not Palindrome")
