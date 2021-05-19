from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, URL, Email, Length
from flask_ckeditor import CKEditorField
import email_validator

##WTForm
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")

class RegisterForm(FlaskForm):
    email = StringField(label="Email", validators=[DataRequired(), Email(message="invalid email address")])
    password = PasswordField(label="Password", validators=[DataRequired(), Length(min=5, message="Field must be at least 5 characters long")])
    name = StringField(label="Name", validators=[DataRequired()])
    submit = SubmitField("SIGN ME UP!")

class LoginForm(FlaskForm):
    email = StringField(label="Email", validators=[DataRequired(), Email(message="invalid email address")])
    password = PasswordField(label="Password", validators=[DataRequired(), Length(min=5, message="Field must be at least 5 characters long")])
    submit = SubmitField("LET ME IN!")

class CommentForm(FlaskForm):
    comment = CKEditorField("Comment", validators=[DataRequired()])
    submit = SubmitField("SUBMIT COMMENT")