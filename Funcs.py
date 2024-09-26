import pandas as pd
import requests
from requests.auth import HTTPBasicAuth


# Your client ID and client secret
client_id = '6ab02cc1a1c140f0bd213d0b27e8c74c'
client_secret = 'VTrUzsJw0XDmKfJvM1QIXpn1QC1Hs96e'

# OAuth token URL
url = 'https://us.battle.net/oauth/token'

# Request access token
response = requests.post(
    url,
    data={'grant_type': 'client_credentials'},
    auth=HTTPBasicAuth(client_id, client_secret)
)

# Parse response
if response.status_code == 200:
    access_token = response.json()['access_token']
    # print(f"Access Token: {access_token}")
else:
    print(f"Failed to get access token: {response.status_code}")

#############################
#############################
#############################
#############################
#############################

def get_pvp_season(token):
    url = "https://us.api.blizzard.com/data/wow/pvp-season/index"
    
    # Parameters for the GET request
    params = {
        "namespace": "dynamic-us",
        "locale": "en_US",
        "access_token": token
    }    
    # Send the GET request
    response = requests.get(url, params=params)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON content
        
        data = response.json()
        return data['current_season']['id']
    
    else:
        # Handle the error
        print(f"Failed to retrieve data: {response.status_code}")
        return None
    
#############################
#############################
#############################
#############################
#############################
    
def GetCharacterRatings(charactername, server, bracket, token):
        
    url = f"https://us.api.blizzard.com/profile/wow/character/{server}/{charactername}/pvp-bracket/{bracket}"
    print(url)

    
    params = {
        "namespace" : "profile-us",
        "locale" : "en_US",
        "access_token" : token
    }
    
    response = requests.get(url, params=params)
    
    # print(response.json())
    
    # for key in response.json():
    #     print(key)
        
    return(response.json()['rating'])
    
#############################
#############################
#############################
#############################
#############################
    
def GetCharacterPic(charactername, server, token):
    url = f"https://us.api.blizzard.com/profile/wow/character/{server}/{charactername}/character-media"
    params = {
        "namespace" : "profile-us",
        "locale" : "en_US",
        "access_token" : token
    }
    
    response = requests.get(url, params=params)
    
    # for key in response.json():
    #     print(key)
        
    pics_df = response.json()['assets']
    
    df = pd.DataFrame(pics_df)
    
    main_raw_pic = df.value[2]
    
    return(main_raw_pic)
        