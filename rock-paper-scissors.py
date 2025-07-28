import random

def get_choices():
  player_choice = input("Enter your choice (rock, paper, scissors) : ")
  options = ['rock' , 'paper' , 'scissors']
  computer_choice = random.choice(options)
  choices = {'player' : player_choice , 'computer' : computer_choice}
  return choices

def check_win(player,computer):
  print(f"Player choice : {player} and Computer choice : {computer}")
  if player == computer :
    return "It's a tie!"
  
  elif player == 'rock':
    if computer == "paper":
      return "You lose!"
    else:
      return "You win!"
    
  elif player == 'paper':
    if computer == 'rock':
      return 'You win!'
    else:
      return 'You lose!'
    
  elif player == 'scissors':
    if computer == 'rock':
      return 'You lose!'
    else:
      return 'You win!'
    
  else:
    return 'Invalid prompt..Try again!'
  
choices = get_choices()
result = check_win(choices['player'],choices['computer'])
print(result)