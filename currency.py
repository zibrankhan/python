import requests

# Where USD is the base currency you want to use
url = 'https://api.exchangerate-api.com/v4/latest/USD'

# url = 'http://data.fixer.io/api/latest?access_key=40eac7a32ba84e0369830d99248246b7'

# Making our request
response = requests.get(url)
data = response.json()

# Your JSON object
print (data)