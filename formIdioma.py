from wtforms import validators, StringField, Form

class Buscar(Form):
    
    palabraSearch = StringField('Palabra a Buscar', [
        validators.DataRequired(message = "El campo es requerido"),
        validators.length(min=2, max=20, message="ingresa una palabra valida")
        ])
    idioma = StringField('idioma')