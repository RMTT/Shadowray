import requests

def parse_yes_or_no(text):
    text = str(text).lower()

    if text == "yes" or text == "y":
        return True
    elif text == "no" or text == "n":
        return False
    else:
        return None


def download_file(url,filename):
    r = requests.get(url)

    with open(filename,"w") as file:
        file.write(r.content)


