import random

questions = {
    "strong": "Do ye like yer drinks strong?",
    "salty": "Do ye like it with a salty tang?",
    "bitter": "Are ye a lubber who likes it bitter?",
    "sweet": "Would ye like a bit of sweetness with yer poison?",
    "fruity": "Are ye one for a fruity finish?",
}

ingredients = {
    "strong": ["glug of rum", "slug of whisky", "splash of gin"],
    "salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
    "bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
    "sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
    "fruity": ["slice of orange", "dash of cassis", "cherry on top"],
}

responses = {}

categories = ['strong', 'salty', 'bitter', 'sweet', 'fruity']

adjectives = ['spicy', 'sassy', 'classy']
nouns = ['dawg', 'cat', 'mouse']


# Part 1
def bartender_function():
  for i in range(0, len(categories)):
    response = input(questions[categories[i]] + ' Y/N ')
    if response.upper() == 'Y' or response.lower() == 'yes':
      responses[categories[i]] = 'True'
    else:
      responses[categories[i]] = 'False'
  return responses

# Part 2
def recommendations(a_dict):
  drink = []
  for i in range(0, len(categories)):
    if a_dict[categories[i]] == 'True':
      drink.append((random.choice(ingredients[categories[i]])))
  return drink

# Challenge - Provide Drink Name
def drink_name():
    name = random.choice(adjectives) + ' ' + random.choice(nouns)
    return name
    
# Part 3 - Provide a Main Function to Run Results from Bash
if __name__ == '__main__':
    bartender_function()
    print(recommendations(responses))
    print(drink_name())
    
    # Challenge - Ask for more than one drink 
    answer = input('Do you want another drink?: Y/N ')
    if answer.upper() == 'N' or answer.lower() == "no":
      print('Thank you, bye!')
    else:
      while answer.upper() == 'Y' or answer.lower() == 'yes':
        bartender_function()
        print(recommendations(responses))
        print(drink_name())
        answer = input('Do you want another drink? Y/N ')
      else:
        print('Thank you, bye!')
  




# Test Results 
'''
print(bartender_function())
print(recommendations(responses))
print(drink_name())
'''

    
''' # Part 2 - Long Method #    
  if a_dict['strong'] == 'True':
    drink.append((random.choice(ingredients['strong'])))
  if a_dict['salty'] == 'True':
    drink.append((random.choice(ingredients['salty'])))
  if a_dict['bitter'] == 'True':
    drink.append((random.choice(ingredients['bitter'])))
  if a_dict['sweet'] == 'True':
    drink.append((random.choice(ingredients['sweet'])))
  if a_dict['fruity'] == 'True':
    drink.append((random.choice(ingredients['fruity'])))
  return drink  
'''