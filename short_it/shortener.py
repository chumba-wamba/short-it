import requests
import json
from short_it.models import URL


# Random URL Generator where it acquires three
# random words from the api hosted at the link
# below, and concatenates them with a hyphen ("-")
# and returns this string
def random_url_gen():
    random_url_flag = False
    url = "https://random-word-api.herokuapp.com/word?number=3"
    while(not random_url_flag):
        words = json.loads(requests.get(url).text)

        flag = False
        for word in words:
            if "-" in word:
                flag = True
        if flag == True:
            continue

        random_url = "-".join(words)
        objects = URL.objects(shortened_url="random_url")
        if(len(objects) > 0):
            continue

        random_url_flag = True

    return random_url.lower()
