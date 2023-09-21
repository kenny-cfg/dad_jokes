import requests


def get_joke():
    response = requests.get('https://icanhazdadjoke.com/', headers={'Accept': 'application/json'})
    json_response = response.json()
    joke_text = json_response['joke']
    return joke_text


def write_to_file(text):
    with open('joke.txt', 'a') as joke_file:
        joke_file.write(text)
        joke_file.write('\n')


if __name__ == '__main__':
    joke = get_joke()
    write_to_file(joke)
