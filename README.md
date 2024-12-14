# DominoAI

This is a Dominos AI which find the piece you could play which would have the highest probability of success through a Depth 1 Expectimax, which finds the probability of your opponent not being able to place a domino given all potential moves you are able to make, and selects the one that would maximize that likelihood. 

Standard Hardware is sufficient to run this code, and it utilizes no outside data sources. It is run via python3, and can be done so via the command: python3 dominos.py

Once you are in, command line prompts will guide you while inputting the state space. If you would like to have an artificial hand for testing purposes, type our “TEST” in the command line, and it will give you a hand with the following 7 dominoes: 
(6,5),(6,4),(6,3),(6,2),(6,1),(5,0),(4,0)

If you are playing dominoes in real life and would like to insert your own hand, hit enter and you can do so number by number, inserting the greater number on each individual domino first. 

From there, you will be able to indicate whether you are starting, or if your opponent is starting, and what the starting domino is. It will then take you through the game, turn by turn, through which you can insert your opponent’s moves and, if applicable, the dominoes you have picked from the pile, and it will return for you the move which maximizes your chances at winning. 

My motivation for this project came from playing dominos with my uncle growing up. It was a lot of fun and, while seemingly random, takes a little bit of strategy in order to deny your opponent the ability to make moves. As such, I wanted to create an algorithm which would allow me to maximize my chances of winning any future game of dominos I play and allow me to become a domino world champion. 

While I initially imagined this program being able to predict moves out until the end of the game, and finding the move which maximizes the likelihood of winning overall, due to the exceedingly large state space, considering every potential tile on the board, every potential tile in your hand, every potential tile in their hand, and every potential tile in the pile, it was not practical to calculate very far into the future for each possibility, nor would it be useful due to the fact that the next state space encompasses the state spaces which come after. Since each sequential state space is the same as the current state space, just with one or more pieces removed from the pile or added to the board, predicting the likelihood of your opponent being able to place a piece on the board given any given move on this turn also calculates that same likelihood on future turns. As such, the algorithm in this file is I believe cheaper and more effective than what my original vision was.  

I believe that this program is successful because it increases the likelihood of winning a game of dominos by suggesting moves that deny your opponent the ability to place dominos on the board and maximize your ability to play dominos, thereby allowing you to get rid of your dominos before your opponent does and win the game.
