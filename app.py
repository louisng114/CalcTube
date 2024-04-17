from flask import Flask, request, render_template, redirect, flash, session, g
from flask_debugtoolbar import DebugToolbarExtension
from sqlalchemy.exc import IntegrityError

from models import db, connect_db, User, Video, Topic
from forms import UserForm, VideoForm, VideoEditForm

from secret import secret_key

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///calctube_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = False
app.config['SECRET_KEY'] = secret_key

app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

connect_db(app)
with app.app_context():
    db.create_all()

##############################################################################
# User routes


@app.before_request
def add_user_to_g():
    """If we're logged in, add curr user to Flask global."""

    if "curr_user" in session:
        g.user = User.query.get(session["curr_user"])

    else:
        g.user = None


def do_login(user):
    """Log in user."""

    session["curr_user"] = user.username


def do_logout():
    """Logout user."""

    if "curr_user" in session:
        del session["curr_user"]


@app.route('/register', methods=["GET", "POST"])
def register():
    """Show registration form and handle registration."""
    form = UserForm()

    if form.validate_on_submit():
        try:
            user = User.register(
                username=form.username.data,
                password=form.password.data,
            )
            db.session.commit()

        except IntegrityError:
            flash("Username already taken", 'danger')
            return render_template('users/register.html', form=form)

        do_login(user)

        return redirect("/")

    else:
        return render_template('users/register.html', form=form)


@app.route('/login', methods=["GET", "POST"])
def login():
    """Handle user login."""

    form = UserForm()

    if form.validate_on_submit():
        user = User.authenticate(form.username.data,
                                 form.password.data)

        if user:
            do_login(user)
            flash(f"Hello, {user.username}!", "success")
            return redirect("/")

        flash("Invalid credentials.", 'danger')

    return render_template('users/login.html', form=form)
    # TODO: MAKE


@app.route('/logout')
def logout():
    """Handle logout of user."""

    do_logout()
    flash("Successfully logged out", 'info')

    return redirect('/login')


@app.route('/favorites')
def users_favorites():
    """Show user's favorited videos."""

    if not g.user:
        flash("Access unauthorized.", "danger")
        return redirect("/")

    favorite_video_ids = []
    for video in g.user.favorites:
        favorite_video_ids.append(video.id)

    videos = (Video
                .query
                .filter(Video.id.in_(favorite_video_ids))
                .limit(50)
                .all())
    return render_template('users/favorites.html', videos=videos)
    # TODO: MAKE


##############################################################################
# Video routes

@app.route('/videos/new', methods=["GET", "POST"])
def videos_add():
    """Nominate a video:

    Show form if GET. If valid, add video and redirect to user page.
    """

    if not g.user:
        flash("Access unauthorized.", "danger")
        return redirect("/")

    form = VideoForm()
    form.topics.query = Topic.query.all()

    if form.validate_on_submit():
        video_id = form.id.data
        video = Video.add_video(id=video_id, nominator=g.user.username)
        video.topics.extend(form.topics.data)

        db.session.commit()

        return redirect(f"/videos/{video_id}")

    return render_template('videos/new.html', form=form)


@app.route('/videos/<video_id>', methods=["GET", "POST"])
def video_view(video_id):
    """View video. Can favorite, vote, and change topic if logged in."""

    video = Video.query.get_or_404(video_id)

    if not g.user:
        return render_template("/videos/video-anon.html", video=video)

    form = VideoEditForm(data={"topics" : video.topics})
    form.topics.query = Topic.query.all()

    if form.validate_on_submit():
        video.topics.clear()
        video.topics.extend(form.topics.data)

        db.session.add(video)
        db.session.commit()

        return redirect(f"/videos/{video_id}")

    return render_template("/videos/video.html", form=form, video=video)


