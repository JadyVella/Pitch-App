from flask import render_template, url_for, redirect, request, abort
from . import main
from .forms import PickUpLines, Interview, BusinessPlan
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


@main.route('/pitch')
def pitch():
    
    '''
    view pitch page function that returns the pitch page and its data
    '''

    title = 'Pitching best ideas'
    
    return render_template('pitch.html', title = title)


@main.route('/business_plan', methods = ['GET','POST'])
@login_required
def business_plan():
    form = BusinessPlan()
    '''
    view business_plan function that returns the business_plan page and its data
    '''

    title = 'Business Plan'

    return render_template('business_plan.html', title = title, business_plan_form = form)


@main.route('/interview')
@login_required
def interview():
    form = Interview()
    '''
    view interview function that returns the interview page and its data
    '''

    title = 'Interview'

    return render_template('interview.html', title = title,interview_form = form)


@main.route('/pick_up_lines')
@login_required
def pick_up_lines():
    form = PickUpLines()
    '''
    view pick_up_lines function that returns the pick_up_lines page and its data
    '''

    title = 'Pick Up Lines'

    return render_template('pick_up_lines.html', title = title, pickup_lines_form = form)
