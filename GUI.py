import random
import time
import pygame
import sys
pygame.init()


class GUIFunctions():
  """
  A class to represent the functions for the GUI
  
  ...
  Attributes
  ----------
  w : int
    Width of the screen
  h : int
    Height of the screen
  gameDisplay : pygame function
    Used the display the screen with width and height
  bgColour : list
    Sets the colour of side window
  sidePos : 1x4 array
    Sets the dimensions of side screen
  buttonColour : list
    Sets the colour of button
  text : pygame function
    Determines the font and size that will be used
  textPosX : int
    Determines the side text will be centered around
  blackColour : list
    Sets black colour
  tokenDict : dictionary
    Loads the images of each token
  boardGUI : image
    Loads the board image
  boardPosT : 2 x 40 array
    Sets the position of the first token on each square
  boardWidth : int
    Width of the board
  boardHeight : int
    Height of the board
  positions : 2 x 6 array
    Position of each player on the square
  housePic : image
    This loads the house image
  hotelPic : image
    This loads the hotel image
  boardWidth : int
    It sets the width of the board
  boardHeight : int
    It sets the height of the board
  tokenGUI : list
    It loads the token images
  dicePic : image
    It loads the dice image
  playerButtonPos : 1 x 6 array
    Sets the position of button when choosing the number of players
  tokensAtGo : 1 x 6 array
    Sets the position of tokens at go square in the beginning

  Methods
  -------
  createScreen()
    sets the GUI screen
  setSideText(sentence, posX, posY)
    Displays the message on the side screen
  setTextFont (message, font)
    Chooses the font
  click(x, y, w, h)
    Alerts the user that they have clicked on a button 
  toQuit()
    Allows user to quit the game
  clearSideScreen()
    Clears the side screen
  addButton(word, posX, posY)
    It is used to add a button for the GUI
  updateBoard()
    Update the board with the new position of tokens
  createTextBox(posX, posY)
    Creates a text box where users can enter the required input
  userInput(posY)
    Allows user to enter a number
  displayHouseHotel()
    Displays the image of house or hotel after the player has improved their property
  """

  w = 950
  h = 650
  gameDisplay = pygame.display.set_mode((w,h))
  bgColour = (238,213,210) # the colour of the side window
  sidePos = [650,0,300,650] # the dimentions of the side screen
  buttonColour = (0,255,170) 
  text = pygame.font.SysFont("freesansbold", 15)
  textPosX = 800 # what side text is centered around
  blackColour = (0,0,0)
  tokenDict = {'Boot': pygame.image.load('shoe.png'), 'Smartphone': pygame.image.load('smartphone.png'),
                    'Goblet': pygame.image.load('goblet.png'), 'Hatstand': pygame.image.load('hatstand.png'),
                    'Cat': pygame.image.load('cat.png'), 'Spoon': pygame.image.load('spoon.png')} #assigns picture of the token to its name
  boardGUI = pygame.image.load('monopboard.jpg') # loads the board image
  boardPosT = [[606, 590], [510, 590], [460, 590], [405,590], [350,590],
               [297, 590], [245,590], [190,590], [140,590], [90, 590],
               [10, 590],[10, 510], [10, 460], [10, 408], [10, 355],
               [10, 300], [10, 250], [10, 195], [10, 140], [10, 90],
               [10, 10], [90, 10],[142, 10], [195,10], [247,10],
               [302,10], [353,10], [405,10], [460,10], [510, 10],
               [585, 10], [590, 90], [590, 143], [590, 195], [590, 247],
               [590, 300], [590, 355], [590, 410], [590, 463], [590, 514]] #positions of the first token on each square
  boardWidth = 650 # is the width of the board
  boardHeight = 650 # is the height of the board
  positions  = [[0,0],[20,20], [0,20], [20,0], [10,20], [10,0]] #position of each player on the square
  propWHouses = [] #list of properties with houses on them
  boardPosH = [[-50,-50],[510,565],[-50,-50],[405,565],[-50,-50],
                    [-50,-50],[243,565],[-50,-50],[140,565],[90,565],
                    [-50,-50],[65,510],[-50,-50],[65,408],[65,355],
                    [-50,-50],[65,246],[-50,-50],[65,140],[65,90],
                    [-50,-50],[90,65],[-50,-50],[195,65],[250,65],
                    [-50,-50],[355,65],[406,65],[-50,-50],[510,65],
                    [-50,-50],[565,90],[565,143],[-50,-50],[565,248],
                    [-50,-50],[-50,-50],[565,410],[-50,-50],[565,515]]#positions of the first house or the hotel on each square   
  boardSquares = ['Go', 'Crapper Street', 'Pot Luck', 'Gangsters Paradise', 'Income Tax', 'Brighton Station', 'Weeping Angel', 'Opportunity Knocks',
                       'Potts Avenue', 'Nardole Drive', 'Jail/just Visiting', 'Skywalker Drive', 'Tesla Power Co', 'Wookie Hole', 'Rey Lane',
                       'Hove Station', 'Cooper Drive', 'Pot Luck', 'Wolowitz Street', 'Penny Lane', 'Free Parking', 'Yue Fei Square', 'Opportunity Knocks',
                       'Mulan Rouge', 'Han Xin Gardens','Falmer Station','Kirk Close','Picard Avenue','Edison Water','Crusher Creek','Go to Jail',
                       'Sirat Mews','Ghengis Crescent','Pot Luck', 'Ibis Close', 'Lewes Station','Opportunity Knocks','Hawking Way','Super Tax',
                       'Turing Heights'] #list of the names of the squares on the board
  housePic = pygame.image.load('house.png') # loads the house image
  hotelPic = pygame.image.load('hotel.png') # loads the hotel image
    
  def __init__(self):
    self.boardWidth = 650 # is the width of the board
    self.boardHeight = 650 # is the height of the board
    self.tokenGUI = [(pygame.image.load('shoe.png'),(70,50)) , (pygame.image.load('smartphone.png'),(40,50)),
                     (pygame.image.load('goblet.png'),(40,50)) , (pygame.image.load('hatstand.png'), (40,50)),
                     (pygame.image.load('cat.png'),(40,50)), (pygame.image.load('spoon.png'),(50,50)) ]
    self.dicePic = pygame.image.load('dice.png')# loads the dice image
    self.playerButtonPos = [660, 710, 760, 810, 860, 910] #buttons x-axis position when choosing the number of players
    self.tokensAtGO = [[565, 570], [620, 615], [565, 615], [620,570], [590,570], [590,615]] #positions of each player at the beginning  


  def createScreen(self):
    """ Displays the GUI screen

    """
    pygame.display.set_caption('Property Tycoon') # sets windows title
    pygame.draw.rect(Game.gameDisplay, self.bgColour, self.sidePos) # draws the side display window
    Game.gameDisplay.blit(pygame.transform.scale(GUIFunctions.boardGUI, (self.boardWidth, self.boardHeight)), (0,0)) # displays the board
    pygame.display.update() # updates the window


  def setSideText(self, sentence, posX, posY):
    """ Displays the message on the side screen with given coordinates and font

    Parameters
    ----------
    sentence : str
      a sentence to be displayed on the side screen
    posX : int
      an integer that represents the X position on the grid
    posY : int
      an integer that represents the Y position on the grid
    """
    noOfPText = self.setTextFont(str(sentence), GUIFunctions.text) #gets the chosen font of the message
    noOfPText[1].center = (posX, posY) #centers the text around the x and y coordinate sent
    Game.gameDisplay.blit(noOfPText[0], noOfPText[1])
    pygame.display.update()


  def setTextFont(self, message, font):
    """ Chooses the font

    Parameters
    ----------
    message : string
      A text to be displayed
    font : Font
      The font of the string

    Returns
    -------
    textSurface : Surface
      Draws text on a surface
    textSurface.get_rect() : Rect
      Creates rectangle
    
    """
    textSurface = font.render(message, True, GUIFunctions.blackColour)#chooses the font
    return textSurface, textSurface.get_rect()

  def click(self, x, y, w, h): #takes the x and y position and the size
    """ Alerts the user that they have clicked on a button by creating a shadow effect on the corresponding button

    Parameters
    ----------
    x : int
      X position on the grid
    y : int
      y position on the grid
    w : int
      width of the area where click can be made
    h : int
      height of the area where click can be made

    Returns
    -------
    Boolean
      Indicates if the click has been made or not

    """
    mouse = pygame.mouse.get_pos() #the position of the mouse
    click = pygame.mouse.get_pressed() #if the mouse is clicked
    if ((x+w>mouse[0]>x) and (y+h>mouse[1]>y)):
      #if it is hovering over that particular button
      if click[0] == 1: #if that button was clicked
        pygame.draw.rect(GUIFunctions.gameDisplay, GUIFunctions.blackColour, [x,y,w,h])
        #shows the user its been clicked
        pygame.display.update()
        return True #returns that its been clicked

  def toQuit(self):
    """ Allows user to quit the game
    """
    for event in pygame.event.get(): #allows user to quit
      if event.type == pygame.QUIT:
        pygame.quit(); sys.exit();

  def clearSideScreen(self): #clears the side screen
    """ Clears the side screen by updating the game
    """
    pygame.draw.rect(GUIFunctions.gameDisplay, GUIFunctions.bgColour, GUIFunctions.sidePos)
    pygame.display.update() #updates the screen
              
  def addButton(self, word, posX, posY):
    """ Used to add a button for the GUI

    Parameters
    ----------
    word : str
      The word displayed on the button
    posX : int
      an integer that represents the X position on the grid
    posY : int
      an integer that represents the Y position on the grid
    """
    pygame.draw.rect(GUIFunctions.gameDisplay, GUIFunctions.buttonColour, [posX, posY, 80, 40])
    p = self.setTextFont(word, GUIFunctions.text)
    p[1].center = (int(posX+(80/2)),int(posY+(40/2)))
    Game.gameDisplay.blit(p[0], p[1])

  def updateBoard(self):#clears the board then updates it
    """ Update the board with the new position of tokens.
    If two or more tokens are on the same square, changes their position so that they can all be seen on the square
    """
    GUIFunctions.gameDisplay.blit(pygame.transform.scale(GUIFunctions.boardGUI, (GUIFunctions.boardWidth, GUIFunctions.boardHeight)), (0,0)) #displays the board
    for i,player in enumerate(Player.playerList): #for every player
      tokenPic = GUIFunctions.tokenDict[player.token] #changes the postion of the token, therefore all tokens can be seen if they are all on the same square
      x = GUIFunctions.boardPosT[player.position][0] + GUIFunctions.positions[i][0]
      y = GUIFunctions.boardPosT[player.position][1] + GUIFunctions.positions[i][1]
      GUIFunctions.gameDisplay.blit(pygame.transform.scale(tokenPic, (30,30)), [x, y]) #update the board with the token's new position
    pygame.display.update()

  def createTextBox(self, posX, posY): #creates a text box
    """ Creates a text box where users can enter the required input, Users press enter after entering an input

    Parameters
    ----------
    posX : int
      an integer that represents the X position on the grid
    posY : int
      an integer that represents the Y position on the grid


    Returns
    -------
    string : string
      A string that represents the input the user made to the inputBox 
    """
    textField = pygame.draw.rect(GUIFunctions.gameDisplay, (255,255,255), [posX, posY, 80, 20]) #displays a textbox
    pygame.display.update()
    string = '' #empty string when the while-loop starts
    askForInput = True
    while askForInput:
      GUIFunctions.toQuit(self) #allows user to quit
      k = GUIFunctions.userInput(self, posY) #asks user for input
      if k == 'return': #when user presses enter 
        askForInput = False #the loop is broken
      else:
        string += k #adds to the string the key that has been pressed by the user
        #displays the numbers which were pressed by the user
        textField = pygame.draw.rect(GUIFunctions.gameDisplay, (255,255,255), [posX, posY, 80, 20])
        p = GUIFunctions.setTextFont(self, string, GUIFunctions.text)
        p[1].center = (int(posX+20),int(posY+(20/2)))
        GUIFunctions.gameDisplay.blit(p[0], p[1])
        pygame.display.update()
    return int(string) #retrurns the string converted to int

  def userInput(self, posY): #takes the input
    """ Only allows user to input number from 0,1,2,3,4,5,6,7,8,9

    Parameters
    ----------
    posY : int
      an integer that represents the Y position on the grid
    """
    while True:
      GUIFunctions.toQuit(self) #allows user to quit
      event = pygame.event.poll()
      keys = pygame.key.get_pressed() 
      if event.type == pygame.KEYDOWN: #when user presses the key
        key = pygame.key.name(event.key) #stores its value in the 'key' variable
        if key in ('0', '1','2','3','4','5','6','7','8','9'): #allows only numbers to be input in the box
          return key
        elif key == 'return': #when enter is pressed returns 'return' string
          return key
        else:
          self.setSideText('Please enter a number', GUIFunctions.textPosX, posY+30)
          
  def displayHouseHotel(self): 
    """ Displays the image of house or hotel after the player has improved their property
    It rotates the image of house or hotel corresponding to the position they should be displayed on the board
    """
    for prop in GUIFunctions.propWHouses:
      index = GUIFunctions.boardSquares.index(prop.name) #takes the position on the board where the house is supposed to be displayed
      if index <11 : #takes into the account positions from 0 to 10
        if prop.currentRent == 5: #checks if the house or the hotel should be displayed
          x = GUIFunctions.boardPosH[index][0] #x-axis position of the house
          y = GUIFunctions.boardPosH[index][1] #y-axis position of the house
          self.updateBoard()
          GUIFunctions.gameDisplay.blit(pygame.transform.scale(GUIFunctions.hotelPic, (20,20)), [x, y]) #displays the hotel
          pygame.display.update() 
        else:
          for i in range(prop.currentRent):
            x = GUIFunctions.boardPosH[index][0] + 10*i
            y = GUIFunctions.boardPosH[index][1] 
            GUIFunctions.gameDisplay.blit(pygame.transform.scale(GUIFunctions.housePic, (20,20)), [x, y]) #displays the house
            pygame.display.update() 
      elif index in range(11, 20): #takes into the account positions from 11 to 20
        if prop.currentRent == 5:
          x = GUIFunctions.boardPosH[index][0]
          y = GUIFunctions.boardPosH[index][1]
          self.updateBoard()
          hotel = pygame.transform.rotate(GUIFunctions.hotelPic, 270)#rotates the picture of the house by 270 degrees counter-clockwise
          GUIFunctions.gameDisplay.blit(pygame.transform.scale(hotel, (20,20)), [x, y]) #displays the hotel
          pygame.display.update() 
        else:
          for i in range(prop.currentRent):
            x = GUIFunctions.boardPosH[index][0] 
            y = GUIFunctions.boardPosH[index][1] + 10*i
            house = pygame.transform.rotate(GUIFunctions.housePic, 270)#rotates the picture of the house by 270 degrees counter-clockwise
            GUIFunctions.gameDisplay.blit(pygame.transform.scale(house, (20,20)), [x, y]) #displays the house
            pygame.display.update() 
      elif index in range(21, 30): #takes into the account positions from 21 to 30
        if prop.currentRent == 5:
          x = GUIFunctions.boardPosH[index][0]
          y = GUIFunctions.boardPosH[index][1]
          self.updateBoard()
          hotel = pygame.transform.rotate(GUIFunctions.hotelPic, 180)#rotates the picture of the house by 180 degrees counter-clockwise
          GUIFunctions.gameDisplay.blit(pygame.transform.scale(hotel, (20,20)), [x, y]) #displays the hotel
          pygame.display.update() 
        else:
          for i in range(prop.currentRent):
            x = GUIFunctions.boardPosH[index][0] + 10*i
            y = GUIFunctions.boardPosH[index][1]
            house = pygame.transform.rotate(GUIFunctions.housePic, 180)#rotates the picture of the house by 180 degrees counter-clockwise
            GUIFunctions.gameDisplay.blit(pygame.transform.scale(house, (20,20)), [x, y]) #displays the house
            pygame.display.update() 
      else: #takes into the account positions from 31 to 39
        if prop.currentRent == 5: 
          x = GUIFunctions.boardPosH[index][0]
          y = GUIFunctions.boardPosH[index][1]
          self.updateBoard()
          hotel = pygame.transform.rotate(GUIFunctions.hotelPic, 90) #rotates the picture of the house by 90 degrees counter-clockwise
          GUIFunctions.gameDisplay.blit(pygame.transform.scale(hotel, (20,20)), [x, y]) #displays the hotel
          pygame.display.update() 
        else:
          for i in range(prop.currentRent):
            x = GUIFunctions.boardPosH[index][0]  
            y = GUIFunctions.boardPosH[index][1] + 10*i
            house = pygame.transform.rotate(GUIFunctions.housePic, 90)#rotates the picture of the house by 90 degrees counter-clockwise
            GUIFunctions.gameDisplay.blit(pygame.transform.scale(house, (20,20)), [x, y]) #displays the house
            pygame.display.update()  
        
      
