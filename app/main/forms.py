from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField
from wtforms.validators import Required,Length,DataRequired

class ReviewForm(FlaskForm):

    title = StringField('Review title',validators=[Required()])
    review = TextAreaField('Movie review', validators=[Required()])
    submit = SubmitField('Submit')


class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.', validators=[Required()])
    submit = SubmitField('Submit')


class PostForm(FlaskForm):
    CATEGORIES = [('FASHION & BEAUTY', 'FASHION & BEAUTY'), ('ART', 'ART'), ('CAREER & FINANCE',
                                                                             'CAREER & FINANCE'), ('MOTHERHOOD', 'MOTHERHOOD'), ('GAMING', 'GAMING'), ('MUSIC', 'MUSIC')]
    category = SelectField("CATEGORIES", choices=CATEGORIES)
    title = StringField("TITLE", validators=[DataRequired()])
    post = TextAreaField("BLOG", validators=[Required()])
    submit = SubmitField('Publish Now')
  
  


class PostCommentForm(FlaskForm):
    comment = TextAreaField('Write a comment')
    submit = SubmitField('Comment')
