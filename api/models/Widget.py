from api.core import Mixin

from .base import db


class Widget(Mixin, db.Model):
    """Widget Table."""

    __tablename__ = "Widget"
    background_colour = db.Column(db.String, nullable=False)
    background_image = db.Column(db.String, nullable=False)
    id = db.Column(db.Integer, unique=True, primary_key=True)
    height = db.Column(db.String, nullable=False)
    content_background_colour = db.Column(db.String, nullable=False)
    border_radius = db.Column(db.String, nullable=False, default=1)
    content_body_text = db.Column(db.String, nullable=False)


class Page(Mixin, db.Model):
    """Page Table."""

    __tablename__ = "Page"
    id = db.Column(db.Integer, unique=True, primary_key=True)
    background_image_alt_text = db.Column(db.String, nullable=False)
    content = db.Column(db.String, nullable=False)