class Player(GUIFunctions):
  """
  A class usd to represent a player

  Attributes
  ----------
  playerList : list of objects
    Becomes a list of all the players objects that are playing
  Token : string
    Is the players token that they choose at the start
  Properties : list
    A list of property objects that the player owns
  Bankrupt : boolean
    To show if the player is bankrupt or not, true if player has ran out of properties and money
  roundsInJail : int
    The total number rounds in jail (used for one of the 3 options to get out of jail)
  inJail : boolean
    True if the player is in jail, false if they player is not
  Dice : Dice object
    Is the dice for that player (one for each player to keep track of the doubles)
  Balance : int
    The total in the players bank
  Position : int
    The index location on the board
  Lap : int
    How many times the player has moved around the board
  currentSquare : object
    Of the square that the player lands on
  Groups : int
    Of property objects, sorted into their groups - will never include utilities, squares or stations
  getOutOfJailCardOpportunity : int
    Number of get out of jail free cards in the opportunity knocks pile
  getOutOfJailCardPot : int
    Number of get out of jail free cards in the pot luck pile

  Methods
  -------
  start()
    Starts players turn
  move()
    Moves the token on the board to the corresponding position that has been rolled on the dice
  displayOptions()
    Displays the options for the user to take their go
  raiseFunds()
    Allows the user to raise money
  outOfJail()
    Allows player the chance of getting out of jail
  improveProperty()
    Gives the option of improving properties to the player.
  improve()
    Finds a list of possible properties that can be improved
  addHouseHotel(group)
    Allows user to upgrade their property to add houses/hotel
  mortgageProperty()
    Allows user to put a property up for mortgage
  unmortgage()
    Allows user to unmortgage a mortgaged property
  sellHouses(groupNo)
    Allows user to sell their houses on their properties
  sellProperties(possProp)
    Allows user to sell their properties
  findOptions()
    Goes through the players groups and checks if the player has all properties in that group
  viewProperties()
    Displays users squares
  checkDouble()
    Check if a user rolled a double
  passGoCheck()
    Check to see if users counter passes go
  checkBankrupt()
    Checks if user has any money or assets
  checkEnoughMoney(toPay)
    Checks if user has enough money to pay for the price in 'toPay'
  sellEverything()
    Used for selling all assets of a player, only in abridged version of game 
  """
  playerList = [] #is a list of each player

  def __init__(self, token):
    """
    Parameters
    ----------
    token : str
      The name of the token that the player uses
    """
    GUIFunctions.__init__(self)
    Player.playerList.append(self) # adds this player's object into the list of players
    self.token = token
    self.properties = [] # lists all players property objects
    self.bankrupt = False # boolean value - true if the player has ran out of money
    self.roundsInJail = 0 # how many rounds have the player waited to be released from jail
    self.inJail = False # true if the player is in jail
    self.dice = Dice() # creates an object dice
    self.balance = 1500 # players banks start off with £1500
    self.position = 0 # location on the board 0-39
    self.lap = 1 # how many times the player has moved around the board
    self.currentSquare = Game.board[self.position] # is the object of what square the player lands on
    self.groups = [[],[],[],[],[],[],[],[]] # a list of lists of properties, sorted into their groups 
    self.getOutOfJailCardOpportunity = 0 # how many get out of jail free cards they have
    self.getOutOfJailCardPot = 0 # how many get out of jail free cards they have
    
  def start(self):
    """Completes jail checks, then produces the main menu
    """
    self.checkBankrupt() # check if the player is bankrupt
    if self.bankrupt == False:
      if self.roundsInJail == 2: # when a player has choosen to stay in jail for 2 rounds and has completed those 2 rounds
        self.clearSideScreen()
        self.setSideText(('Player ' +str(self.token)), self.textPosX, 100)
        self.setSideText('You have waited 2 rounds and are now released from jail.', self.textPosX, 120)
        time.sleep(3)
        self.inJail = False
        self.roundsInJail = 0
      if self.inJail == True: # gives the players options to get out of jail
        self.outOfJail()
      else:
        self.displayOptions() 
        self.checkBankrupt() # checks if player is bankrupt
        if (self.bankrupt == False) and (self.inJail == False) and (self.lap>1):
          self.improveProperty()
          

  def move(self):
    """ Moves the token on the board to the corresponding position that has been rolled on the dice
    Displays the name of the square the player has landed on in the sidebar
    """
    self.checkBankrupt()
    if self.bankrupt == False:    
      self.dice.roll() # rolls the dice
      noSpaces = self.dice.total
      self.position += noSpaces # moves that many spaces on the dice
      self.pastGoCheck() # checks to see if the player has gone past go
      self.currentSquare = Game.board[self.position]
      self.setSideText(('Player ' +self.token+ ', you have landed on ' +str(self.currentSquare.name)), self.textPosX, 520)
      self.updateBoard()
      self.displayHouseHotel()
      time.sleep(3)
      self.currentSquare.triggerEvent(noSpaces) # triggers the event of the square that is landed on
      self.checkDouble() # checks to see if the dice is a double
      

  def displayOptions(self): 
    """ Displays the money balance and options the player has on the sidebar before they
    have clicked on the dice to roll the dice
    """
    self.clearSideScreen()
    self.setSideText(('Player ' +Game.currentPlayer.token), self.textPosX, 100)
    self.setSideText(('Balance = £' +str(self.balance)), self.textPosX, 120)
    self.setSideText(('Main Menu:'), self.textPosX, 140)
    self.addButton('Properties', 760, 160)
    self.addButton('Raise funds', 760, 220) # lets the player raise their funds by selling properties or mortgaging the properties
    self.addButton('Unmortgage', 760, 280)# option to pay off the mortgage of mortgaged properties
    GUIFunctions.gameDisplay.blit(pygame.transform.scale(self.dicePic, (60,60)), (770, 340)) #displays the dice
    pygame.display.update() #displays the buttons 
    while True:  
      self.toQuit()
      click1 = self.click(760, 160, 80, 40) #button 'Properties' is clicked
      click2 = self.click(760, 220, 80, 40) #button 'Raise funds' is clicked
      click3 = self.click(760, 280, 80, 40) #button 'Unmortgage' is clicked
      clickDice = self.click(770, 340, 60, 60) #dice picture is clicked
      if clickDice == True:
        time.sleep(0.2)
        self.move()
        break
      if click1 == True:
        time.sleep(0.2)
        self.viewProperties()
        break
      if click2 == True:
        time.sleep(0.2)
        self.raiseFunds()
        break
      if click3 == True:
        time.sleep(0.2)
        self.unmortgage()
        break
        
  def raiseFunds(self):
    """   Displays and processes the options player has if they choose to raise funds on the sidebar
    """
    if len(self.properties) > 0: # if the player can raise any funds they need to own a property
      self.clearSideScreen()
      self.setSideText(('Player ' +Game.currentPlayer.token+ ', what would you like to sell?'), self.textPosX, 100)
      self.setSideText('1. Properties/Utilities/Stations', self.textPosX, 120)
      self.addButton('Go', 760, 130)
      self.setSideText('2. Houses/Hotels', self.textPosX, 180)
      self.addButton('Go', 760, 190)
      self.setSideText('3. Mortgage a property', self.textPosX, 240)
      self.addButton('Go', 760, 250)
      self.addButton('Back', 800, 550)
      pygame.display.update()
      possProp, possHouseHotel = self.findOptions()  # returns a list of possible properties to sell (possProp) and a list of possible properties with hotels on them (possHotel)
      while True:
        self.toQuit()
        click1 = self.click(760, 130, 80, 40) 
        click2 = self.click(760, 190, 80, 40) 
        click3 = self.click(760, 250, 80, 40) 
        clickb = self.click(800, 550, 80, 40) 
        if click1 == True:
          time.sleep(0.2)
          if len(possProp) > 0: # if there is no possible properties then this option is not avaliable
            self.sellProperties(possProp)
            break
          else:
            self.clearSideScreen()
            self.setSideText(('Player ' +Game.currentPlayer.token+ ', you cannot sell any properties right now'), self.textPosX, 100)
            time.sleep(3)
            self.displayOptions()
            break
        if click2 == True:
          time.sleep(0.2)
          if len(possHouseHotel) > 0: # if there are any properties with houses that can be sold
            self.clearSideScreen()
            self.setSideText(('Player ' +Game.currentPlayer.token), self.textPosX, 100)
            counter = 0
            for i in possHouseHotel:
              self.setSideText(('Group: ' +str(possHouseHotel[counter]+1)+' '+ str(Property.groupColour[i])), self.textPosX, 120+10*i) # lists the group that can sell houses from 
              counter += 1
            self.setSideText('Which group would you like to sell a house or a hotel from?', self.textPosX, 210)
            self.setSideText('(enter the number)', self.textPosX, 230)
            valid = True
            while valid:
              groupID = self.createTextBox(760, 250)
              if groupID in range(1, 9):
                valid = False
              else:
                self.setSideText('Number out of range.', self.textPosX, 280)
                self.setSideText('Please enter number of the group', self.textPosX, 300) 
            self.sellHouses(groupID)
            time.sleep(3)
            self.displayOptions()
            break
          else:
            self.clearSideScreen()
            self.setSideText(('Player ' +Game.currentPlayer.token), self.textPosX, 100)
            self.setSideText('You cannot sell any houses or hotels right now', self.textPosX, 120)
            time.sleep(3)
            self.displayOptions()
            break
        if click3 == True:
          time.sleep(0.2)
          if len(self.properties) > 0:
            self.mortgageProperty()
            self.displayOptions()
            break
          else:
            self.clearSideScreen()
            self.setSideText(('Player ' +Game.currentPlayer.token), self.textPosX, 100)
            self.setSideText('You do not have any properties to mortgage', self.textPosX, 120)
            time.sleep(3)
            self.displayOptions()
            break
        if clickb == True:
          time.sleep(0.2)
          self.displayOptions()
          break
    else: # cannot raise any funds when the player has no properties
      self.clearSideScreen()
      self.setSideText(('Player ' +Game.currentPlayer.token+ ', you do not own any properties'), self.textPosX, 100)
      self.addButton('Back', 800, 550)
      pygame.display.update()
      while True:
        self.toQuit()
        click = self.click(800, 550, 80, 40)
        if click == True:
          time.sleep(0.2)
          self.displayOptions()
          break

  def outOfJail(self):
    """ Allows the user to choose an option to get out of jail
    """
    if self.roundsInJail == 1:
      self.clearSideScreen()
      self.setSideText(('Player ' +self.token), self.textPosX, 100)
      self.setSideText('You have previously chosen to wait 2 rounds', self.textPosX, 120)# if the player has previously choosen to wait in jail for 2 rounds, therefore has got 1 left
      self.setSideText('You have 1 round left to wait.', self.textPosX, 140)
      time.sleep(3)
      self.roundsInJail += 1 # increments the number of rounds
    else:
      self.clearSideScreen()
      self.setSideText(('Player ' +self.token+ ', you are in jail, options:'), self.textPosX, 100)# menu is output
      self.setSideText('You have 1 round left to wait.', self.textPosX, 120)
      self.addButton('Pay £50', 760, 130)
      self.addButton('Wait 2 rounds', 760, 180)
      pygame.display.update()
      if( self.getOutOfJailCardPot > 0 or self.getOutOfJailCardOpportunity > 0): # if they have a get out of jail free card then this is an option
        self.setSideText('You can use a get out of jail free card', self.textPosX, 230)
        self.addButton('Use a card', 760, 240)
        pygame.display.update()
      while True:
        self.toQuit()
        click1 = self.click(760, 130, 80, 40)
        click2 = self.click(760, 180, 80, 40)
        click3 = self.click(760, 240, 80, 40)
        if click1 == True:
          time.sleep(0.2)
          if self.checkEnoughMoney(50) == True: #checks to see if the player has enough money
            self.balance -= 50 
            Game.freeParking += 50
            self.setSideText('You have payed £50 and are released from jail!', self.textPosX, 260)
            time.sleep(3)
            self.inJail = False # player is released from jail
            break
          else:
            self.setSideText('You do not have enough money, wait 2 rounds', self.textPosX, 260)
            self.roundsInJail += 1
            break
        if click2 == True:
          time.sleep(0.2)
          self.setSideText('You have to wait 2 rounds to be released from jail', self.textPosX, 260)
          self.roundsInJail += 1
          break
        if click3 == True:
          time.sleep(0.2)  
          if self.getOutOfJailCardOpportunity > 0:
            self.getOutOfJailCardOpportunity -= 1
            OpportunityKnocks.getOutOfJailOwned = False
          else:
            self.getOutOfJailCardPot -= 1
            PotLuck.getOutOfJailOwnedPot = False
          self.setSideText('You have used get out of jail free card', self.textPosX, 260)
          self.setSideText('And are released from jail!', self.textPosX, 280)
          self.inJail = False
          break

  def improveProperty(self):
    """ Allows user to improve properties by clicking on a button
    """
    self.clearSideScreen()
    self.setSideText(('Player ' +Game.currentPlayer.token), self.textPosX, 100)
    self.setSideText('Would you like to improve any properties with houses/hotel?', self.textPosX, 120)
    self.addButton('Yes', 670, 150)
    self.addButton('No', 850, 150)
    pygame.display.update()
    while True:
      self.toQuit()
      clickY = self.click(670, 150, 80, 40)
      clickN = self.click(850, 150, 80, 40)
      if clickY == True:
        time.sleep(0.2)
        self.improve()
        break
      if clickN == True:
        time.sleep(0.2)
        break
      
  def improve(self):
    """ Allows user to choose properties to add houses/hotels too
    """
    possibleImprovements = [] # will become a list of possible properties that can be improved
    for i, group in enumerate(self.groups, start = 0): 
      canAdd = True # used as true if the group is a possible option to improve
      if len(group) == Property.noInGroups[i]: # if the player has all properties in that group
        for prop in group: # for each property object in the group
          if prop.mortgaged == True: # cannot add houses to mortgaged properties
            canAdd = False
        if canAdd == True:
          possibleImprovements.append(group) # adds the group to the list of properties that can be improved
    if len(possibleImprovements) > 0: # if the player can improve any properties
      self.clearSideScreen()
      self.setSideText('Menu: ', self.textPosX, 210)
      for i, posGroup in enumerate(possibleImprovements):
        self.setSideText(('Group ' +str(posGroup[0].group)+' ' +str(Property.groupColour[posGroup[0].group-1])), self.textPosX, 230+50*i) # prints the group number and colour - using the first property in the group to get the group number
        for k, prop in enumerate(posGroup):
          self.setSideText(('   ' +prop.name), self.textPosX, ((230+40*i+10)+10*k)) # prints the property in that group
        self.setSideText(('To improve this group costs £' +str(Property.hotelHouseCost[posGroup[0].group - 1])), self.textPosX, 270+40*i)
      self.setSideText('Which group would you like to add houses/hotel too?', self.textPosX, 430)
      self.setSideText('(enter the group number)', self.textPosX, 450)
      valid = True
      while valid:
        groupToImprove = self.createTextBox(760, 470)
        if groupToImprove in range(1,9):
          valid = False
        else:
          self.setSideText('Number out of range.', self.textPosX, 500)
          self.setSideText('Please enter number of the group', self.textPosX, 510) 
      self.addHousesHotel(groupToImprove)
    else:
      self.setSideText('You need all properties of a group to start improvements', self.textPosX, 210) # when the player cannot improve any properties
      time.sleep(3)

    
  def addHousesHotel(self, group):
    """ Gives the player options on the sidebar, allowing them to enter the number of the property the want to improve

    Parameters
    ----------
    group : int
      the number of the group that the player has chosen to improve
    """
    lowestNoOfHouses = 5 # lowestNoOfHouses will be set to the number of houses on the property with the lowest number of houses in that group
    for prop in self.groups[group-1]:
      if lowestNoOfHouses > prop.currentRent:
        lowestNoOfHouses = prop.currentRent
    if lowestNoOfHouses == 5: # if the lowest number is 5 then it means that all properties have one hotel on them
      self.setSideText('You have improved all your properties in this group.', self.textPosX, 470)
      time.sleep(3)
    else: # if there is still room to add houses/hotels
      avaliableProps = []
      for prop in self.groups[group-1]:
        if prop.currentRent == lowestNoOfHouses:
          avaliableProps.append(prop) # adds all properties with the lowest number of houses - e.g. prop1 = 2, prop2 = 2 and prop3 = 3 - avaliableProps = [prop1, prop2]
      self.clearSideScreen()
      self.setSideText('Menu:', self.textPosX, 100)
      for i, prop in enumerate(avaliableProps, start = 1): # lists all properties that can be improved
        self.setSideText((str(i) +' Add to '+ prop.name), self.textPosX, 80+30*i)
        self.setSideText(('It costs £' +str(prop.houseHotelPrice)+ ' to improve this property'), self.textPosX, 90+30*i)
      if self.checkEnoughMoney(prop.houseHotelPrice) == True: # checks to see if the player has enough money to buy a house onto the property
        self.setSideText('Which property would you like to add to? (enter a number)', self.textPosX, 480)
        valid = True
        while valid:
          option = self.createTextBox(760, 490)
          if option in range(1,(len(avaliableProps)+1)):
            valid = False
          else:
            self.setSideText('Number out of range.', self.textPosX, 520)
            self.setSideText('Please enter number between 1 and ' +str(len(avaliableProps)), self.textPosX, 530) 
        chosenProp = avaliableProps[option-1]
        GUIFunctions.propWHouses.append(chosenProp)
        chosenProp.currentRent = chosenProp.currentRent + 1
        self.displayHouseHotel()
        self.balance -= chosenProp.houseHotelPrice
        Game.bankBalance += chosenProp.houseHotelPrice
        self.setSideText('Would you like to improve any more of your properties? ', self.textPosX, 530)
        self.addButton('Yes', 670, 550)
        self.addButton('No', 850, 550)
        pygame.display.update()
        while True:
          self.toQuit()
          clickY = self.click(670, 550, 80, 40)
          clickN = self.click(850, 550, 80, 40)
          if clickY == True:
            time.sleep(0.2)
            self.improve()
            break
          if clickN == True:
            time.sleep(0.2)
            break
        
  def mortgageProperty(self):
    """ If player has properties available that can be mortgage,
    it will display a message asking players to choose the property they want to mortgage
    """
    noHouseProp = [] # will become a list of property objects that can be put on morgage
    allProps = []
    allProps.extend(self.properties) # becomes a duplication of a list of all property objects that the player has   
    for group in self.groups: # checks to see if the group has houses on it - if it does, it needs to sell the houses before being mortgaged
      total = 0
      for prop in group:
        total += prop.currentRent
        allProps.remove(prop) #removes all properties - leaves with utilities and stations
      if total == 0:
        noHouseProp.extend(group) # adds the properties of a group that doesn't have any houses/hotels on their property
    noHouseProp.extend(allProps) # adds all utilities and stations to the options to be mortgaged
    propOptions = [] # will become a list of all the properties that are not already mortgaged
    for prop in noHouseProp:
      if prop.mortgaged == False:
        propOptions.append(prop)
    if len(propOptions) == 0: # if there are no avaliable properties that can be mortgaged
      self.clearSideScreen()
      self.setSideText(('Player ' +Game.currentPlayer.token+ ', you do not have any properties to mortgage'), self.textPosX, 100)
    else:
      self.clearSideScreen()
      self.setSideText(('Player ' +Game.currentPlayer.token), self.textPosX, 100)
      self.setSideText('Menu:', self.textPosX, 120)
      for i, prop in enumerate(propOptions, start = 1): # will list all properties that can be mortaged
        self.setSideText((str(i)+ '. ' +str(prop.name)), self.textPosX, 130+10*i)
      self.setSideText('Which property would you like to mortgage?(enter number)', self.textPosX, 350)  
      valid = True
      while valid:
        option = self.createTextBox(760, 360)
        if option in range(1,(len(propOptions)+1)):
          valid = False
        else:
          self.setSideText('Number out of range.', self.textPosX, 390)
          self.setSideText('Please enter number between 1 and ' +str(len(propOptions)), self.textPosX, 400)
      p = propOptions[option-1] # mortgages the property that the player chooses - updates the property
      self.balance += p.cost * 0.5
      Game.bankBalance -= p.cost * 0.5
      p.mortgaged = True
      print(p.name)

  def unmortgage(self):
    """ If player has properties can that be unmortgaged,
    it will display a message asking player which property they want to unmortgage
    """
    self.clearSideScreen()
    self.setSideText(('Player ' +Game.currentPlayer.token), self.textPosX, 100)
    mortgagedProps = [] # becomes a list of properties that have a mortgage to be paid
    for prop in self.properties: 
      if prop.mortgaged == True:
        mortgagedProps.append(prop)
    if len(mortgagedProps) == 0: # if no properties have a mortgage to be paid off
      self.addButton('Back', 800, 550)
      pygame.display.update()
      self.setSideText('You do not have any mortgaged properties.', self.textPosX, 120)
      while True:
        self.toQuit()
        clickb = self.click(800, 550, 80, 40)
        if clickb == True:
          time.sleep(0.2)
          self.displayOptions()
          break
    else:
      self.setSideText('Menu:', self.textPosX, 120)
      for i, mProp in enumerate(mortgagedProps, start = 1): # lists the properties that the player can off the mortgages
        self.setSideText((str(i)+ '. ' +str(mProp.name)), self.textPosX, 130+10*i)
      self.setSideText('Which property would you like to unmortgage?(enter number)', self.textPosX, 350) 
      valid = True
      while valid:
        option = self.createTextBox(760, 360)
        if option in range(1,(len(mortgagedProps)+1)):
          valid = False
        else:
          self.setSideText('Number out of range.', self.textPosX, 390)
          self.setSideText('Please enter number between 1 and ' +str(len(mortgagedProps)), self.textPosX, 400) 
      chosenProp = mortgagedProps[option-1]
      if self.checkEnoughMoney(chosenProp.cost * 0.5) == True: # of the player has enough money to pay off the mortgage, balances and property is updated
        self.balance -= chosenProp.cost * 0.5
        Game.bankBalance += chosenProp.cost * 0.5
        chosenProp.mortgaged = False
        self.displayOptions()

    
  def sellHouses(self, groupNo):
    """   Displays a message on the sidebar asking player which property they
    would like to sell the house from, updates the bank and properties.
    Displays a message on the sidebar asking player which property they would like to
    sell the house from, updates the bank and properties.

    Parameters
    ----------
    groupNo : int
      Is the current group index of the group that the player is selling houses from to raise funds
    """
    maxHouseNo = 0 # will become the highest number of houses on a property in the group with the id - groupNo
    for prop in self.groups[groupNo-1]: # for each property in the current group
      if prop.currentRent > maxHouseNo: # if the property has a higher number of houses, maxHouseNo is updated 
        maxHouseNo == prop.currentRent
    avaliableProps = [] # will become a list of the property/ies with the highest number of houses/hotels in this group
    for prop in self.groups[groupNo-1]:
      if prop.currentRent == maxHouseNo:
        avaliableProps.append(prop)
    self.setSideText('Menu:', self.textPosX, 280)
    for i, prop in enumerate(avaliableProps, start = 1): # lists through all properties with the highest amount of houses/hotels
      self.setSideText((str(i) +'. ' +str(prop.name)), self.textPosX, 290+10*i)
    self.setSideText(('Which property would you like to remove your house/hotel from?(enter number)'), self.textPosX, 340)  
    valid = True
    while valid:
      option = self.createTextBox(760, 350)
      if option in range(1,(len(avaliableProps)+1)):
        valid = False
      else:
        self.setSideText('Number out of range.', self.textPosX, 370)
        self.setSideText('Please enter number between 1 and ' +str(len(avaliableProps)), self.textPosX, 390)  
    propToSell = avaliableProps[option-1] # sells the house back, updates the property and the banks
    propToSell.currentRent -= 1
    if propToSell.currentRent == 0:
      GUIFunctions.propWHouses.remove(propToSell)
    self.balance += propToSell.houseHotelPrice
    Game.bankBalance -= propToSell.houseHotelPrice
    
    
  def sellProperties(self, possProp):
    """ Clears the sidebar and displays a message asking player
    which property they would like to sell and allows the player to enter a number.

    Parameters
    ----------
    possProp : int
      Is the position of the property
    """
    self.clearSideScreen()
    self.setSideText(('Player ' +Game.currentPlayer.token), self.textPosX, 100)
    self.setSideText('Menu:', self.textPosX, 110)
    self.setSideText('(If the property is morgaged you only receieve half its cost)', self.textPosX, 120)
    possProp, possHouseHotel = self.findOptions()  # returns a list of possible properties to sell (possProp) and a list of possible properties with hotels on them (possHotel)
    for i, prop in enumerate(possProp, start = 1): #prints the list of the properties that can be sold and the buttons with the numbers of the properties
      self.setSideText((str(i)+ '. ' +str(prop.name)+ ' - ' +str(prop.cost)), self.textPosX, 120+10*i)   
    self.setSideText('Which property would you like to sell? ', self.textPosX, 380)
    self.setSideText('enter the number', self.textPosX, 390)
    valid = True
    while valid:
      no = self.createTextBox(760, 400)
      if no in range(1,(len(possProp)+1)):
        valid = False
      else:
        self.setSideText('Number out of range.', self.textPosX, 430)
        self.setSideText('Please enter number between 1 and ' +str(len(possProp)), self.textPosX, 450) 
    time.sleep(0.2)
    propertyToSell = possProp[no-1] 
    propertyToSell.updateSoldProp() # updates the property
    possProp.remove(propertyToSell)
    self.clearSideScreen()
    self.setSideText('Would you like to sell any more of your properties?', self.textPosX, 440)
    self.addButton('Yes', 670, 460)
    self.addButton('No', 850, 460)
    pygame.display.update()
    while True:
      self.toQuit()
      clickY = self.click(670, 460, 80, 40)
      clickN = self.click(850, 460, 80, 40)
      if clickY == True:
        time.sleep(0.2)
        self.sellProperties(possProp)
        break
      if clickN == True:
        time.sleep(0.2)
        self.raiseFunds()
        break

  def findOptions(self):
    """ Goes through the players groups and checks if the player has all properties in that group
    If they do the properties in that group are checked to see if there is existing houses on them, if not
    then the group ID (the index) is added to a list of other groups that have houses/hotels on them 
    If the player doesn’t have all properties in the group then they are added to the list of properties that can be sold
    
    Returns
    -------
    possibleProperties : list
      A list of property objects that the player can sell to raise funds
    possibleHouseHotel : list
      A list of group indices that will point to groups that have at least one house on at least one of the group properties 
    """
    tempProperties = []
    tempProperties.extend(self.properties) # will become a list of properties not including any full group of player owned properties
    possibleProperties = [] # will be a list of properties that do not have any houses on it
    possibleHouseHotel = [] # will be a list of group numbers which have 1 or more houses on the group
    for i, group in enumerate(self.groups, start = 0): # looks through self.groups - a list of lists of the properties sorted into their group
      if(len(self.groups[i]) == int(Property.noInGroups[i])): # if the player owns all properties of the current group
        totalHouses = 0
        for currentProp in group: # adds the total number of houses of each property in the group 
          totalHouses += currentProp.currentRent
          tempProperties.remove(currentProp) # removes the property from tempProperties
        if totalHouses > 0:
          possibleHouseHotel.append(i) # if this group has houses on at least one of their properties it is added to possibleHouseHotel
        else:
          possibleProperties.extend(group)# if the player has no houses on the current group then is added to possibleProperties
    possibleProperties.extend(tempProperties) # adds all the extra properties left over
    return possibleProperties, possibleHouseHotel
      
  def viewProperties(self):
    """ Displayes the players properties
    """
    self.clearSideScreen()
    self.setSideText('Properties of Player ' +str(self.token), self.textPosX, 100)
    if not self.properties: #checks if the list of the properties is empty
      self.setSideText('You don\'t have any properties', self.textPosX, 130)
    else:
      for i,prop in enumerate(self.properties):
        if prop.mortgaged == True:
          self.setSideText(str(i+1)+ '. ' +str(prop.name)+ '(Mortgaged)', self.textPosX, 130+i*10)
        else:
         self.setSideText(str(i+1)+ '. ' +str(prop.name), self.textPosX, 130+i*10)
    self.addButton('Back', 800, 550)
    pygame.display.update()
    while True:
      self.toQuit()
      clickb = self.click(800, 550, 80, 40)
      if clickb == True:
        time.sleep(0.2)
        self.displayOptions()
        break

  def checkDouble(self):
    """Checks whether if the player has rolled a double or not, if 2 doubles, another go, 3 doubles the player is sent to jail
    """
    if self.dice.doublesCount == 1 or self.dice.doublesCount == 2: # retrieves the doublesCount from the players dice
      if(self.inJail == False):
        self.clearSideScreen()
        self.setSideText(('Player ' +Game.currentPlayer.token), self.textPosX, 100)
        self.setSideText('You rolled a double, therefore get another go', self.textPosX, 120)
        GUIFunctions.gameDisplay.blit(pygame.transform.scale(self.dicePic, (60,60)), (770, 340)) #displays the dice
        pygame.display.update()
        while True:
          self.toQuit()
          clickDice = self.click(770, 340, 60, 60)
          if clickDice == True:
            time.sleep(0.2)
            self.move() # if they roll a double they get another go
            break
      else:
        self.clearSideScreen()
        self.setSideText(('Player ' +Game.currentPlayer.token), self.textPosX, 100)
        self.setSideText('Although you have rolled double, you are now in jail', self.textPosX, 120)
        time.sleep(3)
        self.dice.doublesCount = 0
    elif self.dice.doublesCount == 3:
      self.clearSideScreen()
      self.setSideText(('Player ' +Game.currentPlayer.token), self.textPosX, 100)
      self.setSideText('You have rolled three doubles, therefore go to jail', self.textPosX, 120)
      self.inJail = True # if they get 3 doubles then they go to jail
      self.position = 10 # updates the players position to jail
      self.updateBoard()
      self.displayHouseHotel()
      time.sleep(3)
    else:
      self.dice.doublesCount = 0 # if the current dice is not a double - the double check is set back to 0

  def pastGoCheck(self):
    """ Checks whether the player has passed go square, if they have, it displays a message on the sidebar saying,
    ‘You have passed go, therefore have collected £200’ and updates bank balance
    """
    if self.position > 39: # when the position is larger than 39 it means that the player has gone past go
      self.position -= 40
      self.balance += 200
      Game.bankBalance -= 200
      self.clearSideScreen()
      self.setSideText('You have passed go, therefore have collected £200', self.textPosX, 100)
      self.updateBoard()
      self.displayHouseHotel()
      time.sleep(3)      
      self.lap += 1       
    
  def checkBankrupt(self):
    """ Checks whether the player has minus balance
    """
    if self.balance < 0: # if the player has a minus balance 
      while (len(self.properties) > 0) and (self.balance < 0): # checks to see if the player can get out of bankrupcy by raising funds
        self.clearSideScreen()
        self.setSideText('Player' +str(self.token)+ ', you are currently bankrupt, balance =' +str(self.balance)+ ', however you can still raise funds.', self.textPosX, 100)
        time.sleep(2)
        self.raiseFunds()
      if (len(self.properties) == 0) and (self.balance < 0): # if the player has no properties - therefore no way of raising funds, then they are declared bankrupt
        self.bankrupt = True
        
  def checkEnoughMoney(self, toPay):
    """ Checks to see if the player can pay the money

    Parameter
    ---------
    toPay : float
      is the amount the the player is requested to pay for

    Returns
    -------
    Boolean
      True if the player has enough money
    """
    if self.balance < toPay: # if the player doesn't have enough money to pay for the cost - toPay - then returns False
      self.clearSideScreen()
      self.setSideText(('Player ' +str(self.token)), self.textPosX, 100)
      self.setSideText('You do not currently have enough money to pay this.', self.textPosX, 120)
      time.sleep(2)
      return False 
    return True # if the player has enough money then true is returned

  def sellEverything(self):
    """ Used for selling all assets of a player, only in abridged version of game
    """
    tempProperties = self.properties
    for i, group in enumerate(self.groups, start = 0): 
      if len(self.groups[i]) == Property.noInGroups[i]: #if a player has all properties within a group
        for prop in group:
          if prop.currentRent > 0: 
            self.balance += (prop.currentRent * prop.hotelHouseCost)
          self.balance += prop.cost
          tempProperties.remove(prop)
    for prop in tempProperties:
      if prop.mortgaged == True:
        self.balance += prop.cost * 0.5
      else:
        self.balance += prop.cost


        
