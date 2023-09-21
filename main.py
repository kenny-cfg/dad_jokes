import requests


def get_joke():
    response = requests.get('https://icanhazdadjoke.com/')
    print(response)


if __name__ == '__main__':
    get_joke()