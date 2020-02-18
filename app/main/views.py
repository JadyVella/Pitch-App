from flask import render_template, url_for, redirect, request, abort
from . import main
from .forms import PickUpLines, Interview, BusinessPlan, UpdateProfile
from ..models import PICKUPLINES, INTERVIEW, User
from .. import db
from flask_login import login_required

@main.route('/')
def index():

    '''
    view root page function that returns the index page and its data
    '''
    
    title = 'Your best pitching site'
    message = 'Write your Pitch'
    return render_template('index.html',title = title,message = message)


@main.route('/pitch', methods = ['GET', 'POST'])
@login_required
def pitch():
    
    pickuplines_form = PickUpLines()
    interview_form = Interview()
    businessplan = BusinessPlan()

    if pickuplines_form.validate_on_submit():
        title = pickuplines_form.title.data
        pitchs = pickuplines_form.pitch.data

        new_pitchs = PICKUPLINES(title=title,pitch=pitchs)


        new_pitchs.save_pickupline()
        return redirect(url_for('.index',title=title))

    title = 'Pitching best ideas'
    
    return render_template('pitch.html',title = title, pickup_lines_form = pickuplines_form, interview_form = interview_form, business_plan_form = businessplan )



@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)



@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):

    user = User.query.filter_by(username = uname).first()
    if user in None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))
    return render_template('profile/update.html',form = form)