class Agent(Player):#inherits from Player
  """
  A class that represents all the virtual players

  Attributes
  ----------
  agentList : list
    A list of virtual players
  listRoad : list
    A list of stations
  listUtili : list
    A list of utilities
  funds : int
    Amount of money to be raised
  possibleImprovements : list
    List of the colout groups of properties

  Methods
  -------
  start()
    Starts the virtual players turn
  outOfJail()
    Allows player to choose an option to get out of jail
  improvPossible()
    Checks to see if a property can be improved
  addHousesHotel()
    adds Houses/hotel to the property
  raiseFunds(group)
    Allows the virtual player to raise funds
  findOptions()
    Recieves the properties/houses/groups that can be sold
  sellHouses(groupNo)
    Sells houses/hotel until the money is raised or the group don’t own any houses/hotel
  mortgageProperty()
    Allows properties/stations/utilities to be mortaged
  unmortgage()
    Allows properties/stations/utilities to be unmortaged
  checkEnoughMoney(toPay)
    checks if the virtual player can pay 'toPay'
  checkDouble()
    Check if the vitual player rolled a double
  """
  
  agentList = [] #is a list of virtual players
  listRoad = [5,15,25,35] #list of stations
  listUtili = [12,28]#list of utilities
  
  def __init__(self, token):
    """
    Parameters
    ----------
    token : string
      Represents the name of the vitual players token 
    """
    super().__init__(token)
    Agent.agentList.append(self)#creates a list that contains all the player agents
    self.funds = 0 #variable used to know the amount of money to be raised
    self.possibleImprovements = []# list of the colour groups of properties
 
  def start(self):
    """
    Starts the virtual players turn
    """
    self.checkBankrupt() # check if the player is bankrupt
    if self.bankrupt == False:
      if self.roundsInJail == 2: # when a player has choosen to stay in jail for 2 rounds and has completed those 2 rounds
        self.clearSideScreen()
        self.setSideText(('Player ' +str(self.token)), self.textPosX, 100)
        self.setSideText('You have waited 2 rounds and are now released from jail.', self.textPosX, 120)
        time.sleep(3)
        self.inJail = False #agent out of jail
        self.roundsInJail == 0 # update rounds
      if self.inJail == True: # gives the players options to get out of jail
        self.outOfJail() #Other options such as paying or using get out of jail card
      else:
        self.clearSideScreen()
        self.setSideText('Player ' +Game.currentPlayer.token, self.textPosX, 100)
        if self.improvPossible():#check if properties can be improved
          self.improveProperty()#improve the properties
        self.unmortgage()#pay off mortgage
        GUIFunctions.gameDisplay.blit(pygame.transform.scale(self.dicePic, (60,60)), (770, 340)) #displays the dice
        pygame.display.update()
        time.sleep(1)
        pygame.draw.rect(Game.gameDisplay, self.blackColour,[770, 340, 60, 60])
        pygame.display.update()
        time.sleep(0.2)
        self.move() # moves around the board  

  def outOfJail(self):
    """ This method will check the state of the agent, then will decide between 3 options
    If the agent's lap is less than 4 and its balance is higher than £500. The agent will pay to get out of jail
    If the agent has a get out of jail card it will use this
    Otherwise, it will wait two rounds
    """
    if self.roundsInJail == 1:
      self.roundsInJail += 1 # increments the number of rounds
    else:
      if(self.lap < 4) and self.balance >= 500:#checks the cash and turns of the agent 
        self.balance -= 50# pay to get out of jail
        Game.freeParking += 50#payment on freeparking
        self.clearSideScreen()
        self.setSideText(('Player ' +Game.currentPlayer.token), self.textPosX, 100)
        self.setSideText('You have payed £50 and are released from jail!', self.textPosX, 120)
        time.sleep(3)
        self.inJail = False# update agent state to out of jail
      elif ( self.getOutOfJailCardPot > 0 or self.getOutOfJailCardOpportunity > 0): # if they have a get out of jail free card then this is an option
        if self.getOutOfJailCardOpportunity > 0:
            self.getOutOfJailCardOpportunity -= 1 # update agent's cards
            OpportunityKnocks.getOutOfJailOwned = False
        else:
            self.getOutOfJailCardPot -= 1 # it updates agent's cards
            PotLuck.getOutOfJailOwnedPot = False
        self.clearSideScreen()
        self.setSideText(('Player ' +Game.currentPlayer.token), self.textPosX, 100)
        self.setSideText('You have used get out of jail free card', self.textPosX, 120)
        self.setSideText('And are released from jail!', self.textPosX, 140)
        time.sleep(3)
        self.inJail = False # updates agent state to out of jail
      else:
        self.clearSideScreen()
        self.setSideText(('Player ' +Game.currentPlayer.token), self.textPosX, 100)
        self.setSideText('You have to wait 2 rounds to be released from jail', self.textPosX, 120)
        time.sleep(3)
        self.roundsInJail += 1 #Updates rounds
                
  def improvPossible(self):
    """ Iterates over all the properties owned by the agent and
    implements the groups that can be improved into the list possibleImprovement.

    Returns
    -------
    canAdd : Boolean
      True if the improvement is possible
    """
    canAdd = False
    for i, group in enumerate (self.groups, start = 0):
      canAdd = True # used as true if the group is a possible option to improve
      if len(group) == Property.noInGroups[i]: # if the agent has all properties in that group
        for prop in group: # for each property object in the group
          if prop.mortgaged == True: # cannot add houses to mortgaged properties
            canAdd = False
        if canAdd == True:
          self.possibleImprovements.append(group)
      if len(self.possibleImprovements) > 0:# if the agent can improve any properties
        canAdd = True
    return canAdd

  def improveProperty(self):
    """ Improves properties that are owned by the player agent
    """
    improvSelect = []# Creates new list 
    for posGroup in self.possibleImprovements:# iterates over all the possible groups that can be improved
      if self.checkEnoughMoney(Property.hotelHouseCost[posGroup[0].group-1]):#checks that the agent has enough money to improve a property from the group
        improvSelect.append(posGroup)#implements the group to the list
    if len(improvSelect) > 0:
      self.addHousesHotel(random.choice(improvSelect))#randomly selects a group that can be improved 
         
      
  def addHousesHotel(self, group):
    """ Adds houses/hotel to the properties on group referenced by 'group'

    Parameter
    ---------
    group : list
       the  group that the player has chosen to improve
    """
    lowestNoOfHouses = 5 # lowestNoOfHouses will be set to the number of houses on the property with the lowest number of houses in that group
    for prop in group:
      if lowestNoOfHouses > prop.currentRent:#compares the rent of each property(the lowest rent indicates lowest number of houses)
        lowestNoOfHouses = prop.currentRent#stores the property with the lowest houses
    if lowestNoOfHouses != 5:# if there is still room to add houses/hotels 
      for prop2 in group:
        if prop2.currentRent == lowestNoOfHouses: # adds all properties with the lowest number of houses - e.g. prop1 = 2, prop2 = 2 and prop3 = 3 - avaliableProps = [prop1, prop2]
          if self.checkEnoughMoney(prop2.houseHotelPrice) == True: # checks to see if the agent has enough money to buy a house onto the property
            prop2.currentRent = prop2.currentRent + 1 #updates rent
            self.balance -= prop2.houseHotelPrice #updates agent's balance
            Game.bankBalance += prop2.houseHotelPrice # updates bank's balance
    
  def raiseFunds(self):
    """ Allows the agent to raise money - The agent will first mortgage all the properties in possProp,
    Now is the turn to sell properties if more money is needed, the agent raise the funds it will stop selling
    """
    for i in (self.properties):#iterates over all the agent's properties
      util = Game.board.index(i)# stores the location of the property on the board
      if (util in self.listUtili or util in self.listRoad) and (self.balance < self.funds):#checks if the property is an utility or station
        propertyToSell = util
        propertyToSell.updateSoldProp() # sells the utility or station and updates the agent's balance, properties and groups list.It also updates the banker's balance
    if len(self.properties) > 0 and (self.balance < self.funds) : # if the agent can raise any funds they need to own a property
        possProp, possHotel, possColour = self.findOptions()  # returns a list of possible properties to sell (possProp) and a list of possible properties with hotels on them (possHotel) and a list of colour groups properties (possColour)
        if len(possProp) > 0: # if there is no possible properties then this option is not avaliable
          self.mortgageProperty()#the agent will first mortgage the properties that don't complete a colour group or/and that don't have houses 
        if self.balance < self.funds:#checks if the agent nedds to raise more money
          Maintain = []
          allprop = []
          for player in Player.playerList: #iterates over all the players (This includes agents)
            if (player.token != self.token)and (len(possProp)>0) and (self.balance < self.funds):#checks if the agent needs to raise more funds, it owns properties and the current token is not the agent 
              for notsell in possProp:#iterates over the possProp list
                index = notsell.group #stores the position of the property 
                if(len(player.groups[index-1])+1 == Property.noInGroups[index-1]):#checks if the property is needed by another player to complete a colour group
                  Maintain.append(notsell)# stores the property in a list
        if (self.balance < self.funds):#checks if the agent needs to raise more money
          allprop.extend(possProp) #assign possProp list to a new list so the next iteration does not fail
          for sell in allprop:#iterates over allprop
            if sell not in Maintain and (self.balance < self.funds):# checks if it is not a property needed by another player to complete a colour group and if the agent still needs to raise funds
                propertyToSell = sell #stores the property
                propertyToSell.updateSoldProp() # sells and updates the property owner(no one)
                possProp.remove(propertyToSell)#remove it from possProp as the agent sold it
        if (self.balance < self.funds) and (len(Maintain) > 0):#checks if more cash is required and if the list Maintain is not empty
          for prop2 in Maintain:#iterates over Maintain
            if (self.balance < self.funds):#checks if more money is needed
              propertyToSell = prop2 #stores property
              propertyToSell.updateSoldProp() # sells and updates the property
              possProp.remove(propertyToSell)#remove the property from possProp
        if (self.balance < self.funds) and (len(possColour)>0):#checks if more money is required and if the agent owns more properties(colour group properties: the agent owns all the properties in a group)
          allprop.extend(possColour)#duplicate the list so the iteration is possible
          for prop3 in allprop:#iterates over allProp
            if self.balance < self.funds:#checks if the agent can pay funds
              propertyToSell = prop3 #stores the property
              propertyToSell.updateSoldProp() # sells and updates the property
              possColour.remove(propertyToSell)#remove the property from possColour as the agent sold it
        if (self.balance < self.funds) and (len(possHotel)>0):#Checks if the agent owns properties with houses/hotels and need for money
          while len(possHotel) > 0  and self.balance < self.funds:#Checks if the agent owns properties with houses/hotels and need for money
            self.sellHouses(possHotel[0])#sells the houses of the properties in the group
            possHotel.remove(possHotel[0])#removes them from the list as they don't own any houses
    if len(self.properties) > 0 and (self.balance < self.funds) :#checks if there are still properties available and the need for money
      self.raiseFunds()#recursive call until agent reaises funds or ends up bankrupt      

  def findOptions(self):
    """ Finds options of the agent player to sell

    Returns
    -------
    PossProp : list
      a list of property objects that the agent can sell to raise funds
    PossColour : a list
      a list of property objects that form a whole group, but does not own houses/hotel 
    PossHotel : a list
      a list of group indices that will point to groups that have at least one house on at least one of the group properties 
    """
    tempProperties = []
    tempProperties.extend(self.properties)# will become a list of properties not including any full group of player owned properties
    possibleProperties = [] # will be a list of properties that do not have any houses on it
    possibleHouseHotel = [] # will be a list of group numbers which have 1 or more houses on the group
    possibleGroupsNoH = [] # will be a list of properties that form a group
    for i, group in enumerate(self.groups, start = 0): # looks through self.groups - a list of lists of the properties sorted into their group
      if(len(self.groups[i]) == int(Property.noInGroups[i])): # if the player owns all properties of the current group
        totalHouses = 0
        for currentProp in group: # adds the total number of houses of each property in the group 
          totalHouses += currentProp.currentRent
          tempProperties.remove(currentProp) # removes the property from tempProperties
        if totalHouses > 0:
          possibleHouseHotel.append(i) # if this group has houses on at least one of their properties it is added to possibleHouseHotel
        else:
          possibleGroupsNoH.extend(group)# if the player has no houses on the current group then is added to possibleProperties
    possibleProperties.extend(tempProperties) # adds all the extra properties left over
    return possibleProperties, possibleHouseHotel, possibleGroupsNoH  
  
  def sellHouses(self, groupNo):
    """ Goes through the properties in the group with groupNo and checks for the highest number of houses,
    sells houses/hotel until the money is raised or the group don’t own any houses/hotel

    Parameters
    ----------
    groupNo : int
      Is the current group index of the group that the agent is selling houses from to raise funds
    """
    propert = None
    maxHouseNo = 0 # will become the highest number of houses on a property in the group with the id - groupNo
    for prop in self.group[groupNo]: # for each property in the current group
      if prop.currentRent > maxHouseNo: # if the property has a higher number of houses, maxHouseNo is updated 
        maxHouseNo == prop.currentRent# stores the rent of the property with the highest number of houses
        propert = prop# stores the property with the highest number of houses
    for prop2 in self.groups[groupNo]:
      if prop2.currentRent == maxHouseNo:#sells the houses of the properties with the highest number of houses
        if self.balance < self.funds:
          propToSell = prop2 # sells the house back, updates the property and the banks
          propToSell.currentRent -= 1# reduces the property's rent
          self.balance += propToSell.houseHotelPrice # updates agent's balance
          Game.bankBalance -= propToSell.houseHotelPrice  #updates bank's balance
    if propert.currentRent > 0 and self.balance < self.funds:#checks if there are houses available and if the agent needs to raise more funds
      self.sellHouses(groupNo)# recursive call to sell more houses
      
  def mortgageProperty(self):
    """ Allows the agent to mortgage a property
    """
    noHouseProp = [] # will become a list of property objects that can be put on morgage 
    allProps = []
    allProps.extend(self.properties) # becomes a duplication of a list of all property objects that the player has
    for group in self.groups: # checks to see if the group has houses on it - if it does, it needs to sell the houses before being mortgaged
      total = 0
      for prop in group:
        total += prop.currentRent
        allProps.remove(prop) #removes all properties - leaves with utilities and stations
      if total == 0:
        noHouseProp.extend(group) # adds the properties of a group that doesn't have any houses/hotels on their property
    noHouseProp.extend(allProps) # adds all utilities and stations to the options to be mortgaged
    for prop in noHouseProp:
      if (prop.mortgaged == False) and self.balance < self.funds:
        p = prop # mortgages the property 
        self.balance += p.cost * 0.5#updates agent's balance
        Game.bankBalance -= p.cost * 0.5 # updates bank's balance
        p.mortgaged = True # updates the property state to mortgage

  def unmortgage(self):
    """ Allows the agent to unmortgage a property
    """
    mortgagedProps = [] # becomes a list of properties that have a mortgage to be paid
    for prop in self.properties: 
      if (prop.mortgaged == True) and (self.balance - (prop.cost*0.5)) > 100: # checks if the agent  has enough money to pay off the mortgage
        self.balance -= prop.cost * 0.5 #updates agent's balance
        Game.bankBalance += prop.cost * 0.5 #updates bank's balance
        prop.mortgaged = False # update the property's state to not mortgaged
       
  def checkEnoughMoney(self, toPay):
    """ Checks to see if the agent has enough money to pay

    Parameter
    ---------
    toPay : float
      is the amount the the agent is requested to pay for

    Returns
    -------
    Boolean
      True - if the agent has a balance larger than the value of ‘toPay’, False - if the agent has a balance less than the value of ‘toPay’
    """
    self.funds = toPay
    if self.balance < toPay: # if the player doesn't have enough money to pay for the cost - toPay - then returns False
      return False 
    return True # if the player has enough money then true is returned

  def checkDouble(self):
    """ Checks to see how many doubles the agent has got in a row
    """
    if self.dice.doublesCount == 1 or self.dice.doublesCount == 2: # retrieves the doublesCount from the players dice
      if(self.inJail == False):
        self.clearSideScreen()
        self.setSideText(('Player ' +Game.currentPlayer.token), self.textPosX, 100)
        self.setSideText('You rolled a double, therefore get another go', self.textPosX, 120)
        GUIFunctions.gameDisplay.blit(pygame.transform.scale(self.dicePic, (60,60)), (770, 340)) #displays the dice
        pygame.display.update()
        time.sleep(1)
        pygame.draw.rect(Game.gameDisplay, self.blackColour,[770, 340, 60, 60])
        pygame.display.update()
        time.sleep(0.2)
        self.move() # moves around the board
      else:
        self.clearSideScreen()
        self.setSideText(('Player ' +Game.currentPlayer.token), self.textPosX, 100)
        self.setSideText('Although you have rolled double, you are now in jail', self.textPosX, 120)
        time.sleep(3)
        self.dice.doublesCount = 0
    elif self.dice.doublesCount == 3:
      self.clearSideScreen()
      self.setSideText(('Player ' +Game.currentPlayer.token), self.textPosX, 100)
      self.setSideText('You have rolled three doubles, therefore go to jail', self.textPosX, 120)
      self.inJail = True # if they get 3 doubles then they go to jail
      self.position = 10 # updates the players position to jail
      self.updateBoard()
      self.displayHouseHotel()
      time.sleep(3)
    else:
      self.dice.doublesCount = 0 # if the current dice is not a double - the double check is set back to 0        
  
