![hangman](assets/images/HANGMAN.jpg)
[The live link can be found here](https://hangman32.herokuapp.com/)

Hangman is a classic word-guessing game where one player thinks of a word and the other player tries to guess the word by suggesting letters. I recreated this game in Python, using basic programming concepts like loops, conditional statements, and functions.

![terminal](assets/images/pic1.png)

## How to play:

- The program picks a random word for the words.py file and then represent each letter of the word with an underscore (_).

- The user starts guessing letters of the word. For each correct guess, the program reveals the letter in the correct position in the word.

- For each incorrect guess, the program prints a graphical part of a "hangman" figure. The figure typically consists of a gallows and a stick figure.

- The game continues until the user guesses the entire word, or the hangman figure is completed.

## Flowchart

I created the following flowchart during the planning process as a basic guideline to follow when coding my project.

![flowchart](assets/images/flow.png)



## Features

### Existing Features


**Allowing user to pick a username, showing attempts remaining in blue, previous guesses in red and providing an output to the user in yellow font**

![](assets/images/pic2.png)

**Invalid input message as it only accepts letters**

![](assets/images/ivalidinput.png)

**Providing one HINT per game**

![](assets/images/hint.png)

**Retyping HINT after it has been used and getting back a message stating the hint has been used**

![](assets/images/hintused.png)
 
 **Keeps track of previous guesses**
 
![](assets/images/previousguesses.png)

**Incorrect word will not be accepted**

![](assets/images/incorrecrtword.png)

**Game breaks if user runs out of lives, correct word is printed out and full hangman image is shown**

![](assets/images/youlose.png)

** Give user the option to play again. yes option restarts, no option prints a message to the user**

![](assets/images/yes.png)

![](assets/images/no.png)



### Future Features

**Different difficulty levels**
I would like to add a function that allows the user to pick between easy, medium or hard.

**Scoreboard**
I would like to add a feature that allows users to view high scores.


## Technology Used

**Languages** - Python.

**Libraries**

[random](https://www.thewordfinder.com/random-word-generator/?msclkid=d948c7d79c351dcc5c07a434482ab5e2) - to select random words.

[colorama](https://pypi.org/project/colorama/) - to change the output font colour.

[freemonogrammaker](https://make.freemonogrammaker.com/bubble-letters-generator/) - to make the hangman bubble writing for this readme.

[Github](https://github.com/) - To save and store the project files for the game.

[Git](https://git-scm.com/) - Used to code and backup all of my code.

[Heroku](https://gitpod.io/workspaces) - Used to deploy the website.

### Bugs 

**Fixed Bugs**

Bug: When guessing the wrong word, it was showing up inncorect input.

Fix: Changed the if statment to if charachters entered was greater than one the terminal would know the user was trying to guess the word.

Bug: When testing hangman graphics, the last part of the leg was not showing up.

Fix: Replaced \ with double \\ as I belive the terminal was picking it up as a special character.

Bug: When printing the stages of the hangman to the terminal the print statments were being displayed above the image which made the user scroll up.

Fix: moved the position of the print statements within the hangman function.

Bug: IF 2 of the same charachters were in the word if wouldnt pick this up.

Fix: I had to move the updating the board list inside the if char in rletters as I had it outside of this function.

Bug: Error messages stating lines were too long.

Fix:I Split these lines up into seperate lines.

**Currently One noticable bug remaining**

bug: The user can guess one more time even after it says all guesses have been used.


## Testing

I have manually tested the project by doing the following:
1.Tested python code through code institutes CI Python Linter ([https://pep8ci.herokuapp.com/]) and fixed any errors.

**Showing errors**

![](assets/images/issues.png)

**No errors**

![](assets/images/noerrors.png)

2.Manually tested user inputs by purposefully inputing incorrect data to confirm error messages were capturing wrong inputs.

![](assets/images/ivalidinput.png)

3.I Tested it on both the local terminal and on the deployed site on Heroku.

4.I sent it to several friends to test out and send feedback. 

![](assets/images/Sfeedback.png)

5.Lighthouse testing

![](assets/images/lighthouse.png)


*I took into account the expectations of a user and what I wanted the project to do:*

1.An introduction to the game and to create a username

2.Clear information how what to do within the terminal

3.Fun to Play and appealing to the user

*Results*

As a user I was able to:

1.Be introduced to the Game & Enter a unique username

2.The information provided to the user was clear

3.Different font colours were provided to make it more appealing and clear to understand, I believe it was fun to play.


 
### Deployment
The project was deployed using Code Institutes mock terminal for Heroku.

I followed the below steps using the Code Institute tutorial:

- Add any external liberies useds to requirements.txt.

- Create a new app in Heroku.

- Add project name & Changed Region to relevant country.

- Select "New" and "Create new app".

- In "Settings" select "BuildPack" and select Python and Node.js. (Python must be at the top of the list).

- Within "Settings", click "Reveal Config Vars" and input Check config var add PORT & 8000 as I did not have any confidential files this was all that was needed.

- Click on "Deploy" and select your deploy method and repository.

- Click "Connect" on selected repository.

- Either choose "Enable Automatic Deploys" or "Deploy Branch" in the manual deploy section.

- Heroku will now deploy the site.

 **How to clone**
If you would like to download this repository and store it locally you can do so by cloning it

1.Click the GitHub repository.

2.Click on the drop down arrow on the Code button located on the top right.

3.Select and copy the link that appears.

4.Open Gitpod & select the location where you would like the clone to be saved.

5.In the terminal type 'git clone' and paste the link.

6.Press enter to create your local clone.

 ## Credits
 
**Code Used**

- [CODEFATHER](https://codefather.tech/blog/hangman-game-python/) I Used this website as a guideline for creating my game.

- [How to Code a Game of Hangman](https://www.youtube.com/watch?v=cJJTnI22IF8) I Used this youtube video as a guideline for creating my game.

- [Python cheat sheet](https://www.pythoncheatsheet.org/cheatsheet/basics) I used python cheat sheet sheet when I was unsure about certain code.
- Code institute for providing me with a template.

 
 
## Acknowledgments

I would like to acknowledge the following people who helped me in completing this project:
- My Course Mentor Harry Dhillon for his support and guidance.
- My friends for their continued support in testing and providing feedback.

Thank you for viewing my project.

 
 
