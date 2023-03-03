from wrforms import forms
from wtforms import StrinField, IntegerField
from wtforms import EmailField
from wtforms  import validators

class UserForm(From):
    id = IntegerField('id')
    nombre = StrinField('nombre')
    apellidos = StrinField('apellidos')
    email = EmailField('correo')
    