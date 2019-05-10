#import json
import json

# import data json file for dictionary word
data = json.load(open("data.json"))


def translate(word):
    if word in data:
        return data[word]
    else:
        return "The word doesn't exist within the database."


word = input("Enter word: ")

print(translate(word))
