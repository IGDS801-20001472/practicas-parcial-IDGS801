from wtforms import StringField, TelField, IntegerField, EmailField, Form


class Resistencia(Form):
    color1 = StringField('color1')
    color2 = StringField('color2')
    color3 = StringField('color3')
    tolerancia = StringField('tolerancia')