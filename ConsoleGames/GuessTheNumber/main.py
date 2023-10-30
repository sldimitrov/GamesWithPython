import random
special = random.randint(1, 100)
is_guessed = False
print()
print('   Welcome to my new game.')
print('You should guess a number between')
print('          1 and 100.   ')
counter = 0
while True:
    guess = int(input())
    counter += 1
    if guess == special:
        break
    elif guess < special:
        print('Go higher.')
    elif guess > special:
        print('Go lower buddy.')
print('Congratulations, you guessed ')
print(f'     at your {counter} try!')
# Print User output
# Adding something new just for a test
