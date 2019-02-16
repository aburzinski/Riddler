import random
import statistics

def newCarPrice():
    carPrice = [1 + random.randrange(i + 2) for i in range(5)]
    return carPrice

def guessPrice(carPrice, guess, openGuesses):
    guessedCorrectly = [True if carPrice[i] == guess[i] and openGuesses[i]
        else False for i in range(5)]
    return guessedCorrectly

def updateOpenGuesses(guessedCorrectly, openGuesses):
    return [False if guessedCorrectly[i] else openGuesses[i] for i in range(5)]

def updateGuess(guess, guessedCorrectly, openGuesses):
    return [guess[i] + 1 if openGuesses[i] and not guessedCorrectly[i]
        else guess[i] for i in range(5)]

def playGame():
    carPrice = newCarPrice()
    guess = [1 for _ in range(5)]
    openGuesses = [True for _ in range(5)]
    guesses = 0

    while True:
        guesses += 1
        guessedCorrectly = guessPrice(carPrice, guess, openGuesses)
        openGuesses = updateOpenGuesses(guessedCorrectly, openGuesses)

        if openGuesses == [False for _ in range(5)]:
            return (True, guesses)
        if guessedCorrectly == [False for _ in range(5)]:
            return (False, guesses)

        guess = updateGuess(guess, guessedCorrectly, openGuesses)

def simulateGames(numGames):
    wins = 0
    for _ in range(numGames):
        result, totalGuesses = playGame()
        if result:
            wins += 1
    return 100.0 * wins / numGames


numSims = 1000
numGames = 1000
sims = [simulateGames(numGames) for _ in range(numSims)]

print('You won ' + str(sum(sims) / len(sims)) + ' percent of the time')
print('The simulations had a standard deviation of ' + str(statistics.stdev(sims)))
