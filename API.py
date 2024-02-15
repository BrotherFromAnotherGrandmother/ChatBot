import requests

url = 'https://dvmn.org/api/long_polling/'
headers = {
    "Authorization": "Token 6ebf52cd576855857e60303b91c292a6cab40497"
}
while True:
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
    except requests.exceptions.ReadTimeout:
        continue
    print(response.json())