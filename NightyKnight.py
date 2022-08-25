
import pygame
from pygame.locals import *
import random 

#initiates pygame
pygame.init()
#sets window size
window = pygame.display.set_mode([900, 900])

#loads in all game images that i created
gameBG = pygame.image.load('background.png')
knightHead = pygame.image.load('headOnly.png')
knightBody = pygame.image.load('headBody.png')
knightRArm = pygame.image.load('oneArm.png')
knightLArm = pygame.image.load('bothArms.png')
knightRLeg = pygame.image.load('oneLeg.png')
knightLLeg = pygame.image.load('fullBody.png')
instructions = pygame.image.load('Instructions.png')
home = pygame.image.load('homeScreen.png')
antiVeggie = pygame.image.load('vegTwo.png')
antiFruit = pygame.image.load('fruitsTwo.png')
antiCarMaker = pygame.image.load('carBrands.png')
antiColors = pygame.image.load('colorTwo.png')
playerScreen = pygame.image.load('playerScreen.png')
winner = pygame.image.load('won.png')
loser = pygame.image.load('loss.png')
antiRestart = pygame.image.load('restartTwo.png')

#creates a rectagle in pygame so it can detect when mouse is over location
#used to swap image out with the anti image
rectVeggie = pygame.Rect(127, 440, 300, 85) # x, y, width, height
rectFruit = pygame.Rect(477, 310, 300, 85) 
rectColors = pygame.Rect(477, 440, 300, 85) 
rectCarMaker = pygame.Rect(127, 310, 300, 85) 
rectRestart = pygame.Rect(300, 520, 300, 85)

#global items that will be updated when the game resets
missesLeft = 6 #misses allowed in game
userChoices = [] #letter guesses from user
choice = '' #category that was chosen during the homescreen 

global displayList #global list is the hidden word printed at bottom of game screen
displayList = []

#if the choosen word is in this list it will continue the loop
#all categories combined 
allCategoryList = ['MAZDA', 'HONDA', 'GMC', 'DODGE',
                   'BANANAS', 'STRAWBERRRY', 'APPLE', 'GRAPES', 
                   'CUCUMBER', 'TOMATOES', 'PEPPERS', 'LETTUCE',
                   'PURPLE', 'GREEN', 'YELLOW', 'BLUE', 'RED',
                   'ORANGE', 'PINK', 'WHITE', 'BLACK']

#used the random library to pick a word from the below categories 
#function is used in the homeScreen function and passes back the secretWord to be used in gameLogic
def computer_Choice(category): 
    carTypeList = ['MAZDA', 'HONDA', 'GMC', 'DODGE']
    fruitsList = ['BANANAS', 'STRAWBERRY', 'APPLE', 'GRAPES']
    veggiesList = ['CUCUMBER', 'TOMATOES', 'PEPPERS', 'LETTUCE']
    colorsList = ['PURPLE', 'GREEN', 'YELLOW', 'BLUE', 'RED', 'ORANGE', 'PINK', 'WHITE', 'BLACK']
#uses random based off the word provided by the button being clicked
    if category == 'car maker':
        secretWord = random.choice(carTypeList)
    elif category == 'fruits':
        secretWord = random.choice(fruitsList)
    elif category == 'veggies':
        secretWord = random.choice(veggiesList)
    elif category == 'colors':
        secretWord = random.choice(colorsList)
    return secretWord

#gameScreen function decides what background to display based off the misses left
#this function is used inside of key_Pressed to update background
def gameScreen(misses):
    if misses == 6:
        window.blit(gameBG, (0, 0)) #image to be blit and then x/y coordinates to start the top left of the image at
    elif misses == 5:               #blit is just loading the image in to be displayed you still have to flip screen
        window.blit(knightHead, (0, 0))
    elif misses == 4:
        window.blit(knightBody, (0, 0))
    elif misses == 3:
        window.blit(knightRArm, (0, 0))
    elif misses == 2:
        window.blit(knightLArm, (0, 0))
    elif misses == 1:
        window.blit(knightRLeg, (0, 0))
    elif misses == 0:
        window.blit(knightLLeg, (0, 0))
        
    #the following text will always be displayed so it is added into this function
    #font being configured to what font style will be rendered
    font = pygame.font.Font('schluber.ttf', 50) #font name and size // i used dafont.com to download a free font (please see supporting files to credit the artist)
    text = font.render(choice, True, (236, 236, 236)) #renders my text 
    textpos = text.get_rect(x = 165, y = 13) #sets the position x position is centering on screen
    text2 = font.render(str(misses), True, (236, 236, 236))
    text2pos = text.get_rect(x = 225, y = 70)
    window.blit(text, textpos) #blit the text just like a image
    window.blit(text2, text2pos)

    font2 = pygame.font.Font('schluber.ttf', 30) #create a second font size
    text3 = font2.render("Your word is:", True, (10, 10, 10))
    text3pos = text.get_rect(x = 50, y = 650)
    #window.blit(text3, text3pos)

    window.blit(playerScreen, (0, 0))

