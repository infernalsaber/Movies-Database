# from data import movies
# print(movies[0])


import requests, json
from math import floor
from PIL import Image
def desc_series(entry: tuple)-> tuple:
    apiData = requests.get(f"https://api.jikan.moe/v4/anime/{entry[0]}/full").json()
    img = apiData["data"]["images"]["jpg"]["large_image_url"]
    synopsis = apiData["data"]["synopsis"]
    # Image.open(requests.get(img, stream=True).raw).convert("RGB")

    output = '''{} is a {} hour {} minute {} animated movie that came out in the year {}.
It is rated {} on the site MAL.
Produced by the studio {},it has {} onboard as the {}.

Additional info:
Synopsis - {}

A picture of the poster: 
    '''.format(entry[1], floor(entry[4]/60), entry[4]%60, entry[6], entry[3], entry[2], entry[5], entry[8], entry[9], synopsis)

    return (output, img)


# desc_series(1)