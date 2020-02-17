from flask import render_template,url_for,redirect
from . import main
from .forms import PickUpLines, Interview, BusinessPlan
from ..models import PICKUPLINES, INTERVIEW

@main.route('/')
def index():

    '''
    view root page function that returns the index page and its data
    '''
    
    title = 'Your best pitching site'
    message = 'Write your Pitch'
    return render_template('index.html',title = title,message = message)


@main.route('/pitch', methods = ['GET','POST'])
def pitch():
    pickuplines_form = PickUpLines()
    interview_form = Interview()
    businessplan = BusinessPlan()

    '''
    View the pitch page that returns the pitch form and its data
    '''
    title = 'Pitching best ideas'
    
    return render_template('pitch.html',title = title, pickup_lines_form = pickuplines_form, interview_form = interview_form, business_plan_form = businessplan )