class Level():
  """
  A class that represents the level object of the game

  Attributes
  ----------
  listRoad : list
    Contain the index of the stations
  ftotal : int
    Stores the value of the agent's balance after rents are extracted
  mrent : int
    Stores the maximum rent from the position of the agent on the board to the square go

  Methods
  -------
  buyProperty(prop)
    It will check if the agent has enough money to buy the property and if the return value of decision method is true
  checkCash(prop, cost, player)
    
  Auction(prop, cost, player)
    When the player chooses easy or medium level, the auction is updated here when playing with an agent
  """

  listRoad = [5,15,25,35]#list with the postion of the stations
  
  def __init__(self):
    self.ftotal = 0#variable with the value of the agents balance after rents are extracted
    self.mrent = 0# variable that contains the rents

  def Buyproperty(self, prop):
    """ It will check if the agent has enough money to buy the property and if the return value of decision method is true

    Parameters
    ----------
    prop : Property object
      The property object to be bought, mortgage or auction

    Returns
    -------
    Boolean or char
      Represents if the player buys, mortgages or puts the property up for auction
    """
    currentplayer = Game.currentPlayer# variable that stores current agent
    index = Game.board.index(prop)# variable that sustains the property position
    if currentplayer.checkEnoughMoney(prop.cost) and self.decision(index, prop.cost):
      return "b"#buy property
    elif currentplayer.checkEnoughMoney(prop.cost * 0.5) and self.decision(index, prop.cost * 0.5):
      return "m"#mortgage property
    else:
      return False #for auction

  def checkCash(self, prop, cost, player):
    """

    Parameters
    ----------
    prop : int
      The index of the property to be bought, mortgage or auction
    cost : int
      The cost of the property to be bought, mortgage or auction
    player : Agent
      The agent that might buy or mortgage the property

    Returns
    -------
    Boolean
      It will return true if the agents balance is higher than the collected rents, otherwise it will return false
    """
    currentplayer = player
    houses = {}#variable that will have all the groups
    frent = 0
    maxrent = 0#Contains the maximum rent
    choice = False
    pos = prop
    for player in Player.playerList:#iterates over every player
      if (player != currentplayer) and (len(player.properties)>0):
        for j, group in enumerate(player.groups):
          if (len(group) == Property.noInGroups[j]) and (Game.board.index(group[-1]) > pos):
            maximum = 0#stores the highest rent of the group
            index = []#stores the position of the properties in the group
            for x in group:
              index.append(Game.board.index(x))
              if x.currentRent > maximum:
                maximum = x.currentRent
            houses[maximum]= index #dictionary that has the highest rent of the group as key and the position of the properties as items
      # sort the array from lowest rent to highest
      houses_sorted = sorted(houses, key=houses.get)
      for rent in houses_sorted:
        if rent > maxrent:
          maxrent = rent# stores the highest rent of the dictionary
        for position in houses.get(rent):# iterates over the items(properties) of the current key(rent)
          if pos + 6 == position:#checks if the position is six position away form the current agent
            pos = position# new position used for further comparison
            frent += rent # sums rent
          elif pos + 7 == position:#checks if the position is six position away form the current agent
            pos = position# new position used for further comparison
            frent += rent # sums rent
          elif pos + 8 == position:#checks if the position is six position away form the current agent
            pos = position# new position used for further comparison
            frent += rent # sums rent
      total =  currentplayer.balance - 50 - frent - cost
      self.ftotal = currentplayer.balance - frent #set the total cash after rent deduction
      self.mrent = maxrent#set the highest rent
      if total > 50 and total + 200 >= maxrent:#checks the balance of the player after deductions 
        choice = True
      return choice

  def Auction(self, prop, cost, player):
    """ Agent completes the auction

    Parameters
    ----------
    prop : int
      The index of the property to be bought, mortgage or auction
    cost : int
      The cost of the property to be bought, mortgage or auction
    player : Agent object
      The agent that might buy or mortgage the property

    Returns
    -------
    bid : int
      The agents bid
    """
    bid = 10#initial bid
    currentPlayer = player#set agent to this variable
    if Game.board.index(prop) in [12, 28]:#utilites are auctioned
      bid = 10
    elif Game.board.index(prop) in self.listRoad:# stations are auctioned
      bid = prop.cost *0.5#new bid 
    elif currentPlayer.balance > 200:#if agents balance is higher than 200 able to bid
      if currentPlayer.checkEnoughMoney(cost+prop.prices[2]):
        bid = random.randint(cost-prop.prices[0],cost+prop.prices[1])# bid randomly in adequate range
    return bid

class Easy(Level):#inherits from level
  """
  A class to represent easy levels of the game
  ...

  Methods
  -------
  decision(prop, cost)
    Is the decision the agent makes to buy or mortgage a property
  """

  def decision(self, prop, cost):
    """ Decision that the agent buys or mortgages a property

    Parameter
    ---------
    prop : int
      The index of the property to be bought, mortgage or auction
    cost : int
      The cost of the property to be bought, mortgage or auction

    Returns
    -------
    Boolean
      The decision to buy or mortgage a property

    """
    decisions = [True, False]# random decision to buy or mortgage
    return random.choice(decisions)


class Medium(Level):#inherits from level
  """
  A class to represent the medium levels of the game
  ...

  Methods
  -------
  decision(index, cost)
    Is the decision the agent makes to buy or mortgage a property
  """
  
  def decision(self, index, cost):
    """ Decision that the agent buys or mortgages a property

    Parameter
    ---------
    index : int
      The index of the property to be bought, mortgage or auction
    cost : int
      The cost of the property to be bought, mortgage or auction

    Returns
    -------
    Boolean
      The decision to buy or mortgage a property under certain conditions
    """
    currentPlayer = Game.currentPlayer#set agent to this variable
    if currentPlayer.balance > 600 and self.checkCash(index, cost, currentPlayer):#states if balance is higher than 600 and low probability of bankruptcy 
      return True
    elif currentPlayer.balance > 250 and self.checkCash(index, cost, currentPlayer):#states if balance is higher than 250 and low probability of bankruptcy 
      decisions = [True, False]
      return random.choice(decisions) #random decision to buy property
    else:
      return False

class Hard(Level):#inherits from level
  """
  A class to represent the hard levels of the game
  ...

  Attributes
  ----------
  listSky : list
    Contain the index of the properties in group 8
  List1 : list
    Contains the index of some properties 
  List2 : list
    Contains the index of some properties

  Methods
  -------
  decision(index, cost)
    Is the decision the agent makes to buy or mortgage a property
  number(prop, cost, player)
    Depending on the number of players the agent buys different properties
  Auction(prop, cost, player)
    When the player chooses a hard level, the auction is controlled by the agent player
  """
  listSky = [37,39] #list containing the position of  sky properties
  list1 =[6,8,9,16,18,19,26,27,29] #list containing the position of  some properties
  list2 =[16,18,19,21,23,24,31,32,34] #list containing the position of  some properties

  def decision(self, index, cost):
    """ Decision that the agent buys or mortgages a property

    Parameter
    ---------
    index : int
      The index of the property to be bought, mortgage or auction
    cost : int
      The cost of the property to be bought, mortgage or auction

    Returns
    -------
    Boolean
      The decision to buy or mortgage a property under certain conditions
    """
    currentPlayer = Game.currentPlayer# set the agent
    choice = False
    if self.number(index, cost, currentPlayer):# checks number of players to implement the right strategy
      choice = self.checkCash(index, cost, currentPlayer) # checks if there is low probability of bankruptcy 
    return choice

  def number(self, prop, cost, player):
    """ It will check the number of the players in the game and if the property is useful for the agent.

    Parameters
    ----------
    prop : int
      The index of the property to be bought, mortgage or auction
    cost : int
      The cost of the property to be bought, mortgage or auction
    player : Agent object
      The agent that might buy or mortgage the property

    Returns
    -------
    choice : Boolean
      True if the property is useful for the agent    
    """
    currentplayer = player # set the agent
    choice = False
    if currentplayer.lap <=4 and prop in self.listRoad:#only but stations at the beginning of the game
      choice = True
    elif len(Player.playerList) ==2:
      if prop in self.list1:# if there are two players buy properties in list1
        choice = True
    elif len(Player.playerList) ==3:
      if prop in self.list2[:6]:# if there are three players buy properties in list2 besides the three last
        choice = True
    elif len(Player.playerList) == 4:
      if prop in self.list2:# if there are four players buy properties in list2
        choice = True
    elif len(Player.playerList) >= 5:
      if prop in self.list2:# if there are five players or more buy properties in list2
        choice = True 
      elif currentplayer.lap > 6 and prop in self.listSky:# buy the sky properties later on the game
        choice = True
    if prop not in self.listRoad :#checks the property is not a station
      if prop not in [1,3, 12, 28]:#checks the property is not an utility or brown group
        propt = Game.board[prop]
        for i in Player.playerList:
          if len(i.groups[propt.group - 1])+1 == Property.noInGroups[propt.group - 1]:# checks if any player needs it for group completion 
            choice = True  
    return choice

  def Auction(self, prop, cost, player):
    """ Agent completes the auction

    Parameters
    ----------
    prop : int
      The index of the property to be bought, mortgage or auction
    cost : int
      The cost of the property to be bought, mortgage or auction
    player : Agent object
      The agent that might buy or mortgage the property

    Returns
    -------
    bid : int
      The agents bid
    """
    bid = 10 # initial bid
    if self.number(Game.board.index(prop), cost, player):#checks if startegy to bid higher is needed
      currentplayer = player#set agent
      self.checkCash(Game.board.index(prop), cost,player)# establish ftotal and highest rent
      total = self.ftotal
      if Game.board.index(prop) in self.listRoad:#checks if property is a station
        bid = cost # the bis will be the cost of the station
      elif Game.board.index(prop) not in [1,3,12,28]:# checks if property is brown or an utility
        decision = False
        for i in Player.playerList:#iterates over all the players(include agent)
          if len(i.groups[prop.group - 1])+1 == Property.noInGroups[prop.group - 1]:# checks if any player needs it for group completion 
            total -= cost # balance - the cost of the current property - the further rents
            if total > 50 and total + 200 >= self.mrent:#checks if total is higher than 50 and if after go it will be higher than the highest rent
              decision = True 
              bid = cost + 50 + prop.prices[1] # new bid
          elif (decision == False):# property will not complete any players' group but is a good decision to bid high for it
            bid = random.randint(cost * 0.2, cost) # new bid
    return bid
  
class Dice():
  """
  A class that represents the dice on the board
  ...

  Attributes
  ----------
  doublesCount : int
    This counts how many doubles a player gets in a row
  total : int
    Is the total of the 2 dice after roll()

  Methods
  -------
  roll()
    Allows the player to roll the dice
  setSideTest(sentence, posX, posY)
    Sets the display of the dice on the side window
  """

  def __init__(self):
    self.doublesCount = 0 # counts how many doubles a player gets in a row
    self.total = 0 # total on dies's last roll
  
  def roll(self):
    """ Uses the library random to create 2 random numbers between 1 and 6
    """
    dice1 = random.randint(1,6) # rolls 2 dice, assigns a random value
    dice2 = random.randint(1,6)
    if dice1 == dice2:
      self.doublesCount += 1 # if a double then appends to the count
    else: 
      self.doublesCount = 0
    self.setSideText(('You have rolled ' +str(dice1)+ '+' +str(dice2)+ '=' +str(dice1+dice2)), GUIFunctions.textPosX, 500) #prints the value just rolled
    self.total = dice1+dice2
    
  def setSideText(self, sentence, posX, posY):
    """ Displays the message on the side screen with given coordinates

    Parameters
    ----------
    sentence : str
      a sentence to be displayed on the side screen
    posX : int
      an integer that represents the X position on the grid
    posY : int
      an integer that represents the Y position on the grid
    """
    noOfPText = GUIFunctions.setTextFont(self, str(sentence), GUIFunctions.text) #gets the chosen font of the message
    noOfPText[1].center = (posX, posY) #centers the text around the x and y coordinate sent
    GUIFunctions.gameDisplay.blit(noOfPText[0], noOfPText[1])
    pygame.display.update()


