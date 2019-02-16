import random
import statistics

def newCarPrice():
    carPrice = [1 + random.randrange(i + 2) for i in range(5)]
    return carPrice

def guessPrice(carPrice, guess, openGuesses, firstNumWait = -1):
    if firstNumWait < 0:
        pass
    elif openGuesses.count(False) < firstNumWait:
        guess[0] = 0
    else:
        guess[0] = carPrice[0]

    # print(guess)
    return [True if carPrice[i] == guess[i] and openGuesses[i]
        else False for i in range(5)]

def updateOpenGuesses(guessedCorrectly, openGuesses):
    return [False if guessedCorrectly[i] else openGuesses[i] for i in range(5)]

def updateGuess(guess, guessedCorrectly, openGuesses, firstWaitNum = -1):
    if firstWaitNum < 0:
        pass
    elif openGuesses.count(False) < firstWaitNum:
        guess[0] = 0
    return [guess[i] + 1 if openGuesses[i] and not guessedCorrectly[i]
        else guess[i] for i in range(5)]

def playGame(firstNumWait = -1):
    carPrice = newCarPrice()
    # print(carPrice)
    guess = [1 for _ in range(5)]
    openGuesses = [True for _ in range(5)]
    guesses = 0

    while True:
        guesses += 1
        # print(openGuesses, guess)
        guessedCorrectly = guessPrice(carPrice, guess, openGuesses, firstNumWait)
        # print(guessedCorrectly)
        openGuesses = updateOpenGuesses(guessedCorrectly, openGuesses)

        if openGuesses == [False for _ in range(5)]:
            return (True, guesses)
        if guessedCorrectly == [False for _ in range(5)]:
            return (False, guesses)

        guess = updateGuess(guess, guessedCorrectly, openGuesses, firstNumWait)

def simulateGames(numGames, firstWaitNum):
    wins = 0
    for _ in range(numGames):
        result, _ = playGame(firstWaitNum)
        if result:
            wins += 1
    return 100.0 * wins / numGames


numSims = 100
numGames = 1000

for i in range(-1, 5):
    sims = [simulateGames(numGames, i) for _ in range(numSims)]
    print('You won ' + str(sum(sims) / len(sims)) + ' percent of the time'
        + ' if you wait until there are at least ' + str(i) + ' correct guesses'
        + ' before guessing the first guess correctly')
    print('The simulations had a standard deviation of ' + str(statistics.stdev(sims)))
