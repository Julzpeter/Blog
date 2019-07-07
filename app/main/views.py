from flask import render_template,request,redirect,url_for,abort
from . import main
from .forms import ReviewForm, UpdateProfile,PostPitchForm,PostCommentForm
from ..models import  User, Pitch,Comment
from flask_login import login_required,current_user
from .. import db,photos
import markdown2


# Views
@main.route('/', methods = ['GET','POST'])
def index():

    '''
    View root page function that returns the index page and its data
    '''
    title = 'Pitch| Home'
    pitches = Pitch.query.all()

    form = PostPitchForm()
    if form.validate_on_submit():
        pitch_category = form.pitch_category.data
        pitch = form.text.data

        #Updated post
        new_pitch = Pitch(pitch_category=pitch_category,text=pitch,user=current_user)

        #save pitch method
        new_pitch.save_pitch()
        return  redirect(url_for('main.index'))

    return render_template('index.html', title=title, pitch_form=form,pitches=pitches)



@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username=uname).first()

    if user is None:
        abort(404)

        posted_pitches = Post.query.filter_by(user_id=current_user.id).all()


    return render_template("profile/profile.html", user=user)


@main.route('/user/<uname>/update', methods=['GET', 'POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username=uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()
        return redirect(url_for('.profile', uname=user.username))
    return render_template('profile/update.html', form=form)

@main.route('/user/<uname>/update/pic', methods=['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username=uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile', uname=uname))


@main.route('/pitches/<int:id>', methods=['GET', 'POST'])
def pitch(id):
    pitch = Pitch.get_pitch(id)
    if request.args.get("like"):
        pitch.likes = pitch.likes + 1
        db.session.add(pitch)
        db.session.commit()
        return redirect("/pitches/{pitch_id}".format(pitches_id=pitch_id))

    elif request.args.get("dislike"):
        pitch.dislikes = pitch.dislikes + 1
        db.session.add(pitch)
        db.session.commit()
        return redirect("/pitches/{pitch_id}".format(pitches_id=pitch_id))

    comment_form=PostCommentForm()
    if comment_form.validate_on_submit():
        comment=comment_form.comment.data
        new_comment = Comment(pitch_comment=comment,user=current_user,pitch_id=pitch)
        new_comment.save_comment()
    comments = Comment.get_comment(pitch)
    return render_template('pitch.html', pitch=pitch, comment_form=comment_form,comments=comments)


        # comment_form = PostCommentForm()
        # if comment_form.validate_on_submit():
        #     comment=comment_form.text.data
        #     new_comment = Comment(comment=comment,user = current_user.pitches_id= pitch)
        #


    # #getting comments for a pitch
    # all_comments = Comment.query.filter_by(pitch_id=id).all()
    #
    # pitch = Post.query.filter_by(id=id).first()
    # form = PostCommentForm()
    # #from for comments
    # if form.validate_on_submit():
    #     comment = form.comment.data
    #
    #     new_comment = Comment(pitch_comment=comment,
    #                           user=current_user, post_id=id)
    #     db.session.add(new_comment)
    #     db.session.commit()
    #     return redirect(url_for('main.pitch', id=pitch.id))
    #
    #
