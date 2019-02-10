import random

class card:
    def __init__(self, rank):
        self.rank = rank
        self.value = self.convertRank(rank)

    def __gt__(self, other):
        if self.getValue() > other.getValue():
            return True
        else:
            return False
    
    def __str__(self):
        return self.rank

    def convertRank(self, rank):
        if rank == 'A':
            return 14
        elif rank == 'K':
            return 13
        elif rank == 'Q':
            return 12
        elif rank == 'J':
            return 11
        else:
            return int(rank)

    def getValue(self):
        return self.value

    def getRank(self):
        return self.rank

class deck:
    def __init__(self):
        self.cards = []

    def __str__(self):
        return str(self.cards)

    def addCard(self, card):
        self.cards.append(card)

    def shuffle(self):
        shuffledDeck = []
        deckLen = len(self.cards)
        while deckLen > 0:
            cardNum = random.randrange(deckLen)
            shuffledDeck.append(self.cards[cardNum])
            del self.cards[cardNum]
            deckLen -= 1
        self.cards = shuffledDeck

    def playCard(self):
        return self.cards.pop()


def createDeck(ranks):
    newDeck = deck()
    for i in range(4):
        newDeck.addCard(card(ranks[0]))
        newDeck.addCard(card(ranks[1]))
        newDeck.addCard(card(ranks[2]))
    newDeck.shuffle()
    return newDeck


def playGame(deck1, deck2):
    score1 = 0
    score2 = 0
    while score1 < 5 and score2 < 5:
        card1 = deck1.playCard()
        card2 = deck2.playCard()
        #print(card1, card2)
        if card1 > card2:
            score1 += 1
        else:
            score2 += 1
        #print(score1, score2)
    if score1 >= 5:
        return True
    else:
        return False

def simulateGames(ranks1, ranks2, numGames):
    deck1Wins = 0
    for i in range(numGames):
        deck1 = createDeck(ranks1)
        deck2 = createDeck(ranks2)
        if playGame(deck1, deck2):
            deck1Wins += 1
    return 100.0 * deck1Wins / numGames

redRanks = ['A', '9', '7']
blueRanks = ['K', 'J', '6']
blackRanks = ['Q', '10', '8']
numGames = 10000

print('Red beat Blue ' + str(simulateGames(redRanks, blueRanks, numGames)) +
    ' percent of the time out of ' + str(numGames) + ' games')

print('Blue beat Black ' + str(simulateGames(blueRanks, blackRanks, numGames)) +
    ' percent of the time out of ' + str(numGames) + ' games')

print('Black beat Red ' + str(simulateGames(blackRanks, redRanks, numGames)) +
    ' percent of the time out of ' + str(numGames) + ' games')
