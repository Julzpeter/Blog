from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField
from wtforms.validators import Required

class ReviewForm(FlaskForm):

    title = StringField('Review title',validators=[Required()])
    review = TextAreaField('Movie review', validators=[Required()])
    submit = SubmitField('Submit')


class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.', validators=[Required()])
    submit = SubmitField('Submit')


class PostPitchForm(FlaskForm):
    pitch_category = SelectField('Select the pitch_category', choices=[('Religion', 'Religion'), ('General', 'General'), ('Educative', 'Educative'), ('Inspirational', 'Inspirational')])
    text = TextAreaField('Type your pitch')
    submit = SubmitField('Post')


class PostCommentForm(FlaskForm):
    comment = TextAreaField('Write a comment')
    submit = SubmitField('Comment')
