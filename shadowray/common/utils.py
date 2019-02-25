import requests
import time
import json


def parse_yes_or_no(text):
    text = str(text).lower()

    if text == "yes" or text == "y":
        return True
    elif text == "no" or text == "n":
        return False
    else:
        return None


def print_progress(percent, width=60, extra=''):
    if percent > 100:
        percent = 100

    format_str = ('[%%-%ds]' % width) % ('#' * int(percent * width / 100.))
    print('\r%s  %.2f%%  %s' % (format_str, percent, extra), end='')


def download_file(url, filename, show_progress=False):
    r = requests.get(url, stream=True)

    length = float(r.headers['content-length'])

    f = open(filename, "wb")

    count = 0

    time_s = time.time()
    speed = 0
    count_s = 0
    for chunk in r.iter_content(chunk_size=512):
        if chunk:
            f.write(chunk)
            count += len(chunk)

            if show_progress:
                percent = (count / length) * 100.

                time_e = time.time()
                if time_e - time_s > 1:
                    speed = (count - count_s) / (time_e - time_s) / 1024 / 1024
                    count_s = count
                    time_s = time_e

                print_progress(percent, extra='%.2fM/S' % speed)

    f.close()


