from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import Required

class PickUpLines(FlaskForm):

    title = StringField('Pickup lines title',validators=[Required()])
    pitch = TextAreaField('Pickup lines pitch',validators=[Required()])
    submit = SubmitField('Submit')


class Interview(FlaskForm):

    title = StringField('Interview title',validators=[Required()])
    Pitch = TextAreaField('Interview pitch',validators=[Required()])
    submit = SubmitField('Submit')


class BusinessPlan(FlaskForm):

    title = StringField('Business plan title',validators=[Required()])
    Pitch = TextAreaField('Business plan pitch',validators=[Required()])
    submit = SubmitField('Submit')