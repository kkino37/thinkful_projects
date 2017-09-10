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
 
if __name__ == '__main__':
    print(bartender_function())
    print(recommendations(responses))
    
# Test Results 
print(bartender_function())
print(recommendations(responses))

    
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