import ItsHidden
import requests
import random

key = ItsHidden.api_key
hash_key = ItsHidden.hashkey

generateNumber = random.randint(1009000, 1009999)

print(generateNumber)

url = f"https://gateway.marvel.com/v1/public/characters?id={generateNumber}&ts=567&apikey={key}&hash={hash_key}"






