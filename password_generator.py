# Get input from user for password length
# Format as int

# Create an empty string for password

# Loop through n times = to password length
    # Choose random letter from ascii
    # Concatenate to password string
    
# Output new password

from random import randrange, random

def createNewPassword():
    passwordLength = int(input('How many characters for your password? '))
    
    password = ''
    
    for letter in range( passwordLength ):
        
        lowerOrCapital = random()
        if lowerOrCapital < 0.5:
            nextLetter = chr( randrange(65, 91) )
        else:
            nextLetter = chr( randrange(97, 123) )
        
        password = password + nextLetter
    
    print('Your new password is: {}'.format( password ) )
    
createNewPassword()