import requests
from random import choice
from pyfiglet import figlet_format
from termcolor import colored

app_header = colored(figlet_format("DAD JOKES"), color = "cyan", attrs=["bold", "dark"])
print(app_header)

term =  input("What would you like to search for?\n").lower()
url = "https://icanhazdadjoke.com/search"
response = requests.get(
    url, 
    headers = {
        "Accept": "application/json"
    },
    params = {
        "term": term,
    },
).json()
num_jokes = response["total_jokes"]
results_jokes = response["results"]
if num_jokes > 0:
    if num_jokes == 1:
        print(f"There is 1 Joke about term: {term}. Here is the one:")
        print(results_jokes[0]["joke"])
    else:
        print(f"There are {num_jokes} Joke about term: {term}. Here's one randomly choosen:")
        print(choice(results_jokes)["joke"])
else:
    print(f"There are no jokes with your term: {term}")
