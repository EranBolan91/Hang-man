import random

wordslist = ['correction', 'childish', 'beach', 'python', 'assertive', 'interference', 'complete', 'share', 'credit card', 'rush', 'south']
word = random.choice(wordslist)
hidden_word = []
inGame = True
times = 0

for index,ch in enumerate(word):
    if index % 3 == 0:
        hidden_word.append(ch)
    else:
        hidden_word.append("*")

while inGame:
    char_input = input("Please enter your letter ")
    if len(char_input) == 2:
        print("Pleaser enter only one letter")
        continue
    else:
        for i, char in enumerate(word):
          if(char_input == char):
              hidden_word[i] = char_input
              print(hidden_word)
          else:
              print(hidden_word)
              #need to print on GUI the hangman
          if(times == 6):
              print("You have lost")
              #pop up a text box and also 'play again' button
              inGame = False
              break
        times +=1