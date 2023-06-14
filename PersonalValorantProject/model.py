import requests

#"https://ap.api.riotgames.com/val/content/v1/contents?api_key=RGAPI-763c2c75-634a-49a5-844e-57d76c3af9c6"

api_key = "RGAPI-763c2c75-634a-49a5-844e-57d76c3af9c6"
api_url = "https://latam.api.riotgames.com/val/content/v1/contents?locale=juandnn#LAN"
api_url = api_url + "?api_key="+api_key


resp = requests.get("https://ap.api.riotgames.com/val/content/v1/contents?api_key=RGAPI-763c2c75-634a-49a5-844e-57d76c3af9c6")
complete_info = resp.json()
player_titles = complete_info["playerTitles"]

for element in player_titles:
    if dict(element).get("localizedNames",0) != 0:
        print(element["localizedNames"]["es-MX"])