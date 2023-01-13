import requests

# Asks the user to enter the URL to shorten
long_url = input("Enter the URL to shorten: ")

# Defines the URL of the Google URL Shortener API
url = "https://www.googleapis.com/urlshortener/v1/url"

# Prepares the data for the request
payload = {"longUrl": long_url}
headers = {"Content-Type": "application/json"}

# Sends the request to the API
response = requests.post(url, json=payload, headers=headers)
data = response.json()

# Prints the shortened URL
print("Shortened URL: ", data["id"])