#function runs to cover user input from the user
#the hidden word and the users input are the values being used
def key_Pressed(word, letter):
    #alphabet is used so that the other input keys outside of a-z will be ignored
    alphabet = ['A', 'B', 'C', 'D', 'E',
            'F', 'G', 'H', 'I', 'J',
            'K', 'L', 'M', 'N', 'O',
            'P', 'Q', 'R', 'S', 'T',
            'U', 'V', 'W', 'X', 'Y',
            'Z']
    #calling userChoice and missesLeft to update lists for display
    global userChoices
    global missesLeft 
    displayList.clear() #clearing out the displayed list to create a update list every loop
    window.fill((0, 0, 0)) #clearing the screen of all images and text by just making it black (you never see this happen)
    font = pygame.font.Font('schluber.ttf', 50) #could globalize fonts so they do not have to be called here
    font2 = pygame.font.Font('schluber.ttf', 30)

    #if statement below makes sure that you do not get additional misses for the same letter
    if letter not in word and letter not in userChoices:
        if letter in alphabet:
            missesLeft = missesLeft - 1
    #if statement makes sure that multiple of the same letter are not displayed on the user guesses
    if letter in alphabet and letter not in userChoices:
        userChoices.append(letter)

    #calls the gameScreen to blit all images and text since we reset display
    gameScreen(missesLeft)

    #below is used to print the guesses the user makes to the screen
    text = font2.render('Guesses:', True, (10, 10, 10))
    textPos = text.get_rect(centerx = window.get_width() / 2, y = 750)
    #window.blit(text, textPos)
    a = 60 #sets the first x and y positions for printing the guesses
    b = 825
    for j in userChoices: #interates through user guesses to print to screen
        guess = font2.render(j, True, (236, 236, 236))
        guessPos = guess.get_rect(x = a, y = b)
        window.blit(guess, guessPos)
        a = a + 50  #moves the next guess over
        if a == 410: #if the guesses fill up the first row move down one and start again
            b = 865  #i only allow six guesses so this is unused but available if you up the misses allowed
            a = 50
    #creates a list of letters and dashes to create the hidden word
    #if you wanted to use to word phrases elif would have to add a ' ' statement
    for j in range(0, len(word)):
        if word[j] in userChoices:
            displayList.append(word[j])
        else:
            displayList.append('_')
    #interates the list created to blit it to the screen
    i = 430
    for j in displayList: 
        dash = font.render(j, True, (236, 236, 236))
        dashPos = dash.get_rect(x = i, y = 698)
        window.blit(dash, dashPos)
        i = i + 40
    
 
#checks to see if the mouse is in my rect statements 
def is_over(rect, pos):
    # function takes a tuple of (x, y) coords and a pygame.Rect object
    # returns True if the given rect overlaps the given coords
    # else it returns False
    return True if rect.collidepoint(pos[0], pos[1]) else False   

#display for the opening game screen
def homeScreen():
    global choice #calls string variable to be shared with the main loop
    pygame.mouse.set_visible(True) #makes the mouse visable not needed but wanted to add in
    pos = pygame.mouse.get_pos() #gets position of mouse
    window.blit(home, (0, 0)) #blits the starting images
 

    for event in pygame.mouse.get_pressed(): # Checks all events.
        if event == False: #if the mouse button is not clicked but hovering the following posistions it changes the image
            if is_over(rectFruit, pos):
                window.blit(antiFruit, (0, 0))
            elif is_over(rectVeggie, pos):
                window.blit(antiVeggie, (0, 0))
            elif is_over(rectCarMaker, pos):
                window.blit(antiCarMaker, (0, 0))
            elif is_over(rectColors, pos):
                window.blit(antiColors, (0, 0))
            pygame.display.flip() #flips the screen so that when you hover on off it will change back

        elif event == True:  #if the mouse button is clicked send the 
            if is_over(rectFruit, pos):
                choice = 'fruits' #updates choice so it can be displayed on the game screen 
                return computer_Choice(choice) #picks the secret word and returns it
                break #breaks the loop
            elif is_over(rectVeggie, pos):
                choice = 'veggies'
                return computer_Choice(choice)
                break
            elif is_over(rectCarMaker, pos):
                choice = 'car maker'
                return computer_Choice(choice)
                break
            elif is_over(rectColors, pos):
                choice = 'colors'
                return computer_Choice(choice)
                break
 
