from wtforms import validators, StringField, Form

class Diccionario(Form):
    palabraE = StringField('Palabra Español', [
        validators.DataRequired(message = "El campo es requerido"),
        validators.length(min=2, max=20, message="ingresa una palabra valida.")
        ])
    palabraI = StringField('Palabra Inglés', [
        validators.DataRequired(message = "El campo es requerido"),
        validators.length(min=2, max=20, message="ingresa una plabra valida")
        ])
   