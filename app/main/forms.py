from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import Required

class PickUpLines(FlaskForm):

    title = StringField('Pickup lines title',validators=[Required()])
    pitch = TextAreaField('Pickup lines pitch',validators=[Required()])
    submit = SubmitField('Submit')


class Interview(FlaskForm):

    title = StringField('Interview title',validators=[Required()])
    pitch = TextAreaField('Interview pitch',validators=[Required()])
    submit = SubmitField('Submit')


class BusinessPlan(FlaskForm):

    title = StringField('Business plan title',validators=[Required()])
    pitch = TextAreaField('Business plan pitch',validators=[Required()])
    submit = SubmitField('Submit')

class UpdateProfile(FlaskForm):

    bio = TextAreaField('More about you', validators=[Required()])
    submit = SubmitField('Submit')


class CommentForm(FlaskForm):

    comments = TextAreaField('Leave your comment', validators=[Required()])
    submit = SubmitField("Leave your comment")