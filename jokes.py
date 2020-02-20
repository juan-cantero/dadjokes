import requests #import the library to make http requests

url = "https://icanhazdadjoke.com/search" #save the url in string

#this save the response in an object type response
response = requests.get(url, 
headers = {"Accept" : "application/json"},
params= {"term" : "dog", "limit" : 3}
)

#returns the json encoded content from the object response and it is a python dictionary
data = response.json()

print(data["results"][0]["joke"])

# I get the value in the key joke inside the dictionary 
#joke = data["joke"]

# I print the value
#print(joke)