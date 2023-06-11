# Rock, Paper, Scissors
In this project, you will create a rock, paper, scissors game using Python. The game will allow the user to choose either rock, paper, or scissors, and then the computer will randomly choose its move. The winner is determined based on the standard rock, paper, scissors rules:
* Rock smashes scissors.
* Paper covers rock.
* Scissors cut paper.

1. Create a flowchart of the desired behavior of the program. Here’s a flowchart that describes how to play games repeatedly until the user decides to stop.<br>
![flowchart](https://github.com/aramb-dev/rock-paper-scissors/blob/main/Flowchart.jpg?raw=true)

2. Create a new Python project on [Replit](https://replit.com/~).
3. Create a function ``computer_move()`` that generates and prints a random move for the computer. You can do this by using the ``random.choice()`` function to generate a random item from the list ``[‘rock’, ‘paper’, ‘scissors’]``.
4. Ask the user to input their move using the ``input()`` function, then call the ``computer_move()`` function. Make sure to validate the users input with a conditional to ensure that they choose either rock, paper, or scissors.
5. Use conditional statements to determine the winner of the game. Remember that rock beats scissors, paper beats rock, and scissors beat paper. Display the winner on the screen.
6. (Optional) Ask the user if they want to play again. If they do, loop back to step 3. If they don't, end the game.

**Example Output:**<br><br>
![output](https://github.com/aramb-dev/rock-paper-scissors/blob/main/output.jpg?raw=true)

**Helpful hints:**
* Use the ``lower()`` function to convert the user's input to lowercase, making it easier to validate their input.
* Use a loop to ask the user to input their move until they choose a valid move.
* Use a loop to allow the user to play multiple rounds of the game.
