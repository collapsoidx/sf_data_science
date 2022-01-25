"""Game to guess number"""

import numpy as np

number = np.random.randint (1, 101) # Guess number

# number of attemps
count = 0

while True:
    count+=1
    predict_number = int(input("Guess number form 1 till 100\n"))
    
    if predict_number > number:
        print('Number must be smaller\n')
        
    elif predict_number < number:
        print('Number must be bigger\n')
        
    else:
        print(f'You got it! Number is {number} in {count} times')
        break # End game
    