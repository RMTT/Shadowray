import base64


def decode(text):
    n = len(text)
    if n % 3 is 1:
        text += "=="

    if n % 3 is 2:
        text += "="

    text = bytes(text, encoding='utf8')
    return str(base64.b64decode(text), encoding='utf8')
