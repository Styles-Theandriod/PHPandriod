

# Person = {'name': 'John', 'last_name': ' Doe', 'Age': 36}

# print(Person['name'])
# print(Person)

items = list()
empty_list = []
print(empty_list)

fav_food = [ 'pounded yam', 'rice with chicken', 'Banga soup and stach', 'Beans' ]

cars = ['Tesla', 'Benz', 'Mustang', 'Mustang', 23490582388, True,]

countries = ['Canada', 'Sweeden', ' Portugal', 'Silicon Valley In USA',]
print(cars[-1])


# UnPACKING A LIST 

artist = ['Chris brown', 'Psquare', 'Wiskid', 'Rema']
first_artist, second_artist, *rest = artist
# print(first_artist, second_artist)
print(first_artist, second_artist)

fav_football_players = ['Nwabai', 'Messi', 'Ronaldo', 'Nema', 'Osimehn']
fav_football_players = ['Nwabai', 'Messi', 'Ronaldo', 'Nema', 'Osimehn']


# print(artist[0:3])
# print(artist[:-1])
# print(artist[::2])
# print(artist[-3:-1])
print(fav_football_players[-1:-3])
print(fav_football_players[-1:-3])
print(fav_football_players[-1:-3])
print(fav_football_players[-1:-3])
print(fav_football_players[-1:-3])
print(fav_football_players[-1:-3])

# changing items in a list
phones_models = ['Iphone', 'Samsung', 'Hawaii', 'Oppor']

changed_items = phones_models[3] = 'itel'
print(changed_items)

# Adding items to the list

phones_models.append('infinise')

print(phones_models)

# Popping items in the list
fav_drinks = ['Coca Cola', 'Bigie', 'fanta']

fav_drinks.pop(0)
fav_drinks.pop()

print(fav_drinks)


# Deleting items in the list
brands = ['gucci', 'vasscii', 'dng', 'fendi', 'theandriod']
del brands[0:2]

print(brands)

# List comprehension
language = 'python'
lst = [language]
print(lst)


# Python game creation 

# checks data from thinking with user input if they match returns True


userInput = float( input('Enter your year of birth: '))

currentYear = 2024

print('Your current age is: ', userInput - currentYear)



import random

database = []  # Make database a global variable
print(database)

def Game():
    while True:
        score = 0

        thinking = ['education', 'coding', 'science', 'Programming', 'Fathering', 'Mothering', 'sisters']
        computer_thinking = random.choice(thinking)

        userInput = input('What am I thinking: ')

        if userInput == computer_thinking:
            print('You got my thinking 😂')
            score += 1
        else:
            print('Wrong! Try again 😭')

def createAccount():
    print('#1 Create Account \t  #2 Login Account')

    userInput = input('Enter a number: ')

    if userInput == str(1):
        username = input('Enter username: ')
        password = input('Enter password: ')
        database.append({'username': username, 'password': password})
        Game()
    elif userInput == str(2):
        username = input('Enter username: ')
        password = input('Enter password: ')
        if any(entry['username'] == username and entry['password'] == password for entry in database):
            Game()
        else:
            print('Invalid credentials. Try again.')

createAccount()


























# import random

# thinking = ['gucci', 'education', 'fendi', 'theandriod', 'dng', 'jadrolita', 'bizmarrow']


# while True:

#     random_thinking = random.choice(thinking)

#     print(random_thinking)

#     print('what am i thinking about')

#     userInput = input('Your guess: ')

#     score = 0

#     if(userInput  in random_thinking):
#         print('you got my thought 😂')
#         score = score + 1
#         print('your score is ' + str(score))
#     else:
#         print('wrong try again 😭')
#         score = score - 1

#     play_again = input('Do you want to play again? (yes/no):').lower()
#     if(play_again != 'yes'):
#         break;




