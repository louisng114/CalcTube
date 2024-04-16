from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, widgets
from wtforms.validators import InputRequired, Length
from wtforms_alchemy import QuerySelectMultipleField

## Form for registrations and logins ##
class UserForm(FlaskForm):
    username = StringField("Username: ", validators=[InputRequired(message="Username required"), Length(max=15, message="Username cannot exceed 15 characters")])
    password = PasswordField("Password: ", validators=[InputRequired(message="Password required")])

## extend QuerySelectMultipleField class to turn option selection into checkboxes ##
class QuerySelectMultipleFieldWithCheckboxes(QuerySelectMultipleField):
    widget = widgets.ListWidget()
    option_widget = widgets.CheckboxInput()

## Form for nominating videos ##
class VideoForm(FlaskForm):
    id = StringField("Video ID: ", validators=[InputRequired(message="Video ID required"), Length(max=15, message="Please enter a valid video ID")])
    topics = QuerySelectMultipleFieldWithCheckboxes("Select all topics the video falls under: ")

## Form for changing video topics ##
class VideoEditForm(FlaskForm):
    topics = QuerySelectMultipleFieldWithCheckboxes("Select all topics the video falls under: ")