#displayed when misses left equals zero            
def loserScreen(secretWord): #accepts the secret word
    pos = pygame.mouse.get_pos() #get the mouse position
    window.blit(loser, (0,0)) #add image
    font = pygame.font.Font('schluber.ttf', 30) #font style
    text = font.render(secretWord, True, (236, 236, 236)) #adds the secret word so you know what word you missed
    textpos = text.get_rect(x = 459, y = 464)
    window.blit(text, textpos)

    pygame.event.clear() #clears out events 
    for event in pygame.mouse.get_pressed(): #waiting for mouse button to be clicked
        if is_over(rectRestart, pos):
            if event == False: #changes the restart button to anti restart
                window.blit(antiRestart, (0, 0))
            elif event == True: #returns true to break the loop and restart the game if clicked
                return True
      


def winnerScreen(): #shows that you won the game
    window.blit(winner, (0,0))
    pos = pygame.mouse.get_pos()
    pygame.event.clear() #clears out events
    for event in pygame.mouse.get_pressed(): #changes color of restart button
        if is_over(rectRestart, pos):
            if event == False:
                window.blit(antiRestart, (0, 0))
            elif event == True:
                return True
     
        

#runs game processes
def gameLogic(secretWord):
    global choice #imports the globals that i need
    global missesLeft
    global userChoices
    window.blit(gameBG, (0, 0)) #starter screen 
    
    if pygame.font: #if font loads correctly then it does these things
        font = pygame.font.Font('schluber.ttf', 50) #same as in gameScreen just does it for the initial load
        text = font.render(choice, True, (236, 236, 236))
        textpos = text.get_rect(x = 165, y = 13)
        text2 = font.render("6", True, (236, 236, 236))
        text2pos = text.get_rect(x = 225, y = 70)
        window.blit(text, textpos)
        window.blit(text2, text2pos)
        font2 = pygame.font.Font('schluber.ttf', 30) 
        text3 = font2.render("Your word is:", True, (10, 10, 10))
        text3pos = text.get_rect(x = 50, y = 650)
        #window.blit(text3, text3pos)
        window.blit(playerScreen, (0, 0))
    i = 430 #displays the user hidden word for the starting screen
    for j in range(0, len(secretWord)):
        displayList.append('_')
        dash = font.render('_', True, (236, 236, 236))
        dashPos = dash.get_rect(x = i, y = 698)
        window.blit(dash, dashPos)
        i = i + 40
    pygame.display.flip()
    
    #game loop for the given word
    run = True
    while run:
        for event in pygame.event.get(): #allows you to exit if you hit the exit button
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif '_' not in displayList: #if the list does not have the underscore that would mean you guessed the word and won
                pygame.key.stop_text_input() #stops the keyboard from accepting input
                window.fill((0, 0, 0))
                key_Pressed(secretWord, keyCode)
                winnerScreen()
                pygame.display.flip()#displays the winner screen
                while winnerScreen() == False: #if you havent clicked the mouse this is false and runs the winnerScreen loop
                    winnerScreen()
                if winnerScreen() == True: #if you have clicked the restart this is true
                    missesLeft = 6 #resets misses allowed
                    userChoices.clear() #clears the users choices
                    return 2 #returns 2 to restart main loop

            elif missesLeft == 0: #if your misses left are zero then you lost the game and did not guess word
                pygame.key.stop_text_input() #stops keyboard input
                window.fill((0, 0, 0))
                key_Pressed(secretWord, keyCode)
                loserScreen(secretWord) #runs loser function
                pygame.display.flip()
                while loserScreen(secretWord) == False: #if not clicked false
                    loserScreen(secretWord)
                if loserScreen(secretWord) == True: #if you hit restart
                    missesLeft = 6 #reset misses
                    userChoices.clear() #clear out the users choices
                    return 2 #restart main loop
                
            elif event.type == pygame.KEYDOWN: #when you make a new guess by hitting a key
                keyCode = str(pygame.key.name(event.key))  #take the key hit and get the key name (found this in the doc to get the character) turn it into string
                keyCode = keyCode.upper() #make it uppercase to compare to alphabet and words
                key_Pressed(secretWord, keyCode) #pass that info to the key_Pressed function
                pygame.display.flip()
                             
#main loop
run = True
while run:
    for event in pygame.event.get(): #lets you quit by hitting the exit button
        if event.type == pygame.QUIT:
            run = False
        else:
            catWord = homeScreen() #runs home screen and return the category and saves it to variable
            i = 1
            while i == 1: #if you havent choosen a word category keep the home screen displayed
                if catWord not in allCategoryList:
                    break #breaks the while loop if you havnt picked a category
                elif gameLogic(catWord) == 2: #if you hit restart it returns 2
                    catWord ='none' #resets the catWord so that it breaks loop and displays screen till new cat chose
                    i == 2
                else:
                    gameLogic(catWord) #runs the game when you picked a category
                    


        

    
           
    