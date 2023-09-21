import requests


def get_joke():
    response = requests.get('https://icanhazdadjoke.com/', headers={'Accept': 'application/json'})
    print(response.text)
    # json_response = response.json()
    # print(json_response)


if __name__ == '__main__':
    get_joke()