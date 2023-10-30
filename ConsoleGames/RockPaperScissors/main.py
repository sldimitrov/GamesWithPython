import random
ai_options = ['rock', 'paper', 'scissors']
ai_choose = random.choice(ai_options)
print(ai_choose + 'demo')

winner = ''
start = (input('Enter any key to start\n'))

print('          You\'re now challenged by AI')
print('Choose one of the followings - rock / paper / scissors')
print('        Your opponent has already done it')
human_choice = input()
# Logic
if human_choice == 'rock' and ai_choose == 'paper':
    winner = ai_choose
if human_choice == 'rock' and ai_choose == 'scissors':
    winner = human_choice
if human_choice == ai_choose:
    print('                  Draw')
    print('Real or not, you both think about the same thing!')
    exit()
if human_choice == 'paper' and ai_choose == 'scissors':
    winner = ai_choose
if human_choice == 'paper' and ai_choose == 'rock':
    winner = human_choice
if human_choice == 'scissors' and ai_choose == 'rock':
    winner = ai_choose
if human_choice == 'scissors' and ai_choose == 'paper':
    winner = human_choice

# Print Game output
if winner == human_choice:
    print('         Well done!')
    print(f'Your {human_choice} beats AI\'s {ai_choose}')
    print()
    print('You now have the ability to decide over Artificial Intelligence future')
else:
    print('HA HA HA ' * 7)
    print('Sorry, you human-being, now you\'re under my control ;)')

