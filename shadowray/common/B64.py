import base64


def decode(text):
    n = len(text)
    missing_padding = 4 - n % 4

    if missing_padding:
        text += '=' * missing_padding
    text = bytes(text, encoding='utf8')
    return str(base64.b64decode(text), encoding='utf8')
