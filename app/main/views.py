from flask import render_template,request,redirect,url_for,abort
from . import main
from .forms import  UpdateProfile,PostPitchForm,PostCommentForm
from ..models import  User, Pitch,Comment
from flask_login import login_required,current_user
from .. import db,photos
import markdown2
import datetime


# Views
@main.route('/', methods=['GET', 'POST'])
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
        new_pitch = Pitch(pitch_category=pitch_category,
                          text=pitch, user=current_user)

        #save pitch method
        new_pitch.save_pitch()
        return redirect(url_for('main.index'))

    return render_template('index.html', title=title, pitch_form=form, pitches=pitches)

@main.route("/pitches/<category>")
def pitches_category(category):
    title = f'My Blog --{category.upper()}'
    # if category == "all":
    #     pitches = Pitch.query.order_by(Pitch.time.desc())
    # else:
    #     pitches = Pitch.query.filter_by(
    #         # pitch_category=pitches_category).all()
    return render_template("/pitch.html", title=title)


@main.route('/<uname>/new/pitch', methods=['GET', 'POST'])
@login_required
def new_pitch(uname):
    form = PostPitchForm()

    user = User.query.filter_by(username=uname).first()

    if user is None:
        abort(404)

    title_page = "My Blog -- Add New Post"

    if form.validate_on_submit():

        # title = form.title.data
        text= form.text.data
        pitch_category = form.pitch_category.data
        pitch = Pitch(
                      text=text,
                      pitch_category=pitch_category,
                      user=current_user)
        db.session.add(pitch)
        db.session.commit()
                      

                     
        

        return redirect(url_for('main.pitches_category', category=pitch_category))

    return render_template('new_pitch.html', title=title_page, form=form)


@main.route("/<uname>/pitch/<pitch_id>/new/comment", methods=["GET", "POST"])
@login_required
def new_comment(uname, pitch_id):
    user = User.query.filter_by(username=uname).first()
    pitch = Pitch.query.filter_by(id=pitch_id).first()

    form = PostCommentForm()
    title_page = "My Blog -- Comment Blog"

    if form.validate_on_submit():
        title = form.title.data
        comment = form.comment.data
        date = datetime.datetime.now()
        time = str(date.time())
        time = time[0:5]
        date = str(date)
        date = date[0:10]
        new_comment = Comment(post_comment=comment, user=user,
                              pitch=pitch, time=time, date=date)

        db.session.add(new_comment)
        db.session.commit()

        return redirect(url_for("main.display_comments", pitch_id=pitch.id))
    return render_template("new_comment.html", title=title_page, form=form, pitch=pitch)


@main.route("/<pitch_id>/comments")
@login_required
def display_comments(pitch_id):
    # user = User.query.filter_by(username = current_user).first()
    pitch = Pitch.query.filter_by(id=pitch_id).first()
    title = "My Blog -- Comments"
    comments = Comment.get_comments(pitch_id)

    return render_template("display_comments.html", comments=comments, pitch=pitch, title=title)


@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username=uname).first()

    if user is None:
        abort(404)

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
