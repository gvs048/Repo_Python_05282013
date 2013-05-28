import random 
 
print ("Guessing Game! Guess what number I'm thinking") 
 
 
number = int(random.random()*10 + 1) 
tries = 0 
#print "%d" % number
#remove comment above to see the random number generated. 
print( "What number am I thinking? \n It's a number between 1 and 10\n") 
 
tryAgain = True 
while tryAgain:
    guess = int(input())    
    tries +=1 
   
 
 
    if number == guess: 
        print ("That's correct!") 
        if tries == 1: 
            print ("Excellent! You're a Genius!") 
        else:  
                if tries <= 3: 
                    print ("Superb! You just made %d tries!" % (tries) )
                else: 
                    if tries <7: 
                        print("Great! %d tries!" % (tries) )
                    else:  
                        print ("%d tries. At least you tried." % (tries)  )  
                        tryAgain = False          
    else:  
        if guess == number + 1: 
            print ("A bit lower, try again") 
        else: 
            if guess == number - 1:  
                print ("A little more, try again")      
            else: 
                if guess < number: 
                    print ("Too low, try again") 
                else:  
                    if guess > 10: 
                        print( "Guess only numbers from 1 to 10") 
                    else: 
                        print ("Too high, once more")        
          
