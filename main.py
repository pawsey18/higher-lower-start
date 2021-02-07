
from art import logo, vs
from game_data import data
import random
from replit import clear

def format_data(account):
  """take account data return  printable format!"""
  account_name = account["name"]
  account_description = account["description"]
  account_country = account["country"]
  return f"{account_name}, {account_description}, {account_country}"

def check_answer(guess, a_followers, b_followers):
  """Take the user guess and follower return if right"""
  if a_followers > b_followers:
    return guess == "a"
  else:
    return guess == "b" 

score = 0
print(logo)
continue_game = True
account_b = random.choice(data)

while continue_game:

  # Display art
 
  # Generate a random account from the game data.
  account_a = account_b
  account_b = random.choice(data)
 
  while account_a == account_b:
    account_b = random.choice(data)

  print(f"Compre A:{format_data(account_a)}.")
  print(vs)
  print(f"Against B:{format_data(account_b)}.")


  #ask user for guess
  guess = input("Who has more followers? Type 'A' or 'B':").lower()
  ##get follower count of each account
  a_follower_count = account_a["follower_count"]
  b_follower_count = account_b["follower_count"]
  #check if user is correct
  is_guess_correct = check_answer(guess, a_follower_count, b_follower_count)

  
  clear()
  print(logo)
  #give user feedback on their guess
  if is_guess_correct:
    score += 1
    print(f"You are correct. Your current score: {score}")
  else:
    continue_game = False
    print("Sorry, you lose")  

