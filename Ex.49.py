# How to connect to an API(Application Programming Interface) using Python

import requests
# Download this 'requests' module via 'Terminal' inside Python

# https://pokeapi.co/api/v2/ is for Pokemon API

base_url = "https://pokeapi.co/api/v2/"

def get_pokemon_info(name):
    url = f"{base_url}/pokemon/{name}"
    response = requests.get(url)

    if response.status_code == 200:
       pokemon_data = response.json()
       return pokemon_data
    else:
        print(f"Failed to retrieve data {response.status_code}")

# pokemon_name = "pikachu"
pokemon_name = "typhlosion"
pokemon_info = get_pokemon_info(pokemon_name)

# The call-out function will give the HTTP status code [200]
# [200] means response is ok, for more info check HTTP response via the internet

if pokemon_info:
    print(f"Name: {pokemon_info["name"].capitalize()}")
    print(f"Id: {pokemon_info["id"]}")
    print(f"Height: {pokemon_info["height"]}")
    print(f"Weight: {pokemon_info["weight"]}")

