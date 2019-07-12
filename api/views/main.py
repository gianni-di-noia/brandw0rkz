"""Main view."""
from flask import Blueprint, jsonify, request

from flask_babel import gettext, lazy_gettext

from api.core import create_response, logger, serialize_list
from api.models import Widget, db

main = Blueprint("main", __name__)  # initialize blueprint


@main.route("/")
def index():
    """Home Page"""
    # you are now in the current application context with the main.route decorator
    # access the logger with the logger from api.core and uses the standard logging module
    # try using ipdb here :) you can inject yourself
    # return "ciao"
    return {"a": lazy_gettext("greeting")}


@main.route("/data", methods=["GET"])
def get_data():
    """Retrive widgets data. arguments are filters."""
    if request.args:
        data = Widget.query.filter_by(**request.args.to_dict()).all()
    else:
        data = Widget.query.all()
    return create_response(data={"data": serialize_list(data)})


# POST request for /data
@main.route("/data", methods=["POST"])
def create_widget():
    def missing_data(field):
        msg = "No %s provided for widget." % field
        logger.info(msg)
        return create_response(status=422, message=msg)

    data = request.get_json()
    logger.info("Data recieved: %s", data)
    if "background_colour_r" not in data:
        return missing_data("background_colour_r")
    if "background_colour_b" not in data:
        return missing_data("background_colour_b")
    if "background_colour_g" not in data:
        return missing_data("background_colour_g")
    if "background_colour_a" not in data:
        return missing_data("background_colour_a")
    if "background_image" not in data:
        return missing_data("background_image")
    if "height" not in data:
        return missing_data("height")
    if "content_background_colour_r" not in data:
        return missing_data("content_background_colour_r")
    if "content_background_colour_b" not in data:
        return missing_data("content_background_colour_b")
    if "content_background_colour_g" not in data:
        return missing_data("content_background_colour_g")
    if "content_background_colour_a" not in data:
        return missing_data("content_background_colour_a")
    if "border_radius" not in data:
        return missing_data("border_radius")
    if "content_body_text" not in data:
        return missing_data("content_body_text")

    # create SQLAlchemy Objects
    background_colour = ",".join(
        [
            str(data["background_colour_r"]),
            str(data["background_colour_g"]),
            str(data["background_colour_b"]),
            str(data["background_colour_a"]),
        ]
    )
    content_background_colour = ",".join(
        [
            str(data["content_background_colour_r"]),
            str(data["content_background_colour_g"]),
            str(data["content_background_colour_b"]),
            str(data["content_background_colour_a"]),
        ]
    )
    assert len(background_colour.split(",")) == 4
    assert len(content_background_colour.split(",")) == 4
    new_widget = Widget(
        background_colour=background_colour,
        background_image=data["background_image"],
        height=data["height"],
        content_background_colour=content_background_colour,
        border_radius=data["border_radius"],
        content_body_text=data["content_body_text"],
    )
    # commit it to database
    db.session.add(new_widget)
    db.session.commit()
    return jsonify({"id": new_widget.id})