class ToBuySquare():
  """
  A class to buy properties
  ...

  Attributes
  ----------
  name : str
    This is thename of the square
  owner : none
    This means that the property is owned by the bank
  cost : int
    This is the cost of the square
  mortgaged : boolean
    This determines whether if the square is mortgaged
  currentRent : int
    This is the number of houses on the property

  Methods
  -------
  triggerEvent(dice)
    Displays option menu if property can be bought. Checks if the players have to pay rent
  triggerEventAgent(dice)

  displayOptions()
    Shows options menu
  aution()
    Starts auction if property is not bought
  placeBids()
    Allows players to place bid
  buyProperty(bOrM)
    Allows player to buy property, both full price and mortgaged
  buy(p)
    Used as a defaultmethod for utilities and stations
  payOwner(x)
    Players pay rent to the square owner
  updateSoldProp()
    Updates the sold property accordingly to the action taken by player
  sell()
    Used as a default method for utilities and stations
  clearSideScreen()
    Clears side screen
  setSideText()
    Sets the text in right position
  addButton()
    Adds a button
  click()
  Alerts the user they have clicked on a button
  """

  
  def __init__(self, name, cost):

    """
    Parameters
    ---------
    name : str
      Name of the list
    cost : int
      Cost of the square
    """
    self.name = name # name of the square
    self.owner = None # None is when the property is the owned by the bank
    self.cost = cost # cost of the square
    self.mortgaged = False # true if the square is mortgaged
    self.currentRent = 0 #default number of houses on the property
    
  def triggerEvent(self, dice):
    """If a player lands on sqaure owned by the bank, option menu will be displayed. If player lands on property they own, a message informing that will be displayed.
        If players land on property another player owns, payOwner() method will be referenced and will be payed the right amount.

    Parameters
    ----------
    dice : int
      Number on the rolled dice
    """
    currentPlayer = Game.currentPlayer # gets the current player
    if currentPlayer.lap > 1: # players cannot buy properties until they have done a full lap of the board
      if (self.owner == None)and (currentPlayer not in Agent.agentList): #MS change # if the square is not owned by any players
        self.clearSideScreen()
        self.setSideText(('Player ' +str(currentPlayer.token)), GUIFunctions.textPosX, 100)
        self.setSideText('you have landed on a property owned by the bank', GUIFunctions.textPosX, 110)
        self.displayOptions()
      elif self.owner == currentPlayer: # when they own the current square
        self.clearSideScreen()
        self.setSideText(('Player ' +str(currentPlayer.token)), GUIFunctions.textPosX, 100)
        self.setSideText('You have landed on your own property', GUIFunctions.textPosX, 120)
        time.sleep(2)        
      elif(self.owner == None) and (currentPlayer in Agent.agentList):
        self.triggerEventAgent(dice)
      else:
        self.payOwner(dice) # when they land on a square owned by a different player - therefore have to pay rent

  def triggerEventAgent(self, dice):
    """triggerEvent methods for the Agent

    Parameters
    ----------
    dice : int
      Number on the rolled dice
    """
    currentPlayer = Game.currentPlayer
    if Game.level.Buyproperty(Game.board[currentPlayer.position])== "b":
      self.buyProperty("b")
    elif Game.level.Buyproperty(Game.board[currentPlayer.position])== "m":
      self.buyProperty("m")
    else:
      self.auction()

  def displayOptions(self):
    """
    Clears the sidebar and display options menu
    """
    
    self.clearSideScreen()
    self.setSideText(('Main Menu:'), GUIFunctions.textPosX, 130)
    self.setSideText(('1. Buy the property - £' + str(self.cost)), GUIFunctions.textPosX, 150) # can buy the property for full price 
    self.addButton('Buy', 760, 170)
    self.setSideText(('2. Buy morgaged property - £' + str(self.cost*0.5)), GUIFunctions.textPosX, 230) # can buy the property with a mortgage - therefore half original cost 
    self.addButton('Buy mortgaged', 760, 250)
    self.setSideText(('3. View square details'), GUIFunctions.textPosX, 310) # can view the information about the square 
    self.addButton('View', 760, 330)
    self.addButton('Move on', 760, 410)
    pygame.display.update()
    while True:
      GUIFunctions.toQuit(self)
      click1 = self.click(760, 170, 80, 40)
      click2 = self.click(760, 250, 80, 40)
      click3 = self.click(760, 330, 80, 40)
      click4 = self.click(760, 410, 80, 40)
      if click1 == True:
        time.sleep(0.2)
        self.buyProperty('b') # buys property with full price
        break
      if click2 == True:
        time.sleep(0.2)
        self.buyProperty('m') # buys property with a mortgage of half price
        break
      if click3 == True:
        time.sleep(0.2)
        self.viewProperty() # views the property info
        break
      if click4 == True:
        time.sleep(0.2)
        self.auction()
        break

  def auction(self):
    """
    This method is actovated if current player cannot pay the price of the property or if the player decides to move on
    Allows players to place bids, by referencing the placeBids() methods
    """
    self.clearSideScreen()
    self.setSideText(('AUCTION'), GUIFunctions.textPosX, 100)
    self.setSideText(('As player ' +Game.currentPlayer.token+ ' does not want to/cannot buy the square,'), GUIFunctions.textPosX, 120)
    self.setSideText(('it is now up for auction!!'), GUIFunctions.textPosX, 140)
    time.sleep(3)
    winningBid = self.placeBids(Player.playerList) # retrieves a the player and their bid, if there is not one then = []
    if winningBid == []: # if there are no bids
      self.clearSideScreen()
      self.setSideText('Square remains unsold', GUIFunctions.textPosX, 100)
      time.sleep(3)
    else: # updates the property and player with the winning bid
      player, bid = winningBid
      self.clearSideScreen()
      self.setSideText(('Player ' +player.token+ ' has won the bid, with a total of £' +str(bid)), GUIFunctions.textPosX, 100)
      time.sleep(3)
      player.balance -= bid # updates the balances
      Game.bankBalance += bid
      self.buy(player) # used for property squares to update the group
      self.owner = player # updates the owner to the winning player
      player.properties.append(self) # adds to the winning players properties
    
  def placeBids(self, playList):
    """
    Gives an option to each player to make a bid or not, displaying a message and two buttons names ‘yes’ and ‘no’
    Allows players to enter a value in a text box

    Parameters
    ----------
    playList : list
      List of player objects, it contains a list of players that makes bids

    Returns
    -------
    bidList : list
      Checks entered values and returns the highest value as the winning bid, if there are no bids, returns an empty list
  
    """
    bidList = [] # is a list of lists of the player and their bid
    while len(playList) > 1: # if there is more than 1 property making a bid
      bidList = []
      bid2 = 0
      for player in playList: 
        if (player in Agent.agentList) and (player != Game.currentPlayer) and (player.inJail == False) and (player.lap > 1):#Chechs if the player is an agent
          bid = Game.level.Auction(self,self.cost, player)#Retrieve the bid
          if player.checkEnoughMoney(bid) == True: # only places bid if the player has enough money
                bidList.append([player, bid]) # adds the player object and their bid to the bidList
                bid2 = bid
        elif (player != Game.currentPlayer) and (player.inJail == False) and (player.lap > 1): # if the player is eligable to make a bid
          self.clearSideScreen()
          self.setSideText(('Player ' + player.token + ', would you like to make a bid?'), GUIFunctions.textPosX, 100)
          self.addButton('Yes', 670, 120)
          self.addButton('No', 850, 120)
          pygame.display.update()
          while True:
            GUIFunctions.toQuit(self)
            clickY = self.click(670, 120, 80, 40)
            clickN = self.click(850, 120, 80, 40)
            if clickN == True:
              time.sleep(0.2)
              break
            if clickY == True:
              time.sleep(0.2)
              self.setSideText('What is your bid? (enter only the value)', GUIFunctions.textPosX, 180) 
              bid = GUIFunctions.createTextBox(self, 760, 200)
              if player.checkEnoughMoney(bid) == True: # only places bid if the player has enough money
                bidList.append([player, bid]) # adds the player object and their bid to the bidList
                break
              else:
                break
        elif (player.inJail == True):
          self.clearSideScreen()
          self.setSideText(('Player ' + player.token + ', you are now in Jail'), GUIFunctions.textPosX, 100)
          self.setSideText(('Therefore you can\'t make a bid'), GUIFunctions.textPosX, 120)
          time.sleep(3)
      playList = [] # will be a list of players who have to bid again
      if len(bidList) > 1: # if there is more than one bid
        highestBid = 0 # will become the highest bid
        for playerBid in bidList:
          if playerBid[1] > highestBid: # if the bid is larger than the current highestBid the highestBid is updated
            highestBid = playerBid[1]
        newList = [] # will become a list of players and their bids if their bids are equal to the highestBid
        for playerBid in bidList:
          if playerBid[1] == highestBid:
            playList.append(playerBid[0])
            newList.append(playerBid)
        bidList = newList # updates the current bidList
    if bidList == []: # if there are no bids, then an empty list is returned
      return []
    else:
      return bidList[0] # if there is one bid left then it is returned as the winning bid 

                               
  def buyProperty(self, bOrM): # bOrM is a string - 'b' if option 1 is choosen and 'm' if option 2 is choosen
    """
    Checks whether player chooses to buy property full price or mortgage and updates the game accordingly

    Parameters
    ----------
    bOrM  : string
      Is 'b' if player chooses to buy property full price (option 1) or 'm' when player chooses to buy property mortgaged (option 2)      
    """

    
    if bOrM == 'b':
      cost = self.cost # if the player chooses to buy the property for full cost
    else:
      cost = self.cost * 0.5 # when the player chooses to buy the property with a mortgage - therefore half the cost
    currentPlayer = Game.currentPlayer
    if currentPlayer.checkEnoughMoney(cost) == True: # if the player has enough money to buy the square for the cost - either full or half
      self.owner = currentPlayer 
      currentPlayer.balance -= cost # updates the balances
      Game.bankBalance += cost
      currentPlayer.properties.append(self) # adds the property to the players property list
      if bOrM == 'm':
        self.mortgaged = True # if they brought with a mortgage then mortgaged is set to true
      self.buy(currentPlayer) # is used for properties to be updated further
      self.clearSideScreen()
      self.setSideText(('Player ' +str(currentPlayer.token)), GUIFunctions.textPosX, 100)
      self.setSideText('Congratulations, you now own ' +str(self.name), GUIFunctions.textPosX, 120)
      self.setSideText('Current balance = £' +str(currentPlayer.balance), GUIFunctions.textPosX, 140)
      time.sleep(3)
    else: # if they currently don't have enough money it is put up for auction
      self.auction()

      
  def buy(self, p): # used as a default method for utilities and stations
    """
    This method is used as a default method for utilities and stations

    Parameters
    ----------
    p : int
    """
    return

  def payOwner(self,x): # x is the number on the dice
    """
    This method is triggered when players land on a property that is owned by players
    If player lands on their own property, a message informing this is displayed
    If owner is in jail, they are not able to collect rent
    If property is mortgaged, owner won't be able to collect rent
    If player is not able to pay rent, their whole balance is given to owner

    Parameters
    ----------
    x : int
      Number on the die
    """
    self.clearSideScreen()
    self.setSideText(('You have landed on the property belonging to ' +str(self.owner.token)), GUIFunctions.textPosX, 100)
    time.sleep(3)
    if self.owner.inJail == True: # if the player is in jail, no rent is accepted
      self.setSideText('Player is in jail,', GUIFunctions.textPosX, 120)
      self.setSideText('therefore cannot collect any rents from other players', GUIFunctions.textPosX, 140)
      time.sleep(2)
    elif self.mortgaged == True: # if the square currently has a mortgage, the rent is not collected
      self.setSideText('This property is currently mortgaged', GUIFunctions.textPosX, 120)
      self.setSideText('Therefore no rents are being collected', GUIFunctions.textPosX, 140)
      time.sleep(2)
    else: # if the player and square are eligable 
      rent = self.collectRent(x) # returns the rent of the current square
      player = Game.currentPlayer
      while (player.checkEnoughMoney(rent) == False) and (len(player.properties) > 0): # when the player doesnt have enough money to pay rent and has properties they can sell
        player.raiseFunds() # gives player a chance to get out of bankruptcy
      if player.balance < rent: # if player has sold all properties possible and still cannot pay
        self.owner.balance += player.balance # player gives all their balance over to the owner
        player.bankrupt == True
        self.setSideText(('Player ' +str(player.token)+ ', you are bankrupt, therefore can only pay player ' +str(self.owner.token)), GUIFunctions.textPosX, 160)
        self.setSideText(('£' +str(player.balance)), GUIFunctions.textPosX, 170)
        time.sleep(3) 
        player.balance -= rent
      else:
        self.owner.balance += rent # when the player can afford the rent
        player.balance -= rent
      
  def updateSoldProp(self):
    """
    This methodus is used to half the prices of mortgaged properties, updates the game if players decide to sell their property and gives it back to the bank and also unmortagegs the properties.
    Updates the bank balance of the player accordingly
    """
    player = Game.currentPlayer 
    if self.mortgaged == True: #checks to see if the square is mortgaged
      cost = self.cost * 0.5 # if it is then the cost is halfed
    else:
      cost = self.cost
    player.balance += cost # updates the balances
    Game.bankBalance -= cost
    player.properties.remove(self) #deletes the sold property from the players properties
    self.mortgaged = False # unmortgages the property
    self.owner = None # the property is owned by the bank again
    self.sell() # used to update property squares

  def sell(self): # used as a default method for utilities and stations
    """
    This is a default method for utilities and stations
    """
    return
      
  def clearSideScreen(self): #clears the side screen
    """
    Used to clear side screen by using display.update function in pygame library
    """
    pygame.draw.rect(GUIFunctions.gameDisplay, GUIFunctions.bgColour, GUIFunctions.sidePos)
    pygame.display.update() #updates the screen
    
  def setSideText(self, sentence, posX, posY):
    """
    Centres the text that will be displayed on sidebar in correct position and updates the screen

    Parameters
    ----------
    sentences : string
      The sentence that will be displayed
    posX : int
      Position of x-axis
    posY : int
      Position of y-axis
    """
    noOfPText = GUIFunctions.setTextFont(self, str(sentence), GUIFunctions.text) #gets the chosen font of the message
    noOfPText[1].center = (posX, posY) #centers the text around the x and y coordinate sent
    GUIFunctions.gameDisplay.blit(noOfPText[0], noOfPText[1])
    pygame.display.update()
    return

  def addButton(self, word, posX, posY):
    """
    This method is used to add  a button

    Parameters
    ----------
    posX : int
      Position of x-axis
    posY : int
      Position of y-axis
    """
    pygame.draw.rect(GUIFunctions.gameDisplay, GUIFunctions.buttonColour, [posX, posY, 80, 40])
    p = GUIFunctions.setTextFont(self, word, GUIFunctions.text)
    p[1].center = (int(posX+(80/2)),int(posY+(40/2)))
    GUIFunctions.gameDisplay.blit(p[0], p[1])

  def click(self, x, y, w, h): #takes the x and y position and the size
    """
    Alerts the user they have clicked on a button by creating a shadow effect on the button

    Parameters
    ----------
    x : int
      Position of x-axis
    y : int
      Position of y-axis
    w : int
      Width of shadow
    h : int
      Height of shadow
    """
    mouse = pygame.mouse.get_pos() #the position of the mouse
    click = pygame.mouse.get_pressed() #if the mouse is clicked
    if ((x+w>mouse[0]>x) and (y+h>mouse[1]>y)):
      #if it is hovering over that particular button
      if click[0] == 1: #if that button was clicked
        pygame.draw.rect(GUIFunctions.gameDisplay, GUIFunctions.blackColour, [x,y,w,h])
        #shows the user its been clicked
        pygame.display.update()
        return True #returns that its been clicked
      
    
class Property(ToBuySquare):
  """


  Parameters
  ----------
  hotelHouseCost : list
    List of costs of each group
  groupColour : list
    List of colours matching to the group
  noInGroups : list
    States the number of properties in each coloured group

  Methods
  -------
  viewProperty()
    Shows players information about the property
  collectRent(x)
    Makes sure players pay the correct amount of rent to the property owner
  buy(player)
    Adds the property to the list of the player
  sell()
    Removes the property from the list if the player
  """
  hotelHouseCost = [50, 50, 100, 100, 150, 150, 200, 200] # list of the costs of each group - group 1 and 2 costs £50 to add a house
  groupColour = ['Brown', 'Blue', 'Purple', 'Orange', 'Red', 'Yellow', 'Green', 'Navy'] # the colour matching the group - group1's colour is brown
  noInGroups = [2, 3, 3, 3, 3, 3, 3, 2] # states the number of properties in each coloured group
  
  def __init__(self, name, group, cost, prices):
    """
    Parameters
    ----------
    name : str
      Name of the property
    group : int
      Group number
    cost : int
      Cost of the property
    prices : list
      List of rent proces for the properties
    """
    super().__init__(name, cost) # inherits from ToBuySquare
    self.group = group # integer representing the group number (brown = 1, blue = 2) - STARTS AT 1
    self.prices = prices # a list of rent prices to pay when landed on it - 1 house, 2, 3, 4 and 5 the hotel e.g. Crapper Street (2, 10, 30, 90, 160, 250)
    self.houseHotelPrice = Property.hotelHouseCost[group - 1] # the cost of adding a house - group1 = HotelHouseCost[0] = £50
    self.currentRent = 0 # is the index for the prices - 0 = no houses, 1 = 1 house etc., 5 = 1 hotel
 
  def viewProperty(self): #prints to the player the information about the property
    """
    Prints a list of information about the current propety the player is on
    """
    self.clearSideScreen()
    self.setSideText(('Name = ' +str(self.name)), GUIFunctions.textPosX, 100)
    if self.owner == None: # owner is none, when it is owned by the bank
      self.setSideText('Owner = Bank', GUIFunctions.textPosX, 120)
    else:
      self.setSideText(('Owner = ' + str(self.owner.token)), GUIFunctions.textPosX, 120)
    self.setSideText(('Price to buy = ' +str(self.cost)), GUIFunctions.textPosX, 140)  
    for i in range(5):
      self.setSideText(('Price to rent with ' +str(i)+ ' houses = ' +str(self.prices[i])), GUIFunctions.textPosX, 160+20*i)
    self.setSideText(('Price to rent with a hotel = ' +str(self.prices[5])), GUIFunctions.textPosX, 260)  
    self.addButton('Back', 800, 550) #adds a button 'back' which allows the user to go back to the previous window
    pygame.display.update()
    while True:
      GUIFunctions.toQuit(self)
      clickb = self.click(800, 550, 80, 40)
      if clickb == True:
        time.sleep(0.2)
        self.displayOptions()
        break

  def collectRent(self, x):
    """
    Checks if the property has one or more houses or a hotel on it, and doubles the rent accordingly to the right amount
    If there are no houses or a hotel on the property, finds the normal rent price and updates the game

    Parameters
    ----------
    x : int
      Number on the rolled dice

    Returns
    -------
    Returns the rent it finds according to whether it is the normal price or doubled price
    """
    group = self.owner.groups[self.group-1] # group is the list of properties in the current properties group (self.group-1) that the owner of this property owns 
    total = 0 # is the total number of houses on the properties in group 
    for prop in group: # for each of the properties in the group
      if prop.currentRent > 0: # if the property has one or more houses on it, total is incremented
        total += 1
    if (Property.noInGroups[self.group - 1]) == (len(self.owner.groups[self.group-1])) and (total == 0): # if the player owns all properties in that group and they all have no houses on it
      rent = self.prices[self.currentRent] * 2 # the rent is double when the player owns all properties in the group and none of them posess houses
      self.setSideText('The rent is doubled', GUIFunctions.textPosX, 120)
      self.setSideText('Because the player owns all properties in the group', GUIFunctions.textPosX, 140)
    else:
      rent = self.prices[self.currentRent] # rent is cost found from self.prices with the self.currentRent as its index 
    self.setSideText(('Therefore you have to pay a rent of '  +str(rent)), GUIFunctions.textPosX, 160)
    self.setSideText(('Your balance is £'+str(self.owner.balance)), GUIFunctions.textPosX, 180)
    time.sleep(3)
    return rent # the found rent is returned 

  def buy(self, player):
    """
    This methods is used to add the object of property to the list of propety of the player that has bought
    """
    player.groups[self.group-1].append(self) # adds the object of the property to the list of properties of the player, grouped in lists per group


  def sell(self):
    """
    This method is used to remove the object of the property from the list of groups of properties with the correct index
    """
    Game.currentPlayer.groups[self.group-1].remove(self) # removes the property from the list of groups of properties with the index self.group-1


    
