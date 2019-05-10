# import json
import json
# import difflib to compare words
from difflib import get_close_matches
# import data json file for dictionary word
data = json.load(open("data.json"))


# Function to translate/define word
def translate(word):
    # Make all words automatically lowercase
    word = word.lower()
    if word in data:
        return data[word]

     # Proper noun checkpoint
    elif word.title() in data:
        return data[word.title()]

    # Acronym Checkpoint
    elif word.upper() in data:
        return data[word.upper()]

    # Basic algorithm to check for incorrectly typed words and match
    elif len(get_close_matches(word, data.keys())) > 0:
        wordCheck = input("Did you mean %s instead? Enter Y if yes, or N if no." %
                          get_close_matches(word, data.keys())[0])
        if wordCheck == "Y":
            return data[get_close_matches(word, data.keys())[0]]
        elif wordCheck == "N":
            return "The word doesn't exist within the database."
        else:
            return "Please doublecheck your entry."
    else:
        return "The word doesn't exist within the database."


# Get word from user
word = input("Enter word: ")

# Print definition
output = translate(word)

# Multiple definition output organization
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
