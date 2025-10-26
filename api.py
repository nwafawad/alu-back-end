import requests

url = "https://api.kanye.rest"
def get_kanye_quote():
    response = requests.get(url)
    if response.status_code == 200:
        return response.json().get("quote")
    else:
        return "Error fetching quote"
    
print(get_kanye_quote())