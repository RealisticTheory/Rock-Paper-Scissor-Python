import random
print('Welcome to Rock, Paper, Scissor!\n'
      'Do you wanna play? Enter Yes or No')

start = input('Enter Yes or No: ').lower()

t = True
def startEnd(start):
      while t:
         if start == str.lower("Yes"):
               print('Game Start!')
               gameBegin(t)
               break
         elif start == str.lower("No"):
               print('Good Bye!')
         else:
               start = input('Enter Yes or No: ').lower()

def gameBegin(trueorfalse):
      global comAnswer
      i = 0
      while i < 1:
            comp = random.randint(0, 2)
            choose = input("Enter rock, paper, or scissor: ")
            if comp == 0:
                  comAnswer = 'rock'
            elif comp == 1:
                  comAnswer = 'paper'
            elif comp == 2:
                  comAnswer = 'scissor'
            print('Computer chooses ' + comAnswer)

            # rock results
            if comp == 0 and choose == 'rock':
                  print('Tie')
            elif comp == 0 and choose == 'paper':
                  print('You Win!')
            elif comp == 0 and choose == 'scissor':
                  print('You lose')

            # paper results
            if comp == 1 and choose == 'rock':
                  print('You lose')
            elif comp == 1 and choose == 'paper':
                  print('Tie')
            elif comp == 1 and choose == 'scissor':
                  print('You Win!')

            # scissor results
            if comp == 2 and choose == 'rock':
                  print('You Win!')
            elif comp == 2 and choose == 'paper':
                  print('You lose')
            elif comp == 2 and choose == 'scissor':
                  print('Tie')

            # play again?
            again = input('\nPlay again? Enter Yes or No: ').lower()
            if again == str.lower('yes'):
                  continue
            elif again == str.lower('no'):
                  print('Thank you for playing!')
                  break


startEnd(start)