class Station(ToBuySquare):
  """
  This method is used to display information and collect rent for the stations on the board

  Attributes:
  -----------
  rent : list
    It is the list of rents for the stations on the board
  stationList : list
    Empty list, becomes a list of station objects
  name : string
    Name of the station
  cost : string
    Cost to purchase the station

  viewProperty()
    Shows information about the station to the user
  collectRent(diceNo)
    Collects amount of rent to be collected
  """
  rent = [25, 50, 100, 200] # is a list of integers of the rent  - index 0 (25) when 1 station is owned by a player, index 1 (50) when 2 stations are owned by the same player etc.
  stationList = [] # a list of station objects
  
  def __init__(self, name, cost):
    """
    Parameters
    ----------
    name : str
      Name of the station
    cost : int
      Cost of the station
    """
    Station.stationList.append(self)  # adds the stations to the list 'stationList'
    super().__init__(name, cost) # inherits from ToBuySquare class

  def viewProperty(self): # prints to the player the information about the station
    """
    Displays information menu for the player on the sidebar
    """
    self.clearSideScreen()
    self.setSideText(('Name = ' +str(self.name)), GUIFunctions.textPosX, 100)
    if self.owner == None:
      self.setSideText('Owner = Bank', GUIFunctions.textPosX, 120)
    else:
      self.setSideText(('Owner = ' + str(self.owner.token)), GUIFunctions.textPosX, 120)
    self.setSideText(('Price to buy = ' +str(self.cost)), GUIFunctions.textPosX, 140) 
    for i in range(4):
      self.setSideText(('Price to rent with ' +str(i+1)+ ' stations is ' +str(Station.rent[i])), GUIFunctions.textPosX, 160+20*i)
    self.addButton('Back', 800, 550) #adds a button 'back' which allows the user to go back to the previous window
    pygame.display.update()
    while True:
      GUIFunctions.toQuit(self)
      clickb = self.click(800, 550, 80, 40)
      if clickb == True:
        time.sleep(0.2)
        self.displayOptions()
        break

  def collectRent(self, x):
    """
    Makes sure the correct amount of rent is payed by the player that lands on the owned station

    Parameters
    ----------
    x : int
      Number on the rolled dice

    Returns
    -------
    rent : int
      The rent of the station
    """
    count = 0 # is the number of stations the owner owns
    for station in Station.stationList:
      if station.owner == self.owner:
        count += 1
    rent = Station.rent[count-1] # rent is found using the number of station the owner owns as the index to 'rent'
    self.setSideText(('Therefore you have to pay a rent of '  +str(rent)), GUIFunctions.textPosX, 140)
    time.sleep(3)
    return rent # returns the rent of the station

  
class Utility(ToBuySquare):
  """
  This method is used to display information and collect rent for the utilities on the board

  Attributes
  ----------
  rent : list
    It is the list of rents for the utilities on the board
  name : string
    Name of the utility
  cost : string
    Cost to purchase the utility

  Methods
  -------
  viewProperty()
    Shows information about the utility to the user
  collectRent(diceNo)
    Collects amount of rent to be collected

  """
  rent = [4, 10]
  
  def __init__(self, name, cost):
    """
    Parameters
    ----------
    name : str
      Name of the utility
    cost : int
      Cost of the utility
    """
    super().__init__(name, cost) # inherits from toBuySquare

  def viewProperty(self): # prints to the player the information about the utility
    """
    Displays information menu for the player on the sidebar
    """        
    self.clearSideScreen()
    self.setSideText(('Name = ' +str(self.name)), GUIFunctions.textPosX, 100)
    if self.owner == None:
      self.setSideText('Owner = Bank', GUIFunctions.textPosX, 120)
    else:
      self.setSideText(('Owner = ' + str(self.owner.token)), GUIFunctions.textPosX, 120)
    self.setSideText(('Price to buy = ' +str(self.cost)), GUIFunctions.textPosX, 140)
    self.setSideText('With 1 utility rent is 4 times value shown on the dice', GUIFunctions.textPosX, 160)
    self.setSideText('With 2 utilities rent is 10 times value shown on the dice', GUIFunctions.textPosX, 180)
    self.addButton('Back', 800, 550) #adds a button 'back' which allows the user to go back to the previous window
    pygame.display.update()
    while True:
      GUIFunctions.toQuit(self)
      clickb = self.click(800, 550, 80, 40)
      if clickb == True:
        time.sleep(0.2)
        self.displayOptions()
        break

  def collectRent(self, diceNo):
    """
    Makes sure the correct amount of rent is payed by the player that lands on the owned utility

    Parameters
    ----------
    x : diceNo
      Number on the rolled dice

    Returns
    -------
    rent : int
      The rent of the station
    """
    if (Game.board[12].owner == Game.board[28].owner): # if the utility is owned by the same player
      noOfUtilities = 2
    else: # if only the current is owned 
      noOfUtilities = 1
    rent = Utility.rent[noOfUtilities-1] * diceNo # rent is calculated from the noOfUtilites owned
    self.setSideText(('Therefore you have to pay a rent of '  +str(rent)), GUIFunctions.textPosX, 140)
    time.sleep(3)
    return rent # the calculated rent is then returned

    
class Square():
  """
  Class to represent the squares

  Attributes
  ----------
  name : str
    Name of the square
  prop : list
    Refers to tax, go to jail, free parking. False is default

  Methods
  -------
  triggerEvent(x)
    Completes the action when the player lands on the square
  clearSideScreen()
    Clears the side screen
  setSideText(sentence, posX, posY)
    isplays the message on the side screen
  updateBoard()
    Update the board with the new position of tokens
  displayHouseHotel()
    Displays the image of house or hotel after the player has improved their property
    It rotates the image of house or hotel corresponding to the position they should be displayed on the board
  """
  
  
  def __init__(self, name,  prop = False):
    """
    Parameters
    ----------
    name : str
      Name of the square
    prop : boolean
      Properties will equal false for go and just visiting as no further actions happen
    """
    self.name = name
    self.prop = prop # prop = false if default, if prop is not the default relates to [tax, go to jail, freeParking] 

  def triggerEvent(self, x): # x = number on the dice, not needed for Square objects
    """
    Follows the rules of the requirements for squares

    Parameteres
    -----------
    x : int
      The number on the dice
    """
    if self.prop != False: # id
      if self.prop[0] != False: # when they land on a tax square
        self.setSideText(('You are being charged £' +str(self.prop[0])), GUIFunctions.textPosX, 540)
        Game.currentPlayer.balance -= self.prop[0] # updates the balance
        Game.freeParking += self.prop[0]
        self.setSideText('Your balance is ' +str(Game.currentPlayer.balance), GUIFunctions.textPosX, 560)
        time.sleep(2)
      elif self.prop[1] != False: # when they land on 'Go to jail'
        self.clearSideScreen()
        self.setSideText(('You are being sent to Jail'), GUIFunctions.textPosX, 100)         
        Game.currentPlayer.inJail = True # updates the player to being in jail
        Game.currentPlayer.position = 10
        self.updateBoard()
        self.displayHouseHotel()
        time.sleep(2)
      elif self.prop[2] != False: # when they land on 'Free parking'
        self.clearSideScreen()
        self.setSideText(('Congratulations Player ' +Game.currentPlayer.token), GUIFunctions.textPosX, 100) 
        self.setSideText(('You have won the money under free parking: £' +str(Game.freeParking)), GUIFunctions.textPosX, 120)
        time.sleep(2)
        Game.currentPlayer.balance += Game.freeParking # updates the balance
        Game.freeParking = 0

  def clearSideScreen(self): #clears the side screen
    """ Clears the side screen by updating the game
    """
    pygame.draw.rect(GUIFunctions.gameDisplay, GUIFunctions.bgColour, GUIFunctions.sidePos)
    pygame.display.update() #updates the screen
    
  def setSideText(self, sentence, posX, posY):
    """ Displays the message on the side screen with given coordinates and font

    Parameters
    ----------
    sentence : str
      a sentence to be displayed on the side screen
    posX : int
      an integer that represents the X position on the grid
    posY : int
      an integer that represents the Y position on the grid
    """
    noOfPText = GUIFunctions.setTextFont(self, str(sentence), GUIFunctions.text) #gets the chosen font of the message
    noOfPText[1].center = (posX, posY) #centers the text around the x and y coordinate sent
    GUIFunctions.gameDisplay.blit(noOfPText[0], noOfPText[1])
    pygame.display.update()

  def updateBoard(self):#clears the board then updates it
    """ Update the board with the new position of tokens.
    If two or more tokens are on the same square, changes their position so that they can all be seen on the square
    """
    GUIFunctions.gameDisplay.blit(pygame.transform.scale(GUIFunctions.boardGUI, (GUIFunctions.boardWidth, GUIFunctions.boardHeight)), (0,0)) #displays the board
    for i,player in enumerate(Player.playerList): #for every player
      tokenPic = GUIFunctions.tokenDict[player.token] #changes the postion of the token, therefore all tokens can be seen if they are all on the same square
      x = GUIFunctions.boardPosT[player.position][0] + GUIFunctions.positions[i][0]
      y = GUIFunctions.boardPosT[player.position][1] + GUIFunctions.positions[i][1]
      GUIFunctions.gameDisplay.blit(pygame.transform.scale(tokenPic, (30,30)), [x, y]) #update the board with the token's new position
    pygame.display.update()
    
  def displayHouseHotel(self): #displays houses/hotels after being bought by the user
    """
    Displays the image of house or hotel after the player has improved their property
    """
    for prop in GUIFunctions.propWHouses:
      index = GUIFunctions.boardSquares.index(prop.name) #takes the position on the board where the house is supposed to be displayed
      if index <11 : #takes into the account positions from 0 to 10
        if prop.currentRent == 5: #checks if the house or the hotel should be displayed
          x = GUIFunctions.boardPosH[index][0] #x-axis position of the house
          y = GUIFunctions.boardPosH[index][1] #y-axis position of the house
          self.updateBoard()
          GUIFunctions.gameDisplay.blit(pygame.transform.scale(GUIFunctions.hotelPic, (20,20)), [x, y]) #displays the hotel
          pygame.display.update() 
        else:
          for i in range(prop.currentRent):
            x = GUIFunctions.boardPosH[index][0] + 10*i
            y = GUIFunctions.boardPosH[index][1] 
            GUIFunctions.gameDisplay.blit(pygame.transform.scale(GUIFunctions.housePic, (20,20)), [x, y]) #displays the house
            pygame.display.update() 
      elif index in range(11, 20): #takes into the account positions from 11 to 20
        if prop.currentRent == 5:
          x = GUIFunctions.boardPosH[index][0]
          y = GUIFunctions.boardPosH[index][1]
          self.updateBoard()
          hotel = pygame.transform.rotate(GUIFunctions.hotelPic, 270)#rotates the picture of the house by 270 degrees counter-clockwise
          GUIFunctions.gameDisplay.blit(pygame.transform.scale(hotel, (20,20)), [x, y]) #displays the hotel
          pygame.display.update() 
        else:
          for i in range(prop.currentRent):
            x = GUIFunctions.boardPosH[index][0] 
            y = GUIFunctions.boardPosH[index][1] + 10*i
            house = pygame.transform.rotate(GUIFunctions.housePic, 270)#rotates the picture of the house by 270 degrees counter-clockwise
            GUIFunctions.gameDisplay.blit(pygame.transform.scale(house, (20,20)), [x, y]) #displays the house
            pygame.display.update() 
      elif index in range(21, 30): #takes into the account positions from 21 to 30
        if prop.currentRent == 5:
          x = GUIFunctions.boardPosH[index][0]
          y = GUIFunctions.boardPosH[index][1]
          self.updateBoard()
          hotel = pygame.transform.rotate(GUIFunctions.hotelPic, 180)#rotates the picture of the house by 180 degrees counter-clockwise
          GUIFunctions.gameDisplay.blit(pygame.transform.scale(hotel, (20,20)), [x, y]) #displays the hotel
          pygame.display.update() 
        else:
          for i in range(prop.currentRent):
            x = GUIFunctions.boardPosH[index][0] + 10*i
            y = GUIFunctions.boardPosH[index][1]
            house = pygame.transform.rotate(GUIFunctions.housePic, 180)#rotates the picture of the house by 180 degrees counter-clockwise
            GUIFunctions.gameDisplay.blit(pygame.transform.scale(house, (20,20)), [x, y]) #displays the house
            pygame.display.update() 
      else: #takes into the account positions from 31 to 39
        if prop.currentRent == 5: 
          x = GUIFunctions.boardPosH[index][0]
          y = GUIFunctions.boardPosH[index][1]
          self.updateBoard()
          hotel = pygame.transform.rotate(GUIFunctions.hotelPic, 90) #rotates the picture of the house by 90 degrees counter-clockwise
          GUIFunctions.gameDisplay.blit(pygame.transform.scale(hotel, (20,20)), [x, y]) #displays the hotel
          pygame.display.update() 
        else:
          for i in range(prop.currentRent):
            x = GUIFunctions.boardPosH[index][0]  
            y = GUIFunctions.boardPosH[index][1] + 10*i
            house = pygame.transform.rotate(GUIFunctions.housePic, 90)#rotates the picture of the house by 90 degrees counter-clockwise
            GUIFunctions.gameDisplay.blit(pygame.transform.scale(house, (20,20)), [x, y]) #displays the house
            pygame.display.update()  
         
        

      
class OpportunityKnocks():
  """
  A class that represents the opportuinity knock cards
  ...

  Attributes
  ----------
  cards : list
    Each item in the list represents the card chosen
  cardNumber : int
    Originally set to 0, is the number of current card
  name : string
    Name of the square
  getOutOfJailOwned : Boolean
    Represents if the get out of jail free card is owned
  
  Methods
  -------
  triggerEvent(x)
    Completes the action when the player lands on the opportunity knocks square
  clearSideScreen()
    Clears the side screen by using the display.update() function in pygame library
  setSideText()
    Gets the chosen font and centres the text that will be displayed on the side
  updateBoard()
    Clears the board and updates it
  displayHouseHotel()
    displays the houses/hotels

  """
  
  cards = ['Bank pays you divided of £50',#0
            'You have won a lip sync battle. Collect £100',#1
            'Advance to Turing Heights',#2
            'Advance to Han Xin Gardens. If you pass GO, collect £200',#3
            'Fined £15 for speeding',#4
            'Pay university fees of £150',#5
            'Take a trip to Hove station. If you pass GO collect £200',#6
            'Loan matures, collect £150',#7
            'You are assessed for repairs, £40/house, £115/hotel',#8 
            'Advance to GO',#9
            'You are assessed for repairs, £25/house, £100/hotel',#10
            'Go back 3 spaces',#11
            'Advance to Skywalker Drive. If you pass GO collect £200',#12
            'Go to jail. Do not pass GO, do not collect £200',#13
            'Drunk in charge of a skateboard. Fine £20',#14
            'Get out of jail free'] #15
  cardNumber = 0 # the number of the card that is next - goes through the pile of 15 cards, setting value to 0 once all cards have been used
  
  def __init__(self, name):
    """
    Parameters
    ----------
    name : string
      The name of the landed on square
    """
    GUIFunctions.__init__(self)
    self.name = name # the name of the square - 'Opportunity Knocks'
    self.getOutOfJailOwned = False # checks if get out of jail free is owned by anyone

  def triggerEvent(self, x):
    """ Follows the rules of the opportunity knocks card and triggers the event on the card

    Parameters
    ----------
    x : int
      the number on the dice, not needed for this class
    """
    cN = OpportunityKnocks.cardNumber
    player = Game.currentPlayer
    self.clearSideScreen()
    self.setSideText(('Player '+str(player.token)), GUIFunctions.textPosX, 100)
    self.setSideText('Your card', GUIFunctions.textPosX, 130) 
    self.setSideText(str(OpportunityKnocks.cards[cN]), GUIFunctions.textPosX, 150) # states the card at the top of the pack
    if (cN == 0):
      player.balance += 50 #adds £50 to the players bank
      Game.bankBalance -= 50 # minus £50 from the bank
      time.sleep(3)
    elif (cN == 1):
      player.balance += 100 #adds £100 to the players bank
      Game.bankBalance -= 100
      time.sleep(3)      
    elif (cN == 2):
      time.sleep(3) 
      player.position = 39 #moves player to Turing Heights 
      self.setSideText('You are on Turing Heights', GUIFunctions.textPosX, 170) 
      self.updateBoard()
      self.displayHouseHotel()
      time.sleep(3)
      Game.board[player.position].triggerEvent(player.dice.total)
    elif (cN == 3):
      if(player.position > 24): # checks if the player would pass go
        player.balance += 200
        player.lap += 1
        Game.bankBalance -= 200
      player.position = 24 #moves player to Han Xi Gardens
      self.setSideText('You are on Han Xi Gardens', GUIFunctions.textPosX, 170) 
      self.updateBoard()
      self.displayHouseHotel()
      time.sleep(3)
      Game.board[player.position].triggerEvent(player.dice.total)
    elif (cN == 4):
      if player.balance < 15:
        self.setSideText('You need to raise funds or you will become bankrupt', GUIFunctions.textPosX, 170) 
        player.raiseFunds()
      player.balance -= 15 # removes £15 from the players bank
      Game.freeParking += 15 # adds the money to free parking
      time.sleep(3)
    elif (cN == 5):
      if player.balance < 150:
        self.setSideText('You need to raise funds or you will become bankrupt', GUIFunctions.textPosX, 170) 
        player.raiseFunds()
      player.balance -= 150 #removes £150 from the players bank
      Game.freeParking += 150
      time.sleep(3)
    elif (cN == 6):
      if(player.position > 15): # checks if the player passes go
        player.balance += 200
        Game.bankBalance -= 200
        player.lap += 1
      player.position = 15
      self.setSideText(('You are on ' + str(Game.board[player.position].name)), GUIFunctions.textPosX, 170) 
      self.updateBoard()
      self.displayHouseHotel()
      time.sleep(3)
      Game.board[player.position].triggerEvent(player.dice.total)
    elif (cN == 7):
      player.balance += 150 #adds £150 to the players bank
      Game.bankBalance -= 150
      time.sleep(3)
    elif (cN == 8): # fines the players for each of there properties
      noHotels = 0
      noHouses = 0
      for prop in player.properties:
        if prop.currentRent == 5: # for each hotel
          noHotels += 1
        else:
          noHouses += prop.currentRent
      total = (40 * noHouses) + (115 * noHotels)
      self.setSideText(('For ' +str(noHouses)+ ' houses and ' +str(noHotels)+ ' hotels'), GUIFunctions.textPosX, 170)
      self.setSideText(('You owe £' +str(total)+ ' in repairs'), GUIFunctions.textPosX, 190)
      time.sleep(3)
      if player.balance < total:
        self.setSideText('You need to raise funds or you will become bankrupt', GUIFunctions.textPosX,210) 
        time.sleep(2)
        player.raiseFunds()
      player.balance -= total
      Game.bankBalance += total
    elif (cN == 9):     
      player.position = 40 #moves player to go -> 40 therefore will 
      player.pastGoCheck()
      self.updateBoard()
      self.displayHouseHotel()
      self.setSideText('You are on now on Go', GUIFunctions.textPosX, 170)
      time.sleep(3)
    elif (cN == 10): # fines the players for each of there properties
      noHotels = 0
      noHouses = 0
      for prop in player.properties:
        if prop.currentRent == 5: # for each hotel
          noHotels += 1
        else:
          noHouses += prop.currentRent
      total = (25 * noHouses) + (100 * noHotels)
      self.setSideText(('For ' +str(noHouses)+ ' houses and ' +str(noHotels)+ ' hotels'), GUIFunctions.textPosX, 170)
      self.setSideText(('You owe £' +str(total)+ ' in repairs'), GUIFunctions.textPosX, 190)
      time.sleep(3)
      if player.balance < total:
        self.setSideText('You need to raise funds or you will become bankrupt', GUIFunctions.textPosX, 210) 
        time.sleep(3)
        player.raiseFunds()
      player.balance -= total
      Game.bankBalance += total
    elif (cN == 11):
      player.position -= 3 #moves player 3 places backwards
      if self.position < 0:
        self.position += 40
        self.lap -= 1
      self.setSideText(('You are on ' + str(Game.board[player.position].name)), GUIFunctions.textPosX, 170) 
      self.updateBoard()
      self.displayHouseHotel()
      time.sleep(3)
      Game.board[player.position].triggerEvent(player.dice.total)
    elif (cN == 12):
      if(player.position > 11): # checks if player passes go
        player.balance += 200
        Game.bankBalance -= 200
        player.lap += 1 
      player.position = 11
      self.setSideText(('You are on ' + str(Game.board[player.position].name)), GUIFunctions.textPosX, 170) 
      self.updateBoard()
      self.displayHouseHotel()
      time.sleep(3)
      Game.board[player.position].triggerEvent(player.dice.total)
    elif (cN == 13):
      player.position = 10 #moves player in the jail
      player.inJail = True 
      self.updateBoard()
      self.displayHouseHotel()
      self.setSideText('You are now in Jail', GUIFunctions.textPosX, 170)
      time.sleep(3)
    elif (cN == 14):
      if player.balance < 20:
        self.setSideText('You need to raise funds or you will become bankrupt', GUIFunctions.textPosX, 170) 
        time.sleep(3)
        player.raiseFunds()
      player.balance -= 20 #removes £20 from the players bank
      Game.freeParking += 20
    elif (cN == 15):
      if(self.getOutOfJailOwned == False):
        player.getOutOfJailCardOpportunity += 1 #adds a card to be used to be released
        self.getOutOfJailOwned = True
      else:
        OpportunityKnocks.cardNumber = 0
        OpportunityKnocks.triggerEvent() 
    OpportunityKnocks.cardNumber += 1 # reset the card deck
    if OpportunityKnocks.cardNumber > 15:
      OpportunityKnocks.cardNumber = 0
  
  def clearSideScreen(self): #clears the side screen
    """ clears the side screen
    """
    pygame.draw.rect(GUIFunctions.gameDisplay, GUIFunctions.bgColour, GUIFunctions.sidePos)
    pygame.display.update() #updates the screen
    
  def setSideText(self, sentence, posX, posY):
    """ Displays the message on the side screen with given coordinates and font

    Parameters
    ----------
    sentence : str
      a sentence to be displayed on the side screen
    posX : int
      an integer that represents the X position on the grid
    posY : int
      an integer that represents the Y position on the grid
    """
    noOfPText = GUIFunctions.setTextFont(self, str(sentence), GUIFunctions.text) #gets the chosen font of the message
    noOfPText[1].center = (posX, posY) #centers the text around the x and y coordinate sent
    GUIFunctions.gameDisplay.blit(noOfPText[0], noOfPText[1])
    pygame.display.update()
    
  def updateBoard(self):#clears the board then updates it
    """ Update the board with the new position of tokens.
    If two or more tokens are on the same square, changes their position so that they can all be seen on the square
    """
    GUIFunctions.gameDisplay.blit(pygame.transform.scale(GUIFunctions.boardGUI, (GUIFunctions.boardWidth, GUIFunctions.boardHeight)), (0,0)) #displays the board
    for i,player in enumerate(Player.playerList): #for every player
      tokenPic = GUIFunctions.tokenDict[player.token] #changes the postion of the token, therefore all tokens can be seen if they are all on the same square
      x = GUIFunctions.boardPosT[player.position][0] + GUIFunctions.positions[i][0]
      y = GUIFunctions.boardPosT[player.position][1] + GUIFunctions.positions[i][1]
      GUIFunctions.gameDisplay.blit(pygame.transform.scale(tokenPic, (30,30)), [x, y]) #update the board with the token's new position
    pygame.display.update()
    
  def displayHouseHotel(self): #displays houses/hotels after being bought by the user
    """ Displays the image of house or hotel after the player has improved their property
    It rotates the image of house or hotel corresponding to the position they should be displayed on the board
    """
    for prop in GUIFunctions.propWHouses:
      index = GUIFunctions.boardSquares.index(prop.name) #takes the position on the board where the house is supposed to be displayed
      if index <11 : #takes into the account positions from 0 to 10
        if prop.currentRent == 5: #checks if the house or the hotel should be displayed
          x = GUIFunctions.boardPosH[index][0] #x-axis position of the house
          y = GUIFunctions.boardPosH[index][1] #y-axis position of the house
          self.updateBoard()
          GUIFunctions.gameDisplay.blit(pygame.transform.scale(GUIFunctions.hotelPic, (20,20)), [x, y]) #displays the hotel
          pygame.display.update() 
        else:
          for i in range(prop.currentRent):
            x = GUIFunctions.boardPosH[index][0] + 10*i
            y = GUIFunctions.boardPosH[index][1] 
            GUIFunctions.gameDisplay.blit(pygame.transform.scale(GUIFunctions.housePic, (20,20)), [x, y]) #displays the house
            pygame.display.update() 
      elif index in range(11, 20): #takes into the account positions from 11 to 20
        if prop.currentRent == 5:
          x = GUIFunctions.boardPosH[index][0]
          y = GUIFunctions.boardPosH[index][1]
          self.updateBoard()
          hotel = pygame.transform.rotate(GUIFunctions.hotelPic, 270)#rotates the picture of the house by 270 degrees counter-clockwise
          GUIFunctions.gameDisplay.blit(pygame.transform.scale(hotel, (20,20)), [x, y]) #displays the hotel
          pygame.display.update() 
        else:
          for i in range(prop.currentRent):
            x = GUIFunctions.boardPosH[index][0] 
            y = GUIFunctions.boardPosH[index][1] + 10*i
            house = pygame.transform.rotate(GUIFunctions.housePic, 270)#rotates the picture of the house by 270 degrees counter-clockwise
            GUIFunctions.gameDisplay.blit(pygame.transform.scale(house, (20,20)), [x, y]) #displays the house
            pygame.display.update() 
      elif index in range(21, 30): #takes into the account positions from 21 to 30
        if prop.currentRent == 5:
          x = GUIFunctions.boardPosH[index][0]
          y = GUIFunctions.boardPosH[index][1]
          self.updateBoard()
          hotel = pygame.transform.rotate(GUIFunctions.hotelPic, 180)#rotates the picture of the house by 180 degrees counter-clockwise
          GUIFunctions.gameDisplay.blit(pygame.transform.scale(hotel, (20,20)), [x, y]) #displays the hotel
          pygame.display.update() 
        else:
          for i in range(prop.currentRent):
            x = GUIFunctions.boardPosH[index][0] + 10*i
            y = GUIFunctions.boardPosH[index][1]
            house = pygame.transform.rotate(GUIFunctions.housePic, 180)#rotates the picture of the house by 180 degrees counter-clockwise
            GUIFunctions.gameDisplay.blit(pygame.transform.scale(house, (20,20)), [x, y]) #displays the house
            pygame.display.update() 
      else: #takes into the account positions from 31 to 39
        if prop.currentRent == 5: 
          x = GUIFunctions.boardPosH[index][0]
          y = GUIFunctions.boardPosH[index][1]
          self.updateBoard()
          hotel = pygame.transform.rotate(GUIFunctions.hotelPic, 90) #rotates the picture of the house by 90 degrees counter-clockwise
          GUIFunctions.gameDisplay.blit(pygame.transform.scale(hotel, (20,20)), [x, y]) #displays the hotel
          pygame.display.update() 
        else:
          for i in range(prop.currentRent):
            x = GUIFunctions.boardPosH[index][0]  
            y = GUIFunctions.boardPosH[index][1] + 10*i
            house = pygame.transform.rotate(GUIFunctions.housePic, 90)#rotates the picture of the house by 90 degrees counter-clockwise
            GUIFunctions.gameDisplay.blit(pygame.transform.scale(house, (20,20)), [x, y]) #displays the house
            pygame.display.update()   
        
        
    
