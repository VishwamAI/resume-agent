import requests
from flask import Flask, redirect, request, url_for

app = Flask(__name__)

# LinkedIn OAuth 2.0 credentials
CLIENT_ID = '86jwmes8cqsua0'
CLIENT_SECRET = 'gaICAyUcnVcRuYj0'
REDIRECT_URI = 'http://localhost:5000/callback'
AUTHORIZATION_URL = 'https://www.linkedin.com/oauth/v2/authorization'
TOKEN_URL = 'https://www.linkedin.com/oauth/v2/accessToken'

@app.route('/')
def index():
    return redirect(f'{AUTHORIZATION_URL}?response_type=code&client_id={CLIENT_ID}&redirect_uri={REDIRECT_URI}&scope=r_liteprofile%20r_emailaddress%20w_member_social')

@app.route('/callback')
def callback():
    code = request.args.get('code')
    if not code:
        return 'Error: No code provided'

    # Exchange authorization code for access token
    token_response = requests.post(TOKEN_URL, data={
        'grant_type': 'authorization_code',
        'code': code,
        'redirect_uri': REDIRECT_URI,
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET
    })

    token_json = token_response.json()
    access_token = token_json.get('access_token')
    if not access_token:
        return 'Error: No access token obtained'

    return f'Access Token: {access_token}'

if __name__ == '__main__':
    app.run(debug=True)
