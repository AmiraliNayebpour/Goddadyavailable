import requests
from colorama import Fore


domain_name_list = [
    #Enter your domain names here
]


def check_domain_availability(api_key, api_secret, domain_name):
    url = f"https://api.godaddy.com/v1/domains/available?domain={domain_name}"
    
    headers = {
        "Authorization": f"sso-key {api_key}:{api_secret}",
        "Content-Type": "application/json"
    }

    try:
        response = requests.get(url, headers=headers)
        data = response.json()

        if response.status_code == 200:
            available = data.get('available', False)
            return available
        else:
            print(f"Error: {data['message']}")
            return None

    except Exception as e:
        print(f"Error: {e}")
        return None

# Replace 'YOUR_API_KEY' and 'YOUR_API_SECRET' with your actual API key and API secret
api_key = 'YOUR_API_KEY'
api_secret = 'YOUR_API_SECRET'
for char in domain_name_list : 
	
	domain_name = char

	availability = check_domain_availability(api_key, api_secret, domain_name)

	if availability is not None:
		if availability:
			print(Fore.GREEN , f"The domain '{domain_name}' is available.")
		else:
			print(Fore.RED , f"The domain '{domain_name}' is not available.")

