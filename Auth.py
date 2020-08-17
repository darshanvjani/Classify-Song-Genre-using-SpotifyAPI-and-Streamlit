import requests
import base64

# Client ID: 5e5b17cbade949d7b149c0a5c9061b98
# Client Secret Key: d4c01f8e64074565903ce95119582f77

class client_Auth:
    
    client_id = '5e5b17cbade949d7b149c0a5c9061b98'
    client_secret = 'd4c01f8e64074565903ce95119582f77'
    
    def __init__(self):
        
        self.OATHToken = None
        
    def token_request(self):
        
        client_creds = f"{self.client_id}:{self.client_secret}"
        client_creds_b64 = base64.b64encode(client_creds.encode())

        token_url = "https://accounts.spotify.com/api/token"
        method = "POST"
        token_data = {
            "grant_type": "client_credentials"
        }
        token_headers = {
            "Authorization": f"Basic {client_creds_b64.decode()}" # <base64 encoded client_id:client_secret>
        }

        r = requests.post(token_url, data=token_data, headers=token_headers)
        url_response = r.json()
        self.OATHToken = url_response.get('access_token')
        
        return self.OATHToken
    
