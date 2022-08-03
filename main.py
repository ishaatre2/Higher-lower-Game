from game_data import data 
import random
import art
import replit

def random_data():
  #returns a random entry from the data
  entry = random.choice(data)
  return entry


def access_data(entry):
  #provides the specific information and returns the compare statement
  name = entry['name']
  description = entry['description']
  country = entry['country']

  return f"{name}, a {description}, from {country}."

def compare(first_entry,second_entry):
  follower_count_a = first_entry['follower_count']
  follower_count_b = second_entry['follower_count']

  if follower_count_a > follower_count_b:
    return 'A'
  else:
    return 'B'


def track(first_entry,second_entry):
  score = 0
  final_answer = compare(first_entry,second_entry)
  print(final_answer)
  user_guess = input("Who has more followers? Type 'A' or 'B':")
  
  while final_answer == user_guess:
    score = score + 1
    replit.clear()
    print(art.logo)
    print(f"Your current score is {score}")
    first_entry = second_entry
    a = access_data(first_entry)
    print(f"Compare A: {a}")
    
    print(art.vs)

    second_entry = random_data()
    b = access_data(second_entry)
    print(f"Compare B: {b}")

    final_answer = compare(first_entry,second_entry)
    print(final_answer)
    user_guess = input("Who has more followers? Type 'A' or 'B':")

    if final_answer != user_guess:
      replit.clear()
      print(f"Sorry you lose, your final score is {score-1}")
      
      
  if final_answer != user_guess:
    replit.clear()
    print(f"Sorry you lose, your final score is {score}")
  

def game():
  print(art.logo)
  first_entry = random_data()
  a = access_data(first_entry) 
  print(f"Compare A: {a}")
       
  print(art.vs)

  second_entry = random_data()
  if first_entry == second_entry:
    second_entry = random_data()    
  b = access_data(second_entry)
  print(f"Compare B: {b}")

    

  track(first_entry, second_entry)
  
game()


  





  



