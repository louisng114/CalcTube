from datetime import datetime

from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy

bcrypt = Bcrypt()
db = SQLAlchemy()

def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)

class User(db.Model):
    """Model for the User class."""

    __tablename__ = "users"

    username = db.Column(
        db.String(15),
        primary_key=True
    )

    hashed_password = db.Column(
        db.String,
        nullable=False
    )

    role = db.Column(db.String)

    created_at = db.Column(
        db.DateTime,
        nullable=False,
        default=datetime.now
    )

    favorites = db.relationship(
        "Video",
        secondary="favorites"
    )

    basic_votes = db.relationship(
        "Video",
        secondary="basic_votes",
        backref=db.backref("basic_vote_users")
    )

    depth_votes = db.relationship(
        "Video",
        secondary="depth_votes",
        backref=db.backref("depth_vote_users")
    )

    engage_votes = db.relationship(
        "Video",
        secondary="engage_votes",
        backref=db.backref("engage_vote_users")
    )

    @classmethod
    def register(cls, username, password):
        """Register user.

        Hashes password and adds user to system.
        """

        hashed_pwd = bcrypt.generate_password_hash(password).decode('UTF-8')

        user = User(
            username=username,
            hashed_password=hashed_pwd,
        )

        db.session.add(user)
        return user

    @classmethod
    def authenticate(cls, username, password):
        """Find user with `username` and `password`.

        This is a class method (call it on the class, not an individual user.)
        It searches for a user whose password hash matches this password
        and, if it finds such a user, returns that user object.

        If can't find matching user (or if password is wrong), returns False.
        """

        user = cls.query.filter_by(username=username).first()

        if user:
            is_auth = bcrypt.check_password_hash(user.hashed_password, password)
            if is_auth:
                return user

        return False

class Video(db.Model):
    """Model for the Video class"""

    __tablename__ = "videos"

    # video id on YouTube
    id = db.Column(
        db.String(15),
        primary_key=True
    )

    # user who nominated the video
    nominator = db.Column(
        db.String(15),
        db.ForeignKey(
            "users.username",
            ondelete="CASCADE"
        ),
        nullable=False
    )

class Topic(db.Model):
    """Model for the Topic class"""

    __tablename__ = "topics"

    name = db.Column(
        db.String,
        primary_key=True
    )

    description = db.Column(
        db.String
    )

    videos = db.relationship(
        "Video",
        secondary="topics_videos",
        backref=db.backref("topics")
    )

    def __str__(self):
        return self.name

class Favorite(db.Model):
    """Secondary between User and Video for favorite videos"""

    __tablename__ = "favorites"

    user_username = db.Column(
        db.String(15),
        db.ForeignKey("users.username", ondelete="cascade"),
        primary_key=True
    )

    video_id = db.Column(
        db.String(15),
        db.ForeignKey("videos.id", ondelete="cascade"),
        primary_key=True
    )

class Basic_Vote(db.Model):
    """Secondary between User and Video for votes in the best basics category"""

    __tablename__ = "basic_votes"

    user_username = db.Column(
        db.String(15),
        db.ForeignKey("users.username", ondelete="cascade"),
        primary_key=True
    )

    video_id = db.Column(
        db.String(15),
        db.ForeignKey("videos.id", ondelete="cascade"),
        primary_key=True
    )

class Depth_Vote(db.Model):
    """Secondary between User and Video for votes in the best in-depth category"""

    __tablename__ = "depth_votes"

    user_username = db.Column(
        db.String(15),
        db.ForeignKey("users.username", ondelete="cascade"),
        primary_key=True
    )

    video_id = db.Column(
        db.String(15),
        db.ForeignKey("videos.id", ondelete="cascade"),
        primary_key=True
    )

class Engage_Vote(db.Model):
    """Secondary between User and Video for votes in the most engaging category"""

    __tablename__ = "engage_votes"

    user_username = db.Column(
        db.String(15),
        db.ForeignKey("users.username", ondelete="cascade"),
        primary_key=True
    )

    video_id = db.Column(
        db.String(15),
        db.ForeignKey("videos.id", ondelete="cascade"),
        primary_key=True
    )

class Topic_Video(db.Model):
    """Secondary between Topic and Video"""

    __tablename__ = "topics_videos"

    topic_name = db.Column(
        db.String,
        db.ForeignKey("topics.name", ondelete="cascade"),
        primary_key=True
    )

    video_id = db.Column(
        db.String(15),
        db.ForeignKey("videos.id", ondelete="cascade"),
        primary_key=True
    )
