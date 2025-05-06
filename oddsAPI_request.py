import requests
import json
response = requests.get('https://api.the-odds-api.com/v4/sports/soccer_epl/odds/', params={
    'apiKey': 'a2de488451701efbac4942402a19c516', #odds-api key
    'regions': 'us',
    'markets': 'h2h'
})
data = response.json()

json_formatted_str = json.dumps(data, indent=2)

print(json_formatted_str)