@app.route('/videos/<video_id>/basic', methods=["POST"])
def add_basic(video_id):
    """Add or remove a best basics vote for the currently-logged-in user."""

    if not g.user:
        flash("Access unauthorized.", "danger")
        return redirect("/")

    video = Video.query.get_or_404(video_id)

    if video not in g.user.basic_votes:
        g.user.basic_votes.append(video)
    else:
        g.user.basic_votes.remove(video)
    db.session.commit()

    return redirect(f"/videos/{video_id}")
# TODO: TURN THIS INTO AJAX


@app.route('/videos/<video_id>/depth', methods=["POST"])
def add_depth(video_id):
    """Add or remove a best in-depth vote for the currently-logged-in user."""

    if not g.user:
        flash("Access unauthorized.", "danger")
        return redirect("/")

    video = Video.query.get_or_404(video_id)

    if video not in g.user.depth_votes:
        g.user.depth_votes.append(video)
    else:
        g.user.depth_votes.remove(video)
    db.session.commit()

    return redirect(f"/videos/{video_id}")
# TODO: TURN THIS INTO AJAX


@app.route('/videos/<video_id>/engage', methods=["POST"])
def add_engage(video_id):
    """Add or remove a most engaging vote for the currently-logged-in user."""

    if not g.user:
        flash("Access unauthorized.", "danger")
        return redirect("/")

    video = Video.query.get_or_404(video_id)

    if video not in g.user.engage_votes:
        g.user.engage_votes.append(video)
    else:
        g.user.engage_votes.remove(video)
    db.session.commit()

    return redirect(f"/videos/{video_id}")
# TODO: TURN THIS INTO AJAX


@app.route('/videos/<video_id>/favorite', methods=["POST"])
def add_favorite(video_id):
    """Add or remove a favorite for the currently-logged-in user."""

    if not g.user:
        flash("Access unauthorized.", "danger")
        return redirect("/")

    clicked_video = Video.query.get_or_404(video_id)

    if clicked_video not in g.user.favorites:
        g.user.favorites.append(clicked_video)
    else:
        g.user.favorites.remove(clicked_video)
    db.session.commit()

    return redirect("/favorites")
# TODO: TURN THIS INTO AJAX


@app.route('/videos/<video_id>/delete', methods=["POST"])
def remove_vid(video_id):
    """Delete a video."""

    if not g.user:
        flash("Access unauthorized.", "danger")
        return redirect("/")

    video = Video.query.get_or_404(video_id)

    if video.nominator != g.user.id:
        flash("Access unauthorized.", "danger")
        return redirect("/")

    db.session.delete(video)
    db.session.commit()

    return redirect("/favorites")


##############################################################################
# Topic routes


@app.route('/topics/<name>')
def topic_view(name):
    """View topic. Can favorite, vote, and change topic if logged in."""

    topic = Topic.query.get_or_404(name)
    desc = topic.description.split("; ")

    if not g.user:
        return render_template("topics/topic-anon.html", topic=topic, desc=desc)

    return render_template("topics/topic.html", topic=topic, desc=desc)
    # TODO
    # show name and description
    # show videos tagged with topic


##############################################################################
# Homepage and error pages


@app.route('/')
def homepage():
    """Show homepage"""
    topics = Topic.query.all()

    return render_template('home.html', topics=topics)


##############################################################################
# Additional resources pages


@app.route('/resources')
def resources_page():
    """Show resources page"""

    return render_template('resources.html')
    # TODO
    # show instruction getting url
    # remind student to practice
    # collegeboard
    # brilliant
    # khanacademy


##############################################################################
# TODO: REMOVE AFTER PRODUCTION
@app.after_request
def add_header(req):
    """Add non-caching headers on every request."""

    req.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    req.headers["Pragma"] = "no-cache"
    req.headers["Expires"] = "0"
    req.headers['Cache-Control'] = 'public, max-age=0'
    return req


# form = VideoForm(data={"choices" : video.topics})
# form.choices.query = Topic.query.all()

# video.topics.clear()
# video.topics.extend(form.choices.data)
# db.session.commit()

# Use form.choices in the HTML
# Remove bullets with CSS

# TODO: pip freeze for requirement.txt