from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField
from wtforms.validators import Required




class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.', validators=[Required()])
    submit = SubmitField('Submit')


class PostPitchForm(FlaskForm):
    pitch_category = SelectField('Select the pitch_category', choices=[('Fashion', 'fashion-blog'), ('Food', 'food-blog'), ('Music', 'music-blog'), ('Sports', 'sports-blog')])
    text = TextAreaField('Type here')
    submit = SubmitField(' Create a Post')


class PostCommentForm(FlaskForm):
    title = StringField('Comment Title')
    comment = TextAreaField('Write a comment')
    submit = SubmitField('Comment')
