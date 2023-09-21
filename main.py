import requests


def get_joke():
    response = requests.get('https://icanhazdadjoke.com/', headers={'Accept': 'application/json'})
    json_response = response.json()
    joke_text = json_response['joke']
    print(joke_text)


if __name__ == '__main__':
    get_joke()