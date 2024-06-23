import requests

def fetch_linkedin_profile(access_token):
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Connection': 'Keep-Alive',
        'X-Restli-Protocol-Version': '2.0.0'
    }
    profile_url = 'https://api.linkedin.com/v2/me'
    response = requests.get(profile_url, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        return None

if __name__ == '__main__':
    access_token = input("Enter your LinkedIn access token: ")
    profile_data = fetch_linkedin_profile(access_token)

    if profile_data:
        print("LinkedIn Profile Data:")
        print(profile_data)
    else:
        print("Failed to fetch LinkedIn profile data.")
