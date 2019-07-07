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


class PostForm(FlaskForm):
    category = SelectField('Select the category', choices=[('FASHION & BEAUTY', 'FASHION & BEAUTY'), ('CAREER & FINANCE', 'CAREER AND FINANCE'), ('GAMING', 'GAMING'), ('ART', 'ART')])
    text = TextAreaField('Type your pitch')
    submit = SubmitField('Post')


class PostCommentForm(FlaskForm):
    comment = TextAreaField('Write a comment')
    submit = SubmitField('Comment')
