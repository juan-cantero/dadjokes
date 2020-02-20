import requests #import the library to make http requests
import random
import sys

url = "https://icanhazdadjoke.com/search" #save the url in string

# [1] is the first argument
term = sys.argv[1]

#this save the response in an object type response
response = requests.get(url, 
headers = {"Accept" : "application/json"},
params= {"term" : term}
)

#returns the json encoded content from the object response and it is a python dictionary
data = response.json()

totalJokes = len(data["results"])


index = random.randint(0,totalJokes -1)


# data is a dictionaty, "results" is a key, it has a list with dictionaries inside, index is the
#dictionary that I want and "joke" is the key 
jokeToTell = data["results"][index]["joke"]

def tellAJoke():
    if (index < 1):
        print("sorry I don't know any joke about " + term)
    elif (index == 1):
        print(jokeToTell)
    else:
        print(f'I have {totalJokes} about {term}, here is one: ')
        print(jokeToTell)

tellAJoke()

