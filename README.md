# Welcome to Turbulent Tic Tac Toe

This is a remake of my original [Extravagant Tic Tac Toe](https://github.com/shakey0/ExtravagantTicTacToe) - my first project, which I undertook just three weeks after starting to learn to code.

I plan to use many of the ideas from the original game, although a significant part of this project will be to develop a kind of AI computer player that analyses the board and calculates the best move to gain an advantage over the player (of course, with difficulty levels that essentially randomise whether the computer picks the best option or not).

I will begin by developing the backend, which will mostly use a class-based system to maintain the board and keep track of the various animals and natural disasters that move around the board (checkout [Extravagant Tic Tac Toe](https://github.com/shakey0/ExtravagantTicTacToe) and choose As Many As You Can or Cards mode to see the animals and natural disasters moving around the board - yes, it's absolutely crazy). Redis will also be used for caching the game data between requests.

After developing the backend of the main game, I will launch it as a multiplayer game, allowing up to four players. I will implement a logging system to collect data in a Postgres database so I can analyse various aspects of the game and make improvements. At the same time, I will also begin developing the AI component so users can play against the computer.

The final goal is to have a storyline that the individual user follows and progresses through. New patterns and animals/natural disasters will be introduced as the user advances through the storyline.