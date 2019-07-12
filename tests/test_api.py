from api.models import db

# from api.views.main import main

# client passed from client - look into pytest for more info about fixtures
# test client api: http://flask.pocoo.org/docs/1.0/api/#test-client
def test_index(client):
    res = client.get("/")
    assert res.status_code == 200


def test_post_widget(client):
    data = {
        "background_colour_r": 234,
        "background_colour_g": 234,
        "background_colour_b": 234,
        "background_colour_a": 1,
        "background_image": "test",
        "height": "30px",
        "content_background_colour_r": 234,
        "content_background_colour_g": 234,
        "content_background_colour_b": 234,
        "content_background_colour_a": 1,
        "border_radius": "1px",
        "content_body_text": "Hello World",
    }

    res = client.post("/data", json=data)
    assert res.status_code == 200
    ret_dict = res.json
    assert isinstance(ret_dict["id"], int)
    assert ret_dict["id"] == 1


def test_get_widget(client):
    res = client.get("/data")
    ret_dict = res.json
    assert len(ret_dict["result"]["data"]) == 1
    assert ret_dict["result"]["data"][0]["_id"] == 1


def test_query_widget(client):
    res = client.get("/data?id=1")
    ret_dict = res.json
    assert len(ret_dict["result"]["data"]) == 1
    assert ret_dict["result"]["data"][0]["_id"] == 1
    # assert len(ret_dict["result"]["data"]) == 1
    assert ret_dict["result"]["data"][0]["border_radius"] == "1px"