class PotLuck():
  """
  A class that represents the pot luck cards
  ...

  Attributes
  ----------
  cards : list
    Each item in the list represents the card chosen
  cardNumber : int
    Originally set to 0, is the number of current card
  name : string
    Name of the square
  getOutOfJailOwnedPot : Boolean
    Represents if the get out of jail free card is owned

  Methods
  -------
  triggerEvent(x)
    Completes the action when the player lands on the potluck square
  clearSideScreen()
    Clears the side screen by using the display.update() function in pygame library
  setSideText()
    Gets the chosen font and centres the text that will be displayed on the sidebar
  updateBoard()
    Update the board with the new position of tokens
  addButton(word, posX, posY)
    Adds button to the GUI
  click(x, y, w, h)
    Recieves the place the player has clicked on
  displayHouseHotel()
    displays the houses/hotels
    
  """
  cards = ['You inherit £100',#0
           'You have won 2nd prize in a beauty contest, collect £20',#1
           'Go back to Crapper Street',#2
           'Student loan refund. Collect £20',#3
           'Bank error in your favour. Collect £200',#4
           'Pay bill for text books of £100',#5
           'Mega late night taxi bill pay £50',#6
           'Advance to go',#7
           'From sale of Bitcoin you get £50',#8
           'Pay a £10 fine or take opportunity knocks',#9
           'Pay insurance fee of £50',#10
           'Savings bond matures, collect £100',#11
           'Go to jail. Do not pass GO, do not collect £200',#12
           'Received interest on shares of £25',#13
           'It\'s your birthday. Collect £10 from each player',#14
           'Get out of jail free']#15
  cardNumber = 0
  
  def __init__(self, name):
    """
    Parameters
    ----------
    name : string
      The name of the landed on square
    """
    self.name = name # the name of the square - 'Pot Luck'
    self.getOutOfJailOwnedPot = False # checks if get out of jail free is owned by anyone

  def triggerEvent(self, x):
    """ Follows the rules of the potluck card and triggers the event on the card

    Parameters
    ----------
    x : int
      the number on the dice, not needed for this class
    """
    cN = PotLuck.cardNumber
    player = Game.currentPlayer
    self.clearSideScreen()
    self.setSideText(('Player '+str(player.token)), GUIFunctions.textPosX, 100)
    self.setSideText('Your card', GUIFunctions.textPosX, 130) 
    self.setSideText(str(PotLuck.cards[cN]), GUIFunctions.textPosX, 150) # states the card at the top of the pack
    if (cN == 0 or cN == 11):
      player.balance += 100 #adds £100 to the players bank
      Game.bankBalance -= 100
      time.sleep(3)
    elif (cN == 1 or cN == 3):
      player.balance += 20 #adds £20 to the players bank
      Game.bankBalance -= 20
      time.sleep(3)
    elif (cN == 2):
      player.position = 1 #moves player to Crapper Street
      self.setSideText('You are now on Crapper Street', GUIFunctions.textPosX, 170)
      self.updateBoard()
      self.displayHouseHotel()
      time.sleep(3)
      Game.board[player.position].triggerEvent(player.dice.total)
    elif (cN == 4):
      player.balance += 200 #adds £200 to the players bank
      Game.bankBalance -= 200
      time.sleep(3)
    elif (cN == 5):
      if player.balance < 100:
        self.setSideText('You need to raise funds or you will become bankrupt', GUIFunctions.textPosX, 170) 
        player.raiseFunds()
      player.balance -= 100 #removes £100 from the players bank
      Game.freeParking += 100
      time.sleep(3)
    elif (cN == 6 or cN == 10):
      if player.balance < 50:
        self.setSideText('You need to raise funds or you will become bankrupt', GUIFunctions.textPosX, 170) 
        player.raiseFunds()
      player.balance -= 50 #removes £50 from the players bank
      Game.freeParking += 50
      time.sleep(3)
    elif (cN == 7):
      time.sleep(3)
      player.position = 40 #moves player to go -> 40 therefore will 
      player.pastGoCheck()
      self.updateBoard()
      self.displayHouseHotel()
      self.setSideText('You are on now on Go', GUIFunctions.textPosX, 170)
      time.sleep(3)
    elif (cN == 8):
      player.balance += 50 #adds £50 to the players bank
      Game.bankBalance -= 50
      time.sleep(3)
    elif (cN == 9):
      self.setSideText('Do you want to pay the £10 fine or take opportunity knocks?', GUIFunctions.textPosX, 170)
      self.addButton('Pay Fine', 670, 190)
      self.addButton('Take a card', 850, 190)
      pygame.display.update()
      while True:
        GUIFunctions.toQuit(self)
        click1 = self.click(670, 190, 80, 40)
        click2 = self.click(850, 190, 80, 40)
        if click2 == True:
          time.sleep(0.2)
          OpportunityKnocks.triggerEvent()
          break
        if click1 == True:
          time.sleep(0.2)
          if player.balance < 10:
            self.setSideText('You need to raise funds or you will become bankrupt', GUIFunctions.textPosX, 250)
            time.sleep(3)
            player.raiseFunds()
          player.balance -= 10 #removes £10 from the players bank
          Game.freeParking += 10
          break
    elif (cN == 12):
      player.position = 10 #moves player in the jail
      player.inJail = True
      self.updateBoard()
      self.displayHouseHotel()
      self.setSideText('You are now in Jail', GUIFunctions.textPosX, 170)
      time.sleep(3)
    elif (cN == 13):
      player.balance += 25 #adds £25 to the players bank
      Game.bankBalance -= 25
      time.sleep(3)
    elif (cN == 14):
      player.balance += (Game.noOfPlayers) * 10 #gets £10 from each player including themselves (taken away in the for loop)
      for i in Player.playerList:
        i.balance -= 10 #minus £10 from each persons bank
        time.sleep(3)
    elif (cN == 15):
      if(self.getOutOfJailOwnedPot == False):
        player.getOutOfJailCardPot += 1 #adds a card to be used to be released
        self.getOutOfJailOwnedPot = True
      else:
        PotLuck.cardNumber = 0
        PotLuck.triggerEvent()
    PotLuck.cardNumber += 1 # reset the card deck
    if PotLuck.cardNumber > 15:
      PotLuck.cardNumber = 0

  def clearSideScreen(self): #clears the side screen
    """ clears the side screen
    """
    pygame.draw.rect(GUIFunctions.gameDisplay, GUIFunctions.bgColour, GUIFunctions.sidePos)
    pygame.display.update() #updates the screen
    
  def setSideText(self, sentence, posX, posY):
    """ Displays the message on the side screen with given coordinates and font

    Parameters
    ----------
    sentence : str
      a sentence to be displayed on the side screen
    posX : int
      an integer that represents the X position on the grid
    posY : int
      an integer that represents the Y position on the grid
    """
    noOfPText = GUIFunctions.setTextFont(self, str(sentence), GUIFunctions.text) #gets the chosen font of the message
    noOfPText[1].center = (posX, posY) #centers the text around the x and y coordinate sent
    GUIFunctions.gameDisplay.blit(noOfPText[0], noOfPText[1])
    pygame.display.update()

  def addButton(self, word, posX, posY):
    """ Used to add a button for the GUI

    Parameters
    ----------
    word : str
      The word displayed on the button
    posX : int
      an integer that represents the X position on the grid
    posY : int
      an integer that represents the Y position on the grid
    """
    pygame.draw.rect(GUIFunctions.gameDisplay, GUIFunctions.buttonColour, [posX, posY, 80, 40])
    p = GUIFunctions.setTextFont(self, word, GUIFunctions.text)
    p[1].center = (int(posX+(80/2)),int(posY+(40/2)))
    GUIFunctions.gameDisplay.blit(p[0], p[1])

  def click(self, x, y, w, h): #takes the x and y position and the size
    """ Alerts the user that they have clicked on a button by creating a shadow effect on the corresponding button

    Parameters
    ----------
    x : int
      X position on the grid
    y : int
      y position on the grid
    w : int
      width of the area where click can be made
    h : int
      height of the area where click can be made

    Returns
    -------
    Boolean
      Indicates if the click has been made or not

    """
    mouse = pygame.mouse.get_pos() #the position of the mouse
    click = pygame.mouse.get_pressed() #if the mouse is clicked
    if ((x+w>mouse[0]>x) and (y+h>mouse[1]>y)):
      #if it is hovering over that particular button
      if click[0] == 1: #if that button was clicked
        pygame.draw.rect(GUIFunctions.gameDisplay, GUIFunctions.blackColour, [x,y,w,h])
        #shows the user its been clicked
        pygame.display.update()
        return True #returns that its been clicked
      
  def updateBoard(self):#clears the board then updates it
    """ Update the board with the new position of tokens.
    If two or more tokens are on the same square, changes their position so that they can all be seen on the square
    """
    GUIFunctions.gameDisplay.blit(pygame.transform.scale(GUIFunctions.boardGUI, (GUIFunctions.boardWidth, GUIFunctions.boardHeight)), (0,0)) #displays the board
    for i,player in enumerate(Player.playerList): #for every player
      tokenPic = GUIFunctions.tokenDict[player.token] #changes the postion of the token, therefore all tokens can be seen if they are all on the same square
      x = GUIFunctions.boardPosT[player.position][0] + GUIFunctions.positions[i][0]
      y = GUIFunctions.boardPosT[player.position][1] + GUIFunctions.positions[i][1]
      GUIFunctions.gameDisplay.blit(pygame.transform.scale(tokenPic, (30,30)), [x, y]) #update the board with the token's new position
    pygame.display.update()

  def displayHouseHotel(self): #displays houses/hotels after being bought by the user
    """ Displays the image of house or hotel after the player has improved their property
    It rotates the image of house or hotel corresponding to the position they should be displayed on the board
    """
    for prop in GUIFunctions.propWHouses:
      index = GUIFunctions.boardSquares.index(prop.name) #takes the position on the board where the house is supposed to be displayed
      if index <11 : #takes into the account positions from 0 to 10
        if prop.currentRent == 5: #checks if the house or the hotel should be displayed
          x = GUIFunctions.boardPosH[index][0] #x-axis position of the house
          y = GUIFunctions.boardPosH[index][1] #y-axis position of the house
          self.updateBoard()
          GUIFunctions.gameDisplay.blit(pygame.transform.scale(GUIFunctions.hotelPic, (20,20)), [x, y]) #displays the hotel
          pygame.display.update() 
        else:
          for i in range(prop.currentRent):
            x = GUIFunctions.boardPosH[index][0] + 10*i
            y = GUIFunctions.boardPosH[index][1] 
            GUIFunctions.gameDisplay.blit(pygame.transform.scale(GUIFunctions.housePic, (20,20)), [x, y]) #displays the house
            pygame.display.update() 
      elif index in range(11, 20): #takes into the account positions from 11 to 20
        if prop.currentRent == 5:
          x = GUIFunctions.boardPosH[index][0]
          y = GUIFunctions.boardPosH[index][1]
          self.updateBoard()
          hotel = pygame.transform.rotate(GUIFunctions.hotelPic, 270)#rotates the picture of the house by 270 degrees counter-clockwise
          GUIFunctions.gameDisplay.blit(pygame.transform.scale(hotel, (20,20)), [x, y]) #displays the hotel
          pygame.display.update() 
        else:
          for i in range(prop.currentRent):
            x = GUIFunctions.boardPosH[index][0] 
            y = GUIFunctions.boardPosH[index][1] + 10*i
            house = pygame.transform.rotate(GUIFunctions.housePic, 270)#rotates the picture of the house by 270 degrees counter-clockwise
            GUIFunctions.gameDisplay.blit(pygame.transform.scale(house, (20,20)), [x, y]) #displays the house
            pygame.display.update() 
      elif index in range(21, 30): #takes into the account positions from 21 to 30
        if prop.currentRent == 5:
          x = GUIFunctions.boardPosH[index][0]
          y = GUIFunctions.boardPosH[index][1]
          self.updateBoard()
          hotel = pygame.transform.rotate(GUIFunctions.hotelPic, 180)#rotates the picture of the house by 180 degrees counter-clockwise
          GUIFunctions.gameDisplay.blit(pygame.transform.scale(hotel, (20,20)), [x, y]) #displays the hotel
          pygame.display.update() 
        else:
          for i in range(prop.currentRent):
            x = GUIFunctions.boardPosH[index][0] + 10*i
            y = GUIFunctions.boardPosH[index][1]
            house = pygame.transform.rotate(GUIFunctions.housePic, 180)#rotates the picture of the house by 180 degrees counter-clockwise
            GUIFunctions.gameDisplay.blit(pygame.transform.scale(house, (20,20)), [x, y]) #displays the house
            pygame.display.update() 
      else: #takes into the account positions from 31 to 39
        if prop.currentRent == 5: 
          x = GUIFunctions.boardPosH[index][0]
          y = GUIFunctions.boardPosH[index][1]
          self.updateBoard()
          hotel = pygame.transform.rotate(GUIFunctions.hotelPic, 90) #rotates the picture of the house by 90 degrees counter-clockwise
          GUIFunctions.gameDisplay.blit(pygame.transform.scale(hotel, (20,20)), [x, y]) #displays the hotel
          pygame.display.update() 
        else:
          for i in range(prop.currentRent):
            x = GUIFunctions.boardPosH[index][0]  
            y = GUIFunctions.boardPosH[index][1] + 10*i
            house = pygame.transform.rotate(GUIFunctions.housePic, 90)#rotates the picture of the house by 90 degrees counter-clockwise
            GUIFunctions.gameDisplay.blit(pygame.transform.scale(house, (20,20)), [x, y]) #displays the house
            pygame.display.update()   
        
  
