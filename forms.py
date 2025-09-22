from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,PasswordField,EmailField
from wtforms.validators import DataRequired, URL,Email,Length
from flask_ckeditor import CKEditorField


# WTForm for creating a blog post
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")


# TODO: Create a RegisterForm to register new users
class RegisterForm(FlaskForm):
    email=EmailField('Email',validators=[Email(),DataRequired()])
    password=PasswordField('Password',validators=[Length(min=8,message='Password should be strong')])
    name=StringField('Name',validators=[DataRequired()])
    submit=SubmitField('Submit')


# TODO: Create a LoginForm to login existing users
class LoginForm(FlaskForm):
    email=EmailField('Email',validators=[Email(),DataRequired()])
    password=PasswordField("Password",validators=[DataRequired()])
    submit=SubmitField('Submit')


# TODO: Create a CommentForm so users can leave comments below posts
class CommentForm(FlaskForm):
    comment_body=CKEditorField("comment Body",validators=[DataRequired()])
    submit=SubmitField('submit')