import string
#function that iterates through the string entered by the user so that spacing is ignored by the program
def remove_whitespace(palstring):
    return "".join(i.lower() for i in palstring if i in string.ascii_letters) #where palstring stands for palindrome string

def reverse(palstring):
    return palstring[::-1] #all items in array(input) are reversed and stored in the variable

def is_palindrome(palstring):   #whitespace ignoring and reverse functions implemented
    palstring = remove_whitespace(palstring)
    return palstring==reverse(palstring)
    
while True: #loop to allow user to keep testing out new strings
    checkthestring = input('Enter a string to check if its a palindrome!: ')#user input is required to check for a palindrome

    if (is_palindrome(checkthestring)):
        print("Yes, it is a palindrome") #simple conditional statements telling the user if the string is a palindrome!
    else:
        print("No, it is not a palindrome")
