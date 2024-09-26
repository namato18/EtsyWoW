import pygame
import sys
import requests
from requests.auth import HTTPBasicAuth
from Funcs import get_pvp_season

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
    print(f"Access Token: {access_token}")
else:
    print(f"Failed to get access token: {response.status_code}")


pvp_season = get_pvp_season(token = access_token)
print(pvp_season)


# Initialize Pygame
pygame.init()

# Create a screen with dimensions similar to your final display
screen = pygame.display.set_mode((480, 320))
pygame.display.set_caption('WoW Character Display')

# Define a font
font = pygame.font.Font(None, 36)

# Sample character data
character_data = {
    "name": "Thrall",
    "level": 60,
    "health": 3250,
    "class": "Shaman",
    "guild": "Warchief",
    "faction": "Horde",
    "season": pvp_season
}

# Main loop to keep the window open and render content
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Fill the screen with black
    screen.fill((0, 0, 0))

    # Render the text on the screen
    name_text = font.render(f"Name: {character_data['name']}", True, (255, 255, 255))
    level_text = font.render(f"Level: {character_data['level']}", True, (255, 255, 255))
    health_text = font.render(f"Health: {character_data['health']}", True, (255, 255, 255))
    class_text = font.render(f"Class: {character_data['class']}", True, (255, 255, 255))
    guild_text = font.render(f"Guild: {character_data['guild']}", True, (255, 255, 255))
    faction_text = font.render(f"Faction: {character_data['faction']}", True, (255, 255, 255))
    season_text = font.render(f"Season: {character_data['season']}", True, (255, 255, 255))

    # Blit the text onto the screen
    screen.blit(name_text, (20, 20))
    screen.blit(level_text, (20, 60))
    screen.blit(health_text, (20, 100))
    screen.blit(class_text, (20, 140))
    screen.blit(guild_text, (20, 180))
    screen.blit(faction_text, (20, 220))
    screen.blit(season_text, (20, 260))

    # Update the display
    pygame.display.flip()

