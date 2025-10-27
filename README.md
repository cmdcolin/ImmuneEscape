# Project Description
ImmuneEscape is a two-player, turn-based battle game in which each player will choose to play as either the immune system or the pathogen and battle! 

# How To Play
This game requires installing the 'pygame' application at https://github.com/pygame/pygame

Run the game and follow the on-screen prompts!

# Code Elements Explained
## Loading Player Type Dictionaries
Each player category (immune system or pathogen) is encoded in a dictionary of dictionaries that holds character specific attributes. The structure is as follows:
Dictionary: Immune System or Pathogen
  Keys: 'Character' Dicitonaries (i.e. virus, bacteria, parasite for the pathogen dictionary)
    Keys: Attributes of the Character (Actions, Damage, Health, Image)
      Lists: Of possible actions, damage amounts, starting health, and image paths.

## Text and Image Import
In this section, we specify all the text used and render the text objects for display on the screen.
We do the same for all images, specifying the image path and assigning them to variables that can be rendered on the appropriate screen.

## Creating Clickable Icons
We created a class of clickable icons that are used during the character selection process.

## Drawing Screens
We created functions that will 'draw' the desired screens that we use at different points in the game, and then set those states as arbitrary values so that they can be defined and called upon during the game loop.

## Game Loop
We created a game loop which, depending on which characters player 1 and player 2 chose, inserts them into a battle. Each character has their own actions that are used to deal different levels of damage. The actions are chosen by specifying key choices on the keyboard. a, s, and d are used for player 1 and up, down, and left for player 2. depending on which action is chosen, the associated damage will be taken from the opponents health bar or if the action is healing, the associated heal will be added to the own players health. This loop also containes instructions to display text depending on which action was chosen and how much damage it dealt. Movements for attacks is back and forward again and for a heal its up and down. Once the loop which specified what happens during the battle the turn based loop allows the players to go back and fourth, one player at a time, until one players health falls below 0 points. In this event, the screen changes to the associated winner of the game. 
### Start Screen

### Gameplay screen
It's an overview of the gameplay--character selection screen, and the keys that the game uses as input for the battle. 

### Character Selection Screen
The character selection screen contains clickable icons that will assign player one and player two to either the pathogen or immune system, which they will select themselves. Once the icon is selected, text displaying their choice appears for two seconds before the screen changes to the corresponding selection screen. The icon they click on will choose which screen they will be directed to next by changing the variable 'current_state,' which specifies the screen. 

### Pathogen Selection Screen
The pathogen selection screen will allow the player playing as the pathogen to select their 'character' from three clickable icons: virus, bacteria, and parasite. The icon they click on will then assign their player number (1 or 2) with the corresponding dictionary key for their character. 
The player number is determined by the order, with the first player to select on the character screen being 'player one.' After player one chooses their character, the screen will progress automatically to the selection screen of the type player one did not choose. 

### Immune System Selection Screen
The immune system selection screen will allow the player playing as the immune system to select their 'character' from two clickable icons: innate or adaptive. This screen works the same as the pathogen selection screen.

### Fight Screen
Once in the fight screen, player 1 selects between their attack or defense options if available to them using the keyboard keys a,s or d. Once player 1's turn concludes, then player 2 can select between their options utilizing the up, down, and left arrows. This will continue until a player is defeated. 

### End Screen
This last screen recognized the individuals who put this together. It also has a restart button that takes you back to the start screen of the game. 
