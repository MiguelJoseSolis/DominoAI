

# Maximizing Agent - Selects a domino Min is least likely to have
def dominoMax(hand, pile, edges, opNum):
    # For all possible actions
    tempEdges = []
    # Starts at 100% Likelihood
    score = 1.00
    bestAction = 0
    edgePlaced = 0
    likelihood = 2.00
    edge = -1
    for action in hand:
        # If it is a legal move
        a, b = action
        if a in edges or b in edges:
            for x in edges:
                tempEdges.append(x)
            if a in edges:
                tempEdges.remove(a)
                tempEdges.append(b)
                edge = a
            else:
                tempEdges.remove(b)
                tempEdges.append(a)
                edge = b
            # Goes to Min given this Max
            likelihood = dominoMin(pile, tempEdges)

            # Best score is the one where Min is least likely to be able to play a domino
            if likelihood < score:
                score = likelihood
                bestAction = action
                edgePlaced = edge
        
    # If there are no possible moves, it will return 0
    # Otherwise, it returns the lowest min likelihood
    return bestAction, edgePlaced
        
# Minimizing Agent - Caculates the likelihood of Min having particular dominos
def dominoMin(pile, tempEdges):
    # Find Distribution of potential edges in pile
    dist = {0:0, 1:0, 2:0, 3:0, 4:0, 5:0, 6:0}
    for a, b in pile:
        dist[a] = dist[a] + 1
        dist[b] = dist[b] + 1
    # It doesn't matter if they have copies of the same edge, because they can only play one domino at a time
    # We change the distribution to represent percentages of the whole, then add it to the likelihood if it matches an edge
    likelihood = 0
    for x in dist.keys():
        dist[x] = dist[x] / (len(pile) * 2)
        if x in tempEdges:
            likelihood = likelihood + dist[x]
  
    return likelihood

# Does Minimax to calculate your turn
def yourTurn(hand, pile, edges, opNum):
    print("Your Turn")
    act, edge = dominoMax(hand, pile, edges, opNum)
    if act == 0:
        print("You must pick a domino from the pile ")
        a = int(input("What was the larger value on the domino you picked? "))
        b = int(input("What was the smaller value on the domino you picked? "))
        pile.remove((a,b))
        hand.append((a,b))
        if len(pile) == 0:
            gameOver(hand, opNum)
            return
    else: 
        print(f"You should put {act} down on a piece with {edge} number of dots ")
        hand.remove(act)
        a,b = act
        edges.remove(edge)
        if a is edge: 
            edges.append(b)
        if b is edge:
            edges.append(a)
        if len(hand) == 0:
            print("You Win!!!")
            return
    opponentTurn(hand, pile, edges, opNum)

# Gets input for what happened during opponent's turn
def opponentTurn(hand, pile, edges, opNum):
    print("Opponent Turn")
    turn = input("If your opponent picked from the pile, type ""PICK"". If your opponent placed a piece, type ""PLACE"" ")
    # They pick a piece from the pile. If the pile is equal to their hand, the pile is empty and the game is over
    if turn == "PICK":
        opNum = opNum + 1
        print(opNum)
        if len(pile) == opNum:
            gameOver(hand, opNum)
            return
            
    elif turn == "PLACE": 
        edge = int(input("What was the number of dots on the board that your opponent placed their piece next to? "))
        if edge not in edges:
            print("That's not Possible!")
            return
        a = int(input("What was the larger value on the domino? "))
        b = int(input("What was the smaller value on the domino? "))
        edges.remove(edge)
        pile.remove((a,b))
        # Add the edge which it was not placed on to edges, since that is now the new edge. 
        if edge is a:
            edges.append(b)
        elif edge is b:
            edges.append(a)
        # Keeping track of how many they have in their hand. 
        opNum = opNum - 1
    if opNum == 0:
        print("You Lose :-(")
        return
    yourTurn(hand, pile, edges, opNum)

# For when the game is over. Defines if you won or lost. 
def gameOver(hand, opNum):
    if len(hand) > opNum:
        print("YOU WIN!")
    elif len(hand) < opNum:
        print("You Lose :-(")
    else:
        print("This isn't possible? How did you get here?")
# Initializing the possible dominos
pile = [(6,6),(6,5),(6,4),(6,3),(6,2),(6,1),(6,0),(5,5),(5,4),(5,3),(5,2),(5,1),(5,0),(4,4),(4,3),(4,2),(4,1),(4,0),(3,3),(3,2),(3,1),(3,0),(2,2),(2,1),(2,0),(1,1),(1,0),(0,0)]

# TEST
# dominoMin(pile, [6, 5])

# Get your starting hand
test = input("If you want an artificial hand for Testing Purposes, type ""TEST"" ")
hand = []
if test == "TEST":
    hand = [(6,5),(6,4),(6,3),(6,2),(6,1),(5,0),(4,0)] # Temp Hand for testing purposes
    for x in hand:
        pile.remove(x)
else: 
    print("What are your seven starting Dominos? ")
    hand = []
    for i in range(7):
        a = int(input(f"What is the larger value of domino {i + 1}? "))
        b = int(input(f"What is the smaller value of domino {i + 1}? "))
        hand.append((a,b))
        pile.remove((a,b))


# Pile will keep track of dominos in the pile and possible dominos in their hand.

# Edges will keep track of the edge dominos on the edge board, keeping track of possible moves
edges = []

# Create the starting state
start = input("Who has the largest domino? Type ""ME"" or ""THEM"" ")
a = int(input("What is the larger value of the starting domino? "))
b = int(input("What is the smaller value of the starting domino? "))

# If you are starting, take the starting piece out of your hand and start your opponent's turn
if start == "ME":
    hand.remove((a,b))
    edges.append(a)
    edges.append(b)
    print(edges)
    opponentTurn(hand, pile, edges, 7)
elif start == "THEM":
    pile.remove((a,b))
    edges.append(a)
    edges.append(b)
    yourTurn(hand, pile, edges, 6)

print("Game End. Have a great day!")
    
