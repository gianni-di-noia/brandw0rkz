"""A module to polupate the posgres database with a widget."""
import random

import requests


def run():
    """Add a widget to postgres"""
    pic = "https://www.brandworkz.com/wp-content/uploads/2016/08/Rathbones-Header.jpg"
    data = {
        "background_colour_r": random.randint(1, 254),
        "background_colour_g": random.randint(1, 254),
        "background_colour_b": random.randint(1, 254),
        "background_colour_a": random.randint(1, 254),
        "background_image": pic,
        "height": "%spx" % random.randint(1, 254),
        "content_background_colour_r": random.randint(1, 254),
        "content_background_colour_g": random.randint(1, 254),
        "content_background_colour_b": random.randint(1, 254),
        "content_background_colour_a": random.randint(1, 254),
        "border_radius": "1px",
        "content_body_text": "Hello World",
    }
    req = requests.post("http://localhost:5000/data", json=data)
    data = req.json()
    print(data)


if __name__ == "__main__":
    run()