class Game(GUIFunctions):
  """
  A class to represent the game

  ...
  Attributes
  ----------
  currentPlayer : Player object
    Is the player object of the current player
  bankBalance : float
    The banks balance
  freeParking : float
    Is the value of money under Free Parking square
  Board : List
    A list of objects, containing all the information about the squares
  hours : int
    Represents the hours for time limit
  minutes : int
    Represents the minutes for time limit
  seconds : int
    Represents the seconds for time limit
  endTime : float
    Represents the end time limit
  noOfPlayers : int
    Represents the number of players, initialised to 0
  noOfAgents : int
    Represents the number of agents
  tokenPos : Array 1x6
    Of the postions of the token on the grid
  tokens : Array
    Array of strings of the tokens names
  abridgedGame : Boolean
    True if the game is abridged
  totalPlay : int
    Total number of players
  playerList : list
    List of Player objects
  playersCurPos : List
    List of each player’s current position
  level : int
    The level of the game, represented by the number

  Methods
  -------
  setUp()
    Sets up the game
  selectLevel(num)
    Chooses the level of difficulty 
  displayTokens()
    Displays the tokens on the window
  buttonStart()
    Displayes the start button to beguin the game
  setFullOrAbr()
    Allows the user to choose Full or Abridged game
  setPlayers()
    Sets the number of players in the game
  addPlayer(minPlay, maxPlay, posY)
    Allows user to click the number of players they want
  setLevel()
    Allows the user to choose the level of difficulty of the virtual player
  pickToken()
    Asks players to choose their token by displaying every token image vertically
  clickOnToken(tGUI)
    The action of clicking on the token
  setTimeLimit()
    Allows users to set the time limit for the abridged game
  agreed()
    Asks the users if they agrree on the time
  setHours()
    Sets the number of hours the game will go on
  setMinutes()
    Sets the number of minutes the game will go on
  play()
    Allows each player to take turns
  playAbridged()
    Sets up the abridged game
  countdown()
    Counts down the time of the abridged game
  checkWinner()
    Checks to see if there is a winner
  whoIsTheWinner()
    Finds the winner of the game
  checkPlayers()
    Checks to see if any of the players are bankrupt
  """
  currentPlayer = None # will be the player object of the current player
  bankBalance = 50000 # the banks balance
  freeParking = 0 # the value of money under the Free Parking square  
  board = [Square('Go'), Property('Crapper Street', 1, 60, (2, 10, 30, 90, 160, 250)), PotLuck('Pot Luck'), Property('Gangsters Paradise', 1, 60, (4, 20, 60, 180,320, 450)),
           Square('Income Tax', [200, False, False]), Station('Brighton Station', 200), Property('Weeping Angel', 2, 100, (6, 30, 90, 270, 400, 550)), OpportunityKnocks('Opportunity Knocks'),
           Property('Potts Avenue', 2, 100, (6, 30, 90, 270, 400, 550)), Property('Nardole Drive', 2, 120, (8, 40, 100, 300,450, 600)), Square('Jail/just Visiting'), 
           Property('Skywalker Drive', 3, 140, (10, 50, 150, 450, 625, 750)), Utility('Tesla Power Co', 150), Property('Wookie Hole', 3, 140, (10, 50, 150, 450, 625, 750)), 
           Property('Rey Lane', 3, 160, (12, 60, 180, 500, 700, 900)), Station('Hove Station',200), Property('Cooper Drive', 4, 180, (14, 70, 200, 550, 750, 950)), PotLuck('Pot Luck'),
           Property('Wolowitz Street', 4, 180, (14, 70, 200, 550, 750, 950)), Property('Penny Lane', 4, 200, (16, 80, 220, 600, 800, 1000)), Square('Free Parking', [False, False, True]), 
           Property('Yue Fei Square', 5, 220, (18, 90, 250, 700, 875, 1050)), OpportunityKnocks('Opportunity Knocks'), Property('Mulan Rouge',  5, 220, (18, 90, 250, 700, 875, 1050)),
           Property('Han Xin Gardens', 5, 240, (20, 100, 300, 750, 925, 110)), Station('Falmer Station',200), Property('Kirk Close', 6, 260, (22, 110, 330, 800, 975,1150)), 
           Property('Picard Avenue', 6, 260, (22, 110, 330, 800, 975, 1150)), Utility('Edison Water', 150), Property('Crusher Creek', 6, 280, (22, 120, 360, 850, 1025, 1200)), 
           Square('Go to Jail', [False, True, False]), Property('Sirat Mews', 7, 300, (26, 130, 390, 900, 1100, 1275)), Property('Ghengis Crescent', 7, 300, (26, 130, 390, 900, 1100, 1275)), 
           PotLuck('Pot Luck'), Property('Ibis Close', 7, 320, (28, 150, 450, 1000, 1200, 1400)), Station('Lewes Station',200), OpportunityKnocks('Opportunity Knocks'), 
           Property('Hawking Way', 8, 350, (35, 175, 500, 1100, 1300, 1500)), Square('Super Tax', [100, False, False]), Property('Turing Heights', 8, 400, (50, 200, 600, 1400, 1700, 2000))]
           # a list of objects, containing all the information about the squares
  hours = 0 
  minutes = 0 
  seconds = 0 
  endTime = 0
  noOfPlayers = 0 # initialised to 0
  
  def __init__(self):
    GUIFunctions.__init__(self)
    self.noOfAgents = 0
    self.tokenPos = [200, 260, 320, 380, 440, 500]
    GUIFunctions().createScreen()
    self.tokens = ['Boot', 'Smartphone', 'Goblet', 'Hatstand', 'Cat', 'Spoon']
    self.abridgedGame = self.setFullOrAbr()
    self.totalPlay = self.setPlayers()
    self.playerList = Player.playerList
    self.playersCurPos = [] #list of each players current position
    self.level = self.setLevel()
    self.setUp()
    if(self.abridgedGame == False):
      self.play() # starts the play of the game
    else:
      self.playAbridged() # starts the play of the abridged game

  def setUp(self):
    """ Sets up the game, choosing the level, tokens, time limit, and starts the game
    """
    if self.level != 0:
      self.selectLevel(self.level)
    self.pickToken() #each player chooses a token they want to play
    self.setTimeLimit() #players agree on the time if they play abridged version
    self.buttonStart() #displays button 'start' to begin the game
    self.displayTokens()

  def selectLevel(self, num):
    """ Chooses the level of difficulty of the virtual player

    Parameters
    ----------
    num : int
      Number of game difficulty
    """
    if num ==1:
      Game.level = Easy()
    elif num ==2:
      Game.level = Medium()
    else:
      Game.level = Hard()

  def displayTokens(self):
    """ Displays the tokens, For every player, displays their token at the beginning of the game on the Go square
    """
    for i, player in enumerate(self.playerList): #for every player
      tokenPic = GUIFunctions.tokenDict[player.token] #displays their token at the square 'Go'
      x = self.tokensAtGO[i][0]
      y = self.tokensAtGO[i][1]
      Game.gameDisplay.blit(pygame.transform.scale(tokenPic, (30,30)), [x, y]) #displays their token at the square 'Go'
    pygame.display.update()      
    
  def buttonStart(self):
    """ Clears the side screen and creates a square with start written,
    once clicked starts the whole game by using Game.gameDisplay() function

    Returns
    -------
    Boolean
      If the start button is clicked, true is returned
    """
    self.clearSideScreen()    
    pygame.draw.rect(Game.gameDisplay, (255, 0, 0), [730, 260, 120, 60])
    p = self.setTextFont('START', self.text)
    p[1].center = (int(730+(120/2)),int(260+(60/2)))
    Game.gameDisplay.blit(p[0], p[1])
    pygame.display.update()
    while True:
      self.toQuit()
      click = self.click(730, 260, 120, 60)
      if click == True:
        time.sleep(0.2)
        return True
        
  def setFullOrAbr(self):
    """ Displays a welcome message and a message asking player if they want to play a full or abridged game

    Returns
    -------
    Boolean
      True if abridged game clicked returns true
    """
    self.setSideText('Welcome to Property Tycoon', self.textPosX, 50)
    self.setSideText('Would you like to play the full game or abridged version?', self.textPosX, 100)
    self.addButton('FULL', 670, 150)
    self.addButton('Abridged', 850, 150)
    pygame.display.update()
    while True:
      self.toQuit()
      clickF = self.click(670, 150, 80, 40)
      clickA = self.click(850, 150, 80, 40)
      if clickF == True:
        time.sleep(0.2)
        return False
      if clickA == True:
        time.sleep(0.2)
        return True

  def setPlayers(self):
    """ Sets the number of players in the game - Clears the side screen and displays a message
    asking how many players and virtual players the user wants

    Returns
    -------
    noOfAgents + noOfPlayers : int
      Total number of players in the game both virtual and real
    """
    self.clearSideScreen()
    self.setSideText('How many players?', self.textPosX, 100)
    Game.noOfPlayers = int(self.addPlayer(1, 7, 150))
    if Game.noOfPlayers != 6:
      self.setSideText('How many virtual players?', self.textPosX, 200)
      maxAgents = 7 - Game.noOfPlayers
      if Game.noOfPlayers > 1: 
        self.noOfAgents = int(self.addPlayer(0, maxAgents, 250) )
      else:
        self.noOfAgents = int(self.addPlayer(1, maxAgents, 250))
    return self.noOfAgents + Game.noOfPlayers

  def addPlayer(self, minPlay, maxPlay, posY):
    """ Creates buttons with numbers from 1 to 6 to be chosen in order to determine how many players the game will include

    Parameters
    ----------
    minPlay : int
      button position
    maxPlay : int
      button position
    posY : int
      click position

    Returns
    -------
    m : int
      The number of players that have been chosen
    """
    noPlayers = []
    buttPos = self.playerButtonPos[:maxPlay]
    for k in range(minPlay, maxPlay): #creates the rectangle
      pygame.draw.rect(Game.gameDisplay, self.buttonColour ,[buttPos[k-minPlay],posY,20,20])
      p = self.setTextFont(str(k), self.text) 
      noPlayers.append(p)
      noPlayers[k-minPlay][1].center = (int(buttPos[k-minPlay]+(20/2)),int(posY+(20/2)))
      Game.gameDisplay.blit(noPlayers[k-minPlay][0], noPlayers[k-minPlay][1])
    pygame.display.update()
    while True:
      self.toQuit()
      for m in range(minPlay, maxPlay):
        x = buttPos[m-minPlay]
        click = self.click(x,posY,20,20)
        if click == True:
          time.sleep(0.2)
          return m

  def setLevel(self):
    """ Allows the user to choose the level of difficulty of the virtual player
    Creates three different buttons named ‘easy’, ‘medium’ and ‘hard’ respectively,
    which then determines the difficulty of the game corresponding to the button that has been clicked

    Returns
    -------
    int
      returns number value of the difficulty of the game
    """
    if self.noOfAgents > 0:
      self.clearSideScreen()
      self.setSideText('What Level of difficulty?', self.textPosX, 100)
      self.addButton('Easy', 670, 150)
      self.addButton('Medium', 760, 150)
      self.addButton('Hard', 850, 150)
      pygame.display.update()
      while True:
        self.toQuit()
        clickE = self.click(670, 150, 80, 40)
        clickM = self.click(760, 150, 80, 40)
        clickH = self.click(850, 150, 80, 40)
        if clickE == True:
          time.sleep(0.2)
          return 1
        if clickM == True:
          time.sleep(0.2)
          return 2
        if clickH == True:
          time.sleep(0.2)
          return 3
    else:
      return 0

  def pickToken(self):
    """ Asks players to choose their token by displaying every token image vertically.
    Assigns chosen token to the player and updates the game
    """
    chooseTokens = self.tokenGUI #list of the pictures of the tokens
    for player in range(Game.noOfPlayers): #iterates through the number of players
      self.clearSideScreen()
      self.setSideText('What token would you like Player '+str(player+1)+'?', self.textPosX, 100)
      choose = self.clickOnToken(chooseTokens) #displays the tokens and allows user to choose the one they want
      Player(self.tokens[choose]) #assigns a token to the player
      self.tokens.remove(self.tokens[choose])
      chooseTokens.remove(chooseTokens[choose])
    for aPlayer in range(self.noOfAgents): #iterates through the number of virtual players
      self.clearSideScreen()
      self.setSideText('What token would you like virtual Player '+str(aPlayer+1)+'?', self.textPosX, 100)
      for i, token in enumerate(self.tokens, start = 0):
        Game.gameDisplay.blit(pygame.transform.scale(chooseTokens[i][0], chooseTokens[i][1]), (750, self.tokenPos[i])) #displays the tokens that can be chosen
      pygame.display.update()
      choose = random.randint(0, len(self.tokens)-1)
      time.sleep(0.2)
      w, h = chooseTokens[choose][1]
      Agent(self.tokens[choose])
      pygame.draw.rect(Game.gameDisplay, self.blackColour,[750, self.tokenPos[choose], w, h]) #simulates the click by the virtual player
      pygame.display.update()
      time.sleep(0.2)
      self.tokens.remove(self.tokens[choose])
      chooseTokens.remove(chooseTokens[choose])
      

  def clickOnToken(self, tGUI):
    """ The action of clicking on the token,
    alerts the user that they have clicked on a button by creating a shadow effect on the corresponding button

    Parameters
    ----------
    tGUI : List of image
      Images of the tokens

    Returns
    -------
    i : token
      The token the player has clicked on
    """
    for i, token in enumerate(self.tokens, start = 0):
      Game.gameDisplay.blit(pygame.transform.scale(tGUI[i][0], tGUI[i][1]), (750, self.tokenPos[i])) #displays the tokens
    pygame.display.update()
    while True:
      self.toQuit()
      for i in range(len(self.tokens)):
        y = self.tokenPos[i]
        w, h = tGUI[i][1]
        click = self.click(750, y, w, h)
        if click == True:
          time.sleep(0.2)
          return i
        
  def setTimeLimit(self):
    """ Allows users to set the time limit for the abridged game
    """
    if(self.abridgedGame == True):
      agreededTime = False
      while(agreededTime == False):            
        self.clearSideScreen()
        self.setSideText('How much time would you like to play?', self.textPosX, 100)
        hours = self.setHours()
        valid = True
        while valid:
          minutes = self.setMinutes(hours)
          if minutes in range(0,60):
            valid = False
          else:
            self.setSideText('Please enter the number in range 0-59', self.textPosX, 220)  
        seconds = 0
        everyoneOk = True
        for i,player in enumerate(self.playerList): #iterates through all of the players and asks them if they agree on the amount of time
          if i < Game.noOfPlayers:
            self.clearSideScreen()
            self.setSideText(('Player '+str(player.token)+ ', do you agree on playing that much time?'), self.textPosX, 100)
            option = self.agreed()
            if not option: #allows the players to choose the time until all of the players agree on the same amount
              everyoneOk = False
        if(everyoneOk == True):
         agreededTime = True
      Game.hours = hours * 60 * 60
      Game.minutes = minutes * 60
      Game.seconds = seconds
      Game.endTime = time.time() + Game.hours + Game.minutes + Game.seconds #sets the time

  def agreed(self):
    """ Asks the users if they agrree on the time

    Returns
    -------
    Boolean
      True if the players agree, false if not
    """
    self.addButton('Yes', 670, 150)
    self.addButton('No', 850, 150)
    pygame.display.update()
    while True:
      self.toQuit()
      clickY = self.click(670, 150, 80, 40)
      clickN = self.click(850, 150, 80, 40)
      if clickN == True:
        time.sleep(0.2)
        return False  
      if clickY == True:
        time.sleep(0.2)
        return True 
    
  def setHours(self):
    """ Sets the number of hours the game will go on

    Returns
    -------
    hours : int
      Returns the hours for the abridged game
    """
    self.setSideText('Hours: ', self.textPosX, 120)
    hours = self.createTextBox(760, 130)
    time.sleep(0.2)
    return hours
   
  def setMinutes(self, hours):
    """ Sets the number of minutes the game will go on

    Returns
    -------
    minutes : int
      Returns the minutes that are entered for the abridged game
    """
    self.hours = hours
    self.setSideText('Minutes: ', self.textPosX, 180)
    minutes = self.createTextBox(760, 190)
    time.sleep(0.2)
    return minutes   

  def play(self):
    """Whilst there is not a winner, each player takes turns
    """
    while self.checkWinner() == False: # whilst there is not winner
      for player in self.playerList: # takes turn for each player to play
        self.checkPlayers() # checks to see if the players are bankrupt
        if player.bankrupt == False: # if the player is not bankrupt then the start is called to
          Game.currentPlayer = player
          player.start()

  def playAbridged(self):
    """ Whilst there is not a winner and there is time left,
    each player takes turns(if time is up we let everyone finish their turn in a round)
    """
    while( self.checkWinner() == False and self.countdown() == True): # whilst there is not winner and they have time left
      for player in self.playerList: # takes turn for each player to play
        self.checkPlayers() # checks to see if the players are bankrupt
        if player.bankrupt == False: # if the player is not bankrupt then the start is called to
          Game.currentPlayer = player
          player.start()
    if(self.countdown() == False):
      self.clearSideScreen()
      self.setSideText('Timer is up!!', self.textPosX, 160)
      time.sleep(3)
      self.whoIsTheWinner()

  def countdown(self): 
    """ Counts down the time
    Checks if actual time value is less than the assigned endTime value

    Returns
    -------
    Boolean
      true if there is time left, false if there is not
    """
    if time.time() < Game.endTime:
      return True
    else:
      return False
          
  def checkWinner(self):
    """ Checks to see if there is a winner - if there is only one player left in the game

    Returns
    -------
    Boolean
       True if there is a winner, false if there is not
    """
    self.checkPlayers() # checks to see if players are bankrupt
    total = len(self.playerList) # total = the number of players remaining
    for player in self.playerList: # checks for each player
      if player.bankrupt == True: # if the player is bankrupt then 
        total -= 1 # then the player is out of the game, therefore one less player
    if total == 1: # if there is only one player left, then there is a winner
      self.clearSideScreen()
      self.setSideText('Well done player '+ str(self.playerList[0].token)+ ' you are the only player left in the game, therefore you are the winner!!', self.textPosX, 100)
      time.sleep(2)
      return True # true is returned if there is a winner
    return False # false is returned when there is no winner

  def whoIsTheWinner(self):
    """ Finds the winner of the game by adding up each players assets and balance and comparing
    """
    highestBalance = 0
    for i, player in enumerate(self.playerList):
      player.sellEverything()
      if(player.balance > highestBalance):
        highestBalance = player.balance
        winners = []
        winners.append(self.playerList[i])
      elif(player.balance == highestBalance):
        winners.append(self.playerList[i])
        self.clearSideScreen()
    for i, player in enumerate(self.playerList):
      self.clearSideScreen()
      self.setSideText((player.token+ ' has got a balance of £' +str(player.balance)), self.textPosX, 120+20*i)
      time.sleep(3)
    if len(winners) == 1:
      self.setSideText(('Well done player ' +winners[0].token), self.textPosX, 250)
      self.setSideText('You were worth the most in this game', self.textPosX, 270)
      self.setSideText('Therefore you are the winner!!', self.textPosX, 290)
      time.sleep(3)
    else:
      self.setSideText('We have couple winners! Congratulations!', self.textPosX, 250)
      for i in enumerate(winners):
        self.setSideText((winners[i].token+ ' you are one of the winners!'), self.textPosX, 270+20*i)
      time.sleep(3)
      
  def checkPlayers(self):
    """ Checks through each player, checks if the player is bankrupt
    """
    for checkPlayer in self.playerList: # for each player remaining
      checkPlayer.checkBankrupt() # check to see if the player is bankrupt
      if checkPlayer.bankrupt == True: # if the player is bankrupt
        self.playerList.remove(checkPlayer) # the player is removed from the player list and removed from the game
        self.clearSideScreen()
        self.setSideText('Player ' +str(checkPlayer.token)+ ', you have run out of money, therefore you are out of game.', self.textPosX, 100)
        time.sleep(3)
    
        
if __name__ == "__main__":
  Game() # starts the game
