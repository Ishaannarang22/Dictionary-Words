import requests


def hack(a):
    url = f'https://owlbot.info/api/v4/dictionary/{a}'
    headers = {"Authorization": "Token b6794ca8f0d8e36338c2fadb62cf54c8dc51069f"}
    r = requests.get(url, headers=headers)
    with open('CoolWords.txt', 'a') as f:
        data = r.json()
        try:
            for item in data['definitions']:
                definition = item['definition']
                f.write(f'\n{a} = {definition}\n')
                print(f"{a} = {definition}\n")
        except:
            f.write(f'\n{a} = No meaning found\n')
            print(f"{a} = No meaning found\n")
    f.close()


while True:
    hack(input('Word: '))
