#import json
import json

# import data json file for dictionary word
data = json.load(open("data.json"))

# Function to translate/define word


def translate(word):
    if word in data:
        return data[word]
    else:
        return "The word doesn't exist within the database."


# Gather input from user
word = input("Enter word: ")

# Print defineition
print(translate(word))
