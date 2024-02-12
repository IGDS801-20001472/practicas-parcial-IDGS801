from wtforms import StringField, TelField, IntegerField, EmailField, Form

class DistanciaForm(Form):
    p1c1 = IntegerField('p1c1')
    p2c1 = IntegerField('p2c1')
    p1c2 = IntegerField('p1c2')
    p2c2 = IntegerField('p2c2')
    resultado  = IntegerField('resultado')